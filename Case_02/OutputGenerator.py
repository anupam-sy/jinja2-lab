from jinja2 import Environment, FileSystemLoader

# Pass the directory containing the templates. "." uses the current directory
file_loader = FileSystemLoader(".")
# Load the environment.
env = Environment(loader=file_loader)
# Load the template.
template = env.get_template("info.template")
# Pass the variables.
output = template.render(truth=True)
# Print the output
print(output)
