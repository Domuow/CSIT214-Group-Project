from flask import flash, redirect, render_template, request, url_for

from database import create_booking, get_bookings, get_facilities


def bookings_main():
	return render_template("bookings.html", bookings=get_bookings(), facilities=get_facilities())


def bookings_post():
	try:
		create_booking(
			request.form.get("facility_id", type=int),
			request.form.get("date", ""),
			request.form.get("start-time", ""),
			request.form.get("end-time", ""),
			request.form.get("booker_name", ""),
			request.form.get("booker_email", ""),
		)
	except ValueError as error:
		flash(str(error), "error")
	else:
		flash("Booking saved successfully.", "success")
	return redirect(url_for("bookings"))