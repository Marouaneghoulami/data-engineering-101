import pytest
import os
import pandas as pd
import logging
from util.api_handler import ApiHandler
from util.config_handler import ConfigHandler
from util.file_handler import FileHandler
from util.exceptions import RequestException
from util.exceptions import InvalidValueException

# This should be decalred in ENV VAR when writing Dockerfile
API_NAME_VAR = "UNIT-TEST-API-v1"
RAW_DIR_VAR = "part-1/data/raw"
CURATED_DIR_VAR = "part-1/data/curated"


"""Test cases for API Handler Functionalities."""
class TestApiHandler:
    @pytest.fixture
    def api_handler(self):
        return ApiHandler(api_name=API_NAME_VAR)

    def test_api_successful_request(self, api_handler, mocker):
        # Mock the requests.get method to return a successful response
        mocker.patch('requests.get').return_value.status_code = 200
        mocker.patch('requests.get').return_value.text = "A,B\n1,a\n2,b\n"
        # Call the get_data method
        df = api_handler.get_data()
        # Check if the DataFrame is not empty
        assert not df.empty
        # Check that the DataFrame has 2 rows
        assert len(df) == 2

    def test_api_failed_request(self, api_handler, mocker):
        # Mock the requests.get method to raise an exception
        mocker.patch('requests.get').return_value.status_code = 500
        # Call the get_data method and expect a RequestException to be raised
        with pytest.raises(RequestException):
            api_handler.get_data()

"""Test cases for File Handler Functionalities."""
class TestFileHandler:
    @pytest.fixture
    def file_handler(self):
        return FileHandler(source_prefix=API_NAME_VAR)

    def test_save_to_csv_bulk(self, file_handler, mocker):
        # Mock the ConfigHandler to return a test directory
        mocker.patch.object(ConfigHandler, 'get_raw_dir', return_value=RAW_DIR_VAR)
        mocker.patch.object(ConfigHandler, 'get_curated_dir', return_value=CURATED_DIR_VAR)
        # Create a DataFrame for testing
        test_data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
        
        # Call the save_to_csv_bulk method
        file_handler.save_to_csv_bulk(test_data, layer='raw')
        file_handler.save_to_csv_bulk(test_data, layer='curated')    
        # Check if the file was created in the expected directory
        raw_expected_file_path = API_NAME_VAR
        curated_expected_file_path = API_NAME_VAR

        # Check if files exists in directory
        assert any(file.startswith(raw_expected_file_path) for file in os.listdir(RAW_DIR_VAR))
        assert any(file.startswith(curated_expected_file_path) for file in os.listdir(CURATED_DIR_VAR))
        # Pass invalid layer argument
        with pytest.raises(InvalidValueException):
            file_handler.save_to_csv_bulk(pd.DataFrame(), layer='invalid_layer')




