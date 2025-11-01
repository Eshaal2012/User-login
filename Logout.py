from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/logout')
def logout():
    name=''
    id=''
    msg='Logged out succesfully'
    return render_template('login.html',msg=msg,name=name,id=id)
