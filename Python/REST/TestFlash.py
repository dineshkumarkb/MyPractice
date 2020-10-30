from flask import Flask

app = Flask(__name__)

print __name__


@app.route("/")
def test():
    return "Hi There!"


if __name__ == "__main__":
    app.run(port=8000,debug=True)