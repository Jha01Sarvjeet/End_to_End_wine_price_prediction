from urllib import request
from src.wine_qulity_predction import logger
import zipfile
import os
from src.wine_qulity_predction.entity.config_entity import (DataIngestionConfig)
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config


    #downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(url=self.config.source_url,
                                                filename=self.config.local_data_file)
            logger.info(f"{filename } download with following info {headers}")

        else:
            logger.info(f"file already exists")

    def zip_file_extract(self):
        """ zip file path: str
        extracts the zip into  the data directory
        Function returns None
        """

        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)


