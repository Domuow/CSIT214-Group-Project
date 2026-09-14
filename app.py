from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home/root URL
@app.route("/")
def home():
    return render_template("index.html")

# Start the local development server
if __name__ == "__main__":
    app.run(debug=True)
