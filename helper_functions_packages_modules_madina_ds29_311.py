from sklearn.model_selection import train_test_split

def null_count(df):
    """This function counts the number of NaN values in a dataframe"""
    return df.isna().sum().sum()


def split(df, frac):
    """This function splits a dataframe into train and test sets"""
    return train_test_split(df, test_size=frac, random_state=42)


def addr_split(series):
    """This function splits an address column into 5 separate columns
    (street number, street, city, state and zipcode)
    """
    return series.str.split(' ', expand=True)
