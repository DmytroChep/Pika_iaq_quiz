import core
from .settings import project
import regestration
import core

core.core_app.add_url_rule(rule="/", view_func=core.render_core, methods=["GET", "POST"])

regestration.reg_app.add_url_rule(rule="/registration", view_func=regestration.render_registration, methods=["GET", "POST"])




project.register_blueprint(blueprint= core.core_app)
project.register_blueprint(blueprint= regestration.reg_app)



