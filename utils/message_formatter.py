from jinja2 import Template

TEMPLATE_FILE = "templates/message.txt"
with open(TEMPLATE_FILE, "r") as file:
    TEMPLATE = file.read()

def generate_message(data):
    template = Template(TEMPLATE)
    return template.render(data)
