from app import db
from flask_login import UserMixin
from app import login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class HrAdmin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(64))

    def __repr__(self):
        return 'HrAdmin {}'.format(self.username)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return HrAdmin.query.get(int(id))


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    address = db.Column(db.String(120))
    age = db.Column(db.Integer)
    phone = db.Column(db.Integer)
    gender = db.Column(db.String(120))
    job_title = db.Column(db.String(120))
    salary = db.Column(db.Integer)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Employee {}'.format(self.employee_name)





