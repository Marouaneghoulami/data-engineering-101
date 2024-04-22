"""Common functions for all API Handling."""
from io import StringIO
import logging
import requests
import pandas as pd
from util.config_handler import ConfigHandler
from util.exceptions import RequestException


LOGGER = logging.getLogger(__name__)

class ApiHandler:
    """Class for API Hanlder Functionalities."""
    def __init__(self, api_name):
        self.config_handler = ConfigHandler()
        self.api_name = api_name
        self.api_url = self.config_handler.get_api_url(api_name)

    def get_data(self):
        """Call API and save data to CSV file."""
        LOGGER.info("fetching new data...")
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            LOGGER.info("data was successfully retrieved.")
            return pd.read_csv(StringIO(response.text))
        except Exception as e:
            raise RequestException("failed to fetch data from API") from e
