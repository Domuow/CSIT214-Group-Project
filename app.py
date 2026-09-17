from flask import Flask, render_template, Blueprint # Blueprint is imported for future use when modularizing the application (using multiple files)

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home/root URL
@app.route("/")
def home():
    return render_template("index.html")

# Temp Route for Facilities - to be alterd when facilities.py is implemented
@app.route("/facilities")
def facilities():
    pass

# Temp Route for Bookings - to be alterd when bookings.py is implemented
@app.route("/bookings")
def bookings():
    pass

# Temp Route for Staff - to be alterd when staff.py is implemented
@app.route("/staff")
def staff():
    pass

# More routes can be added here as needed, following a similar pattern to the above


# Start the local development server
if __name__ == "__main__":
    app.run(debug=True)
