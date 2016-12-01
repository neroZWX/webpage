from flask import Flask, render_template, redirect, url_for, abort, jsonify, g
from flask.ext.bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Length, DataRequired
from database import init_db, db_session
from models import User
import pymysql

class DBConnect:
    def db_connect(DATABASE_URL):
	conn = pymysql.connect(host='localhost',user='root',password='6838699',
				db='test',charset='charset')
	cursor = conn.cursor()
	
		

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('remember me', default=False)
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY']='123'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])  
def login():
    form = LoginForm()
    error = None
    username = form['username']
    if form.validate_on_submit():
	if form['username'] != 'admin' or form['password'] != '123':
		error = 'sorry'
	else:
		return redirect(url_for('sky'))
    return render_template('index.html', form=form, error = error, 			    name=username)  
 
@app.route('/sky')  
def User(): 
    return render_template('user.html')

@app.route('/register')
def T():
    try:
	sql = "insert into userinfo(username,serect) values ('%s', %s)" % 				("username", "password")
	cursor.execute(sql)
   	conn.commit()
    except Exception as e:
		print(e)
    return render_template('register.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
        app.run(debug=True)
