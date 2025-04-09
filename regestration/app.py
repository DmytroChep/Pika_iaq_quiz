import flask 

reg_app = flask.Blueprint(
    name = "regestration",
    import_name= "app",
    template_folder= "regestration/templates",
    static_url_path = "/regestration/",
    static_folder = "/regestration/static",

)
