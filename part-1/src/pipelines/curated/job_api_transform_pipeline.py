import logging
from util.file_handler import FileHandler

LOGGER = logging.getLogger(__name__)

class JobApiTransformPipeline:
    def __init__(self):
        self.file_handler = FileHandler("JOB-API-v1")
    
    def run_pipeline(self):
        LOGGER.info("transforming CAR-API-v1")
        new_files = self.file_handler.track_new_files()
        data = self.file_handler.combine_csv_files(new_files)
        self.file_handler.save_to_csv_bulk(data, layer='curated')
