import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    # merge the dataframes
    merged_df = pd.merge(visits, transactions, on = 'visit_id', how = 'left', indicator = True)

    # filter the dataframe
    no_trans_df = merged_df[merged_df['_merge'] == 'left_only']

    # count no of visit wuthout trans
    result_df = no_trans_df.groupby('customer_id').size().reset_index(name = 'count_no_trans')

    return result_df