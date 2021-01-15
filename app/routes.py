from app import app, db
from flask import redirect, render_template, url_for, flash, request
from app.forms import RegisterForm, LoginForm, EmployeeForm, EmptyForm
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



@app.route('/edit/<employee_name>', methods=['GET', 'POST'])
@login_required
def edit_employee(employee_name):
    form = EmployeeForm()
    if form.validate_on_submit():
        emp = Employee.query.filter_by(employee_name=employee_name).first()
        emp.employee_name = form.employee_name.data
        emp.email = form.email.data
        emp.address = form.address.data
        emp.age = form.age.data
        emp.phone = form.phone.data
        emp.gender = form.gender.data
        emp.job_title = form.job_title.data
        emp.salary = form.salary.data
        db.session.commit()
        flash(f'{ emp.employee_name } has been update ')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        emp = Employee.query.filter_by(employee_name=employee_name).first()
        form.employee_name.data = emp.employee_name
        form.email.data = emp.email 
        form.address.data = emp.address
        form.age.data = emp.age
        form.phone.data = emp.phone
        form.gender.data = emp.gender
        form.job_title.data = emp.job_title
        form.salary.data = emp.salary
    return render_template('add_employee.html', title='Edit Employee', form=form)



@app.route('/delete/<employee_name>', methods=['GET', 'POST'])
@login_required
def delete_employee(employee_name):
    form = EmptyForm()
    emp = Employee.query.filter_by(employee_name=employee_name).first()
    if form.validate_on_submit():
        db.session.delete(emp)
        db.session.commit()
        flash(f'{emp} has been delete.')
        return redirect(url_for('index'))
    return render_template('delete.html', title='Delete Employee', form=form, emp=emp)


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

