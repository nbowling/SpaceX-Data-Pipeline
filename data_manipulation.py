import pandas as pd

data = {
    'rocket':[
        'Falcon 1',
        'Falcon 9',
        'Falcon Heavy',
    ],
    'launches': [5, 100, 3],
}

df = pd.DataFrame(data)

print(df)

# Selecting columns
print(df['rocket'])

# Filtering rows
falcon9_df = df[df['rocket'] == 'Falcon 9']
print(falcon9_df)

# Adding new columns
df['success_rate'] = [0.4, 0.98, 1.0]
print(df)

falcon9_df = df[df['launches'] > 5]
print(falcon9_df)