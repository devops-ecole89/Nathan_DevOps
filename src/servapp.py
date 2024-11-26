from flask import Flask
from test import firstTest
app = Flask(__name__)

@app.route("/")
def hello():
    return firstTest("Nathan")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
