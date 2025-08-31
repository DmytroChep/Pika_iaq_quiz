import flask
from Project.toolbox import config_page

@config_page(template_name= 'tests.html')
def render_tests():
    return {}