import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    num_row, num_column = players.shape
    result = [num_row, num_column]
    return result
    
data = [
    [846, 'Mason', 21, 'Forward', 'RealMadrid'],
    [749, 'Riley', 30, 'Winger', 'Barcelona'],
    [155, 'Bob', 28, 'Striker', 'ManchesterUnited'],
    [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool'],
    [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'],
    [883, 'Ava', 23, 'Defender', 'Chelsea'],
    [355, 'Violet', 18, 'Striker', 'Juventus'],
    [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'],
    [761, 'Jack', 33, 'Midfielder', 'ManchesterCity'],
    [642, 'Charlie', 36, 'Center-back', 'Arsenal']
]

# Creating the DataFrame
players = pd.DataFrame(data, columns=['player_id', 'name', 'age', 'position', 'team'])

# Getting the size of the DataFrame
result = getDataframeSize(players)
print(result)
