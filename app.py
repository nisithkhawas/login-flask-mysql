from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='nisith'
)
cursor = db.cursor()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
        user = cursor.fetchone()

        if user:
            return f'Welcome, {username}!'
        else:
            return 'Invalid login credentials. Please try again.'

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
