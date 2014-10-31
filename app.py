from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import Connection

#mongo setup
conn = Connection()
db = conn["leon_miranda"]

#flask setup
app = Flask(__name__)

def checkLogin(user, pwd):
    return True

@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        username = request.form["user"]
        pwd = request.form["pwd"]
        if checkLogin(user, pwd):
            #set logged in to true somehow idek i think this is your thing Mir
            return redirect(url_for("userpage", user = username))
    return render_template("login.html")
main
@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        #name = request.form["name"]
        #email = request.form["email"]
        #age = request.form["age"]
        username = request.form["user"]
        pwd = request.form["pwd"]
        #if (name == None or email == None or age == None or
         #   username == None or pwd == None): #b/c they are all mandatory
          #  if len(db.users.find({"name":name})) == 0:
           #     db.users.insert({"name":name, "email":email, "age":age,
            #                     "user":username, "pwd":pwd})
             #   return redirect(url_for("main"))
        db.users.insert({"user":username, "pwd":pwd})
        return redirect(url_for("main"))
            #home.html = register.html deal with it
    return render_template("home.html")

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

@app.route("/user")
#protected, what they are sent to immediately, idek what it should contain
def userpage(user = None):
    return render_template("user.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
