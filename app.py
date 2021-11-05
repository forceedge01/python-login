from flask import Flask, render_template, redirect, url_for, request, session

app = Flask (__name__)
app.secret_key = 'this-is-a-secret'

@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/auth', methods = ['POST'])
def auth():
	if 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']

		if username == 'Abdul' and password == 'welcome123':
			session['Login'] = True
			return redirect(url_for('dashboard'))
		else:
			return 'Login unsuccessful'


@app.route('/dashboard')
def dashboard():
	if session['Login'] == True:
		return render_template('dashboard.html')
	else:
		return redirect(url_for('login'))
	
@app.route('/logout', methods = ['GET'])
def logout():
	session.pop('Login', None)
	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)