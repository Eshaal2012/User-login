from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
mysql=MySQL(app)
@app.route('/')
@app.route('/login',methods=['GET','POST,'])
def login():
    msg=''
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username=request.form['username']
        password=request.form['password']
        mydb=mysql.connector.connect(
            host="remotemysql.com",
            user="Rz8hqn1dK4",
            password="nd0WKO3xeO",
            database="Rz8hqn1dK4"
        )
        mycursor=mydb.cursor()
        mycursor.execute('SELECT * FROM loginDetails WHERE Name =% AND Password =% ',(username,password))
        account=mycursor.fetchbone()
        if account:
            print('login successful')
            name=account[1]
            id=account[0]
            msg='Logged in succesfully' 
            print('login successful')
            return render_template('index.html,msg=msg,name=name,id=id')
        else:
            msg='incorrect Credentials.Kindly check'
            return render_template('login.html',msg=msg)
    else:
        return render_template('login.html')