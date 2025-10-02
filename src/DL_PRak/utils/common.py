import os
from box.exceptions import BoxValueEroor
import yaml
from DL_PRak import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations  #decorator
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    """ 
    read your yaml fileand returns 
    
    Args : path_to_yaml
    
    raises: 
    ValueError : if yaml file is empty
    e : empty file
    
    Returns :
    ConfigBox : COnfigBox type
    """ 
    try :
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueEroor:
        return ValueError("yaml file is empty") 
    except Exception as e:
        return e
    

@ensure_annotations
def create_dictionaries(path_to_dictionaries: list , verbose = True):
    """
    create list of directories
    
ARGS : 
     path_to_directories (list ): lit of path of directories
     ignore_log(bool,optional) : ignore if multiple dirs is to be created """

@ensure_annotations
def save_json(path: Path, data : dict):
    with open(path , "w") as f:
    json.dump(data,f, indent = 4)

logger.info(f" json file saved as : {path} ")
""" save json data
ARGS : 
path(Path) :path to json file
data(Dict) : data to be save in json file """





@ensure_annotations
def load_json(path :  Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from : : {path}")
    return
    """
    load json files data
    
    args: path(Path) : path to json file
    
return : 
configbox : data as class attributes instead of dict  """

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

