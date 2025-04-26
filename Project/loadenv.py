import dotenv
import os

PATH = os.path.abspath(os.path.join(__file__, "..", '..', ".env"))

#dotenv.load_dotenv(dotenv_path= PATH)

def execute():
    if os.path.exists(PATH):
        if not os.path.exists(os.path.abspath(os.path.join(__file__, '..', "migrations"))):
            os.system(os.environ["DB_INIT"])
        
        os.system(os.environ["DB_MIGRATE"])
        os.system(os.environ["DB_UPGRADE"])