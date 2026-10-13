from flask import flash, redirect, render_template, request, url_for

from database import create_booking, get_bookings, get_facilities
from route_logic.login import current_user

# Handles the display of the bookings page, including retrieving the current user's bookings and available facilities for booking
def bookings_main():
	user = current_user()
	return render_template(
		"bookings.html",
		bookings=get_bookings(user["email"]),
		facilities=get_facilities(),
		booker_name=user["name"],
		booker_email=user["email"],
		facility_id=request.args.get("facility_id", None, type=int),
		date=request.args.get("date", None, type=str),
		start_time=request.args.get("start_time", None, type=str),
		end_time=request.args.get("end_time", None, type=str)
		)

# Handles the form submission for creating a new booking
def bookings_post():
	user = current_user()
	try:
		create_booking(
			request.form.get("facility_id", type=int),
			request.form.get("date", ""),
			request.form.get("start-time", ""),
			request.form.get("end-time", ""),
			user["name"],
			user["email"],
		)
	except ValueError as error:
		flash(str(error), "error")
	else:
		flash("Booking saved successfully.", "success")
	return redirect(url_for("bookings"))