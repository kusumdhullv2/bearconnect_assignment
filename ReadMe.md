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

# Before Running install these dependencies
pip install fastapi uvicorn jinja2 pandas requests linkedin-api python-multipart

# Python libraries used.
- fastapi           -> for creating HTTP REST API
- uvicorn           -> ASGI Web Server for hosting web apps
- jinja2            -> for templates handling
- pandas            -> CSV handling
- requests          -> HTTP library
- linkedin-api      -> for getting linked-in profiles information

# use this command to run the application
uvicorn app:app --reload
