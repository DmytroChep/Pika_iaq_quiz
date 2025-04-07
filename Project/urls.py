import core
from .settings import project


core.core_app.add_url_rule(rule="/", view_func=core.render_core, methods=["GET", "POST"])



project.register_blueprint(blueprint= core.core_app)