import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    #filter views dataframe for rows  where author_id = viewer_id
    filter_df = views[views['author_id'] == views['viewer_id']]

    #drop duplicate 
    result_df = filter_df[['author_id']].drop_duplicates().rename(columns = {'author_id' : 'id'})

    #sort the result
    result_df = result_df.sort_values(by = 'id').reset_index(drop = True)

    return result_df