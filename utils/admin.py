import sys
import logging


def setup_logging():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger


def install_tool():
  pass

def get_info_from_resource():
  pass
