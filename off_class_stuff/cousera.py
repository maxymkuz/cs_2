"""
def answer_four():
    df['Points'] = df['Gold.2']*3 + df['Silver.2']*2 + df['Bronze.2']
    series = pd.Series(df['Points'], index=df.index)
    return series
def answer_three():
    only_gold = df.where((df['Gold'] > 0) | (df['Gold.1'] > 1))
    return only_gold.loc[abs((df['Gold'] - df['Gold.1'])/(df['Gold'] + df['Gold.1'])).argmax()]
def answer_two():
    return df.loc[abs(df['Gold'] - df['Gold.1']).argmax()]

def answer_one():
    return df.loc[df['Gold'].argmax()]
"""
import requests

url = "https://raw.githubusercontent.com/words-sdsc/coursera/master/big-data-2/csv/census.csv"

csv_file = requests.get(url).content

print(csv_file)