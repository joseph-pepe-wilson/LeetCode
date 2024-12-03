import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:

    # separate start and end timestamps
    start_df = activity[activity['activity_type'] == 'start'].rename(columns = {'timestamp' : 'start_time'})
    end_df = activity[activity['activity_type'] == 'end'].rename(columns = {'timestamp' : 'end_time'})

    # merge
    merge_df = pd.merge(start_df, end_df, on = ['machine_id', 'process_id'])

    # calculate processing time
    merge_df['processing_time'] = merge_df['end_time'] - merge_df['start_time']

    # calculate average processing time
    result_df = merge_df.groupby('machine_id')['processing_time'].mean().reset_index()

    result_df['processing_time'] = result_df['processing_time'].round(3)

    return result_df
