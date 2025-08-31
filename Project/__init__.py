from .settings import project 
from .urls import *
from .db import *
from .loadenv import execute
from .login_manager import *

import registration
import core
import tests


project.register_blueprint(blueprint= core.core_app)
project.register_blueprint(blueprint= registration.reg_app)

project.register_blueprint(blueprint= user_profile.user_profile)
project.register_blueprint(blueprint= tests.tests_app)

