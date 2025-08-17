import os
from dotenv import load_dotenv

# load environment variables from the .env file located in the project root (src folder)
load_dotenv()

# Database file name and debug mode flag
DATABASE = os.getenv("DATABASE", "my_survey.db")
DEBUG = os.getenv("DEBUG", "True").lower() =="true"