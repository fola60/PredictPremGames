from bs4 import BeautifulSoup
import requests
import pickle
import os

years = ["2025","2024","2023","2022","2021","2020","2019","2018"]
team_data_per_year = {} # Map year to team to data {2024:{"manchester united": {goals:1}}}
for year in years:
    team_data_per_year[year] = {}
    
for year in years:
    # Loading html files if they exist
    if os.path.exists('stubs/advanced_goalkeeping_html_' + year):
        with open('stubs/advanced_goalkeeping_html_' + year, 'rb') as f:
            advanced_goalkeeping_html = pickle.load(f)

    if os.path.exists('stubs/shooting_html_' + year):
        with open('stubs/shooting_html_' + year, 'rb') as f:
            shooting_html = pickle.load(f)

    if os.path.exists('stubs/passing_html_' + year):
        with open('stubs/passing_html_' + year, 'rb') as f:
            passing_html = pickle.load(f)

    if os.path.exists('stubs/pass_types_html_' + year):
        with open('stubs/pass_types_html_' + year, 'rb') as f:
            pass_types_html = pickle.load(f)

    if os.path.exists('stubs/goal_shot_creation_html_' + year):
        with open('stubs/goal_shot_creation_html_' + year, 'rb') as f:
            goal_shot_creation_html = pickle.load(f)

    if os.path.exists('stubs/defensive_actions_html_' + year):
        with open('stubs/defensive_actions_html_' + year, 'rb') as f:
            defensive_actions_html = pickle.load(f)

    if os.path.exists('stubs/possesion_html_' + year):
        with open('stubs/possesion_html_' + year, 'rb') as f:
            possesion_html = pickle.load(f)


    # Saving html files if they do not exist
    if os.path.exists('stubs/advanced_goalkeeping_html_' + year) == False:
        with open('stubs/advanced_goalkeeping_html_' + year,'wb') as f:
            
            advanced_goalkeeping_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/keepersadv/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(advanced_goalkeeping_html,f)

    if os.path.exists('stubs/shooting_html_' + year) == False:
        with open('stubs/shooting_html_' + year,'wb') as f:
            shooting_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/shooting/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(shooting_html,f)
        
    if os.path.exists('stubs/passing_html_' + year) == False:
        with open('stubs/passing_html_' + year,'wb') as f:
            passing_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/passing/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(passing_html,f)

    if os.path.exists('stubs/pass_types_html_' + year) == False:
        with open('stubs/pass_types_html_' + year,'wb') as f:
            pass_types_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/passing_types/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(pass_types_html,f)

    if os.path.exists('stubs/goal_shot_creation_html_' + year) == False:
        with open('stubs/goal_shot_creation_html_' + year,'wb') as f:
            goal_shot_creation_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/gca/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(goal_shot_creation_html,f)

    
    if os.path.exists('stubs/defensive_actions_html_' + year) == False:
        with open('stubs/defensive_actions_html_' + year,'wb') as f:
            defensive_actions_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/defense/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(defensive_actions_html,f)

    if os.path.exists('stubs/possesion_html_' + year) == False:
        with open('stubs/possesion_html_' + year,'wb') as f:
            possesion_html = requests.get('https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/possession/players/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats').text
            pickle.dump(possesion_html,f)



    # Defining arrays of data
    advanced_goalkeeping = BeautifulSoup(advanced_goalkeeping_html,'lxml')
    shooting = BeautifulSoup(shooting_html,'lxml')
    passing = BeautifulSoup(passing_html,'lxml')
    pass_types = BeautifulSoup(pass_types_html,'lxml')
    goal_shot_creation = BeautifulSoup(goal_shot_creation_html,'lxml')
    defensive_actions = BeautifulSoup(defensive_actions_html,'lxml')
    possesion = BeautifulSoup(possesion_html,'lxml')

    
    print("link defence: " + 'https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/defense/squads/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats')
    print("link possesion: " + 'https://fbref.com/en/comps/Big5/' + str(int(year) - 1) + '-' + year + '/possession/players/' + str(int(year) - 1) + '-' + year + '-Big-5-European-Leagues-Stats')

    
    # Defining arrays of data points

    # Advanced goalkeeping
    psxg_sot = advanced_goalkeeping.find_all('td',attrs={"data-stat":"gk_psnpxg_per_shot_on_target_against"})
    launched_cpm_perc = advanced_goalkeeping.find_all('td',attrs={"data-stat":"gk_passes_pct_launched"})
    launch_perc = advanced_goalkeeping.find_all('td',attrs={"data-stat":"gk_pct_goal_kicks_launched"})
    av_dist = advanced_goalkeeping.find_all('td',attrs={'data-stat':"gk_avg_distance_def_actions"})
    def_actions_out_pen = advanced_goalkeeping.find_all('td',attrs={'data-stat':'gk_def_actions_outside_pen_area_per90'})

    # Defesnive Actions
    tkl_w = defensive_actions.find_all('td',attrs={'data-stat':'tackles_won'})
    interceptions = defensive_actions.find_all('td',attrs={'data-stat':'interceptions'})
    chl_lost = defensive_actions.find_all('td',attrs={'data-stat':'challenges_lost'})

    # Shooting
    sot_perc = shooting.find_all('td',attrs={'data-stat':'shots_on_target_pct'})
    shot_per_90 = shooting.find_all('td',attrs={'data-stat':'shots_per90'})
    av_shot_dist = shooting.find_all('td',attrs={'data-stat':'average_shot_distance'})

    # Passing
    cmp_per = passing.find_all('td',attrs={'data-stat':'passes_pct'})
    prog_dist = passing.find_all('td',attrs={'data-stat':'passes_progressive_distance'})
    key_pass = passing.find_all('td',attrs={'data-stat':'assisted_shots'})
    pass_into_pa = passing.find_all('td',attrs={'data-stat':'passes_into_penalty_area'})
    crosses_into_pa = passing.find_all('td',attrs={'data-stat':'crosses_into_penalty_area'})

    # Pass Types
    through_ball = pass_types.find_all('td',attrs={'data-stat':'through_balls'})
    switch = pass_types.find_all('td',attrs={'data-stat':'passes_switches'})
    crosses = pass_types.find_all('td',attrs={'data-stat':'crosses'})

    # Goal creating actions
    sca_to = goal_shot_creation.find_all('td',attrs={'data-stat':'sca_take_ons'})
    shot_to_shot = goal_shot_creation.find_all('td',attrs={'data-stat':'sca_shots'})
    sca_def_actions = goal_shot_creation.find_all('td',attrs={'data-stat':'sca_defense'})

    # Possesion
    touches_def_3rd = possesion.find_all('td',attrs={'data-stat':'touches_def_3rd'})
    touches_mid_3rd = possesion.find_all('td',attrs={'data-stat':'touches_mid_3rd'})
    touches_att_3rd = possesion.find_all('td',attrs={'data-stat':'touches_att_3rd'})

    #Checking all variables are valid

    #print(psxg_sot[0],launched_cpm_perc[0],launch_perc[0],av_dist[0],def_actions_out_pen[0],tkl_w[0],interceptions[0],chl_lost[0],sot_perc[0],shot_per_90[0],av_shot_dist[0])
    #print(cmp_per[0],prog_dist[0],key_pass[0],pass_into_pa[0],crosses_into_pa[0])
    #print(through_ball[0],switch[0],crosses[0])
    #print(sca_to[0],shot_to_shot[0],sca_def_actions[0])
    #print(touches_att_3rd[0],touches_def_3rd[0],touches_mid_3rd[0])


    # Mapping index of prem teams to name of team
    team_index = advanced_goalkeeping.find_all('th',attrs={'scope':'row'})
    teams = advanced_goalkeeping.find_all('td',attrs={'data-stat':'comp'})
    team_names = advanced_goalkeeping.find_all('td',attrs={'data-stat':'team'})
    prem_team_index = set()

    for i,t in enumerate(teams):
        if t.get_text() != 'eng Premier League':
            continue
        index = int(team_index[i].get_text()) 
        prem_team_index.add(index - 1)
        team_name = team_names[index - 1].get_text()[1:]
        team_data_per_year[year][team_name] = {}

    for index in prem_team_index:
        team_name = team_names[index].get_text()[1:]

        team_data_per_year[year][team_name]['psxg_sot'] = float(psxg_sot[index].get_text()) if psxg_sot[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['launched_cpm_perc'] = float(launched_cpm_perc[index].get_text()) if launched_cpm_perc[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['launch_perc'] = float(launch_perc[index].get_text()) if launch_perc[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['av_dist'] = float(av_dist[index].get_text()) if av_dist[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['def_actions_out_pen'] = float(def_actions_out_pen[index].get_text()) if def_actions_out_pen[index].get_text() != '' else 0.0

        team_data_per_year[year][team_name]['tkl_w'] = float(tkl_w[index].get_text()) if tkl_w[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['interceptions'] = float(interceptions[index].get_text()) if interceptions[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['chl_lost'] = float(chl_lost[index].get_text()) if chl_lost[index].get_text() != '' else 0.0

        team_data_per_year[year][team_name]['sot_perc'] = float(sot_perc[index].get_text()) if sot_perc[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['shot_per_90'] = float(shot_per_90[index].get_text()) if shot_per_90[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['av_shot_dist'] = float(av_shot_dist[index].get_text()) if av_shot_dist[index].get_text() != '' else 0.0

        team_data_per_year[year][team_name]['cmp_per'] = float(cmp_per[index].get_text()) if cmp_per[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['prog_dist'] = float(prog_dist[index].get_text()) if prog_dist[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['key_pass'] = float(key_pass[index].get_text()) if key_pass[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['pass_into_pa'] = float(pass_into_pa[index].get_text()) if pass_into_pa[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['crosses_into_pa'] = float(crosses_into_pa[index].get_text()) if crosses_into_pa[index].get_text() != '' else 0.0

        team_data_per_year[year][team_name]['through_ball'] = float(through_ball[index].get_text()) if through_ball[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['switch'] = float(switch[index].get_text()) if switch[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['crosses'] = float(crosses[index].get_text()) if crosses[index].get_text() != '' else 0.0
        
        team_data_per_year[year][team_name]['sca_to'] = float(sca_to[index].get_text()) if sca_to[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['shot_to_shot'] = float(shot_to_shot[index].get_text()) if shot_to_shot[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['sca_def_actions'] = float(sca_def_actions[index].get_text()) if sca_def_actions[index].get_text() != '' else 0.0

        team_data_per_year[year][team_name]['touches_def_3rd'] = float(touches_def_3rd[index].get_text()) if touches_def_3rd[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['touches_mid_3rd'] = float(touches_mid_3rd[index].get_text()) if touches_mid_3rd[index].get_text() != '' else 0.0
        team_data_per_year[year][team_name]['touches_att_3rd'] = float(touches_att_3rd[index].get_text()) if touches_att_3rd[index].get_text() != '' else 0.0

if os.path.exists('stubs/team_data_per_year') == False:
        with open('stubs/team_data_per_year','wb') as f:
            pickle.dump(team_data_per_year,f)
print(team_data_per_year)
        
        
    


        


    
    

