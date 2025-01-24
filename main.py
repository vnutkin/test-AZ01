import pandas as pd
home_work_number = 2
if home_work_number == 1:
    df = pd.read_csv('screentime_analysis.csv')
    print(df.head(4 ))
    print(df.tail(4))
    print(df.info)
    print(df.describe())
if home_work_number == 2:
    df = pd.read_csv('dz.csv')
    print(df.head(4 ))
    print(df.tail(4))
    df.dropna(inplace=True)
    group = df.groupby('City')['Salary'].mean()
    print(group)
    df.to_csv('dz-corr.csv', index=False)
