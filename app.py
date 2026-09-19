# This is the main application file for the Flask web application. It sets up the routes and imports the necessary functions from other files in the route_logic directory.
# Run this file in order to run the program! - MUST INSTALL FLASK FIRST - pip install flask

from flask import Flask, render_template, Blueprint # Blueprint is imported for future use when modularizing the application (using multiple files)

from route_logic.home import home_main  # Import the home_main function from the home.py file in the route_logic directory
from route_logic.facilities import facilities_main  # Import the facilities_main function from the facilities.py file in the route_logic directory

# Initialize the Flask application
app = Flask(__name__)

# Set a secret key for the application - this is used for securely signing the session cookie and can be used for other security-related needs by extensions or your application
app.secret_key = 'abc'  # Replace

# Define the route for the home/root URL
@app.route("/")
def home():
    return home_main() # Call the home_main function to render the home page

# Temp Route for Facilities - to be alterd when facilities.py is implemented
@app.route("/facilities")
def facilities():
    return facilities_main() # Call the facilities_main function to render the facilities page

# Temp Route for Bookings - to be alterd when bookings.py is implemented
@app.route("/bookings")
def bookings():
    return "Bookings page is under construction. Please check back later." # Placeholder response for the bookings page

# Temp Route for Staff - to be alterd when staff.py is implemented
@app.route("/staff")
def staff():
    return "Staff page is under construction. Please check back later." # Placeholder response for the staff page

# More routes can be added here as needed, following a similar pattern to the above


# Start the local development server
if __name__ == "__main__":
    app.run(debug=True)
