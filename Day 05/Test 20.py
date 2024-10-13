"""Day 05 MODULES AND LIBRARIES """

#  Write a Python function pandas_operations() -> dict that performs the following operations using the Pandas library:
# Create a DataFrame with the following data:
# {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
# Filter the DataFrame to include only rows where the Age is greater than 28.
# Calculate the sum of the Age column.
# The function should return a dictionary containing the filtered DataFrame and the sum of ages.


import pandas as pd
def pandas_operations()-> dict:
    data={
            "Name":["Alice","Bob","Charlie"],
            "Age":[25,30,35]
    }

    df= pd.DataFrame(data)

    filtered_df=df[df['Age']>28]

    age_sum= filtered_df['Age'].sum()

    return{
            'filtered_data':filtered_df.to_dict(orient='list'),
            'age_sum':int(age_sum)
    }

result=pandas_operations()
print(result)