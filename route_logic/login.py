from functools import wraps

from flask import flash, redirect, request, session, url_for, render_template


# These accounts are intentionally hardcoded for the prototype
USERS = {
    "user": {
        "password": "user123",
        "name": "Demo User",
        "email": "user@example.com",
        "role": "user",
    },
    "admin": {
        "password": "admin123",
        "name": "Staff Administrator",
        "email": "admin@example.com",
        "role": "staff",
    },
}

# Function to get the current logged-in user from the session
def current_user():
    return session.get("user")


# Login function to set the user session after successful authentication
def login_user(username):
    user = USERS[username]
    session["user"] = {
        "username": username,
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
    }

# Logout function to clear the user session and hence log the user out
def logout_user():
    session.pop("user", None)

# Decorator to ensure that a user is logged in before accessing certain routes
def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if current_user() is None:
            flash("Please log in to continue.", "error")
            return redirect(url_for("login", next=request.path))
        
        return view(*args, **kwargs)
    
    # Return the wrapped view function - to be used as a decorator for routes that require staff access
    return wrapped_view

# Decorator to ensure that a user is logged in and has a staff role before accessing certain routes
def staff_required(view):
    @wraps(view)
    # Define a wrapper function that checks if the user is logged in and has a staff role
    def wrapped_view(*args, **kwargs):
        user = current_user()

        # If the user is not logged in, flash an error message and redirect to the login page
        if user is None:
            flash("Please log in as staff to continue.", "error")
            return redirect(url_for("login", next=request.path))

        # If the user is logged in but does not have a staff role, flash an error message and redirect to the bookings page
        if user["role"] != "staff":
            flash("Only staff members can access that page.", "error")
            return redirect(url_for("bookings"))
        return view(*args, **kwargs)

    # Return the wrapped view function - to be used as a decorator for routes that require staff access
    return wrapped_view


def authenticate(username, password):
    # Check if the provided username exists and if the password matches the stored password for that user
    user = USERS.get(username.strip().lower())

    if user is None or user["password"] != password:
        return None
    return username.strip().lower()

# The login route handles both GET and POST requests for the login page
def login_route():
    if request.method == "POST":
        # Retrieve the username and password from the form submission and attempt to authenticate the user
        username = authenticate(
            request.form.get("username", ""),
            request.form.get("password", ""),
        )
        if username is None:
            flash("Invalid username or password.", "error")
            return render_template("login.html")

        # If authentication is successful, log the user in and redirect to the next page or bookings page
        login_user(username)
        flash("You have been logged in successfully.", "success")

        # Check to ensure the next_url is a relative URL to prevent open redirects
        next_url = request.args.get("next") or url_for("bookings")
        if not next_url.startswith("/") or next_url.startswith("//"):
            next_url = url_for("bookings")
        return redirect(next_url)

    # If the request method is GET, render the login page
    return render_template("login.html")