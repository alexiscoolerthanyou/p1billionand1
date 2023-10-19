# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define route and Verify_otp() function below

def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACa2c74b9ed94c01edae2c3af8e7a5cead'
        auth_token = 'fbb7e6938268d77c6c06be8326319bdc'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('IS5cb55c56064bb65fbd6259f3b70e7b06') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('')










        verification = client.verify \
            .services('Enter service sid from twilio') \
            .verifications \
            .create(to=enter mobile number variable here, channel='Enter mode of sending otp here')










if __name__ == "__main__":
    app.run()

