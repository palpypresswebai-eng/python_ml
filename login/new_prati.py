import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        # logging.FileHandler('pratice.log'),
        logging.FileHandler("C:\\Users\\pypre\\OneDrive\\Desktop\\python_ML\\login\\app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("arthmaticapp")

def app(a,b):
    result= a+b
    logger.debug(f'adding {a}+{b}={result}')
    return result 


def subtract(a,b):
    result= a-b
    logger.debug(f'adding {a}-{b} = {result}')
    return result 

def multiply(a,b):
    result= a*b
    logger.debug(f'adding {a}*{b}={result}')
    return result 

def divide(a,b):
    try:
        result = a/b
        logger.debug(f'dividing {a}/{b}= {result}')
        return result
    except ZeroDivisionError:
        logger.error("divide by zero error")
        return None
    
app(5,5)
subtract(5,5)
multiply(5,5)
divide(10,0)