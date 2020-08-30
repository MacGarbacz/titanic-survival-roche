from flask import Flask, request
import pickle as p
from src import build_features as bf
import pandas as pd

app = Flask(__name__)


# Reclate a URL which is to be called via a POST request
@app.route('/api/', methods=['POST'])
def makecalc():
    # Extract the json payload, convert it into a dataframe
    data = request.get_json()
    df = pd.DataFrame(data)

    # Expand the attributes
    cleaned_data = bf.feature_expansion(df, 'api')

    # Predict the outcome using the model and return it as a json object
    prediction = model.predict(cleaned_data)
    json_result = pd.Series(prediction).to_json(orient='values')

    return json_result


# Load the model at start up of the API
if __name__ == '__main__':
    modelfile = '../data/model.pkl'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')
