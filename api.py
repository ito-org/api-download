from flask import Flask, escape, request

app = Flask(__name__)

app.config['APPLICATION_ROOT'] = '/'


@app.route('cases')
def cases():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    return f'Hello, {escape(name)}!'
