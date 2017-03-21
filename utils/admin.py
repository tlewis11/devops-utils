import logging
def setup_logging():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    return logger
