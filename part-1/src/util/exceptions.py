"""Common Exceptions handled in Util package"""
class ApiException(Exception):
    """Custom exception for API errors."""

class FileException(Exception):
    """Custom exception for File errors."""

class RequestException(ApiException):
    """Class for API Request Exception."""

class InvalidValueException(FileException):
    """Class for Invalida Data Layer Exception."""
