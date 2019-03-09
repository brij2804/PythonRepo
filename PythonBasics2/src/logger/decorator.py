import logging
formatter = logging.Formatter('%(asctime)s %(message)s')


def log_file(name,file_name,level=logging.INFO):
    # Create and configure logger
    handler= logging.FileHandler(file_name)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

