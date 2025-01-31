from jinja2 import Template


student_template_file = "templates/message_student.txt"
with open(student_template_file, "r") as file:
    student_template = file.read()

founder_template_file = "templates/message_founder.txt"
with open(founder_template_file, "r") as file:
    founder_template = file.read()

employee_template_file = "templates/message_employee.txt"
with open(employee_template_file, "r") as file:
    employee_template = file.read()

# profile_details must contain
# student = true/False
# student_college_name
# founder = true/False
# founding_company_name
# current_company_name
# current_company_tenure

def select_welcome_message(profile_details):
    print(f"selecting welcome message...")
    if(profile_details["student"]):
        template = Template(student_template)
        #print(f"welcome message selected for student")
        return template.render(profile_details)
    elif(profile_details["founder"]):
        template = Template(founder_template)
        #print(f"welcome message selected for founder")
        return template.render(profile_details)
    else:
        template = Template(employee_template)
        #print(f"welcome message selected for employee")
        return template.render(profile_details)