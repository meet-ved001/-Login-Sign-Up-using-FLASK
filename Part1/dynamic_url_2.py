from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<h1>Welcome to home page!</h1>"
@app.route("/welcome/<name>")
def home1(name):
    return f"<h1>Welcome to {name.title()} page!</h1>"

if __name__ == "__main__":
    app.run(debug=True)