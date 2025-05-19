
from flask import Blueprint, redirect, render_template, url_for

auth = Blueprint('auth',__name__)

@auth.route('auth')
def home ():
    return redirect(url_for('/login'))

@auth.route('/login')
def login ():
    return render_template('auth.html')

