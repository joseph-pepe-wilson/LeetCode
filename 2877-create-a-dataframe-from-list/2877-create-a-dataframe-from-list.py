import pandas as pd

def createDataframe(student_data):
    # Creating the DataFrame
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# Given 2D list
student_data = [
    [1, 15],
    [2, 11],
    [3, 11],
    [4, 20]
]

# Creating the DataFrame using the defined function
student_data  = createDataframe(student_data)

# Displaying the DataFrame
print(student_data )
