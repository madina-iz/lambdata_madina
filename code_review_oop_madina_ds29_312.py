
# Task 1. Create a new class that contains two helper functions:
from sklearn.model_selection import train_test_split


class NullAndSplit:
    def __init__(self, df):
        self.df = df

    def null_count(self):
        return self.df.isna().sum().sum()

    def split(self, frac):
        return train_test_split(self.df, test_size=frac, random_state=42)



# Task 2. Code Review:

# In style_example.py FILE###

"""What would you say if you were working with someone and
this is the code they gave you?"""
import math
import sys


def example_1():
    """This is a long comment and should be wrapped to fit
    within a 72 character limit
    """
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
                     'Long': "Long code lines should be wrapped within 79"
                             "character to prevent page cutoff stuff",
                     'Other': [math.pi, 100, 200, 300, 9_999_292_929_292,
                               "This is a long string that looks gross and"
                               "goes beyond what it should"],
                     'More': {'inner':
                              "This whole logical line should be wrapped"},
                     'Data': [444, 5_555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
                    }
    return (some_tuple,some_variable)


def example_2():
    return {"has_key() is deprecated": True}


class Example3(object):
    def __init__(self, bar):
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
            Indentation in multiple strings should not be touched
            only actual code should be reindented,
            This is more code
            """
            return (sys.path, some_string)
