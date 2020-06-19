from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
app=Flask(__name__)


@app.route('/')
def wel():
    return 'Hello guys'


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    if "HEY" in msg.upper():
        resp = MessagingResponse()
        resp.message("Hey there!!, My Name Twilo . +'\n' + I will help you in +'\n'+ 1). covid case number Please type covid ! "
                    + '\n' +" 2). Joke of the day please type Joke")
        print(type(msg))
        k= str(resp)
        
    elif "JOKE" in msg.upper():
        url='https://official-joke-api.appspot.com/random_joke'
        response=requests.get(url).json()
        resp = MessagingResponse()
        resp.message(response['setup'] +" "+response['punchline'])
        print(type(msg))
        k= str(resp)
    elif "COVID" in msg.upper():
        with open('state.json') as f:
            statecode=json.load(f)
        url='https://api.covid19india.org/state_district_wise.json'
        data=requests.get(url).json()
        dicdata=dict(data)
        #print(dicdata.keys())
        statename=statecode[val.upper()]
        Fullstatename=dicdata['Rajasthan']['districtData']
        active=0
        confirmed=0
        deceased=0
        recovered=0
        Newcase=0
        for i in Fullstatename.keys():
            active +=int(Fullstatename[i]['active'])
            confirmed +=int(Fullstatename[i]['confirmed'])
            deceased +=int(Fullstatename[i]['deceased'])
            recovered +=int(Fullstatename[i]['recovered'])
            Newcase +=int(Fullstatename[i]['delta']['confirmed'])
        details= "Your activecase is : {}".format(active) +" "+ "confirmed is : {}".format(confirmed) +" "+ "recovered is :{}".format(recovered) +'\n' + "newcase :{}".format(Newcase)
        resp = MessagingResponse()
        resp.message(details)   
        k=str(resp)
    else:
        resp = MessagingResponse()
        resp.message("I am still learning ,Shivam is helping me to answer your all question .Thanks")
        k=str(resp)
       
    return k


if __name__=='__main__':
    app.run(debug=True)
