"""Common functions for all Config Handling."""
import configparser

# This should be decalred in ENV VAR when writing Dockerfile
CONFIG_PATH_VAR = "part-1/src/config/config.ini"

class ConfigHandler:
    """Class for Config Hanlder Functionalities."""
    def __init__(self):
        self.config_path = CONFIG_PATH_VAR
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    def get_api_url(self, api_name):
        """Extracts API Url from config file."""
        return self.config.get(api_name, 'url')

    def get_raw_dir(self):
        """Extracts raw directory path from config file."""
        return self.config.get("Paths", 'raw_dir')

    def get_curated_dir(self):
        """Extracts curated directory path from config file."""
        return self.config.get("Paths", 'curated_dir')

    def get_registry_file(self):
        """Extracts registry file path from config file."""
        return self.config.get("Paths", 'registry_file')
