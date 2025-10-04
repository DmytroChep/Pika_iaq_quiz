from .settings import project


import registration
import core
import user_profile
import tests



core.core_app.add_url_rule(rule="/", view_func=core.render_core)
registration.reg_app.add_url_rule(rule="/registration", view_func=registration.render_registration, methods=["GET", "POST"])
registration.reg_app.add_url_rule(rule="/login", view_func=registration.render_login, methods=["GET", "POST"])
registration.reg_app.add_url_rule(rule="/logout", view_func= registration.render_logout, methods = ["GET", "POST"])
user_profile.user_profile.add_url_rule(rule="/profile", view_func=user_profile.render_user_profile, methods=["GET", "POST"])
tests.tests_app.add_url_rule(rule="/test_creation/", view_func=tests.render_tests, methods=["GET", "POST"])
tests.tests_app.add_url_rule(rule="/save_test", view_func=tests.save_test, methods=["GET", "POST"])
tests.tests_app.add_url_rule(rule="/test_passing/<int:test_id>", view_func=tests.render_tests_passing, methods=["GET", "POST"])
