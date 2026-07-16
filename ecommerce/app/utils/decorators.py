import time

from app.utils.logger import logger


def log_execution(function):

    def wrapper(*args, **kwargs):

        logger.info(f"Executing {function.__name__}")

        return function(*args, **kwargs)

    return wrapper


def measure_time(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        logger.info(
            f"{function.__name__} completed in {(end-start):.4f} seconds"
        )

        return result

    return wrapper


def admin_only(function):

    def wrapper(*args, **kwargs):

        print("Admin Access Granted")

        return function(*args, **kwargs)

    return wrapper