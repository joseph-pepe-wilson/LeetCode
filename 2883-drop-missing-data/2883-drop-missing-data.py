import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    result = students.dropna(subset = 'name')
    return result