import pandas as pd
import numpy as np

# Define the number of features
num_features = int(3 * 4)

# Generate feature names
feature_names = [f"feature_{i}" for i in range(num_features)]

# Add the target variable name
feature_names.append("target")

# Create a DataFrame with random values
df = pd.DataFrame(np.random.rand(10, num_features+1), columns=feature_names)  # 10 rows of random data

# Print the DataFrame
print(df)

filename = "data.csv"

# Save the DataFrame to a CSV file
df.to_csv(filename, index=False)

