from flask import Flask,render_template,url_for
from employees3 import employess_data
# create the flask app
app = Flask(__name__)

# home page
@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",title="Home")


# about page
@app.route("/about")
def about():
	return render_template("about.html",title="About")
@app.route("/employees")
def employees():
	return render_template("employees.html",
						title="employees",
						employees=employess_data)

@app.route("/employees/managers")
def managers():
	return render_template("managers.html",
						title="managers",
						employees=employess_data)

@app.route("/evaluate/<int:num>")
def evaluate(num):
	return render_template("evaluate.html",title="Evaluate",number=num)
# start the app
if __name__ == "__main__":
	app.run(debug=True)