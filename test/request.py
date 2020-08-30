import requests
import json
import pandas as pd

url = 'http://127.0.0.1:5000/api/'

#Sample record to be used for a sample call to the API
sample_data = {'PassengerId': [15],
               'Pclass': [1],
               'Name': ["James Mr. Jones"],
               'Sex': ["male"],
               'Age': [20],
               'SibSp': [1],
               'Parch': [2],
               'Ticket': [233] ,
               'Fare': [45.0],
               'Cabin': ['E2232'],
               'Embarked': ['C']}

#Convert the dictionary into json and execute a POST request
j_data = json.dumps(sample_data)
df = pd.DataFrame.from_dict(sample_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)

#Display the results
print(r, r.text)