import os
import pandas as pd
from datetime import datetime
import logging
from util.config_handler import ConfigHandler
from util.exceptions import InvalidValueException

LOGGER = logging.getLogger(__name__)

class FileHandler:
    def __init__(self, source_prefix):
        self.config_handler = ConfigHandler()
        self.source_prefix = source_prefix
        self.directory = self.config_handler.get_raw_dir()
        self.raw_dir = self.config_handler.get_raw_dir()
        self.curated_dir = self.config_handler.get_curated_dir()
        self.registry_file = self.config_handler.get_registry_file()
    
    def save_to_csv_bulk(self, data, layer='raw'):
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{self.source_prefix}_{timestamp}.csv"
        # Save data to CSV file
        if layer == 'raw':
            file_path = os.path.join(self.raw_dir, filename)
        elif layer == 'curated':
            file_path = os.path.join(self.curated_dir, filename)
        else:
            raise InvalidValueException("invalid layer.")
        data.to_csv(file_path, index=False)
        LOGGER.info("data saved.")

    def combine_csv_files(self, file_list):
        data_frames = []
        for filename in file_list:
            LOGGER.info(f"loading {filename}...")
            file_path = os.path.join(self.raw_dir, filename)
            df = pd.read_csv(file_path)
            data_frames.append(df)
        combined_df = pd.concat(data_frames, ignore_index=True)
        LOGGER.info("data loaded.")
        return combined_df
    
    def track_new_files(self):
        all_files = self.list_files()
        processed_files = self.load_registry()
        new_files = [f for f in all_files if f not in processed_files]
        self.update_registry(new_files)
        LOGGER.info(f"listing new files. {new_files}")
        return new_files

    def list_files(self):
        files = [f for f in os.listdir(self.directory) if f.endswith(".csv") and f.startswith(self.source_prefix) and os.path.isfile(os.path.join(self.directory, f))]
        return files
    
    def load_registry(self):
        if not os.path.exists(self.registry_file):
            with open(self.registry_file, "w") as f:
                pass
            return set()
        else:
            with open(self.registry_file, "r") as f:
                return set(line.split("\t")[0] for line in f.read().splitlines())
    
    def update_registry(self, new_files):
        with open(self.registry_file, "a") as f:
            for filename in new_files:
                f.write(filename + "\t" + datetime.now().strftime("%Y-%m-%d-%H:%M:%S") + "\n")
