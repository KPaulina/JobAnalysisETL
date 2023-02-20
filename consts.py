import os
import dotenv
from datetime import datetime

DATE = str(datetime.now())[:10]

dotenv.load_dotenv()

MANGODB_CONNECTION = os.getenv('MANGODB_CONNECTION')
DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')
