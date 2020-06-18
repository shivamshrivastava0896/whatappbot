from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
app=Flask(__name__)


@app.route('/')
def wel():
    return 'Hello guys'


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    if "Hey" in msg:
        resp = MessagingResponse()
        resp.message("Hey my Name Twilo , I will help you in 1. covid case number Please type covid ! "
                    + ' ' +"2. Joke of the day please type Joke")
        print(type(msg))
        k= str(resp)
        
    elif "Joke" in msg:
        url='https://official-joke-api.appspot.com/random_joke'
        response=request.get(url).json()
        resp = MessagingResponse()
        resp.message(response['setup'] + response['punchline'])
        print(type(msg))
        k= str(resp)

    return k


if __name__=='__main__':
    app.run(debug=True)
