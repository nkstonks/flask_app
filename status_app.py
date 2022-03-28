# Got this web app working on heroku by specifying the port waitress should run on.
# Did this by running the script with a port argument (see procfile) 
from flask import Flask, render_template, url_for
import os

status_app = Flask(__name__)

@status_app.route('/')
def home():
    return render_template("status.html")

status_app.secret_key = 'BLAyu#7bcic234yrhnd/nq!@2t5fvk;qcwmwxd;232'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    status_app.run(host ='0.0.0.0', port=port)