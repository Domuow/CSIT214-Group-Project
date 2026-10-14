
**This a document to keep track and record changes/addition/recomendation/etc to the program**

**Can also keep track of any sites/refrence which aided in helping build the softare i.e. w3schools**

19/09:
- Created a layout.html page for all html pages to inhrent from, contains a basic navigation bar as well as comon html elements
- Added some basic logic for searching for a facility without using DB (To be implemented)
- Created a basic html page for facilites to showcase available facilities utilising static data
- Implemented a form for user to search for facilites (BACKEND TBC)
- Implemented flash messaging in flask to display messages to user

25/09:
- Fixed flash messages bug
- Changed search form into post
- Added place holder and debugging logic for post method
- Added post route in main.py which returns a function from facilities.py
- Post method still needs some tweaking and will be improved in new branch

1/10:
- Created database
- DB 1.1:
    - Refactored facililites.py
    - Added DB functionality for facilities
    - Improved html file for facilities
    - Removed irelevnat js
- Updated readme & documentation
- B1.0:
    - Added booking functionality
    - Added booking HTML
    - Added and altered booking route
    - Added booking data handling in database.py

4/10:
- Megred pull request 2:
    - Created facilllities.css in order to style the facilities.html page

12/10:
- Merged pull request 3:
    - Improved overall css styling 
    - Added css styling for navigation bar
    - Created bookings html page specific styling

- Merged Staff Branch (STAFf 1.0)
    - Added staff dashboard
    - Created staff approval for bookings (appove/cancell)
    - Created 3 status for bookings, pending, approved and cancelled
    - Made it so existing DB entries would default to pending
    - Updated db.py to reflect these changes

- Removed developemnt elements
- Updated footer & flash styling

13/10:
- Merge pull request 5:
    - Added/fixed prefill booking from 
    - Fixed some css issues
    - Improveed some css


- Created login system (merge 6):
    - Added login/logout routes & logic to login.py
    - Added the login page in login.html
    - Protected both staff page routes so only the admin account can access them
    - Hid the Staff navigation link from normal users in layout.html
    - Restricted the bookings page to logged-in users
    - Users now only see bookings associated with their logged-in account email
    - New bookings automatically use the logged-in user’s name and email in bookings.py
    - Updated account and usage details in README.md

14/10:
- Completed final testing