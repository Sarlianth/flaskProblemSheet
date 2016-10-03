from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
	
@app.route('/name/<user>')
def name(user):
    return 'Your name is %s' % user
	
if __name__ == "__main__":
	app.run()