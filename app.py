from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_fresh,login_manager,login_remembered,login_required,login_url,login_user,logout_user,current_user,LoginManager
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,ValidationError
from flask_bcrypt import Bcrypt

app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='this is a secret key'
db=SQLAlchemy(app) # create an instance of SQLAlchemy and pass the app in it
bcrypt=Bcrypt(app)




login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))



class user(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(20),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False)    
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self): # what it shows during print
         return (f"{self.id} - {self.user_name}")

class sign_up_form(FlaskForm):
       user_name=StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Username"})
       password=PasswordField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"password"})
       submit=SubmitField("sign-up")
       def existing_user_name_error(self,username):
           status=user.query.filter(username=username.data).first()
           status = user.query.filter_by(user_name=username.data).first()
           if status:
              raise ValidationError("username already exists. Try something new")
           
       
class login_form(FlaskForm):
       user_name=StringField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"Username"})
       password=PasswordField(validators=[InputRequired(),Length(min=4,max=20)],render_kw={"placeholder":"password"})
       submit=SubmitField("login")
       
              
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login',methods=['GET','POST'])
def login():
    form = login_form()
    if form.validate_on_submit():
        User = user.query.filter_by(user_name=form.user_name.data).first()
        if User and bcrypt.check_password_hash(User.password, form.password.data):
            login_user(User)
            return redirect('/dashboard')
    return render_template('login.html', form=form)


@app.route('/sign_up',methods=['GET','POST'])
def sign_up():
    form=sign_up_form()
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data)
        new_user=user(user_name=form.user_name.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('sign_up.html',form=form)


@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/log_out',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect('/login')


if __name__=="__main__":
    app.run(debug=True)
