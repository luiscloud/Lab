import pandas as pd

df = pd.read_csv('results.csv')
df.head(10)
print(df.head(10))
print(df.describe())
print(df.info())

from pandas_profiling import ProfileReport
prof = ProfileReport(df)
prof.to_file(output_file='report.html')