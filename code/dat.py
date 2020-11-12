import pandas as pd
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt
from url_list import URL_list
import random


dataframe_list = []
home_win_list = []
visitor_win_list = []

#contains difference in win loss percentages over the years
diff_dict: Dict[str, int] = {}

# this contains all teams and their home win percentages over the years
x_dict: Dict[str, List] = {}

# this contains all teams and their away win percentages over the years
y_dict: Dict[str, List] = {}

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

for team in teams:
    diff_dict[team] = []

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
    fig = plt.figure()
    # fig, ((ax1, ax2), ax3) = plt.subplots(2, 1)
    
    #graphs home/away line plot
    ax1 = plt.subplot(212)
    ax1.plot(x, away,'-o',color = 'orange')
    ax1.plot(x, home, '-o', color = 'blue')
    # ax1.xlabel('comparison of the percentages of home vs away')
    #graphs home bar/line
    ax2 = plt.subplot(221)
    ax2.bar(x, home, color = 'g', width = 0.35, label='home win percentage')
    ax2.plot(x, home, '-o', color = 'blue')
    # ax2.ylabel('Away win %')
    plt.legend(loc= 'upper left', bbox_to_anchor = (0, 0))

    #graphs away bar/line plot
    ax3 = plt.subplot(222)
    ax3.bar(x, away, color='r', width=0.35, label='away win percentage')
    ax3.plot(x, away,'-o',color = 'orange')
    # ax3.ylabel('Home win %')

    #graphs home/away bars
    #ax4.bar(x + 0.35, home, color = 'g', width = 0.35, label='home win percentage')
    #ax4.bar(x, away, color='r', width=0.35, label='away win percentage')
    fig.suptitle(team)
    plt.legend(loc= 'upper left', bbox_to_anchor= (0, 0))
    # plt.title('home win percentage vs away win percentage')
    plt.show()


def home_win_percent_all():
    for team in x_dict:
        for i in range(0,len(x_dict[team])):
            diff: float = x_dict[team][i] - y_dict[team][i]
            diff_dict[team].append(diff)
    return diff_dict

home_win_percent_all()


def plot_team_diff(team):
    diff_data = diff_dict[team]
    x = np.arange(0,len(diff_data))
    y = []
    for i in range(0,len(diff_data)):
        y.append(0)
    y = np.array(y)
    fig = plt.figure()
    fig.suptitle('home win % minus away win percent.')
    ax1 = fig.add_subplot(111)
    ax1.bar(x, diff_data, color = 'g', width = 0.35, label='home win percentage')
    ax1.plot(x, y)
    plt.title(team)
    plt.show()

good: List[str] = ["Miami Dolphins"]

num: int = 0
while num != 3:
    index: int = random.randint(0,len(teams))
    good.append(teams[index])
    num += 1

for team in good:
    plot_team_diff(team)
    graph_team(team)