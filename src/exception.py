import sys
from src.logger import logging


def extract_error_details(error, error_detail: sys):
    """
    Extracts and formats the error details including the filename, line number, and error message.

    :param error: The error object.
    :param error_detail: The sys module, used to access exception information.
    :return: A formatted error message string.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error Occurred in script [{file_name}] at line [{line_number}] with message [{error}]"

    return error_message


class CustomException(Exception):
    """
    A custom exception class that enhances the standard Exception with detailed error information.
    """

    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = extract_error_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
