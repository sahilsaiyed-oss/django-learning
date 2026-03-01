from functools import wraps
from datetime import datetime


def log_execution_time(func):
    """
    Decorator to log function execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()

        execution_time = (end_time - start_time).total_seconds()
        print(f"Function '{func.__name__}' executed in {execution_time} seconds")

        return result

    return wrapper


def require_non_empty_input(func):
    """
    Decorator to ensure input text is not empty.
    """

    @wraps(func)
    def wrapper(text, *args, **kwargs):
        if not text or not text.strip():
            raise ValueError("Input cannot be empty.")
        return func(text, *args, **kwargs)

    return wrapper
