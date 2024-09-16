from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash,
    session,
    request
)
from flask_session import Session
from forms import LoginForm

app = Flask(__name__)
# Note - Use server side code because when using client sessions, the cookies which is generated can be decode easily and there is a chance of getting your data leaked.
app.config["SECRET_KEY"]="secret_key"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    if "user_name" not in session:
        flash("Login Required")
        return redirect(url_for("login",next=request.url))
    else:
        flash(f"Hi {session['user_name'].title()}, have a Nice weekend")
    return render_template("about.html",title="About")
@app.route("/contact")
def contact():
    if "user_name" not in session:
        flash("Login Required")
        return redirect(url_for("login",next=request.url))
    else:
        flash(f"Hi {session['user_name']}, have a Nice weekend")
    return render_template("contact.html",title="Contact")

@app.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session["user_name"] = form.username.data
        flash(f"Logged In successfully by {session['user_name'].title()} ")
        next_url = request.args.get("next")
        return redirect(next_url or url_for("home"))
    else:
        flash("Incorrect Login details")
    return render_template("login.html",title="Login",form=form)


if __name__ =="__main__":
    app.run(debug=True)