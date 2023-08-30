import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="ML-project"

list_file_name=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components.py/__init__.py",
    f"src/{project_name}/components.py/data_ingestion.py",
    f"src/{project_name}/components.py/data_transformation.py",
    f"src/{project_name}/components.py/model_trainer.py",
    f"src/{project_name}/components.py/model_monitoring.py",
    f"src/{project_name}/pipline.py/__init__.py",
    f"src/{project_name}/pipline.py/traning_pipline.py",
    f"src/{project_name}/pipline.py/prediction_pipline",
    f"src/{project_name}/exeption.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "dockerfile",
    "requirments.txt",
    "setup.py",   
]
for filepath in list_file_name:
    filepath=Path(filepath)
    filedir, filename  = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} is already exists")