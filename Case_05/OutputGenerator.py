from jinja2 import Environment, FileSystemLoader

# Pass the directory containing the templates. "." uses the current directory
file_loader = FileSystemLoader(".")
# Load the environment.
env = Environment(loader=file_loader)
# Load the template.
template = env.get_template("child.template")
# Pass the variables.
output = template.render(title = "Test", body="Hello World.")
# Print the output
print(output)
