from jinja2 import Environment, FileSystemLoader
# class Render:
def my_render(file_to_render, **keyargs):
    file_loader = FileSystemLoader("template")
    env = Environment(loader=file_loader)
    template = env.get_template(file_to_render)
    output = template.render(**keyargs)
    return output

