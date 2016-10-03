from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

##when accessing  127.0.0.1:8000/name/SOMETHING
##returns Your name is SOMETHING	
@app.route('/name/<user>')
def name(user):
    return 'Your name is %s' % user
	
if __name__ == "__main__":
	app.run()