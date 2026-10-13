#!/bin/bash
# Abre la demo con un clic (Mac): deja salidas/ vacía, levanta el tablero y lo abre en Chrome en la mitad izquierda.
# Desde el tablero: Enter arranca (Terminal a la derecha con Claude Code), S sin terminal, P pantalla completa, B plan B, R reinicia.
#   bash herramientas/abrir_demo.sh            en vivo
#   bash herramientas/abrir_demo.sh respaldo   solo el Plan B (corrida grabada, sin internet)
KIT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$KIT" || exit 1
PUERTO=4322
lsof -ti tcp:$PUERTO | xargs kill 2>/dev/null
for f in salidas/*.md; do [ -e "$f" ] && mv "$f" "$HOME/.Trash/$(date +%H%M%S)-$(basename "$f")"; done
EXTRA=""; [ "$1" = "respaldo" ] && EXTRA="--respaldo"
nohup python3 herramientas/tablero.py $EXTRA > /tmp/tablero-agentes.log 2>&1 &
for i in $(seq 1 30); do curl -s -o /dev/null "http://localhost:$PUERTO/estado" && break; sleep 0.2; done
# Área útil de la pantalla principal (sin la barra de menús).
read X Y W H < <(osascript -l JavaScript -e 'ObjC.import("AppKit");var s=$.NSScreen.mainScreen,f=s.frame,v=s.visibleFrame;[v.origin.x,f.size.height-v.origin.y-v.size.height,v.size.width,v.size.height].map(Math.round).join(" ")')
CHROME="/Applications/Google Chrome.app"
MITAD=$(( ${W:-1920} / 2 ))
if [ -d "$CHROME" ]; then
  # Ventana propia de Chrome (perfil aparte) fija en la mitad izquierda; la Terminal irá a la derecha.
  pkill -f "user-data-dir=$HOME/.cache/tablero-agentes" 2>/dev/null; sleep 0.4
  open -na "$CHROME" --args --user-data-dir="$HOME/.cache/tablero-agentes" --no-first-run --no-default-browser-check \
    --app="http://localhost:$PUERTO" --window-position=${X:-0},${Y:-25} --window-size=$MITAD,${H:-1055}
else
  open "http://localhost:$PUERTO"
fi
