import flask 

user_profile = flask.Blueprint(
    name = "user_profile",
    import_name= "user_profile",
    template_folder= "templates",
    static_url_path = "/user_profile/static/",
    static_folder = "static",

)
