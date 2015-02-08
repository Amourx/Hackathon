import json
import os

import flask
from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify
from sqlalchemy import desc

import LanguageAnalysis

app = Flask(__name__)

##############     USER SECTION     ##############################


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/analyze', methods=['GET'])
def analyze_page():
    return render_template('analyze.html')


@app.route('/analyze', methods=['POST'])
def analyze_text():
    text = request.form['text']
    result = LanguageAnalysis.LanguageAnalyzer().analyze(text)
    return render_template('analyze.html', result=result)


if __name__ =="__main__":
    app.run(debug =True)
