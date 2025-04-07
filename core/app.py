import flask 

core_app = flask.Blueprint(
    name = "core",
    import_name= "app",
    template_folder= "core/templates",
    static_url_path = "/core/",
    static_folder = "core/static",

)
