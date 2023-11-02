import pandas as pd


class DataLoader:
    """
    Class for loading data from a CSV file.
    """

    def __init__(self, file_path, delimiter=","):
        self.file_path = file_path
        self.delimiter = delimiter

    def load_data(self):
        """
        Reads the CSV file and returns a Pandas DataFrame.
        Uses the delimiter specified in the constructor.
        """
        try:
            # Load the CSV file into a Pandas DataFrame
            data_frame = pd.read_csv(self.file_path, delimiter=self.delimiter)
            return data_frame
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
            return None
        except Exception as e:
            print(f"An error occurred while loading the data: {str(e)}")
            return None
