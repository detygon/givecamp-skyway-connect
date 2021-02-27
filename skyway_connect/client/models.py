from enum import unique
from ..extensions import db
import datetime

class Race(db.Model):
    __tablename__ = 'races';

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class ClientStatus(db.Model):
    __tablename__ = 'client_statuses';

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class Gender(db.Model):
    __tablename__ = 'genders';

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))

class Client(db.Model):
    __tablename__ = 'clients';

    id = db.Column(db.Integer(), primary_key=True)
    last_name = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    email = db.Column(db.String(255))
    personal_website = db.Column(db.String(255))
    ad_age = db.Column(db.Integer())
    suspected_age = db.Column(db.Integer())

    client_status_id = db.Column(db.Integer(), db.ForeignKey('client_statuses.id'))
    client_status = db.relationship('ClientStatus', backref=db.backref('client_status', lazy='dynamic'))
    gender_id = db.Column(db.Integer(), db.ForeignKey('genders.id'))
    gender = db.relationship('Gender', backref=db.backref('gender', lazy='dynamic'))
    race_id = db.Column(db.Integer(), db.ForeignKey('races.id'))
    race = db.relationship('Race', backref=db.backref('race', lazy='dynamic'))


    def __unicode__(self):
        return '%s' % self.id

    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
    }

