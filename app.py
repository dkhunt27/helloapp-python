from flask import Flask
app = Flask(__name__)

import json
import os

# VERSION gets reset by CI before
# building docker image
VERSION = "{VERSION_NUMBER}"

# ENVIRONMENT gets injected by pipeline deploy action
ENVIRONMENT = os.environ.get('ENVIRONMENT')

VERSION_ENV = VERSION + "." + ENVIRONMENT

@app.route("/")
def hello():
    return "HelloApp! Build Version %s\n" % VERSION_ENV

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
