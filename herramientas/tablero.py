#!/usr/bin/env python3
"""Tablero del equipo: muestra en vivo a los 5 agentes trabajando y sus entregas.

Uso:
  python3 herramientas/tablero.py              en vivo: lee salidas/ y la bitácora de Claude Code
  python3 herramientas/tablero.py --respaldo   Plan B: repite la corrida grabada en ejemplos/
                                               (en vivo también: tecla B en el tablero)
  python3 herramientas/tablero.py --grabar     guarda la última corrida (salidas/ + bitácora) en ejemplos/

En vivo, el tablero arranca la corrida él mismo (Mac):
  Enter  abre la Terminal en la mitad derecha con Claude Code ejecutando /arranca (se ve el trabajo de fondo)
  S      corre /arranca sin terminal, en segundo plano
  R      deja el tablero en cero para otra corrida

Solo usa la biblioteca estándar de Python. Abre http://localhost:4322
"""
import json, re, shlex, shutil, subprocess, sys, time
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
HERR = KIT / "herramientas"
SALIDAS = KIT / "salidas"
EJEMPLOS = KIT / "ejemplos"
PROYECTO = Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(KIT))
PUERTO = 4322
RESPALDO = "--respaldo" in sys.argv
INICIO_SERVIDOR = time.time()
DESDE = [INICIO_SERVIDOR]   # solo cuentan las corridas posteriores a este momento (R lo reinicia)
ARRANCANDO = [None]         # cuándo se pidió la última corrida desde el tablero
HERRAMIENTAS = ["Read", "Glob", "Grep", "Write(salidas/**)", "WebSearch", "WebFetch", "Agent"]

AGENTES = [
    {"id": "atencion", "n": 1, "puesto": "Atención al cliente", "llego": "1 WhatsApp de una clienta nueva"},
    {"id": "prospectos", "n": 2, "puesto": "Califica prospectos", "llego": "8 prospectos del sitio web"},
    {"id": "seguimiento", "n": 3, "puesto": "Seguimiento al CRM", "llego": "Notas de una llamada de venta"},
    {"id": "facturas", "n": 4, "puesto": "Facturas por pagar", "llego": "6 facturas (CFDI) de proveedores"},
    {"id": "investigador", "n": 5, "puesto": "Investigación", "llego": "1 encargo: IA en despachos"},
]


def ts(s):
    """ISO 8601 (con Z) → segundos epoch."""
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
    except (ValueError, AttributeError):
        return None


def accion(nombre, entrada):
    if nombre == "Read":
        return "Abre " + Path(entrada.get("file_path", "")).name
    if nombre == "Grep":
        return "Busca «" + str(entrada.get("pattern", ""))[:40] + "»"
    if nombre == "Glob":
        return "Revisa la carpeta"
    if nombre == "WebSearch":
        return "Busca en internet: " + str(entrada.get("query", ""))[:60]
    if nombre == "WebFetch":
        m = re.search(r"https?://([^/]+)", entrada.get("url", ""))
        return "Lee " + (m.group(1) if m else "una página")
    if nombre in ("Write", "Edit"):
        return "Escribe su entrega"
    return nombre


def sesion_arranca(desde):
    """La sesión más reciente (posterior a `desde`) en la que se escribió /arranca. Devuelve (archivo, inicio)."""
    if not PROYECTO.is_dir():
        return None, None
    mejor = (None, None)
    for f in PROYECTO.glob("*.jsonl"):
        if f.stat().st_mtime < desde:
            continue
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for linea in fh:
                if "<command-name>/arranca</command-name>" in linea:
                    t = ts(json.loads(linea).get("timestamp", ""))
                    if t and t >= desde - 5 and (mejor[1] is None or t > mejor[1]):
                        mejor = (f, t)
    return mejor


