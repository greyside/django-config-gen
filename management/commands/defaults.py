import __main__
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__main__.__file__))
LOG_DIR = os.path.join(PROJECT_ROOT ,'logs')

_config_dir = os.path.join(PROJECT_ROOT ,'config')
TEMPLATES_DIR = os.path.join(_config_dir ,'templates')
GENERATED_DIR = os.path.join(_config_dir ,'generated')
