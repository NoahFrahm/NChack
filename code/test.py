import pandas as pd
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

dataframe_list = []
home_win_list = []
visitor_win_list = []

# this contains all teams and their home win percentages over the years
x_dict: Dict[str, List] = {}

# this contains all teams and their away win percentages over the years
y_dict: Dict[str, List] = {}

URL_list: List[str] = ['https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1978lines.csv', 
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1979lines.csv', 
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1980lines.csv',
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1981lines.csv',
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1983lines.csv',
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1982lines.csv',
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1984lines.csv',
'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1985lines.csv']
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1986lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1987lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1988lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1989lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1990lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1991lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1992lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1993lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1994lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1995lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1996lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1997lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1998lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1999lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2000lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2001lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2002lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2003lines.csv', #from here i just modified links by changing year so if it fails replace links after this
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2004lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2005lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2006lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2007lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2008lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2009lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2010lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2011lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2012lines.csv',
# 'https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl2013lines.csv'
# ]

# dfe = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1983lines.csv')
# df = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1978lines.csv')
# df1 = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1979lines.csv')
# df2 = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1980lines.csv')
# df3 = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1981lines.csv')
# df4 = pd.read_csv('https://raw.githubusercontent.com/Carolina-Data-Challenge/datasets/main/FootballDatasets/NFL/RegSeason/nfl1982lines.csv')

possible_teams: List[str] = []

for url in URL_list:
    dat = pd.read_csv(url)
    org = dat['Visitor'].unique()
    for i in org:
        possible_teams.append(i)
    dataframe_list.append(dat)

duplicate_teams: List = []
# potential team candidates
for team in possible_teams:
    i: int = possible_teams.count(team)
    if i == len(URL_list):
        duplicate_teams.append(team)


teams: List[str] = []

for team in duplicate_teams:
    if team not in teams:
        teams.append(team)

for team in teams:
    x_dict[team] = []
    y_dict[team] = []
print(teams)

def win_percent_calculator(df) -> Dict[str, int]:
    """Takes a dataframe and computes win percentage for home and away teams."""
    """The result is return as tuple (home_win, visitor_win)."""
    visitor_wins: Dict[str, int] = {}
    home_wins: Dict[str, int] = {}
    total_games: Dict[str, int] = {}
    visitor_winpercentage: Dict[str, float] = {}
    home_winpercentage: Dict[str, float] = {}

    for team in teams:
        visitor_wins[team] = 0
        home_wins[team] = 0
        total_games[team] = 0

    for i in range(0, len(df)):
        if (df.iloc[i][1] in teams) and (df.iloc[i][3] in teams):
            visitor_team: str = df.iloc[i][1]
            home_team: str = df.iloc[i][3]

            if df.iloc[i][2] - df.iloc[i][4] > 0:
                visitor_wins[visitor_team] += 1

            elif df.iloc[i][2] - df.iloc[i][4] < 0:
                home_wins[home_team] += 1
        #else:
        #    print("tie")

    # this finds the total games played per team and puts it in a dictionary
    # this is here as a safety in case not all teams play the same number of games
    for key in total_games:
        for i in range(0, len(df)):
            if (df.iloc[i][1] in teams) and (df.iloc[i][3] in teams):
                if df.iloc[i][1] == key:
                    total_games[key] += 1
                elif df.iloc[i][3] == key:
                    total_games[key] += 1

    # finds home and visitor win percentage of each team
    for key in teams:
        if total_games[key] == 0:
            print(key)
        else:
            home_winpercentage[key] = home_wins[key] / (total_games[key])
            visitor_winpercentage[key] = visitor_wins[key] / (total_games[key])
    return (home_winpercentage, visitor_winpercentage)

# a = win_percent_calculator(dfe)


# for team in teams:
#     p = a[0][team] + a[1][team]
#     print(p)
#print(a[1]['Oakland Raiders'])


def run():
    for dataframe in dataframe_list:
        a = win_percent_calculator(dataframe)      
        for team in teams:
            x_dict[team].append(a[0][team])
            y_dict[team].append(a[1][team])
run()

def graph_team(team: str) -> None:
    # these are the y values
    home = x_dict[team]
    away = y_dict[team]
    x = np.arange(0,len(home))
    print(x)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.scatter(x, home, s=10, c='b', marker="s", label='home win percentage')
    ax1.scatter(x, away, s=10, c='r', marker="o", label='away win percentage')
    plt.legend(loc='upper left')
    plt.show()

graph_team('New York Giants')