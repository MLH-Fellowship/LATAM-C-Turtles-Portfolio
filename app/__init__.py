from flask import Flask, render_template, url_for, json, Response
import os


app = Flask(__name__)

# code by kOssi (https://stackoverflow.com/questions/21133976/flask-load-local-json)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
SITE_FOLDER = "static/data"

@app.route('/')
def index():
    return render_template('landing_page.html')

@app.route('/profile/<name>')
def profile(name):
    json_url = os.path.join(SITE_ROOT, SITE_FOLDER, f"{name}.json")
    data = json.load(open(json_url))
    return render_template('profile.html', data=data)

# AWS Health endpoint
@app.route('/health', methods=['GET'])
def health():
    return Response(status=200)