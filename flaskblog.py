from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
	app.run(debug=True)