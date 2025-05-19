'''from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    '''

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7152",
    database="gestion_de_notes"
)
cursor = db.cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pwd))
        result = cursor.fetchone()
        if result:
            session['user'] = user
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user, pwd))
        db.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        student = request.form['student']
        subject = request.form['subject']
        grade = request.form['grade']
        cursor.execute("INSERT INTO notes (student, subject, grade) VALUES (%s, %s, %s)", (student, subject, grade))
        db.commit()
        return redirect(url_for('view_notes'))
    return render_template('add_note.html')

@app.route('/view_notes')
def view_notes():
    if 'user' not in session:
        return redirect(url_for('login'))
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    return render_template('view_notes.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
