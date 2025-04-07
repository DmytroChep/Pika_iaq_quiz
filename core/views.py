import flask

def render_core():
    return flask.render_template(template_name_or_list= "home.html")