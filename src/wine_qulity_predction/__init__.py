import os
import logging
import sys


log_dir=f'logs'
logging_path=os.path.join(log_dir,'logging.log')

logging_format='[%(asctime)s : %(levelname)s : %(module)s : %(message)s] '

os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_format,

    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(logging_path)
    ]
)

logger=logging.getLogger("wineQualityPrediction")
