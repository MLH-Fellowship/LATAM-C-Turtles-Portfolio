from flask import Flask, render_template, url_for, json
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing_page.html')

# code by kOssi (https://stackoverflow.com/questions/21133976/flask-load-local-json)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "saul.json")
data = json.load(open(json_url))

@app.route('/profile')
def profile():
    return render_template('profile.html', data=data)
