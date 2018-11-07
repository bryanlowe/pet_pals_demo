# import necessary libraries
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# @TODO: Setup your database here
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/pets.sqlite"
db = SQLAlchemy(app)

from .models import Pet

@app.route("/")
def home():
    return render_template("index.html")


# @TODO: Create a route "/send" that handles both GET and POST requests
# If the request method is POST, save the form data to the database
# Otherwise, return "form.html"
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name_data = request.form["petName"]
        pet_type_data = request.form["petType"]
        age_data = request.form["petAge"]

        pet = Pet(name=name_data, type=pet_type_data, age=age_data)
        db.session.add(pet)
        db.session.commit()
        return redirect("/", code=302)

    return render_template("form.html")




# @TODO: Create an API route "/api/pals" to return data to plot
@app.route("/api/pals")
def pals():
    results = db.session.query(Pet.type, func.count(Pet.type)).group_by(Pet.type).all()

    pet_type = [result[0] for result in results]
    count_type = [result[1] for result in results]

    trace = {
        "x": pet_type,
        "y": count_type,
        "type": "bar"
    }

    return jsonify(trace)

if __name__ == "__main__":
    app.run()
