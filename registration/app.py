import flask 
import os

reg_app = flask.Blueprint(
    name = "registration",
    import_name= "registration",
    template_folder= "templates",
    static_url_path = "/registration/static",
    static_folder = "static",

)
