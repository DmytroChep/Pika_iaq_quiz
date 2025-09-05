from .settings import project


import registration
import core
import user_profile
import tests



core.core_app.add_url_rule(rule="/", view_func=core.render_core)
registration.reg_app.add_url_rule(rule="/registration", view_func=registration.render_registration, methods=["GET", "POST"])
registration.reg_app.add_url_rule(rule="/login", view_func=registration.render_login, methods=["GET", "POST"])
user_profile.user_profile.add_url_rule(rule="/profile", view_func=user_profile.render_user_profile, methods=["GET", "POST"])
tests.tests_app.add_url_rule(rule="/tests", view_func=tests.render_tests, methods=["GET", "POST"])
#
#project.add_url_rule(
#    rule='/registration',
#    view_func=registration.render_registration,
#    methods=['GET', 'POST']
#)
#project.add_url_rule(
#    rule = '/login',
#    view_func = registration.render_login,
#    methods = ['GET','POST']
#)