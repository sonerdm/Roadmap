from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "\nHello, world from application 2!\n"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')