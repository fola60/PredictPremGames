import csv
from csv import writer
import pickle


years = ["2024","2023","2022","2021","2020","2019","2018"]

# Getting team data
with open('stubs/team_data_per_year','rb') as f:
    team_data_per_year = pickle.load(f)

# Getting fixture data
with open('stubs/prem_fixture_history','rb') as f:
    prem_fixture_history = pickle.load(f)

with open('match_data.csv', 'w', newline='', encoding = 'utf8') as f:
    theWriter = writer(f)
    header = ['year','home_name','away_name','home','away','psxg_sot_home','launched_cpm_perc_home','launch_perc_home','av_dist_home','def_actions_out_pen_home','tkl_w_home','interceptions_home','chl_lost_home','sot_perc_home','shot_per_90_home','av_shot_dist_home','cmp_per_home','prog_dist_home','key_pass_home','pass_into_pa_home','crosses_into_pa_home','through_ball_home','switch_home','crosses_home','sca_to_home','shot_to_shot_home','sca_def_actions_home','touches_def_3rd_home','touches_mid_3rd_home','touches_att_3rd_home','psxg_sot_away','launched_cpm_perc_away','launch_perc_away','av_dist_away','def_actions_out_pen_away','tkl_w_away','interceptions_away','chl_lost_away','sot_perc_away','shot_per_90_away','av_shot_dist_away','cmp_per_away','prog_dist_away','key_pass_away','pass_into_pa_away','crosses_into_pa_away','through_ball_away','switch_away','crosses_away','sca_to_away','shot_to_shot_away','sca_def_actions_away','touches_def_3rd_away','touches_mid_3rd_away','touches_att_3rd_away','home_score','away_score']
    theWriter.writerow(header)
    for year in years:
        for home,away,score in prem_fixture_history[year]:
            home_score,away_score = score
            home_data = team_data_per_year[year][home]
            away_data = team_data_per_year[year][away]
            home_data = [v for k,v in home_data.items()]
            away_data = [v for k,v in away_data.items()]
            print(home)
            print(home_data)
            print(away)
            print(away_data)
            print(home_score,away_score)

            statlist = [year,home,away,1,0]
            statlist.extend(home_data)
            statlist.extend(away_data)
            statlist.extend([home_score,away_score])
            theWriter.writerow(statlist)
print("I cant believe that we made it this far")