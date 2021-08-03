# Create a function to count nulls in a dataframe:
def null_count(df):
    return df.isna().sum().sum()


# Create a function to split a datafram into train-test sets:
from sklearn.model_selection import train_test_split
def split(df, frac):
    return train_test_split(df, test_size=frac, random_state=42)

# Create a function to split addresses into 3 columns:
def addr_split(series):
    return series.str.split(' ', expand=True)