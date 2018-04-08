import urllib
import json
import os
from flask import flask
from flask import request
from flask import make_response

#Flask app shall start in global layout
app = Flask(__name__)

@app.route('/webhook', method=['POST'] )
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req,indent=4))
    res = makeWebhokResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r=make_response(res)
    #header->response
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    #"interest"는 dialogflow에서 본인이 만든 action의 이름
    if req.get("result").get("action")!= "interest":
        return{}
    #result를 받아와야 parameter, action 등을 다 받아올 수 있음. json 파일 참고
    result = req.get("result")
    #우리가 받는 변수들
    parameters = result.get("parameters")
    zone = parameters.get("bank-name")
    #밑에는 constant list인데 dialogflow에서 쓰지 못하는 복잡한 것들,
    #즉 연산에 필요한 것들을 나열해둔것.
    bank = {'Federal Bank':'6.70', 'Andhra Bank':'6.850', ' Bandhan Bank':'1.170'}
    speech = "The interest rate of"+ zone + "is"+ str(bank[name])
    #dialogflow(콘솔)에 내보낼 것들을 Response에 담는다
    print("Response: ")
    print(speech)
    return{
        "speech": speech,
        "displayText":speech,
        #source : agent name
        "source": "BankInterestRates"

    }
if __name__ == '__main__'
    #linking to local server to online with web using jrock?
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host= '0.0.0.0' )