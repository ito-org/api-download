from flask import Flask, escape, request, jsonify

from db import get_cases_by_location

app = Flask(__name__)

app.config['APPLICATION_ROOT'] = '/'


@app.route('cases')
def cases():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    cases = get_cases_by_location(lat, lon)
    return jsonify(cases)
