import pandas as pd

# Define the path to your combined JSON file
json_file_path = '/home/qingshu/Downloads/combined.json'  # Replace with your actual JSON file path

# Read the JSON file into a pandas DataFrame
df = pd.read_json(json_file_path)

# Save the DataFrame to a CSV file
csv_file_path = 'combined.csv'  # Specify the desired CSV output path
df.to_csv(csv_file_path, index=False)

print(f"JSON data has been successfully converted to {csv_file_path}")
