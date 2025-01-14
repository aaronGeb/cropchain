import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from data_preprocessing import DataPreprocessing  

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        self.sample_data = pd.DataFrame({
            "Name": ["Alice", "Bob", "Alice", "Eve"],
            "Age": [25, 30, 25, np.nan],
            "City": ["New York", "Los Angeles", "New York", "Seattle"],
            "Salary": [50000, 60000, 50000, 70000],
        })
        self.processor = DataPreprocessing(self.sample_data.copy())

    def test_read_data(self):
        # Assuming a test CSV file is available
        test_file = "test_data.csv"
        self.sample_data.to_csv(test_file, index=False)
        data = self.processor.read_data(test_file)
        assert_frame_equal(data, self.sample_data)

    def test_remove_duplicate(self):
        result = self.processor.remove_duplicate()
        expected = self.sample_data.drop_duplicates()
        assert_frame_equal(result, expected)

    def test_standardize_columns_names(self):
        self.processor.data.columns = ["Name ", " Age", "City/Location", "Salary?"]
        result = self.processor.standardize_columns_names()
        expected_columns = ["name", "age", "city_location", "salary"]
        self.assertListEqual(result.columns.tolist(), expected_columns)

    def test_rename_observation_column(self):
        self.processor.data["Name"] = [" Alice ", "Bob", "ALICE", "Eve"]
        result = self.processor.rename_observation_column(["Name"])
        expected = self.sample_data.copy()
        expected["Name"] = ["alice", "bob", "alice", "eve"]
        assert_frame_equal(result, expected)

    def test_select_columns(self):
        result = self.processor.select_columns()
        expected = ["Name", "City"]
        self.assertListEqual(result.tolist(), expected)

    def test_check_duplicates(self):
        result = self.processor.check_duplicates()
        expected = 1  # One duplicate row in the sample data
        self.assertEqual(result, expected)

    def test_check_missing_values(self):
        result = self.processor.check_missing_values()
        expected = 1  # One missing value in the sample data
        self.assertEqual(result, expected)

    def test_label_encode(self):
        result = self.processor.lable_encode(["Name", "City"])
        le_name = {"Alice": 0, "Bob": 1, "Eve": 2}
        le_city = {"New York": 0, "Los Angeles": 1, "Seattle": 2}
        expected = self.sample_data.copy()
        expected["Name"] = expected["Name"].map(le_name)
        expected["City"] = expected["City"].map(le_city)
        assert_frame_equal(result, expected)

if __name__ == "__main__":
    unittest.main()