from app import app
from flask import redirect, render_template, url_for, flash
from app.forms import RegisterForm
from app.models import HrAdmin
from app import db


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/login')
def login():
    return render_template('login.html', title='Login')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = HrAdmin(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('{} successfully register.'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

