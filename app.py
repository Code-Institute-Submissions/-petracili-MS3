import os

from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


# flask
app = Flask(__name__)

# mondodb
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/champion")
def champion():
    chempion_list = list(mongo.db.chempion.find())
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("champion.html", chempion_list=chempion_list, user=ObjectId(user["_id"]))
    except:
        user = {}
        return render_template("champion.html", chempion_list=chempion_list, user=user) 

@app.route("/puppy")
def puppy():
    bully_list = list(mongo.db.bully.find())
    try:
        user = mongo.db.users.find_one({"username": session["user"]})
        return render_template("puppy.html", bully_list=bully_list, user=ObjectId(user["_id"])) 
    except:
        user = {}
        return render_template("puppy.html", bully_list=bully_list, user=user)
    
     

@app.route("/contact")
def contact():
    return render_template("contact.html") 


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username").capitalize()))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    if session["user"]:
        user = mongo.db.users.find_one({"username": session["user"]})
        chempion_list = list(mongo.db.chempion.find({'user_id': user['_id']}))
        bully_list = list(mongo.db.bully.find({'user_id': user['_id']}))
        return render_template(
            "profile.html", username=username, chempion_list=chempion_list, bully_list=bully_list)
        
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_chempion", methods=["GET", "POST"])
def add_chempion():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        new_chempion = {
            "img": request.form.get("chempion_img"),
            "title": request.form.get("chempion_title"),
            "text": request.form.get("chempion_text"),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.chempion.insert_one(new_chempion)
        flash("Chempion Successfully Added")
        return redirect(url_for("add_chempion"))

    types = mongo.db.types.find().sort("type", 1)
    return render_template("add_chempion.html", types=types)

@app.route("/edit_champion/<chempion_id>", methods=["GET", "POST"])
def edit_chempion(chempion_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        edit_chempion = {
            "img": request.form.get("chempion_img"),
            "title": request.form.get("chempion_title"),
            "text": request.form.get("chempion_text"),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.chempion.update({"_id": ObjectId(chempion_id)}, edit_chempion)
        flash("Chempion Successfully Edited")
    chempion = mongo.db.chempion.find_one({"_id": ObjectId(chempion_id)})
    return render_template("edit_chempion.html", chempion=chempion)


@app.route("/delete_chempion/<chempion_id>")
def delete_chempion(chempion_id):
    mongo.db.chempion.remove({"_id": ObjectId(chempion_id)})
    flash("Chempion Deleted")
    return redirect(url_for("champion"))

@app.route("/add_bully", methods=["GET", "POST"])
def add_bully():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        new_bully = {
            "img": request.form.get("bully_img"),
            "dob": request.form.get("bully_dob"),
            "first": request.form.get("bully_first"),
            "gender": request.form.get("bully_gender"),
            "hair_color": request.form.get("bully_hair_color"),
            "nationality": request.form.get("bully_nationality"),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.bully.insert_one(new_bully)
        flash("Puppy Successfully Added")
        return redirect(url_for("add_bully"))

    types = mongo.db.types.find().sort("type", 1)
    return render_template("add_puppy.html", types=types)

@app.route("/edit_bully/<bully_id>", methods=["GET", "POST"])
def edit_bully(bully_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        edit_bully = {
            "img": request.form.get("bully_img"),
            "dob": request.form.get("bully_dob"),
            "first": request.form.get("bully_first"),
            "gender": request.form.get("bully_gender"),
            "hair_color": request.form.get("bully_hair_color"),
            "nationality": request.form.get("bully_nationality"),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.bully.update({"_id": ObjectId(bully_id)}, edit_bully)
        flash("Puppy Successfully Edited")
    bully = mongo.db.bully.find_one({"_id": ObjectId(bully_id)})
    return render_template("edit_puppy.html", bully=bully)


@app.route("/delete_bully/<bully_id>")
def delete_bully(bully_id):
    mongo.db.bully.remove({"_id": ObjectId(bully_id)})
    flash("Puppy Deleted")
    return redirect(url_for("puppy"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG", False))