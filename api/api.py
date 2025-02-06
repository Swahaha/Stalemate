from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import subprocess

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

STOCKFISH_PATH = r"C:\Users\swara\Downloads\stockfish-windows-x86-64-sse41-popcnt\stockfish\stockfish-windows-x86-64-sse41-popcnt.exe"  # Update this with the correct path

@app.route('/')
def home():
    return "Flask API is running!"

@app.route("/get_best_move", methods=["POST"]) 
def get_move():
    data = request.get_json()
    fen = data.get("fen")

    if not fen:
        return jsonify({"error": "No FEN provided"}), 400

    best_move = get_best_move(fen)
    return jsonify({"best_move": best_move})


def get_best_move(fen):
    try:
        process = subprocess.Popen(STOCKFISH_PATH, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

        process.stdin.write("uci\n")
        process.stdin.write(f"position fen {fen}\n")
        process.stdin.write("go depth 15\n")
        process.stdin.flush()

        best_move = None
        while True:
            output = process.stdout.readline().strip()
            if output.startswith("bestmove"):
                best_move = output.split()[1]
                break

        process.stdin.write("quit\n")
        process.stdin.flush()
        process.terminate()

        return best_move
    except Exception as e:
        return str(e)



# if __name__ == '__main__':
#     app.run(debug=True)
