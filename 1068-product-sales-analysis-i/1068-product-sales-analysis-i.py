import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    # merge dataframe
    result_df = pd.merge(sales, product, on = 'product_id')

    #select columns
    result = result_df[['product_name', 'year', 'price']]

    return result