import logging

logging.basicConfig(
    filename='Pal.log',
    filemode='w',   # must be lowercase
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)