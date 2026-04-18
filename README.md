AccuKnox User Management Automation

Project Overview
This project automates the User Management module of OrangeHRM using Playwright with Python and Pytest using Page Object Model (POM).

Tech Stack
- Python
- Playwright
- Pytest

Project Structure
pages/ → Page Objects
tests/ → Test Cases
utils/ → Test Data

Setup Instructions

1. Install dependencies
pip install playwright pytest

2. Install browsers
playwright install

How to Run Tests
pytest -v -s tests/test_user_management.py

Features Automated
- Login to application
- Navigate to Admin module
- Add new user
- Search user
- Edit user details
- Delete user

Tool Version
Playwright (latest via pip)

