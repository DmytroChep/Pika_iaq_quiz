import flask
import flask_migrate
import flask_sqlalchemy

project = flask.Flask(
    import_name= "Project",
    template_folder= "templates",
    static_url_path = "/static/",
    static_folder = "static",
)

project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = project)
MIGRATE = flask_migrate.Migrate(app= project, db = DATABASE)