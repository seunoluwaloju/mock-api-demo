import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

fruits = [
    {
        'id': 1,
        'name': 'Banana',
        'botanical_name': 'Musa'
    }
]


@app.route('/api/v1/botanical', methods=['GET'])
def get_botanical_name():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No name field provided. Please specify an id."

    botanical_name = ''

    for fruit in fruits:
        if fruit['id'] == id:
            botanical_name = fruit['botanical_name']

    return jsonify({'botanical_name': botanical_name})


app.run(debug=True, host='0.0.0.0')
