from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse
app=Flask(__name__)


@app.route('/')
def wel():
    return 'Hello'

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))
    print(str(resp))

    return str(resp)



if __name__=='__main__':
    app.run(debug=True)