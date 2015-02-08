import json
import os

import flask
from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify
from sqlalchemy import desc

import LanguageAnalysis
import electric_imp

app = Flask(__name__)

##############     USER SECTION     ##############################

ROMANCE_THRESHOLD = 5


@app.route("/", methods=['GET'])
def index():
    return render_template("home.html")


@app.route("/", methods=['POST'])
def ajax_submit():
    email_addr = request.form['email']
    email_body = request.form['body']

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


if __name__ =="__main__":
    app.run(debug =True)
