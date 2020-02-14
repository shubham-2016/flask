from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect,request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1e83888769c402d5202c15a393672e26'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskblog.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(120), unique=True, nullable=False, default='default.jpg')
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self):
        #return "email %s" % 
        return "User('{username}','{email}','{image_file}')".format(username = self.username, email = self.email, image_file = self.image_file) 
        #return f"User('{self.username}','{self.email}','{self.image_file}')"    
        #return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)     
    def __repr__(self):
        #return f"Post('{self.title}','{self.date_posted}','{self.content}')"
        return "Post('{title}','{date_posted}','{content}')".format(title = self.title, date_posted = self.date_posted, content = self.content) 

posts = [
    {
        'auther' : 'Shubham Yelne',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2020'
    },
    {
        'auther' : 'Rahul Shingate',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'May 20, 2020'
    }
]

@app.route("/")  # decorator of our website
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/sample")
def sample():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():   
        flash(format('Account created for '+ request.form.get('username')),'success') 
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():   
        if form.email.data == 'shubham.yelne@neosofttech.com' and form.password.data == 'password':
            flash(format('Account Login Successfully.'),'success') 
            return redirect(url_for('home'))
        else:
            flash(format('Please check username and password.'),'danger') 

    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)