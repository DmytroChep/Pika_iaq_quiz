import flask 

login_app = flask.Blueprint(
    name = "login",
    import_name= "app",
    template_folder= "login/templates",
    static_url_path = "/login/",
    static_folder = "/login/static",

)
