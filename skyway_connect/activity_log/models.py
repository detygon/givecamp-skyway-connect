from enum import unique
from ..extensions import db
import datetime


activity_results = db.Table('activity_results',
    db.Column('activity_id', db.Integer, db.ForeignKey('activity_logs.id')),
    db.Column('result_id', db.Integer, db.ForeignKey('contact_results.id'))
)

activity_resources = db.Table('activity_resources',
    db.Column('activity_id', db.Integer, db.ForeignKey('activity_logs.id')),
    db.Column('resource_id', db.Integer, db.ForeignKey('resources.id'))
)

class Resource(db.Model):
    __tablename__ = 'resources';

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class ContactResult(db.Model):
    __tablename__ = 'contact_results';

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class ContactType(db.Model):
    __tablename__ = 'contact_types';

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class ActivityLog(db.Model):
    __tablename__ = 'activity_logs';

    id = db.Column(db.Integer(), primary_key=True)
    log_type = db.Column(db.String(255),  nullable=False)
    phone_number_used = db.Column(db.String(50))
    email_used = db.Column(db.String(50))
    is_safe = db.Column(db.Boolean)
    live_locally = db.Column(db.Boolean)
    name_reported = db.Column(db.String(50))
    age_reported = db.Column(db.Integer())
    wants_followups = db.Column(db.Boolean)
    notes = db.Column(db.String(255))
    call_time = db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)
    call_duration = db.Column(db.Integer())

    contact_type_id = db.Column(db.Integer(), db.ForeignKey('contact_types.id'))
    contact_type = db.relationship('ContactType', backref='contact_type')
    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'))
    client = db.relationship('Client', backref='client')
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('User', backref='user')

    contact_results = db.relationship('ContactResult', secondary=activity_results, backref=db.backref('activity_logs', lazy='dynamic'))
    resources = db.relationship('Resource', secondary=activity_resources, backref=db.backref('activity_logs', lazy='dynamic'))


    def __unicode__(self):
        return '%s' % self.id

    def __repr__(self):
        return "%s" % (self.name_reported)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }



