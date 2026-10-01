from flask import flash, render_template, request

from database import get_facilities

def facilities_main():
    return render_template(
        "facilities.html",
        facilities=get_facilities(),
        search={"date": "", "start_time": "", "end_time": ""},
        searched=False,
    )

# Handles the form submission for searching facilities based on date and time
def facilities_post():
    date = request.form.get("date", "")
    start_time = request.form.get("start-time", "")
    end_time = request.form.get("end-time", "")
    search = {"date": date, "start_time": start_time, "end_time": end_time}

    # If any of the date, start time, or end time values are missing, flash an error message and return the facilities page with the current search values and a flag indicating that a search was attempted
    if not all(search.values()):
        flash("Please provide a date, start time and end time.", "error")
        return render_template("facilities.html", facilities=get_facilities(), search=search, searched=False)

    # If all values are provided, retrieve the available facilities based on the specified date and time range and return the facilities page with the search results and a flag indicating that a search was performed
    facilities = get_facilities(date, start_time, end_time)
    return render_template("facilities.html", facilities=facilities, search=search, searched=True)