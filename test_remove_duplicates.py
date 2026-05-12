import pandas as pd
from remove_duplicates import remove_duplicates

def test_duplicates_removed():

    input_file = "dataset (2).csv"
    output_file = "test_output.csv"

    remove_duplicates(input_file, output_file)

    df = pd.read_csv(output_file)

    assert df.duplicated().sum() == 0