def bitacora(sesion):
    """Acciones de cada subagente: {id: [[t, texto], ...]}."""
    res = {a["id"]: [] for a in AGENTES}
    carpeta = sesion.with_suffix("") / "subagents"
    if not carpeta.is_dir():
        return res
    for f in carpeta.glob("*.jsonl"):
        quien, eventos = None, []
        with open(f, encoding="utf-8", errors="ignore") as fh:
            for linea in fh:
                try:
                    d = json.loads(linea)
                except ValueError:
                    continue
                m = d.get("message") or {}
                c = m.get("content")
                if quien is None and d.get("type") == "user" and isinstance(c, str):
                    for a in AGENTES:
                        if f"{a['n']}-{a['id']}" in c:
                            quien = a["id"]
                if isinstance(c, list):
                    for x in c:
                        if isinstance(x, dict) and x.get("type") == "tool_use":
                            eventos.append([ts(d.get("timestamp", "")), accion(x.get("name"), x.get("input") or {})])
        if quien:
            res[quien] = eventos
    return res


def estado_vivo():
    sesion, inicio = sesion_arranca(DESDE[0])
    log = bitacora(sesion) if sesion else {}
    agentes = []
    for a in AGENTES:
        f = SALIDAS / f"{a['n']}-{a['id']}.md"
        listo = None
        md = ""
        if inicio and f.exists() and f.stat().st_mtime >= inicio:
            listo = f.stat().st_mtime
            md = f.read_text(encoding="utf-8")
        agentes.append({**a, "acciones": [[t - inicio, x] for t, x in log.get(a["id"], []) if t and inicio],
                        "listo": (listo - inicio) if listo else None, "md": md})
    return {"modo": "vivo", "inicio": inicio, "ahora": time.time(), "arrancando": ARRANCANDO[0] is not None and not inicio,
            "transcurrido": (time.time() - inicio) if inicio else None, "agentes": agentes}


def estado_respaldo():
    tiempos = json.loads((EJEMPLOS / "tiempos.json").read_text(encoding="utf-8"))
    bit = {}
    if (EJEMPLOS / "bitacora.json").exists():
        bit = json.loads((EJEMPLOS / "bitacora.json").read_text(encoding="utf-8"))
    agentes = []
    for a in AGENTES:
        f = EJEMPLOS / f"{a['n']}-{a['id']}.md"
        agentes.append({**a, "acciones": bit.get(a["id"], []), "listo": tiempos.get(a["id"]),
                        "md": f.read_text(encoding="utf-8") if f.exists() else ""})
    return {"modo": "respaldo", "total": tiempos.get("total"), "costo_usd": tiempos.get("costo_usd"), "agentes": agentes}


