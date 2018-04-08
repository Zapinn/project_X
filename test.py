# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', method=['POST'] )
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)

    r=make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeWebhookResult(req):
    if req.get("result").get("action")== "a1":
        result = req.get("result")
        parameters = result.get("parameters")
        a1 = parameters.get("a1")

    elif req.get("result").get("action") == "a2":
            result = req.get("result")
            parameters = result.get("parameters")
            a2 = parameters.get("a2")

    elif req.get("result").get("action") == "a3":
            result = req.get("result")
            parameters = result.get("parameters")
            a3 = parameters.get("a3")
            fin=1

    if fin == 1:
        speech = "a1=" + a1 + "a2="+  a2 +"a3="+ a3
        fin = 0



    print("Response: ")
    print(speech)
    return{
        "speech": speech,
        "displayText": speech,
        "source": "Project"

    }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host= '0.0.0.0')
