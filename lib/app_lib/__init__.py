from os import environ

from lib.app_lib.classes.base import *  # NOQA
from lib.app_lib.classes.notification import *  # NOQA
from lib.app_lib.messages.message import *  # NOQA
from lib.app_lib.services.main import *  # NOQA
from lib.app_lib.services.notification_service import *  # NOQA
from lib.app_lib.connections import *  # NOQA
from lib.app_lib.enums import *  # NOQA
from lib.app_lib.log import *  # NOQA

DEBUG = environ.get('APP_ENV', '').lower() == 'test'
