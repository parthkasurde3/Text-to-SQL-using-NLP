from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pickle
import pandas as pd, numpy as np


import os
import speech_recognition as sr
import subprocess
import sqlite3

import matplotlib.pyplot as plt

  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'
  
mysql = MySQL(app)


 

@app.route('/')
def home():
	return render_template('home.html')
  

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('test.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  

@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)


@app.route('/Speech', methods=['GET', 'POST'])
def Speech():
    Output = ""
    OutputQuery = ""
    df = None

    if request.method == 'POST':
        if 'inputText' in request.form:
            Output = request.form['inputText']
        else:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                Output = r.recognize_google(audio)
            except:
                pass

    # Create your connection.
    cnx = sqlite3.connect('school.db')
    
    Output = Output.lower()
    print("Speech 2 Text:", Output)

    try:
        df = subprocess.check_output('python -m ln2sql.main -d database_store/school.sql -l lang_store/english.csv -i "' + Output + '"', stderr=subprocess.STDOUT, shell=True)
        df = repr(df)
        df = df.replace(r"\r\n", " ")
        df = df.replace(r"b", "")
        df = df.replace(r'"', "")
        df = df[:-1]
        df = df[1:]
        print("--####>", df)
        df1 = pd.read_sql_query(df, cnx) 
        tables = [df1.to_html(classes='TableBody')]
        titles = df1.columns.values
        OutputQuery = df
    except subprocess.CalledProcessError as exc:
        print("Status: FAIL", exc.returncode, exc.output)
        return "Database not found"
    
    return render_template('test.html', Output=Output, OutputQuery=OutputQuery, tables=tables, titles=titles)

if __name__ == "__main__":
    app.run()
