from app.models import HrAdmin
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
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
    pass



