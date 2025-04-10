from .settings import project


import regestration
import core
import login


core.core_app.add_url_rule(rule="/", view_func=core.render_core, methods=["GET", "POST"])
regestration.reg_app.add_url_rule(rule="/registration/", view_func=regestration.render_registration, methods=["GET", "POST"])
login.login_app.add_url_rule(rule="/login/", view_func=login.render_login, methods=["GET", "POST"])



project.register_blueprint(blueprint= core.core_app)
project.register_blueprint(blueprint= regestration.reg_app)
project.register_blueprint(blueprint= login.login_app)


