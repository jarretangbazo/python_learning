import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import requests


print("All packages imported successfully!")

# Test data creation and analysis
data = {
    'name': ['Alice', 'Bob', 'Carol', 'David'],
    'age': [25, 30, 35, 28],
    'salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print("\n Sample DataFrame:")
print(df)

print(f"\n Mean salary: ${df['salary'].mean():,.2f}")

# Test plotting
plt.figure(figsize=(8, 5))
plt.scatter(df['age'], df['salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.savefig('test_plot.png')
print("\n Plot saved as 'test_plot.png'")

print("\n Your Python data science environment is ready!")
