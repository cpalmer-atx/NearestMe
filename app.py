from flask import Flask, render_template, request

from security import API_KEY, BASE_URL
import requests
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if (request.method == 'POST'):
        userAddress = request.form['address']
        destination = request.form['destination']
        testDestination = "1901+Kelly+Ln,+Pflugerville,+TX+78660"

        # Get response from Google given above parameters
        r = requests.get(BASE_URL + "origins=" + userAddress + "&destinations=" + testDestination + "&key=" + API_KEY)
        print(r.json())
        distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]

    if (userAddress == '' or destination == ''):
        return render_template('index.html', message='Enter required fields')
    # return render_template('index.html')
    return render_template('index.html', message=f'Shortest route from {userAddress} to {destination} is {distance}.')

if __name__ == '__main__':
    app.debug = True
    app.run()