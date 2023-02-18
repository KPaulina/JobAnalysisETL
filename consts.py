import os
import dotenv
from datetime import datetime

DATE = str(datetime.now())[:10]

dotenv.load_dotenv()

MANGODB_CONNECTION = os.getenv('MANGODB_CONNECTION')
