

import pandas as pd
import numpy as np

# Create a Series with 10 random numbers
series = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(series)

# Indexing
print("\nValue at index 2:", series[2])

# Filtering
print("\nNumbers greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nMean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())


