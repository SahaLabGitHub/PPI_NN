#combine multiple energy.json files into one
import os
import json

# Define the directory containing the JSON files
json_directory = '/home/qingshu/Downloads/Nazmul_PDB_scores' 

# Initialize an empty list to store data from all JSON files
combined_data = []

# Loop through all files in the directory
for filename in os.listdir(json_directory):
    if filename.endswith('.json'):
        # Construct the full file path
        file_path = os.path.join(json_directory, filename)

        # Read the JSON file and append its data to the combined_data list
        with open(file_path, 'r') as file:
            data = json.load(file)
            combined_data.append(data)

# Save the combined data to a new JSON file
with open('combined.json', 'w') as output_file:
    json.dump(combined_data, output_file, indent=4)

print("All JSON files have been combined into combined.json")
