import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    #merge the dataframes
    result_df = pd.merge(employees, employee_uni, on = 'id', how = 'left')

    #select columns needed
    result_df = result_df[['unique_id', 'name']]

    return result_df
