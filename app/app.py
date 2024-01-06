from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=["GET", "OPTIONS"])
def hello_world():
    if request.method == "OPTIONS":
        response = app.make_default_options_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)
