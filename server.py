from flask import Flask,request
import simplejson as json

app = Flask(__name__)

@app.route('/log',methods=['POST'])
def log():
	type=request.form['type']
	message=request.form['message']
    return 'Hello World!'

if __name__ == '__main__':
    app.run()