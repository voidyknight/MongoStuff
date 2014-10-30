from flask import Flask, render_template, request, redirect, url_for
from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["leon_miranda"]

#flask setup
app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        username = request.form["user"]
        pwd = request.form["pwd"]
        if checkLogin(user, pwd):
            #set logged in to true somehow idek
            return redirect(url_for("userpage", user = username))
    return render_template("main.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
    return render_template("register.html")

#logout button on other pages will redirect to this
@app.route("/logout")
def logout():
    #log user out
    #page will have button to return to login page
    return render_template("logout.html")

@app.route("/about")
#unprotected page
def about():
    return render_template("about.html")

@app.route("/settings", methods = ["GET", "POST"])
#protected, allows user to change info and put more info also
def settings():
    return render_template("settings.html")

@app.route("/<user>")
#protected, what they are sent to immediately, idek what it should contain
def userpage(user = None):
    return render_template("user.html")

