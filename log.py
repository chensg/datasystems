import logging
from pathlib import Path
from datetime import date

def setup_logger(name):
    logger = logging.getLogger(name)

    # set logging level
    logger.setLevel(logging.DEBUG)

    # set log file name
    date_str = date.today().strftime("%Y%m%d")
    log_file = Path('data', 'log', f"{date_str}.log")

    # set logging handlers, logging will display on console as well
    file_handler = logging.FileHandler(log_file, mode = 'w')
    file_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # set formatter
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s', datefmt='%H:%M:%S')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger