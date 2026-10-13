#!/bin/bash
# Demo en vivo: deja salidas/ vacía, abre el tablero en Chrome y arranca Claude Code.
#   bash demo.sh            en vivo (luego escribe /arranca en Claude Code)
#   bash demo.sh respaldo   Plan B: repite la corrida grabada (Enter en el tablero)
cd "$(dirname "$0")"
PUERTO=4322
lsof -ti tcp:$PUERTO | xargs kill 2>/dev/null

if [ "$1" = "respaldo" ]; then
  python3 herramientas/tablero.py --respaldo &
else
  # Las entregas anteriores van a la Papelera (no se borran).
  for f in salidas/*.md; do [ -e "$f" ] && mv "$f" "$HOME/.Trash/$(date +%H%M%S)-$(basename "$f")"; done
  python3 herramientas/tablero.py &
fi
TABLERO=$!
trap 'kill $TABLERO 2>/dev/null' EXIT
sleep 0.8
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ -x "$CHROME" ]; then
  # Mitad izquierda de la pantalla: el tablero. La terminal va a la derecha (pantalla dividida).
  "$CHROME" --app="http://localhost:$PUERTO" --window-position=0,0 --window-size=960,1080 >/dev/null 2>&1 &
else
  open "http://localhost:$PUERTO"
fi

if [ "$1" = "respaldo" ]; then
  echo "Plan B abierto. En el tablero: Enter arranca, R reinicia. Ctrl+C aquí para cerrar."
  wait $TABLERO
else
  echo "Tablero abierto. Escribe /arranca en Claude Code."
  claude --permission-mode acceptEdits
fi
