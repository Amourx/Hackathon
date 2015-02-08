import json
import os
import flask
from email.mime.text import MIMEText
from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify
import smtplib, smtpd
from sqlalchemy import desc

import LanguageAnalysis
import electric_imp

app = Flask(__name__)
USERNAME = 'amourx4@gmail.com'
PASSWORD = 'amourx4me'
SENDER = 'amourx4@gmail.com'
##############     USER SECTION     ##############################

from threading import Thread

def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()
    return wrapper

@async
def send_mail(text, threshhold, receiver):
   message = "\r\n".join([
        "From: %s" % SENDER,
        "To: %s" % receiver,
        "Subject: You have received a new email with a romance rating of %s" % threshhold,
        "",
       text
        ])
   try:
      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(USERNAME,PASSWORD)
      server.sendmail(SENDER, receiver, message)
      server.quit()
      print "Successfully sent email"
   except smtplib.SMTPException:
      print "Error: unable to send email"


ROMANCE_THRESHOLD = 5


@app.route("/", methods=['GET'])
def index():
    return render_template("home.html")


@app.route("/", methods=['POST'])
def ajax_submit():
    email_addr = request.form['email']
    email_body = request.form['body']

    result = LanguageAnalysis.LanguageAnalyzer().analyze(email_body)
    score = sum(result.values())

    if score < ROMANCE_THRESHOLD and score > 0:
        electric_imp.lukewarm()
    elif score > ROMANCE_THRESHOLD:
        electric_imp.romance()

    send_mail(email_body, score, email_addr)

    return flask.jsonify({'status': 'OK'})

@app.route('/analyze', methods=['GET'])
def analyze_page():
    return render_template('analyze.html')


@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form['text']
    result = LanguageAnalysis.LanguageAnalyzer().analyze(text)
    score = sum(result.values())
    if score < ROMANCE_THRESHOLD and score > 0:
        electric_imp.lukewarm()
    elif score > ROMANCE_THRESHOLD:
        electric_imp.romance()

    return render_template('analyze.html', result=result)

@app.route("/email_processor", methods = ['POST'])
def email_processor():
   data = request.data
   dataDict = json.loads(data)
   body = dataDict['Text-part']
   result = LanguageAnalysis.LanguageAnalyzer().analyze(body)
   score = sum(result.values())
   if score < ROMANCE_THRESHOLD and score > 0:
     electric_imp.lukewarm()
   elif score > ROMANCE_THRESHOLD:
     electric_imp.romance()


if __name__ =="__main__":
    app.run(debug =True)
