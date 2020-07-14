import requests
import flask
from flask import request, jsonify
from decouple import config

app = flask.Flask(__name__)
app.config["DEBUG"] = True

fruits = [
    {
        'id': 1,
        'name': 'Banana',
        'calories': 100,
        'benefit': 'High in Potassium. Good for your heart and blood pressure'
    },
    {
        'id': 2,
        'name': 'Orange',
        'calories': 45,
        'benefit': 'High in Vitamin C'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "banana"


@app.route('/api/v1/fruits/all', methods=['GET'])
def all_fruits():
    return jsonify(fruits)


@app.route('/api/v1/fruits', methods=['GET'])
def get_fruit_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No name field provided. Please specify an id."

        # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for fruit in fruits:
        if fruit['id'] == id:
            results.append(fruit)

    return jsonify(results)


@app.route('/api/v2/fruits', methods=['GET'])
def get_fruit_details():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No name field provided. Please specify an id."

        # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for fruit in fruits:
        if fruit['id'] == id:
            fruit['botanical_name'] = get_botanical_name(id)
            results.append(fruit)

    return jsonify(results)


def get_botanical_name(fruit_id):
    print("in botanical name")

    api_url = config('BOTANICAL_SERVICE_URL')
    response = requests.get(api_url, params={'id': fruit_id})

    json_response = response.json()

    return json_response['botanical_name']


app.run(debug=True, host='0.0.0.0')
