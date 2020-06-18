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

    # Create reply
    resp = MessagingResponse()
    resp.message(" State                        State Code
 Andaman and Nicobar Islands  AN
 Andhra Pradesh               AP
 Andhra Pradesh (New)         AD
 Arunachal Pradesh            AR
 Assam                        AS
 Bihar                        BH
 Chandigarh                   CH
 Chattisgarh                  CT
 Dadra and Nagar Haveli       DN
 Daman and Diu                DD
 Delhi                        DL
 Goa                          GA
 Gujarat                      GJ
 Haryana                      HR
 Himachal Pradesh             HP
 Jammu and Kashmir            JK
 Jharkhand                    JH
 Karnataka                    KA
 Kerala                       KL
 Lakshadweep Islands          LD
 Madhya Pradesh               MP
 Maharashtra                  MH
 Manipur                      MN
 Meghalaya                    ME
 Mizoram                      MI
 Nagaland                     NL
 Odisha                       OR
 Pondicherry                  PY
 Punjab                       PB
 Rajasthan                    RJ
 Sikkim                       SK
 Tamil Nadu                   TN
 Telangana                    TS
 Tripura                      TR
 Uttar Pradesh                UP
 Uttarakhand                  UT
 West Bengal                  WB")

    return str(resp)



if __name__=='__main__':
    app.run(debug=True)
