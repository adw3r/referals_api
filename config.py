from configparser import ConfigParser
import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent
CONFIG = ConfigParser()
CONFIG.read(pathlib.Path(PACKAGE_FOLDER, 'config.ini'))
GENERAL_CONFIG = CONFIG['general']

DEBUG = os.environ.get('DEBUG', False)
GENERAL_CONFIG['DEBUG'] = DEBUG
DEBUG = GENERAL_CONFIG.getboolean('DEBUG')


if not DEBUG:
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = os.environ.get('PORT', 8183)
else:
    HOST = os.environ.get('TEST_HOST', 'localhost')
    PORT = os.environ.get('TEST_PORT', 8283)
