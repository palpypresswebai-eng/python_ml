# 1. Write a Python function to create a basic logger that logs messages to a file named `app.log`.

import logging


# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',
#     handlers=[
#         logging.FileHandler('app.log'),
#         logging.StreamHandler()
#     ]
# )

# logger = logging.getLogger("print_name")

# def write_name():
#     logger.debug("this is a debige meds.")
#     logger.error("this is a error meds.")
#     logger.info("this is a info meds.")
#     logger.warning("this is a warning meds.")
#     logger.critical("this is a CRITICAL meds.")

# write_name()

# 2. Write a Python function to create a logger that logs messages to both a file named `app.log` and the console.


# import logging

# def logger_with_handlers():
#     logger = logging.getLogger('my_logger')
#     logger.setLevel(logging.DEBUG)
    
#     file_handler = logging.FileHandler('app.log')
#     console_handler = logging.StreamHandler()
    
#     file_handler.setLevel(logging.DEBUG)
#     console_handler.setLevel(logging.DEBUG)
    
#     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     file_handler.setFormatter(formatter)
#     console_handler.setFormatter(formatter)
    
#     logger.addHandler(file_handler)
#     logger.addHandler(console_handler)
    
#     logger.debug('This is a debug message')
#     logger.info('This is an info message')
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')

# # Test the function
# logger_with_handlers()


# 1. Write a Python function to create a logger with a custom log message format that includes the timestamp, 
# logging level, and message.

# def logger_with_custom_format():
#     logger = logging.getLogger('custom_name')
#     logger.setLevel(logging.DEBUG)

#     file_handler = logging.FileHandler("custom_name.log")
#     console_name = logging.StreamHandler()

#     formatter= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
#                                  datefmt='%d-%m-%Y %H:%M:%S')
#     file_handler.setFormatter(formatter)
#     console_name.setFormatter(formatter)

#     logger.addHandler(file_handler)
#     logger.addHandler(console_name)

    
#     logger.debug('This is a debug message')
#     logger.info('This is an info message')
#     logger.warning('This is a warning message')
#     logger.error('This is an error message')
#     logger.critical('This is a critical message')

# logger_with_custom_format()




