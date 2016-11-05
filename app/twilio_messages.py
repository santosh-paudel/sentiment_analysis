from flask import Flask, request
from twilio import twiml


app = Flask(__name__)

#route not needed 
#@app.route('/index', methods=['GET','POST'])
def text_message():
    #if methods.request=='POST':
    number = request.form['From']
    message_body = request.form['Body']
    #print(message_body)
    #return 'hello'
    return message_body

if __name__ == '__main__':
    app.run()