import pandas as pd
import os
from data_input import data  # Import data from data_input.py

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Define the output directory and file path
output_dir = "data"
output_file = os.path.join(output_dir, "Overview.csv")

# Ensure the directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the DataFrame to a CSV file
df.to_csv(output_file, index=False)

print(f"File saved to {output_file}")
