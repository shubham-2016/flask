from flask import Flask, render_template, url_for, flash, redirect,request
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '1e83888769c402d5202c15a393672e26'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)