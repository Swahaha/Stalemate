# Stalemate

A RL Chessbot.

Setup guide:
yarn start for frontend in main dir.
yarn start-api for backend in main dir.


Change package.json to:
windows: "start-api": "cd api && venv/Scripts/python -m flask run --no-debugger",
unix: "start-api": "cd api && venv/bin/python -m flask run --no-debugger",


npm install yarn
npm install react-chessboard chess.js
