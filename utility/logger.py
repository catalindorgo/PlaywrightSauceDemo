import logging
from reportportal_client import RPLogger


def configure_logging(name=None):

    #Create loggerr
    logging.setLoggerClass(RPLogger)
    logger = logging.getLogger(name if name else __name__)
    logger.setLevel(logging.DEBUG)
    return logger

if __name__ == '__main__':
    pass