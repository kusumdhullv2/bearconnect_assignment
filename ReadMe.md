# Application Structure
Assignment                  -> Main Project folder
- app.py                    -> Main Application file
- utils                     -> sub-folder for utilities
  - linkedin_scrapper.py    -> python file for getting linkedin profile information
  - message_formatter.py    -> python file for creating a main message to be sent
  - message_selector.py     -> python file for selecting the welcome message based on profile type/information
- templates                 -> sub-folder for message templates
  - message.txt             -> template for the main message
  - message_employee.txt    -> template for employee welcome message
  - message_founder.txt     -> template for founder welcome message
  - message_student.txt     -> template for student welcome message
- testData                  -> sub-folder for test data
  - profiles.csv            -> sample csv of linked-in profiles

# Python libraries used.
- fastapi           -> for creating HTTP REST API
- uvicorn           -> ASGI Web Server for hosting web apps
- jinja2            -> for templates handling
- pandas            -> CSV handling
- requests          -> HTTP library
- linkedin-api      -> for getting linked-in profiles information

# Prerequisite

This application uses a third party library *linkedin-api*, which requires an existing linkedin account. So we will need to provide 2 environment variables:
- ASSIGNMENT_USERNAME
- ASSIGNMENT_PASSWORD

**Do not use *personal* linkedin credentials**

# Running the application

## Before Running install these dependencies
pip install fastapi uvicorn jinja2 pandas requests linkedin-api python-multipart

## use this command to run the application
uvicorn app:app --reload

# Usage
Call the URL http://<HOST_URL>:<HOST_PORT>/process as a HTTP POST, with the payload as CSV file.

## Postman

- HTTP Method : POST
- URL : http://localhost:8000/process
- Body : 
  - Body Type : form-data
  - Key : file
  - Key-Type : file
  - Value : Select input CSV file from your machine.

