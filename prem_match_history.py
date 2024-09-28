from bs4 import BeautifulSoup
import requests
import pickle
import os


# Getting team data
with open('stubs/team_data_per_year','rb') as f:
    team_data_per_year = pickle.load(f)


years = ["2024","2023","2022","2021","2020","2019","2018"]


team_name_map = {
    "Arsenal FC": "Arsenal",
    "Manchester City": "Manchester City",
    "Liverpool FC": "Liverpool",
    "Aston Villa": "Aston Villa",
    "Tottenham Hotspur": "Tottenham",
    "Chelsea FC": "Chelsea",
    "Newcastle United": "Newcastle Utd",
    "Manchester United": "Manchester Utd",
    "West Ham United": "West Ham",
    "Crystal Palace": "Crystal Palace",
    "Brighton & Hove Albion": "Brighton",
    "AFC Bournemouth": "Bournemouth",
    "Fulham FC": "Fulham",
    "Wolverhampton Wanderers": "Wolves",
    "Everton FC": "Everton",
    "Brentford FC": "Brentford",
    "Nottingham Forest": "Nott'ham Forest",
    "Luton Town": "Luton Town",
    "Burnley FC": "Burnley",
    "Sheffield United": "Sheffield Utd",
    "Leicester City": "Leicester City",
    "Leeds United": "Leeds United",
    "Southampton FC": "Southampton",
    "Watford FC": "Watford",
    "Norwich City": "Norwich City",
    "West Bromwich Albion": "West Brom",
    "Cardiff City": "Cardiff City",
    "Huddersfield Town": "Huddersfield",
    "Swansea City": "Swansea City",
    "Stoke City": "Stoke City",
    "West Bromwich Albion": "West Brom"
}

prem_fixture_history = {} # {2023:[ ["home_team_x","away_team_y",(1,2)], ["home_team_x","away_team_y",(1,2)] ]}
for year in years:
    prem_fixture_history[year] = []

for year in years:
    for i in range(100):
        print('===================================') # Making clear distinction between years
    games = []
    for i in range(1,39):
        # Checking if the html fixture pages exist and making them if they dont
        if os.path.exists('stubs/prem_games/game_' + year + '_' + str(i)):
            with open('stubs/prem_games/game_' + year + '_' + str(i),'rb') as f:
                games.append(pickle.load(f))
        if os.path.exists('stubs/prem_games/game_' + year + '_' + str(i)) == False:
            with open('stubs/prem_games/game_' + year + '_' + str(i),'wb') as f:
                game_html = requests.get('https://www.worldfootball.net/schedule/eng-premier-league-' + str(int(year) -1) + '-'+ str(int(year)) +'-spieltag/' + str(i) + '/').text
                games.append(game_html)
                pickle.dump(game_html,f)
    
    
    for i,game in enumerate(games):
        game = BeautifulSoup(game,'lxml')
        print(i)
        print('=============================')

        # Error handling to adjust for each gameweek
        if i == 0 or i == 37:
            start_a = 193
        else:
            start_a = 194

        end_a = start_a + 30
        game_results = game.find_all('a')[start_a:end_a] # Starting at 154 as thats the first game a tag that we need

        for index in range(0,len(game_results),3): # Step 3 because the first tag is the home team 2nd away team and 3rd score
            if not (index + 2 < len(game_results)):
                continue
            home = team_name_map[game_results[index].get_text()]
            away = team_name_map[game_results[index + 1].get_text()]
            score = game_results[index + 2].get_text()

            print('====================')
            print(home)
            print(away)
            print(int(score[0]),int(score[2]))

            #Adding the result to the object
            prem_fixture_history[year].append([home,away,(int(score[0]),int(score[2]))])

# Saving prem fixture history if not already saved
if not os.path.exists('stubs/prem_fixture_history'):
    with open('stubs/prem_fixture_history','wb') as f:
        pickle.dump(prem_fixture_history,f)
        print('dumped')

            


            
        
        
    
    