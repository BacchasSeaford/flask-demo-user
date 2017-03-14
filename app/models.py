from . import db
class UserProfile(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    username=db.Column(db.String(30), primary_key=True)
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(6))
    biography=db.Column(db.String(350))
    file=db.Column(db.String(46))
    date_created=db.Column(db.Date)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __init__(self,id,username,firstname,lastname,age,gender,biography,file,date_created):
        self.id=id
        self.username=username
        self.firstname=firstname
        self.lastname=lastname
        self.gender=gender
        self.age=age
        self.biography=biography
        self.file=file
        self.date_created=date_created
