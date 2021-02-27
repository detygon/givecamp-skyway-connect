from ..extensions import db
import datetime

ads_photographs = db.Table('ads_photographs',
    db.Column('client_id', db.Integer, db.ForeignKey('clients.id')),
    db.Column('ad_id', db.Integer, db.ForeignKey('advertisements.id'))
)

class Advertisement(db.Model):
    __tablename__ = 'advertisements';

    id = db.Column(db.Integer(), primary_key=True)
    scraped_at = db.Column(db.DateTime, default=datetime.datetime.now,  nullable=False)

    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'))
    client = db.relationship('Client', backref=db.backref('client', lazy='dynamic'))
    # ads_photographs = db.relationship('AdPhotograph', backref=db.backref('ad_photographs', lazy='dynamic'))

    def __unicode__(self):
        return '%s' % self.id

    def __repr__(self):
        return "%s" % (self.id)


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



