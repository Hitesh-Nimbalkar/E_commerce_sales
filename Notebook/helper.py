# Data Overview
import matplotlib.pyplot as plt
import numpy as np



class Data_overview:

    def __init__(self,data):
        self.data=data


    def clean_column_labels(self):
        """
        Remove spaces and hyphens from column labels and replace them with underscores in a Pandas DataFrame.

        Parameters:
        - dataframe: The input Pandas DataFrame.

        Returns:
        - A DataFrame with cleaned column labels.
        """
        dataframe=self.data

        # Use list comprehension to clean the column labels
        cleaned_columns = [col.replace(" ", "_").replace("-", "_") for col in dataframe.columns]
        
        # Rename the columns in the DataFrame
        dataframe.columns = cleaned_columns
        return dataframe

    def plot_unique_percentage(self):
        """
        Plot the percentage of unique values for each column in a DataFrame.

        Parameters:
        - dataframe: The input Pandas DataFrame.

        Returns:
        - None
        """
        # Accessing Dataframe
        dataframe=self.data
        


        unique_percentages = []
        column_names = []

        for column in dataframe.columns:
            unique_count = dataframe[column].nunique()
            total_count = len(dataframe)
            percentage = (unique_count / total_count) * 100

            unique_percentages.append(percentage)
            column_names.append(column)

        plt.figure(figsize=(10, 6))
        plt.bar(column_names, unique_percentages)
        plt.xlabel("Columns")
        plt.ylabel("Unique Value Percentage")
        plt.title("Unique Value Percentage for DataFrame Columns")
        plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
        plt.show()

        
    def plot_nan_percentage(self):
        """
        Plot the percentage of NaN values for each column in the Pandas DataFrame.

        Returns:
        - None
        """
        nan_percentages = (self.data.isna().mean() * 100)
        
        plt.figure(figsize=(10, 6))
        nan_percentages.plot(kind='bar')
        plt.xlabel("Columns")
        plt.ylabel("NaN Value Percentage")
        plt.title("NaN Value Percentage for DataFrame Columns")
        plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
        plt.show()