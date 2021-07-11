from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import rds_db as db
# arr=['Id','Name','Phone','Email','Gender','Feedback']
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/insert',methods = ['post'])
def insert():
    
    if request.method == 'POST':
        ID=request.form['num']
        name = request.form['name']
        phone = request.form['phn']
        email = request.form['email']
        gender = request.form['optradio']
        feedback = request.form['fb']
        db.insert_details(ID,name,phone,email,gender,feedback)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('index.html',var=var,details=details)



if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=80)