from ..extensions import db
from flask_security import UserMixin, RoleMixin
import datetime

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
)

class Role(db.Model, RoleMixin):
    __tablename__  = 'roles';

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __unicode__(self):
        return '%s' % self.name

class User(UserMixin, db.Model):
    __tablename__  = 'users';

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255),  nullable=False)
    password = db.Column(db.String(255),  nullable=False)
    active = db.Column(db.Boolean, default=True)
    job_title = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now,  nullable=False)


    organization_id = db.Column(db.Integer(), db.ForeignKey('organizations.id'))
    organization = db.relationship('Organization', backref='organization')
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    #email confirmation
    confirmed_at = db.Column(db.DateTime())
    #tracking
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer())

    def __unicode__(self):
        return '%s' % self.id

    def __repr__(self):
        return "%s %s (%s) <%s>" % (self.first_name, self.last_name, self.id, self.email)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'email'],
        'ordering': ['-created_at']
    }



