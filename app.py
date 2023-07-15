from flask import Flask, jsonify, json
from controller.analytics import analytics

app = Flask(__name__)


@app.route("/", methods=['GET'])
def analize_data_endpoint():
    results = analytics.analize_data_and_return_results()
    response = app.response_class(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    return response
