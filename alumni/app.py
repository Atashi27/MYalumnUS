from flask import (Flask, request, flash, url_for, redirect, render_template)
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alumnUS.sqlite'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_pyfile('config.cfg')

mail = Mail(app)

s = URLSafeTimedSerializer('Thisisasecret!')


db = SQLAlchemy(app)

class alumni_meets(db.Model):
   mid = db.Column('mid', db.Integer, primary_key = True)
   date = db.Column(db.String(100))
   time = db.Column(db.String(50))
   no_of_alumni = db.Column(db.String(200)) 


   def __init__(self, date, time, no_of_alumni, ):	
	   self.date = date
	   self.time = time
	   self.no_of_alumni = no_of_alumni
	   

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/meet', methods = ['GET', 'POST'])
def meet():
   if request.method == 'POST':
      if not request.form['date'] or not request.form['time'] or not request.form['no_of_alumni']:
         flash('Please enter all the fields', 'error')
      else:
         alumni_meet = alumni_meets(request.form['date'], request.form['time'],request.form['no_of_alumni'])
         
         db.session.add(alumni_meet)
         db.session.commit()
         flash('Record was successfully added')
         return render_template('home.html')
   return render_template('meet.html')
   
   
@app.route('/sendreq', methods=['GET', 'POST'])
def sendreq():
    if request.method == 'GET':
        return render_template('sendreq.html')
    
    i=0
    with mail.connect() as conn:
        email = request.form['email']
        users = email.split(",")
        while i < len(users):
            msg = Message('SUBJECT', sender='admin_email_id', recipients=[users[i]])

            msg.body = request.form['content']

            conn.send(msg)
            i=i+1

    return render_template('home.html')

class alumni_personal_details(db.Model):
   aid = db.Column('aid', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   dob = db.Column(db.String(50))
   address = db.Column(db.String(200)) 
   from_y = db.Column(db.String(100))
   to_y = db.Column(db.String(50))
   contact = db.Column(db.String(200)) 
   mail_id = db.Column(db.String(100))
   


   def __init__(self, name, dob, address, from_y, to_y, contact, mail_id):	
	   self.name = name
	   self.dob = dob
	   self.address = address
	   self.from_y = from_y
	   self.to_y = to_y
	   self.contact = contact
	   self.mail_id =mail_id

@app.route('/alumni_per', methods = ['GET', 'POST'])
def alumni_per():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['dob'] or not request.form['address'] or not request.form['from_y'] or not request.form['to_y'] or not request.form['contact'] or not request.form['mail_id']:
         flash('Please enter all the fields', 'error')
      else:
         alumni_personal = alumni_personal_details(request.form['name'], request.form['dob'],request.form['address'],request.form['from_y'],request.form['to_y'],request.form['contact'],request.form['mail_id'])
         
         db.session.add(alumni_personal)
         db.session.commit()
         flash('Record was successfully added')
         return render_template('home.html')
   return render_template('alumni_per.html')
	

class alumni_professional_details(db.Model):
   aid = db.Column('aid', db.Integer, primary_key = True)
   current_company = db.Column(db.String(100))
   current_position = db.Column(db.String(50))
   qualification = db.Column(db.String(200)) 
   
   def __init__(self, current_company, current_position, qualification):	
	   self.current_company = current_company
	   self.current_position = current_position
	   self.qualification = qualification
	   
@app.route('/alumni_prof', methods = ['GET', 'POST'])
def alumni_prof():
   if request.method == 'POST':
      if not request.form['current_company'] or not request.form['current_position'] or not request.form['qualification']:
         flash('Please enter all the fields', 'error')
      else:
         alumni_professional = alumni_professional_details(request.form['current_company'], request.form['current_position'],request.form['qualification'])
         
         db.session.add(alumni_professional)
         db.session.commit()
         flash('Record was successfully added')
         return render_template('home.html')

   return render_template('alumni_prof.html')
   
   
class feedback(db.Model):
   fid = db.Column('fid', db.Integer, primary_key = True)
   q1 = db.Column(db.String(100))
   q2 = db.Column(db.String(50))
   q3 = db.Column(db.String(200))
   q4 = db.Column(db.String(100))
   q5 = db.Column(db.String(50))
   q6 = db.Column(db.String(200)) 
   q7 = db.Column(db.String(100))
   q8 = db.Column(db.String(50))
   q9 = db.Column(db.String(200)) 
   q10 = db.Column(db.String(200))
   
   def __init__(self, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
	   self.q1 = q1
	   self.q2 = q2
	   self.q3 = q3
	   self.q4 = q4
	   self.q5 = q5
	   self.q6 = q6
	   self.q7 = q7
	   self.q8 = q8
	   self.q9 = q9
	   self.q10 = q10
	  

@app.route('/feedback1', methods = ['GET', 'POST'])
def feedback1():
   if request.method == 'POST':
      if not request.form['q1'] or not request.form['q2'] or not request.form['q3'] or not request.form['q4'] or not request.form['q5'] or not request.form['q6'] or not request.form['q7'] or not request.form['q8'] or not request.form['q9'] or not request.form['q10']:
         flash('Please enter all the fields', 'error')
      else:
         feedb = feedback(request.form['q1'], request.form['q2'], request.form['q3'],request.form['q4'], request.form['q5'], request.form['q6'], request.form['q7'], request.form['q8'], request.form['q9'], request.form['q10'])
         
         db.session.add(feedb)
         db.session.commit()
         flash('Record was successfully added')
         return render_template('home.html')
   return render_template('feedback1.html')


   
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
