import logging

def clean_data(data):
    # Helper function to clean and format data
    # ...
    return cleaned_data

def log_message(message, level="info"):
    # Helper function for logging messages
    logging.basicConfig(filename="compliance.log", level=logging.INFO)
    logger = logging.getLogger(__name__)
    getattr(logger, level)(message)
