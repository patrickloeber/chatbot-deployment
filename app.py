from chat import get_response
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

@app.post("/predict")
def predict():
    text= request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text)
    message = {"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=False)
