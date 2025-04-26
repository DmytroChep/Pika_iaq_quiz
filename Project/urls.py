from .settings import project


import registration
import core




core.core_app.add_url_rule(rule="/", view_func=core.render_core)
registration.reg_app.add_url_rule(rule="/registration/", view_func=registration.render_registration, methods=["GET", "POST"])
registration.reg_app.add_url_rule(rule="/login/", view_func=registration.render_login, methods=["GET", "POST"])



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