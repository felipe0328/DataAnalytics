from app.dashboard import bp
from flask import json, Response
from controller.analytics import analytics


@bp.route("/", methods=['GET'])
def analize_data_endpoint():
    results = analytics.analize_data_and_return_results()
    response = Response(
        response=json.dumps(results),
        status=200,
        mimetype='application/json'
    )
    return response
