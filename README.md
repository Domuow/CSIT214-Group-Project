# CSIT214-Group-Project

*CSIT214 Group Project task to develop Community Facility and Maintenance Management System*


1. In order for this program to run the flask package needed to be installed by typing the following in terminal:

    ```bash
    pip install flask
    ```

2. The application creates `facilities.db` automatically when it starts. The SQLite database contains:
    - `facilities`: facility name, description and capacity.
    - `bookings`: saved facility bookings, the booker's contact details and a
      `Pending`, `Approved` or `Cancelled` status.

3. Log in at `/login` to create bookings and view your own bookings. The
   prototype has two hardcoded accounts:
   - User: `user` / `user123`
   - Staff administrator: `admin` / `admin123`

4. Staff functionality is available at `/staff` only after logging in as the
   staff administrator. Staff can review saved booking requests and approve or
   cancel them. This is an initial workflow prototype of the wider system.