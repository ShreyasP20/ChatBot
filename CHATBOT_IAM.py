from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import emoji
service_numbers={};
app=Flask(__name__)

@app.route('/bot', methods=['POST'])

def bot():
    user_number=request.values.get('Wald')
    print(user_number)
    user_msg=request.values.get('Body', '').lower()
    bot_resp= MessagingResponse()
    msg= bot_resp.message()
    if ("hello" in user_msg or "hi" in user_msg) :
        msg.body("Hello Sir, I am assitant from IAM(Integrated Active Monitoring) Pvt Limited. How can I help you \n1. Services:thumbs_up: \n2. Products \n3. Contact Us ")
    if ("services"  in user_msg or "1" in user_msg):
        msg.body("Our Services Include: \n1. Centralized Monitoring System \n2. CCTV Monitoring \n3. Fire Alarm \n4. Guard Patrolling \n5. System Health Monitoring \n6. Temperature Monitoring \n7. Energy Monitoring \n8. Footfall Counting \n9. Dwell Time/Heat Map/Queue Managemnet/ Age Gender \n10. Grocery Vending Machine")
    if ("products" in user_msg or "2" in user_msg):
        msg.body("Our Products Include: \n1. SmartIntegra(Smart 1) \n2. Vechile tracking with Temperature Monitoring \n3. Temperature, Humidity, CO2 Monitoring \n4. Smart Meter and DG Monitoring \n5. People Counting \n6. Electronic Shelf Labels \n7. Virtual Mirror \n8. Sinage Solution \n9. PIR \n10. Hand Sanitizer \n11. Grossery Vending Machine \n12. IR Thermometer Gun \n13. Masks, Glove \n14. Thermal Camera")
    if ("contact" in user_msg or "3" in user_msg):
        msg.body("To Contact us:\n1. Email:enquiry@smartiam.in \n2. Call Us On:+91-020-67479668 ")
    return str(bot_resp)


if __name__=='__main__':
    app.run(debug=True)


    