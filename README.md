# alumnUS
*alumnUS is an Alumni Management System using python Flask framework*
____

**Introduction:**

An evolutionary alumni management system is a software that helps schools and universities to effectively connect with their alumni i.e. their ex-students. It is a system that helps all the passed out students to be socially connected with each other and are kept upto date about various events going on.The purpose of our system is to improve and add efficient features for betterment of alumni management tasks carried out manually.


**Features**

This application is designed for two roles:
1. Alumni Co-ordinator: Admin like entity for management of events on the institution level
2. Alumni : The actual X-student  

Alumni Co-ordinator has 3 main features:

1.	Add Alumni: The alumni coordinator can add the personal details students with a registration form
2.	Add  Events: The alumni coordinator adds events(like alumni meetups) which helps all the students to get notified.
3.	Send Request: Here we are using a special feature of bulk E-mail which means that in no time many emails can be sent to the students.


Alumni  has 2 main features:

1.	Add professional details: The alumni can add the professional details with a registration form 
2.	Give feedback: The alumni can give feedback for any event.

**Steps to be followed for executing the system in Windows 10**

Step 0. git clone https://github.com/Atashi27/MYalumnUS.git

Step 1. Open app.py to add the authorized email id and password of admin in line no 14, 15 and 73. 
Also allow less secure apps for the admin email address in gmail settings using https://myaccount.google.com/lesssecureapps
NOTE: If this step is not followed smtplib.SMTPAuthenticationError will be raised

Step 2. Open command prompt and execute following command

    1.	install python 
    
    2.	pip install virtualenv
    
    3.	cd MyalumnUS
    
    4.	virtualenv flask
    
    5.	flask\Scripts\python.exe
    
    6.	flask\Scripts\pip install flask
    
    7.  pip install Flask-Mail
    
    8.  pip install sqlalchemy

Step 3. cd flask\Scripts
        activate

Step 5. Now enter alumni folder using

    1. cd ..
    
    2. cd alumni
    
Step 6. Run 'python app.py' for opening alumni coordinator login
        OR
        Run 'python app1.py' for opening alumni login

Step 7. Open browser and enter 127.0.0.1:5000 to view the results

