import configparser
import time

config = configparser.ConfigParser()

try:
    config.read("../config/config.ini")
    retry_attempts = config.getint("Retry", "retry_attempts")
    retry_delay = config.getint("Retry", "retry_delay")
except configparser.NoSectionError:
    # Handle the case where the [Retry] section is missing
    print("No Section Error")
    retry_attempts = 3
    retry_delay = 5
except configparser.NoOptionError:
    # Handle the case where retry_attempts or retry_delay is missing
    print("No Option Error")
    retry_attempts = 3
    retry_delay = 5

def retry(func):
    """
    Decorator to retry a function call multiple times if an exception is raised.

    Args:
        func: The function to decorate.

    Returns:
        The decorated function.
    """
    def wrapper(*args, **kwargs):
        for attempt in range(retry_attempts):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt < retry_attempts - 1:
                    print(f"Attempt {attempt+1} failed, retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    raise e
    return wrapper
