from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Global variable to store user info
users = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Storing user info in the global variable
        users[username] = password
        return redirect('/login')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Checking if the user exists in the global variable
        if username in users and users[username] == password:
            # Set username in session to indicate user is logged in
            session['username'] = username
            print("User Info:")
            print("Username:", username)
            print("Password:", password)
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid username or password. Please try again.")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    if username:
        return render_template('dashboard.html', username=username)
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Clear the session to logout the user
    session.clear()
    # Redirect the user to the login page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

