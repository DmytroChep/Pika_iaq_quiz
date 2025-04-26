import flask 

core_app = flask.Blueprint(
    name = "core",
    import_name= "core",
    template_folder= "templates",
    static_url_path = "/core/static/",
    static_folder = "static",

)
