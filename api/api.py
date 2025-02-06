from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running!"

@app.route('/time')
def get_current_time():
    from datetime import datetime
    return jsonify({"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})


# if __name__ == '__main__':
#     app.run(debug=True)
