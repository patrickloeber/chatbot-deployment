from flask import Flask, render_template, request, jsonify
# from flask_cors import CORS 
from chat import get_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
# CORS(app)
limiter = Limiter(app, key_func = get_remote_address)

# Comment out @app.get and index_get() if you are using CORS(app) for standalone frontend and uncomment all other commented lines
@app.get("/")
@limiter.limit("3/second; 200/minute; 1200/hour")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    if len(text) > 100:
        text = "hello" 
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug = True)
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=8080)