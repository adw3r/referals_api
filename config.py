from configparser import ConfigParser
import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent
CONFIG = ConfigParser()
CONFIG.read(pathlib.Path(PACKAGE_FOLDER, 'config.ini'))
GENERAL_CONFIG = CONFIG['general']

DEBUG = os.environ.get('DEBUG')
GENERAL_CONFIG['DEBUG'] = DEBUG
DEBUG = GENERAL_CONFIG.getboolean('DEBUG', False)


if not DEBUG:
    HOST = GENERAL_CONFIG.get('HOST', '0.0.0.0')
    PORT = GENERAL_CONFIG.getint('PORT', 8185)
else:
    HOST = GENERAL_CONFIG.get('TEST_HOST', 'localhost')
    PORT = GENERAL_CONFIG.getint('TEST_PORT', 8285)
