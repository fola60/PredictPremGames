import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

with open('stubs/team_data_per_year','rb') as f:
    team_data_per_year = pickle.load(f)

years = ["2025","2024","2023","2022","2021","2020","2019","2018"]
df = pd.read_csv('./match_data.csv',encoding='latin-1')

df = df.drop(columns = ['home_name','away_name','year'])

X = df.iloc[:,0:52]
y = df.iloc[:,52:54]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=17, test_size=0.2)

rf = MultiOutputClassifier(RandomForestClassifier())
rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

score = rf.score(X_test,y_test)
"""
print(score)

for i, column in enumerate(y.columns):
    print(f"Classification Report for {column}:")
    print(classification_report(y_test.iloc[:, i], y_pred[:, i]))
    print("\n")

for i, estimator in enumerate(rf.estimators_):
    importances = estimator.feature_importances_
    feature_importances = pd.DataFrame(importances, index=X.columns, columns=[f'Classifier {i}'])
    print(f"Feature Importances for Classifier {i}:")
    print(feature_importances.sort_values(by=f'Classifier {i}', ascending=False))
    print("\n")
"""

for year in years:
    team_names = [k for k,v in team_data_per_year[year].items()]

home_team_name = "Chelsea"
away_team_name = "Manchester Utd"

team_home_data = team_data_per_year["2025"][home_team_name]
team_away_data = team_data_per_year["2025"][away_team_name]


team_home_data = [v for k,v in team_home_data.items()]
team_away_data = [v for k,v in team_away_data.items()]

data = [1,0]
data.extend(team_home_data)
data.extend(team_away_data)

single_row = pd.DataFrame([data],columns=X.columns)

y_pred_single_row = rf.predict(single_row)


print(y_pred_single_row)
