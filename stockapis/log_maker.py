import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def debug(message):
    logging.debug(message)


def info(message):
    logging.error(message)


def error(message):
    logging.error(message)
