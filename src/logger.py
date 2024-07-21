import logging
import os
from datetime import datetime

LOG_FILE =  f"{datetime.now().strftime('%Y-%m-%d')}.log"

log_path = os.path.join(os.getcwd(), "logs")

os.makedirs(os.path.join(os.getcwd(), "logs"), exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)    

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")