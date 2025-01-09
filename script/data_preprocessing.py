#!/usr/bin/env python

import pandas as pd
import numpy as np
from typing import Optional
from pandas import DataFrame
import numpy as np
from sklearn.preprocessing import LabelEncoder


class DataPreprocessing:
    def __init__(self, data: Optional[DataFrame] = None):
        self.data = data

    def read_data(self, file_path: str) -> DataFrame:
        """load data from csv file
        Args:
            file_path: str - path to the csv file
        Returns:
            DataFrame: data

        """
        self.data = pd.read_csv(file_path)
        return self.data

    def remove_duplicate(self) -> DataFrame:
        """remove duplicate rows
        Returns:
            DataFrame: data

        """
        self.data = self.data.drop_duplicates()
        return self.data

    def standardize_columns_names(self) -> DataFrame:
        """standardize the data
        Args:
            columns: list of columns to standardize
          Returns:
              data: DataFrame
        """
        self.data = self.data.rename(
            columns=lambda col: col.strip()
            .lower()
            .replace("(", "")
            .replace(")", "")
            .replace("-", "_")
            .replace("/", "_")
            .replace("?", "")
        )
        return self.data

    def rename_observation_column(self, column_name: list) -> DataFrame:
        """rename the observation column
        Args:
            column_name: list - name of the observation column
        Returns:
            DataFrame: data
        """
        for col in column_name:
            if self.data[col].dtype == "object":
                self.data[col] = (
                    self.data[col]
                    .str.lower()
                    .str.strip()
                    .str.replace(" ", "_")
                    .str.replace("(", "")
                    .str.replace(")", "")
                )
        return self.data

    def select_columns(self) -> str:
        """select columns from the data
        Args:
            columns: list of columns to select
        Returns:
            DataFrame: data
        """
        columns = self.data.select_dtypes(include=np.number).columns
        return columns

    def check_duplicates(self) -> int:
        """check for duplicates
        Returns:
            int : number of duplicates
        """
        return self.data.duplicated().sum()

    def check_missing_values(self) -> int:
        """check for missing values
        Returns:
            int : number of missing values
        """
        return self.data.isnull().sum().sum()

    def lable_encode(self, columns: list) -> DataFrame:
        """encode categorical columns
        Args:
            columns: list of columns to encode
        Returns:
            DataFrame: data
        """
        le = LabelEncoder()
        for col in columns:
            if self.data[col].dtype == "object":
                self.data[col] = le.fit_transform(self.data[col])
        return self.data
