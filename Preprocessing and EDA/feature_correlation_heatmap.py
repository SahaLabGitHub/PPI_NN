import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df_energy = pd.read_csv("/Users/qingshuzhao/Documents/ML_PPI_project/training_dataset/top_504_PDBs.csv")

# Drop rows with missing values and reset index
df_energy = df_energy.dropna().reset_index(drop=True)

# Drop columns that are not needed for correlation analysis
df_energy.drop(columns=['resolution', 'kd_molar'], axis=1, inplace=True)

# Save the pdb_id column for future reference if needed
pdb_id = df_energy.pop('pdb_id')

# Calculate correlation matrix
corr_matrix = df_energy.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(13, 11))
sns.heatmap(corr_matrix, annot=True, annot_kws={"fontsize":5}, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Training Data Feature Correlation")
# Adjusting column names max height
plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

outpath = "/Users/qingshuzhao/Documents/ML_PPI_project/Paper/Figures_tables"
plt.savefig(outpath + "Training_data_feature_correlation.png") 
plt.show()