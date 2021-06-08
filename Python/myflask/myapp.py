from flask_oidc import OpenIDConnect
from flask import Flask, jsonify


app = Flask("__main__")
app.config.update({
    'SECRET_KEY': "mysecret",
    'OIDC_CLIENT_SECRETS' : "myjson.json"
})

oidc = OpenIDConnect(app)

@app.route("/", methods=["GET", "POST"])
def index():
    print(f" Hellow world ")
    return jsonify("Hello World")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
