from flask import Flask, session, request, render_template, flash, redirect, url_for, g, jsonify
import model
from model import session as db_session
from model import User, Contact, GPS_Location
import os
import json
from sqlalchemy import desc

##############     USER SECTION     ##############################

@app.route("/")
def index():
	return render_template("index.html")




if __name__ =="__main__":
	app.run(debug =True)