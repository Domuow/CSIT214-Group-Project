# This is just a placeholder file - name, contents and locaiton my change

# Plan is have data (query data) in the website link of page which will contain things like data and time,
# The data will be used to populate the booking page with the relevant data. If no data is avilable it will show a list of facilites manged by the company

# facilities for the purpose of the prototype, will have only 3 facilities

from flask import flash, render_template, request

# Temp Data for the facilities page - to be replaced with actual data from the database when implemented
facilities_data = [
    {"name": "Facility 1", "description": "Description of Facility 1"},
    {"name": "Facility 2", "description": "Description of Facility 2"},
    {"name": "Facility 3", "description": "Description of Facility 3"},
]

# Placeholder function for the facilities route
def facilities_main():

    # This function will be further implemented later to handle the logic for the facilities page
    get_url_data()  # Call the function to get data from the URL parameters
    return render_template("facilities.html", facilities=get_facilities_data())

# Still working on this function - will be used to get the data from the URL parameters and return it to the facilities_main function
def get_url_data():
    # This function will be further implemented later to fetch and return the relevant data from the URL for the facilities page
    date = request.args.get('date')
    start_time = request.args.get('start-time')
    end_time = request.args.get('end-time')

    # Debugging prints to check the values of the URL parameters
    print(date)
    print(start_time)
    print(end_time)

    # If all three parameters are empty, return None - TO BE FIXED
    if date == '' and start_time == '' and end_time == '':
        return

    # Implement JS validation aswell as this
    if date == '' or start_time == '' or end_time == '':
        flash("Please provide the date aswell as the start and end times for the booking.") # Display a message to the user if either date is missing
        return
    
    return date, start_time, end_time # TO BE FIXED

def get_facilities_data():
    # Placeholder function to get facilities data
    # This function will be further implemented later to fetch and return the relevant data for the facilities page
    return facilities_data

# Query db for when the facilities are avaiable as specfied and only return the data for the facilites that are avaiable at that time and date
# If no data is avaiable it will show a list of facilites manged by the company 