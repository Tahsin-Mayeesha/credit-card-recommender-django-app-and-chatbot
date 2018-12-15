from flask import Flask, request, make_response, jsonify
import json

# initialize the flask app
app = Flask(__name__)

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
    return make_response(jsonify({'fulfillmentText': "I want a card"}))
# run the app
if __name__ == '__main__':
   app.run()