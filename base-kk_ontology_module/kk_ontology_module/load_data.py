import pandas as pd

TEST_DATA = 'extras/m2dummyB_small.csv'

def load_data(filename):
    df = pd.read_csv(filename)
    # df = df.astype({'MAPPED_REGIMEN': str})
    return df

# print(load_data(TEST_DATA)['MAPPED_REGIMEN'])