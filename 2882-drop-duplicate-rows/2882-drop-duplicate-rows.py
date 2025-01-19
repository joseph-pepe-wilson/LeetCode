import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # Removing duplicate rows based on the 'email' column and keeping only the first occurrence
    result = customers.drop_duplicates(subset=['email'], keep='first')
    return result

# Sample DataFrame for demonstration
data = [
    [1, 'Ella', 'emily@example.com'],
    [2, 'David', 'michael@example.com'],
    [3, 'Zachary', 'sarah@example.com'],
    [4, 'Alice', 'john@example.com'],
    [5, 'Finn', 'john@example.com'],
    [6, 'Violet', 'alice@example.com']
]

# Creating the DataFrame
customers = pd.DataFrame(data, columns=['customer_id', 'name', 'email'])

# Removing duplicate emails and getting the updated DataFrame
result = dropDuplicateEmails(customers)
print(result)
