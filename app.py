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
    if 'HEY' in msg.upper() or 'HI' in msg.upper() or 'HELLO' in msg.upper() :
        resp = MessagingResponse()
        resp.message("Hello there , I will help you in these cases now : 1.Covid case " +''
                     "2. Weather of your city "+ ' '
                     "3.Joke for you ")
        resp.message()
        k=str(resp)
    return k 


if __name__=='__main__':
    app.run(debug=True)
