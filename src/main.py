import classes

if __name__ == "__main__":
    # Initialize the DataLoader with the CSV file path
    data_loader = classes.DataLoader("your_data.csv")

    # Load the data into a DataFrame
    data = data_loader.load_data()

    # Check if the data was successfully loaded
    if data is not None:
        print("Data loaded successfully:")
        print(data.head())
