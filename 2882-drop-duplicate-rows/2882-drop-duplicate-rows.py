import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Removing duplicate rows based on the 'email' column and keeping only the first occurrence
    result = customers.drop_duplicates(subset=['email'], keep='first')
    return result
