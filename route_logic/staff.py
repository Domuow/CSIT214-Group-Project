# This file contains the logic for handling staff-related routes

from flask import flash, redirect, render_template, request, url_for
from database import get_bookings, update_booking_status

# Define the main route for staff to view all bookings. Displays all the bookings in the system, allowing staff to manage and update their status
def staff_main():
    return render_template("staff.html", bookings=get_bookings())

# Define the route for staff to update the status of a booking - handles the form submission from the staff page, allowing staff to approve or cancel bookings
def staff_post():
    booking_id = request.form.get("booking_id", type=int)
    status = request.form.get("status", "")

    try:
        update_booking_status(booking_id, status)
    except ValueError as error:
        flash(str(error), "error")
    else:
        flash(f"Booking {status.lower()} successfully.", "success")

    return redirect(url_for("staff"))