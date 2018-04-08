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