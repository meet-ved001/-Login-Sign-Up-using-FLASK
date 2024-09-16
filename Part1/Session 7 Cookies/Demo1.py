from flask import Flask,make_response, request

app = Flask(__name__)

@app.route("/")
def home():
    response = make_response("<h1> Home Page <h1>")
    return response
@app.route("/set_cookie")
def set_cookie():
    response = make_response("<h1> Set Cookie Page <h1>")
    response.set_cookie("cookie_name","cookie_value")
    return response

@app.route("/get_cookie")
def get_cookie():
    value = request.cookies.get("cookie_name")
    response = make_response(f"<h1>Cookie value is {value} </h1>")
    return response
if __name__ == "__main__":
    app.run(debug=True)