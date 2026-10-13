# This is the main application file for the Flask web application. It sets up the routes and imports the necessary functions from other files in the route_logic directory.
# Run this file in order to run the program! - MUST INSTALL FLASK FIRST - pip install flask

from flask import Flask, flash, redirect, render_template, request, url_for

from route_logic.bookings import bookings_main, bookings_post
from route_logic.home import home_main  # Import the home_main function from the home.py file in the route_logic directory
from route_logic.facilities import facilities_main, facilities_post  # Import the facilities_main function from the facilities.py file in the route_logic directory
from route_logic.staff import staff_main, staff_post
from route_logic.login import current_user, login_required, logout_user, staff_required, login_route
from database import init_db  # Import the init_db function from the database.py file in the route_logic directory

# Initialize the Flask application
app = Flask(__name__)

# Creates the database and tables if they don't exist, and populates the facilities table with initial data
init_db()

# Set a secret key for the application - this is used for securely signing the session cookie and can be used for other security-related needs by extensions or your application
app.secret_key = 'abc'  # Replace in production environment


@app.context_processor
def inject_current_user():
    return {"current_user": current_user()}

# Web App routes

# Define the route for the home/root URL
@app.route("/")
def home():
    return home_main() # Call the home_main function to render the home page

@app.route("/facilities")
def facilities():
    return facilities_main() # Call the facilities_main function to render the facilities page

@app.route("/facilities_search", methods=["POST"])
def facilities_search():
    return facilities_post() # Call the facilities_post function to handle the form submission for searching facilities

@app.route("/bookings")
@login_required
def bookings():
    return bookings_main()

@app.route("/bookings", methods=["POST"])
@login_required
def save_booking():
    return bookings_post()

@app.route("/staff")
@staff_required
def staff():
    return staff_main()

@app.route("/staff", methods=["POST"])
@staff_required
def update_staff_booking():
    return staff_post()


@app.route("/login", methods=["GET", "POST"])
def login():
    return login_route()  # Call the login_route function to handle the login page and form submission


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


# Start the local development server
if __name__ == "__main__":
    app.run(debug=True)
