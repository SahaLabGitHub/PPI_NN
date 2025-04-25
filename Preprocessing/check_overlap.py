import pandas as pd

# Load the two CSV files into DataFrames
csv_file1 = '/Users/qingshuzhao/Documents/machine learning PPI project/training_dataset_QZ/Rueben_overlaps_drop.csv'  #  first CSV file path
csv_file2 = '/Users/qingshuzhao/Documents/machine learning PPI project/testing_dataset/Nazmul_dataset_20.csv'  # second CSV file path

df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)

# Find overlapping PDB names between 'pdb_id' in the first CSV and 'description' in the second
overlap = pd.merge(df1[['pdb_id']], df2[['description']], left_on='pdb_id', right_on='description')

# Display the overlapping PDB names
print("Overlapping PDB names:")
print(overlap)

# Filter df1 to remove rows where 'pdb_id' is in the overlapping list
df1_filtered = df1[~df1['pdb_id'].isin(overlap['pdb_id'])]

# Save the filtered DataFrame to a new CSV file
filtered_csv_file = '/Users/qingshuzhao/Documents/machine learning PPI project/Rueben_overlaps_drop_new.csv' 
df1_filtered.to_csv(filtered_csv_file, index=False)

print(f"Filtered DataFrame saved to {filtered_csv_file}")








