import csv
import pandas as pd
import Orange
#creating dataframe
df = pd.read_csv("Quarterback Game Logs.csv", header=1)

#sorting dataframe by player ID, Year, Week to put games in order
df = df.sort_values(by=['Player Id', 'Year', 'Week'])

#replacing -- losses with 0
df.replace('--',0,inplace=True)

#adding total wins, next game win/loss columns
df.insert(17, 'Total Wins', 0)
df.insert(18, 'Win Percentage', 0.0)
df.insert(19, 'Next Game', 'L')

#filtering data to only relavant columns
df = ((df[df['Year']>=2000][df['Season']!="Preseason"][df['Season']!="Postseason"][df['Games Started']!="0"]).loc[:,['Player Id', 'Year', 'Week', 'Outcome', 'Passes Completed', 'Passes Attempted', 'Passing Yards', 'Passing Yards Per Attempt', 'TD Passes', 'Ints', 'Sacks', 'Rushing Attempts', 'Rushing Yards', 'Yards Per Carry', 'Rushing TDs', 'Fumbles Lost', 'Total Wins', 'Win Percentage']])

#adding total wins for each QB of each season
curPlayer = ""
curYear = ""
winCount = 0
count = 1
for index, row in df.iterrows():
    if(curPlayer == row['Player Id'] and curYear == row['Year']):
        df.at[index,'Total Wins'] = winCount
        df.at[index,'Win Percentage'] = winCount / float(count)
        if(row['Outcome']=='W'):
            winCount+=1
        count+=1
    else:
        df.at[index,'Total Wins'] = 0
        df.at[index,'Win Percentage'] = 0
        curPlayer = row['Player Id']
        curYear = row['Year']
        if (row['Outcome'] == 'W'):
            winCount = 1
        else:
            winCount = 0
        count = 1


#creating current game dataframes
currentGameData = (df.loc[:,['Player Id', 'Year', 'Week', 'Outcome', 'Passes Completed', 'Passes Attempted', 'Passing Yards', 'Passing Yards Per Attempt', 'TD Passes', 'Ints', 'Sacks', 'Rushing Attempts', 'Rushing Yards', 'Yards Per Carry', 'Rushing TDs', 'Fumbles Lost', 'Total Wins', 'Win Percentage']])

#creating CSVs to work with in Orange
currentGameData.to_csv("current game (outcome=W or L) data.csv", index=False)

#replacing all occurences of W with 1, T with 0 to work with in Jupyter
currentGameData.replace('W',1,inplace=True)
currentGameData.replace('T',0,inplace=True)
currentGameData.replace('L',0,inplace=True)

#creating CSVs to work with in Jupyter
currentGameData.to_csv("current game (outcome=1 or 0) data.csv", index=False)

#adding next game for future game predictions
for index, row in df.iterrows():
    if (row['Outcome'] == 1):
        df.at[index - 1, 'Next Game'] = 'W'
    else:
        df.at[index - 1, 'Next Game'] = 'L'

#creating future game dataframes
futureGameData = (df.loc[:,['Player Id', 'Year', 'Week', 'Outcome', 'Passes Completed', 'Passes Attempted', 'Passing Yards', 'Passing Yards Per Attempt', 'TD Passes', 'Ints', 'Sacks', 'Rushing Attempts', 'Rushing Yards', 'Yards Per Carry', 'Rushing TDs', 'Fumbles Lost', 'Total Wins', 'Win Percentage',  'Next Game']])

#exporting filtered data to CSV
futureGameData.to_csv("future game data.csv", index=False)


