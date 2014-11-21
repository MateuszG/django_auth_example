django_auth_example
===================

Simple auth on Django 1.7

Scenarios (as incogito):

1) New user:
- Register
- Login
- Status: Default settings (en/en)
- Set language to (pl/pl) language/pl/
- Status: (pl/pl)
- Logout logout/
- Status: (pl/None) # cookies exist / no session

2) Returning user:
- Login
- Status: (pl/en) # cookies exist / session for user is default

3) Returning user (closed browser):
- Login
- Status: (en/en) # cookies not exist / session for user is default
