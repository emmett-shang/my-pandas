import pandas as pd
list_of_dicts = [
    {
        'date': '2018-03-04',
        'weather': 'cloudy'
    },
    {
        'date': '2018-03-05',
        'weather': 'sunny'
    },
    {
        'date': '2018-03-06'
    },
    {
        'date': '2018-03-07',
        'weather': 'rain'
    },
    {
        'date': '2018-03-26',
        'weather': 'winday'
    }
]

df = pd.DataFrame(list_of_dicts)
df['weather'] = df['weather'].apply(lambda x: str(x).title())
print(df)
