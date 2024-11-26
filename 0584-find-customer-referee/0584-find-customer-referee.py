import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filter_customer = customer[
        (customer['referee_id']!=2) | (customer['referee_id'].isnull())
    ]
    result = filter_customer[['name']]
    return result