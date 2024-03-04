import os
import pickle

# Specify the absolute path to the data folder
data_folder_path = "/content/drive/My Drive/CS_122/A2/data"

# Dictionary to store values from files with exactly two columns
result_dict = {}

# List to store filenames causing errors
err_files = []

# Iterate through all files in the data folder
for filename in os.listdir(data_folder_path):
    if filename.endswith('.csv'):  # Check if the file is a CSV file
        file_path = os.path.join(data_folder_path, filename)

        try:
            # Open and read the CSV file
            with open(file_path, 'r') as file:
                # Process the first line to get the number of columns
                first_row = next(file, None)
                if first_row is not None:
                    num_columns = len(first_row.strip().split(','))
                    if num_columns < 2:
                      raise ValueError(f"The file {filename} has less than two columns in the first row.")
                    # Check if the number of columns is exactly two
                    if num_columns == 2:
                        print(filename)
                        # Reset the file pointer to the beginning for further processing
                        file.seek(0)

                        # Create a dictionary from the CSV file
                        csv_dict = {key.strip(): value.strip() for key, value in (line.strip().split(',') for line in file)}

                        # Update the result_dict with values from the current file
                        result_dict.update(csv_dict)

        except Exception as e:
            # Capture the filename causing the error and append it to err_files
            err_files.append((filename, str(e)))

# Serialize the resulting dictionary into a pickle file
pickle_file_path = 'mydict.pickle'
with open(pickle_file_path, 'wb') as pickle_file:
    pickle.dump(result_dict, pickle_file)

print(f"Dictionary has been serialized and saved to {pickle_file_path}.")

# Print filenames causing errors
if err_files:
    print("\nFiles causing errors:")
    for err_file, err_message in err_files:
        print(f"{err_file}: {err_message}")