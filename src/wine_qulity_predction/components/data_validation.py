from urllib import request
from src.wine_qulity_predction import logger
import os
import pandas as pd
from src.wine_qulity_predction.entity.config_entity import DataValidationConfig
class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def valiadate_all_columns(self) ->bool:
        try:
            validation_status=None

            data=pd.read_csv(self.config.unzip_data_dir)
            all_col=list(data.columns)

            all_schema=self.config.all_schema.keys()

            flag=True
            for col in all_col:
                if col not in all_schema:
                    validation_status="False"
                    flag=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"validation status: {validation_status}")
                    break

            if flag!=False:
                validation_status="True"
                with open(self.config.STATUS_FILE,'w') as f:
                    f.write(f"validation status: {validation_status}")

        except Exception as e:
            raise e




