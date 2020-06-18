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
    if msg =='Hey':
        resp = MessagingResponse()
        resp.message("Hello there , I will help you in these cases now : 1.Covid case")
        resp.message()
        res =str(resp)
    else:
        resp = MessagingResponse()
        resp.message("Hello there,I will help you: 1.Covid case")
        resp.message()
        res =str(resp)
        res = str(resp)
    return res


if __name__=='__main__':
    app.run(debug=True)
