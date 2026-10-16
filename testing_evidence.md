# Basic Testing Evidence

**Project:** CSIT214 Community Facility and Maintenance Management System  
**Date tested:** 16 October 2026  
**Test type:** Basic Flask route smoke testing

## Purpose

This document records basic evidence that the main Flask routes respond correctly and
that the implemented authentication and validation guards behave as expected.

## Test environment

- Python application started through the Flask test client.
- Flask application configured with `TESTING=True`.
- Existing project database: `facilities.db`.
- No separate automated test framework is currently included in the repository.

## Smoke-test command

The following check was run from the project root:

```powershell
@'
from app import app

app.config.update(TESTING=True)
client = app.test_client()
checks = []

response = client.get("/")
checks.append(("GET / returns 200", response.status_code == 200))

response = client.get("/facilities")
checks.append(("GET /facilities returns 200", response.status_code == 200))

response = client.get("/bookings")
checks.append((
    "Unauthenticated /bookings redirects to login",
    response.status_code == 302 and "/login" in response.headers.get("Location", "")
))

response = client.get("/staff")
checks.append((
    "Unauthenticated /staff redirects to login",
    response.status_code == 302 and "/login" in response.headers.get("Location", "")
))

response = client.post(
    "/facilities_search",
    data={"date": "", "start-time": "", "end-time": ""}
)
checks.append((
    "Incomplete facility search returns 200 with validation message",
    response.status_code == 200
    and b"Please provide a date" in response.data
))

response = client.post(
    "/login",
    data={"username": "user", "password": "user123"}
)
checks.append((
    "Valid user login redirects to bookings",
    response.status_code == 302
    and "/bookings" in response.headers.get("Location", "")
))

response = client.get("/staff")
checks.append((
    "Normal user is denied staff access",
    response.status_code == 302
    and "/bookings" in response.headers.get("Location", "")
))

for name, passed in checks:
    print(("PASS" if passed else "FAIL") + " - " + name)

if not all(passed for _, passed in checks):
    raise SystemExit(1)
print("smoke checks: PASS ({0}/{0})".format(len(checks)))
'@ | python -
```

## Results

| Check | Expected result | Observed result |
|---|---|---|
| `GET /` | HTTP 200 | **PASS** |
| `GET /facilities` | HTTP 200 | **PASS** |
| Unauthenticated `GET /bookings` | Redirects to `/login` | **PASS** |
| Unauthenticated `GET /staff` | Redirects to `/login` | **PASS** |
| Incomplete facility search | HTTP 200 with validation feedback | **PASS** |
| Valid user login | Redirects to `/bookings` | **PASS** |
| Normal user access to `/staff` | Redirects to `/bookings` | **PASS** |

**Summary:** `smoke checks: PASS (7/7)`

## Additional manual tests

The following are scenarios which where tested manually:

1. Create a booking using a future date and confirm it appears for the logged-in user.
2. Attempt a booking with a past date, invalid time range, missing contact details, or an unknown facility.
3. Attempt an overlapping booking and confirm the conflict is rejected.
4. Log in as the staff administrator and approve or cancel a pending booking.
6. Log out and confirm protected pages require authentication again.
