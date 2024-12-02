import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather = weather.sort_values('recordDate')

    # create a shifted datafreame
    weather_shifted = weather.shift(1)

    # merge 
    merged_df = weather.merge(weather_shifted, left_index = True, right_index = True, suffixes = ('', '_prev'))

    # filter
    result_df = merged_df[(merged_df['temperature'] > merged_df['temperature_prev']) &
                          (merged_df['recordDate'] - merged_df['recordDate_prev'] == pd.Timedelta(days = 1))]

    # select id column
    result = result_df[['id']].rename(columns = {'id' : 'Id'})

    return result