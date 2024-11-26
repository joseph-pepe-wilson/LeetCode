import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:

    # Define the conditions for a big country
    is_big_country = (world['area'] >= 3000000) | (world['population'] >= 25000000)
    
    # Filter the DataFrame based on the conditions
    big_countries = world[is_big_country]
    
    # Select the required columns
    result = big_countries[['name', 'population', 'area']]
    
    return result