import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

prooject_name="wine_qulity_predction"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{prooject_name}/__init__.py", 
    f"src/{prooject_name}/components/__init__.py", 
    f"src/{prooject_name}/utils/__init__.py", 
    f"src/{prooject_name}/utils/common.py", 
    f"src/{prooject_name}/config/__init__.py", 
    f"src/{prooject_name}/config/configuration.py", 
    f"src/{prooject_name}/pipeline/__init__.py", 
    f"src/{prooject_name}/entity/__init__.py", 
    f"src/{prooject_name}/entity/config_entity.py", 
    f"src/{prooject_name}/constants/__init__.py", 
    "config/config.yml",
    'params.yml',
    "schema.yml",
    'main.py',
    'Dockerfile',
    'setup.py',
    'research.ipynb',
    'templates/index.html'
]

for file_path in list_of_files:
    filepath=Path(file_path)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as file:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")