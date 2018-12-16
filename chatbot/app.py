from flask import Flask, request, make_response, jsonify
import json
from sklearn.externals import joblib
import numpy as np
import os
from recommender import user_features,make_query

cards = pd.read_csv("data.csv")

def get_card_names(indices):
    return cards.iloc[indices[0],:]["card_name"]
    
# initialize the flask app
app = Flask(__name__)

def make_recommendations():
    pass

# default route
@app.route('/')
def index():
    return 'Hello World!'
# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    req = request.get_json(force=True)
    action = req.get("queryResult").get("action")
    parameters = req.get("queryResult").get("parameters")
    query = make_query(user_features(parameters))
    full_dir = "knn.pickle"
    model = joblib.load(os.path.realpath(full_dir))
    query = np.array(query)
    result = model.kneighbors(query.reshape(1,-1))
    indices = result[1]
    indices = indices.tolist()
    card_names = get_card_names(indices).tolist()
    result_text = ",".join(card_names)
    return make_response(jsonify({'fulfillmentText': str(result_text)}))
# run the app
if __name__ == '__main__':
   app.run()