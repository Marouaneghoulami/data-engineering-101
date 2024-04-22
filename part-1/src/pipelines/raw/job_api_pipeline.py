import logging
from util.api_handler import ApiHandler
from util.file_handler import FileHandler

LOGGER = logging.getLogger(__name__)

class JobApiPipeline:
    def __init__(self):
        self.api_handler = ApiHandler("JOB-API-v1")
        self.file_handler = FileHandler("JOB-API-v1")
    
    def run_pipeline(self):
        LOGGER.info("calling JOB-API-v1")
        data = self.api_handler.get_data()
        self.file_handler.save_to_csv_bulk(data)
