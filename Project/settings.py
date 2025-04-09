import flask
import flask_migrate
import flask_sqlalchemy


import os

project = flask.Flask(
    import_name= "Project",
    template_folder= "templates",
    static_url_path = "/static/",
    static_folder = "static",
    instance_path=os.path.abspath(__file__ + "/.."),
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)
MIGRATE = flask_migrate.Migrate(app= project, db = DATABASE)


#project.register_blueprint(blueprint= core_app)
#project.register_blueprint(blueprint= reg_app)

