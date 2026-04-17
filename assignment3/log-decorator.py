import logging

def logger_decorator(*args, **kwargs):
    logger = logging.getLogger(__name__ + "_parameter_log")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.FileHandler("./decorator.log","a"))
    logger.log(logging.INFO, "this string would be logged")

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def my_second_function(*args, **kwargs):
    return logger_decorator()

logger_decorator()
hello_world()
my_second_function()
