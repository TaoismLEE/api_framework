# -*- coding:utf-8 -*-

import logging.config
from config.setting import PROJECT_PATH

# read logger config file
logging.config.fileConfig(PROJECT_PATH + '/config/logger.ini')

# select logger object
logger = logging.getLogger("loggerObj")
