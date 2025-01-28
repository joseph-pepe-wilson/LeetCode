import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavy_animals = animals[animals['weight'] > 100].sort_values(by = 'weight', ascending = False)
    result = heavy_animals[['name']]
    return result