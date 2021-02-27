from ..extensions import db
import datetime

class OutreachType(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    logo_url = db.Column(db.String(255))
    location = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now,  nullable=False)

    users = db.relationship('User', backref='user')
    outreach_type_id = db.Column(db.Integer(), db.ForeignKey('outreach_types.id'))
    outreach_type = db.relationship('OutreachType', backref='outreach_types')


    def __unicode__(self):
        return '%s' % self.id

    def __repr__(self):
        return "%s" % (self.name)


    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'name'],
        'ordering': ['-created_at']
    }



