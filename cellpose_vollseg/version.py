from importlib.metadata import PackageNotFoundError, version
import sys 
from platform import python_version
import torch 

version = "0.0.3"

version_str = f"""
cellpose version: \t{version} 
platform:       \t{sys.platform} 
python version: \t{python_version()} 
torch version:  \t{torch.__version__}"""