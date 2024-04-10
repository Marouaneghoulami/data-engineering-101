"""Car API Raw layer Pipeline"""
import logging
from util.api_handler import ApiHandler
from util.file_handler import FileHandler

LOGGER = logging.getLogger(__name__)

class CarApiPipeline:
    def __init__(self):
        self.api_handler = ApiHandler("CAR-API-v1")
        self.file_handler = FileHandler("CAR-API-v1")

    def run_pipeline(self):
        LOGGER.info("calling CAR-API-v1")
        data = self.api_handler.get_data()
        self.file_handler.save_to_csv_bulk(data)
