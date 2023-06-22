import pandas as pd

# Specify the file path of the CSV file
csv_file_path = "C:\\Users\\SlightlyHappy\\Documents\\Coding\\VSCode\\Data visulization with python final project\\automobileEDA1.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
filtered_df1 = df[['drive-wheels', 'body-style', 'price']]

output_file_path = "C:\\Users\\SlightlyHappy\\Documents\\Coding\\VSCode\\Data visulization with python final project\\automobileEDA2.csv"
filtered_df1.to_csv(output_file_path, index=False)

# Print the DataFrame
print(filtered_df1)

