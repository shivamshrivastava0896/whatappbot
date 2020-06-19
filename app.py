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
    msg = request.form.get('Body')
    if "HEY" in msg.upper():
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
    elif "COVID" in msg.upper():
         resp = MessagingResponse()
         resp.message("Would you like to See \n 1. State wise then Type Covid {State_Code} like Rajasthan AS Covid RJ \n 2. Total India cases then simply Type Covid India")
         k=str(resp)
         msg = request.form.get('Body')
         if msg == covid
    
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