def grabar():
    sesion, inicio = sesion_arranca(0)
    if not sesion:
        sys.exit("No encontré ninguna corrida de /arranca en " + str(PROYECTO))
    log = bitacora(sesion)
    tiempos = {}
    for a in AGENTES:
        f = SALIDAS / f"{a['n']}-{a['id']}.md"
        if not f.exists():
            sys.exit("Falta " + str(f))
        shutil.copy2(f, EJEMPLOS / f.name)
        tiempos[a["id"]] = round(f.stat().st_mtime - inicio)
    previo = {}
    if (EJEMPLOS / "tiempos.json").exists():
        previo = json.loads((EJEMPLOS / "tiempos.json").read_text(encoding="utf-8"))
    tiempos["total"] = max(tiempos.values()) + 6
    tiempos["costo_usd"] = previo.get("costo_usd")
    tiempos["fecha"] = time.strftime("%Y-%m-%d")
    (EJEMPLOS / "tiempos.json").write_text(json.dumps(tiempos, ensure_ascii=False, indent=1), encoding="utf-8")
    (EJEMPLOS / "bitacora.json").write_text(json.dumps(
        {k: [[round(t - inicio, 1), x] for t, x in v if t] for k, v in log.items()}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("Grabado en ejemplos/:", tiempos)


def osa(script):
    subprocess.run(["osascript", "-e", script], capture_output=True, timeout=20)


def pantalla():
    """Área útil de la pantalla principal (x, y, ancho, alto) en coordenadas de AppleScript."""
    try:
        r = subprocess.run(["osascript", "-l", "JavaScript", "-e",
                            'ObjC.import("AppKit");var s=$.NSScreen.mainScreen,f=s.frame,v=s.visibleFrame;'
                            '[v.origin.x,f.size.height-v.origin.y-v.size.height,v.size.width,v.size.height].join(",")'],
                           capture_output=True, text=True, timeout=10)
        x, y, w, h = (int(float(n)) for n in r.stdout.strip().split(","))
        return x, y, w, h
    except Exception:
        return 0, 25, 1920, 1055


def limpiar_salidas():
    for f in SALIDAS.glob("*.md"):
        f.rename(Path.home() / ".Trash" / f"{time.strftime('%H%M%S')}-{f.name}")


def arrancar(modo):
    """Arranca /arranca: con la Terminal a la derecha (se ve el trabajo) o en segundo plano."""
    limpiar_salidas()
    DESDE[0] = time.time()
    ARRANCANDO[0] = time.time()
    x, y, w, h = pantalla()
    mitad = x + w // 2
    if modo == "terminal":
        orden = f"cd {shlex.quote(str(KIT))} && clear && claude --permission-mode acceptEdits /arranca"
        # La Terminal en la mitad derecha (el tablero ya ocupa la izquierda).
        osa(f'''tell application "Terminal"
  activate
  do script "{orden}"
  delay 0.3
  set bounds of front window to {{{mitad}, {y}, {x + w}, {y + h}}}
end tell''')
    else:
        log = open(KIT / "salidas" / ".ultima-corrida.log", "w")
        subprocess.Popen(["claude", "-p", "/arranca", "--allowedTools", *HERRAMIENTAS], cwd=KIT, stdout=log, stderr=log,
                         start_new_session=True)


class Manejador(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def enviar(self, cuerpo, tipo):
        self.send_response(200)
        self.send_header("Content-Type", tipo)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(cuerpo)

    def do_POST(self):
        ruta = self.path.split("?")[0]
        if self.headers.get("X-Tablero") != "1":   # solo el propio tablero puede pedir esto
            self.send_response(403); self.end_headers(); return
        if ruta == "/arrancar":
            arrancar("fondo" if "fondo" in self.path else "terminal")
        elif ruta == "/reiniciar":
            limpiar_salidas(); DESDE[0] = time.time(); ARRANCANDO[0] = None
        else:
            self.send_response(404); self.end_headers(); return
        self.enviar(b"{}", "application/json")

    def do_GET(self):
        ruta = self.path.split("?")[0]
        if ruta == "/estado":
            e = estado_respaldo() if (RESPALDO or "respaldo" in self.path) else estado_vivo()
            return self.enviar(json.dumps(e, ensure_ascii=False).encode(), "application/json; charset=utf-8")
        if ruta in ("/", "/index.html"):
            return self.enviar((HERR / "tablero.html").read_bytes(), "text/html; charset=utf-8")
        if ruta.startswith("/avatares/") and ruta.endswith(".jpg"):
            f = HERR / "avatares" / Path(ruta).name
            if f.exists():
                return self.enviar(f.read_bytes(), "image/jpeg")
        if ruta.startswith("/fuentes/") and ruta.endswith(".woff2"):
            f = HERR / "fuentes" / Path(ruta).name
            if f.exists():
                return self.enviar(f.read_bytes(), "font/woff2")
        self.send_response(404)
        self.end_headers()


if __name__ == "__main__":
    if "--grabar" in sys.argv:
        grabar()
        sys.exit()
    print(f"Tablero en http://localhost:{PUERTO}  ({'Plan B: corrida grabada' if RESPALDO else 'en vivo'})  · Ctrl+C para cerrar")
    ThreadingHTTPServer(("127.0.0.1", PUERTO), Manejador).serve_forever()
