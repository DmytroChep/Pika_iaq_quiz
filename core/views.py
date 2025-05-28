import flask
from Project.toolbox import config_page

@config_page(template_name= 'home.html')
def render_core():
    return {}