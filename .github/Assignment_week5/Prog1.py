
import numpy as np
import pandas as pd

#part1
df = pd.read_csv(".github/Assignment_week5/matches.csv")
print("1",df.head())
print("2",df.shape)
print("3",df.columns)
print("4",df.info())
print("5",df.describe())

#part2
print("6",df['Season'].head())
print("7",df[['Season', 'team1', 'team2', 'winner']].head())
print("8",df.drop(columns = ['umpire1', 'umpire2', 'umpire3']).head())
a = df['winner']
print(" 9 ",a.index)
df.rename(columns = {'win_by_runs': 'runs_margin'}, inplace = True)
print("10",df.head()) 

#part3
print("11",df[df['Season'] == 'IPL-2017'].head())
print("12",df[df['winner'] == 'Mumbai Indians'].head())
print("13",df[df['runs_margin'] > 50].head())
print("14",df[df['win_by_wickets'] > 7].head())
print("15",df[df['venue'] == 'Wankhede Stadium'].head()) 

#part4
print("16",df[(df['Season'] == 'IPL-2017') | (df['Season'] == 'IPL-2018')].head())
print("17",df[(df['Season'] == 'IPL-2017') | (df['winner'] == 'Sunrisers Hyderabad')].head())
print("18",df[(df['winner'] == 'Mumbai Indians') & (df['team1'] == 'Mumbai Indians')].head())
print("19",df[(df['runs_margin'] > 30) & (df['Season'] == 'IPL-2016')].head())
print("20",df[(df['winner'] != df['team1']) & (df['winner'] != df['team2'])].head()) 

#part5
print("21",df[df['winner'].isin(['Mumbai Indians', 'Chennai Super Kings'])].head())
print("22",df[~df['team1'].isin(['Mumbai Indians', 'Chennai Super Kings']) | 
   ~df['team2'].isin(['Mumbai Indians', 'Chennai Super Kings'])].head())
print("23",df[~df['venue'].isin(['Wankhede Stadium','Eden Gardens'])].head()) 

#part6
print("24",df.isnull().sum())
print("25",df.isnull()['winner'].head())
df['winner'] = df['winner'].fillna('No Result')
print("26",df.isnull()['winner'].sum())
df.dropna(subset=['umpire1','umpire2'], inplace=True)
print("27",df.isnull()['umpire1'].sum(), df.isnull()['umpire2'].sum())
df = df.drop(columns = df.columns[df.isnull().mean() > 0.30])
print("28",df.info()) 

#part7
df['is_super_over'] = np.where(df['result'] == 'tie', True, False)
print("29",df['is_super_over'].head())
df['match_result'] = np.where(df['result'] == 'normal', 
                             np.where(df['runs_margin'] > 0, "Runs", "Wickets"),
                              "No Result")
print("30",df['match_result'].head())
df["Season"] = df["Season"].str.replace("IPL-", "",regex=False)
df["Season"] = df["Season"].astype(int)
print("31",df['Season'].head())
df["team1"] = df["team1"].str.upper()
df["team2"] = df["team2"].str.upper()
print("32",df[['team1', 'team2']].head())

#part8
df.sort_values(by = ['Season'], ascending=True, inplace=True)
df.sort_values(by = ['date'], ascending=False, inplace=True)
print("33",df[['Season', 'date']].head())
df.sort_values(by=['runs_margin'], ascending=False, inplace=True)
print("34",df[['runs_margin']].head())
newdataframe = df.sort_values(by=['runs_margin'], ascending=False).head(10)
print("35",newdataframe.head())
newdataframe = newdataframe.reset_index(drop=True)