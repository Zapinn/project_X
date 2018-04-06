import urllib
import json
import os
from flask import flask
from flask import request
from flask import.make_response

app = Flask(__name__)

@app.route('/webhook', method=['POST'] )
def webhook():
    req = reqeste.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req,indent=4))
    res - makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r=make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("acrion")!= "interest":
        return{}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("bank-name")
    bank = {'Federal Bank':'6.70', 'Andhra Bank':'6.850', ' Bandhan Bank':1.170'}
    speech = "The interest rate of"+zone + "is"+str(bank[name])
    print("Response: ")
    print(speech)
    return{
        "speech": speech,
        "displayText":speech,
        "source": "BankIterestRates"

    }
if __name__ == '__main__'
    prot = int(os.getenv('PORT',5000))
    print("Starting app on port %d" %(port))
    app.run(debug=True, prot=prot, host= '0.0.0.0' )