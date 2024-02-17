import csv
import os

# Specify the folder and file name
folder_name = 'animelist\script'
file_name = 'cleaned.csv'

# Construct the full file path
csv_file_path = os.path.join(folder_name, file_name)

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Skip the header row
    header = next(csv_reader)

    # Specify the index of the column you want to access
    target_column_index = 2  # Replace with the index of the desired column
    num = 0
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Access the specific column using the index
        title = row[0]
        genres = row[1]
        num_of_ep = row[2]
        img = row[3]
        if(img == 'nan'):
            # print(title, genres, num_of_ep, img, "NANANAN")
            pass
        elif(num_of_ep == '?'):
            # print(title, genres, num_of_ep, img, "????????")
            pass
        else:
            if(num == 50):
                break
            print(title, genres, num_of_ep, img)
            num += 1

    print(num)

            
            
