import pandas as pd

data = {
    "Name": ["John", "Anna", "Aamir", "Madhuri"],
    "Location": ["New York", "Paris", "Mumbai", "Pune"],
    "Age": [52, 25, 55, 45]
}

data_pandas = pd.DataFrame(data)
print(data_pandas)  # This will print the entire DataFrame
print(data_pandas[data_pandas.Age > 30])  # This will print the rows where Age is greater than 30
