import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(handler)
logger.log(logging.INFO, "this string would be logged")

def logger_decorator(func):
    def wrapper_decorator(*args, **kwargs):
        pos_params = list(args)
        key_params = list(kwargs)
        value = func(*args, *kwargs)
        message = f"{func.__name__} \n {pos_params}{key_params} \n {value}"
        logger.info(message)
    return wrapper_decorator

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def my_second_function(*args, **kwargs):
    return True

@logger_decorator
def third_func(**kwargs):
    return logger_decorator

logger_decorator()
hello_world()
my_second_function()
