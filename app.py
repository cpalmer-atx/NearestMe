from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if (request.method == 'POST'):
        userAddress = request.form['address']
        destination = request.form['destination']
        # print(f'Submit button should find shortest route from {userAddress} to {destination}.')

    if (userAddress == '' or destination == ''):
        return render_template('index.html', message='Enter required fields')
    # return render_template('index.html')
    return render_template('index.html', message=f'Shortest route from {userAddress} to {destination} will appear here.')

if __name__ == '__main__':
    app.debug = True
    app.run()