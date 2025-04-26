import flask
import flask_migrate
import flask_sqlalchemy


import os

project = flask.Flask(
    import_name= "Project",
    template_folder= "templates",
    static_url_path = "/static",
    static_folder = "static",
    instance_path= os.path.abspath(os.path.join(__file__, '..', 'instance')),
)


