from flask import Flask


app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def index():
    return "Hello this is just a test"

if __name__ == "__main__":
    app.run()
