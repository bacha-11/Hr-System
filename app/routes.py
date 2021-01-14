from app import app, db
from flask import redirect, render_template, url_for, flash
from app.forms import RegisterForm, LoginForm, EmployeeForm
from app.models import HrAdmin, Employee
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/')
@login_required
def index():
    employee_data = Employee.query.all()
    return render_template('index.html', title='Home', employee_data=employee_data)


@app.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(
            employee_name=form.employee_name.data, 
            email=form.email.data, 
            address=form.address.data,
            age=form.age.data,
            phone=form.phone.data,
            gender=form.gender.data,
            job_title=form.job_title.data,
            salary=form.salary.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_employee.html', title='Add Employee', form=form)





@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('successfully logout!')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = HrAdmin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('{} successfully login!'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = HrAdmin(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('{} successfully register.'.format(form.username.data))
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

