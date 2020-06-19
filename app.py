from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
app=Flask(__name__)

GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
@app.route('/')
def wel():
    return 'Hello guys'


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    with open('state.json') as f:
        statecode=json.load(f)
    msg = request.form.get('Body')
    if "HEY" in msg.upper() or "HELLO" in msg.upper() or "HI" ==msg.upper():
        resp = MessagingResponse()
        resp.message("Hey there !! ,\n My Name Twilo 😀! \n I will help you guys in \n 1.) Covid Cases Update Please Type Covid 😷! \n 2.) A Joke for you Please Type Joke 😜! \n I am still learning will offer you more feature in Future 😊")
        print(str(resp))
        k= str(resp)
        
        
    elif "JOKE" in msg.upper():
        url='https://official-joke-api.appspot.com/random_joke'
        response=requests.get(url).json()
        resp = MessagingResponse()
        resp.message(response['setup'] +'\n' +'\n'+ "Reply :" +response['punchline'] +"😜🤣")
        print(type(msg))
        k= str(resp)
    elif "COVID" == msg.upper():
         resp = MessagingResponse()
         resp.message("Would you like to See \n 1. State wise then Type Covid {State_Code} like Rajasthan AS Covid RJ \n 2. Total India cases then simply Type Covid India")
         k=str(resp)
    elif "COVID" in msg.upper() and msg.upper().split(" ")[1] in list(statecode.keys()):
        url='https://api.covid19india.org/state_district_wise.json'
        data=requests.get(url).json()
        dicdata=dict(data)
        #print(dicdata.keys())
        Fullstatename=dicdata[statecode[msg.upper().split(" ")[1]]]['districtData']
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
        resp.message("Your state active cases are : {}".format(active)+"😟" +'\n' +"Your state recovered cases are : {}".format(recovered)+"🤩" +'\n' +"Your state confirmed cases are : {}".format(confirmed) +"😯" +'\n'+"Your state deceased cases are : {}".format(deceased)+"😔"+'\n'+"Your state today New cases are : {}".format(Newcase)+"😔")   
        k=str(resp)
        
    
    else:
        resp = MessagingResponse()
        resp.message("I am still learning , Shivam is helping me to answer your all questions .Keep Asking questions .Thanks")
        k=str(resp)
       
    return k

@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():

    response = MessagingResponse()
    num_media = int(request.values.get("NumMedia"))
    if not num_media:
        msg = response.message("Send us an image!")
    else:
        msg = response.message("Thanks for the image. Here's one for you!")
        msg.media(GOOD_BOY_URL)
    return str(response)


if __name__=='__main__':
    app.run(debug=True)
