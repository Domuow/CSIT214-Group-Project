
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