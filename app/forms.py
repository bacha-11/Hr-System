from app.models import HrAdmin
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField, RadioField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = HrAdmin.query.filter_by(username=username.data).first()
        if user is not None:
            ValidationError('Try different username.')

    def validate_email(self, email):
        user = HrAdmin.query.filter_by(email=email.data).first()
        if user is not None:
            ValidationError('Try different email.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('LogIn')


class EmployeeForm(FlaskForm):
    employee_name = StringField('Employee Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    phone = IntegerField('Phone', validators=[DataRequired()])
    gender = RadioField('Gender', choices = [('Male','Male'),('Female','Female')])
    job_title = SelectField('Job Title', choices = [('s', 'Select Field'),('Clerk', 'Clerk'),('SalesMan', 'SalesMan'), ('Manager', 'Manager')])
    salary = IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Add Employee')


class EmptyForm(FlaskForm):
    submit = SubmitField()




