from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e432b933366c0743c1130c8784bb1d71'
osts = [
	{
		'author': 'Diva D',
		'title': 'Blog 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]
#like homePage
#two routes are being held for the same view fn
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=osts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)