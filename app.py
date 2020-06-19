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
        resp.message("Hey there!! , My Name Twilo !")
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
        url='https://api.covid19india.org/state_district_wise.json'
        data=requests.get(url).json()
        dicdata=dict(data)
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
        resp = MessagingResponse()
        #details= "Your activecase is : {}".format(active) +" "+ "confirmed is : {}".format(confirmed) +" "+ "recovered is :{}".format(recovered) +'\n' + "newcase :{}".format(Newcase)
        resp.message("Your state active cases are : {}".format(active) "\n"
                     "Your state recovered cases are : {}".format(recovered) "\n"
                     "Your state confirmed cases are : {}".format(confirmed) "\n"
                     "Your state deceased cases are : {}".format(deceased) "\n"
                     "Your state today New cases are : {}".format(Newcase) "\n" )   
        k=str(resp)
    else:
        resp = MessagingResponse()
        resp.message("I am still learning , Shivam is helping me to answer your all questions .Keep Asking questions .Thanks")
        k=str(resp)
       
    return k


if __name__=='__main__':
    app.run(debug=True)
