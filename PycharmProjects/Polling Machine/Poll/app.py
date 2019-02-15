from otp import *
from flask import Flask, render_template, redirect,url_for, flash, request
from database import connect, update_vote,find_user,user_login,clear_otp,func1
from flask_cors import CORS
from config import *
from form import LoginForm
from flask_login import LoginManager,UserMixin,current_user,login_user,login_required, logout_user
from flask_sqlalchemy import SQLAlchemy
import hashlib
from multiprocessing import Process


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///poll_database.db'
app.config.from_object(Config)

dbs = SQLAlchemy(app)
login=LoginManager(app)
login.login_view='/'
cors=CORS(app)
conn=connect()
c=conn.cursor()

app.jinja_env.globals.update(update_vote=update_vote)

def main():
    global conn,c

class User(UserMixin,dbs.Model):
    id = dbs.Column(dbs.Integer, primary_key = True)
    Name = dbs.Column(dbs.String(100))
    contact = dbs.Column(dbs.String(14))
    voted = dbs.Column(dbs.Integer)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', defaults={'value': None},methods=['GET', 'POST'])
@app.route('/login/<value>', methods=['GET', 'POST'])
def index(value):

    if current_user.is_authenticated:
        if current_user.voted is 1:
            return redirect('/thank-you')
        else:

            return redirect(url_for('vote'))

    form=LoginForm()

    if (value):
        print(value)
        ad = form.aadharid.data
        st= 'SELECT contact FROM user WHERE id ='+value
        c.execute(st)
        nu=c.fetchone()
        conn.commit()
        print(Config_test)
        if(Config_test):
            otp_test(value,c,nu[0])
            p = Process(target=func1, args = (conn,c,value))
            p.start()
        else:
            otp_default(value,c,nu[0])
            p = Process(target=func1, args=(conn, c, value))
            p.start()
        return redirect("/")


    elif form.validate_on_submit():
        user = User.query.filter_by(id=form.aadharid.data).first()
        otp=find_user(form.aadharid.data)
        x = form.otp.data
        x = hashlib.md5(x.encode())
        x= str(x.hexdigest())
        print(x)
        if (otp == x):
            login_user(user)
            if (current_user.voted is 1):
                return redirect('/thank-you')
            else:

                return redirect(url_for('vote'))
        else:
            flash("Invalid Aadhar Id or OTP")
            return redirect(url_for('index'))

    return render_template('login2.html',form=form)

@app.route('/poll-station', defaults={'value': None})
@app.route('/poll-station/<value>')
@login_required
def vote(value):
    if (current_user.voted is 1):
        return redirect('/thank-you')
    if(value):
        if (current_user.voted is 1):
            return redirect('/thank-you')
        update_vote(conn,c, value, 'example')
        return redirect('/thank-you')
    clrid = current_user.id
    clear_otp(conn, c, 'user', clrid)
    return render_template("pollstation.html")

@app.route('/thank-you')
@login_required
def thanks():
    clrid = current_user.id
    clear_otp(conn, c, 'user', clrid)
    return render_template('thanks.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/why-us')
def why():
    return render_template('why.html')

@app.route('/policies')
@app.route('/help')
@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/vote', methods=['POST'])
@login_required
def poll():
    if (current_user.voted is 1):
        return redirect('/thank-you')
    data = request.data
    print(data)
    return request.data

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)