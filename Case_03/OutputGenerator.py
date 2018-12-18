from jinja2 import Environment, FileSystemLoader

# Pass the directory containing the templates. "." uses the current directory
file_loader = FileSystemLoader(".")
# Load the environment.
env = Environment(loader=file_loader)
# Load the template.
template = env.get_template("info.template")
# Pass the variables.
name = ["Anupam", "Anurag", "Sandeep"]
output = template.render(NameList = name)
# Print the output
print(output)
