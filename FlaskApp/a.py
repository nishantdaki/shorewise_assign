# importing libraries
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app) # instantiate the mail class

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'nishantcodemania@gmail.com'
app.config['MAIL_PASSWORD'] = '99$Nishant'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# message object mapped to a particular URL ‘/’
@app.route("/")
def index():
	msg = Message(
					'Hello',
					sender = app.config['MAIL_USERNAME'],
					recipients = ['nishantd@meditab.com']
				)
	msg.body = 'Hello Flask message sent from Flask-Mail'
	mail.send(msg)
	return 'Sent'

if __name__ == '__main__':
	app.run(debug = True)
