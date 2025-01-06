from datetime import datetime  # For timestamps

def get_timestamp():
    """
    Get the current timestamp in a readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")