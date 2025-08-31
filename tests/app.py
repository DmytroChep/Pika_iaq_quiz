import flask 

tests_app = flask.Blueprint(
    name = "tests",
    import_name= "tests",
    template_folder= "templates",
    static_url_path = "/tests/static/",
    static_folder = "static",

)
