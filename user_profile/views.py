import flask
from Project.toolbox import config_page

@config_page(template_name= 'profile.html')
def render_user_profile():
    return {}