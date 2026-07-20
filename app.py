from flask import Flask, render_template, request
from database import parcels, users
from models import Parcel
from notification import NotificationEngine
from utils import valid_phone, valid_pincode

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = users.find_one({
            "username": username,
            "password": password
        })

        if user:
            return """
            <h2>Login Successful!</h2>

            <a href="/dashboard">
                Go to Dashboard
            </a>
            """

        else:
            return """
            <h2>Invalid Username or Password</h2>

            <a href="/login">
                Try Again
            </a>
            """

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        username = request.form["username"]
        password = request.form["password"]

        user = {
            "fullname": fullname,
            "email": email,
            "mobile": mobile,
            "username": username,
            "password": password
        }

        users.insert_one(user)

        return """
        <h2>Registration Successful!</h2>
        <a href="/login">Go to Login</a>
        """

    return render_template("register.html")

@app.route("/add_parcel")
def add_parcel():
    return render_template("add_parcel.html")


@app.route("/save_parcel", methods=["POST"])
def save_parcel():

    sender = request.form["sender"]
    receiver = request.form["receiver"]
    phone = request.form["phone"]
    address = request.form["address"]
    pincode = request.form["pincode"]

    if not valid_phone(phone):
       return "<h2>Invalid Phone Number</h2>"

    if not valid_pincode(pincode):
       return "<h2>Invalid Pincode</h2>"

    parcel = Parcel(sender, receiver, phone, address, pincode)

    parcels.insert_one(parcel.to_dict())


    return f"""
    <h2>Parcel Booked Successfully!</h2>

    <h3>Your Tracking ID:</h3>

    <h1>{parcel.tracking_id}</h1>

    <a href='/add_parcel'>Book Another Parcel</a>
   """

@app.route("/track")
def track_page():
    return render_template("track.html")

@app.route("/track", methods=["POST"])
def track_parcel():

    tracking_id = request.form["tracking_id"]

    parcel = parcels.find_one({"tracking_id": tracking_id})

    if parcel:
        return render_template(
            "tracking_result.html",
            parcel=parcel
    )
    else:
        return "<h2>Tracking ID Not Found</h2>"

    
@app.route("/dashboard")
def dashboard():

    all_parcels = list(parcels.find())

    return render_template(
        "dashboard.html",
        parcels=all_parcels
    )

@app.route("/update_status", methods=["POST"])
def update_status():

    tracking_id = request.form["tracking_id"]
    status = request.form["status"]

    parcels.update_one(
        {"tracking_id": tracking_id},
        {"$set": {"status": status}}
    )

    parcel = parcels.find_one({"tracking_id": tracking_id})

    NotificationEngine.send_notification(
        parcel["receiver"],
        tracking_id,
        status
    )

    return """
    <h2>Status Updated Successfully!</h2>

    <a href="/dashboard">Back to Dashboard</a>
    """

if __name__ == "__main__":
    app.run(debug=True)