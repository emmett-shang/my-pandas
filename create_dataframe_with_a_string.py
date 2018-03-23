import pandas as pd

# rename all the column names
employee = r"""A,B,C
John,m,30
Alice,f,22
"""

df = pd.read_csv(pd.compat.StringIO(employee))
df.columns = ['Name', 'Gender', 'Age']

print(df)
