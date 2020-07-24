from weather import db

class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer,primary_key = True)
    city = db.Column(db.String(50))

    def __repr__(self):
        return f'City{self.city}'

#class Country(db.Model):
#   __table__ = 'country'
#  id = db.Column(db.Integer, primary_key = True)
# city = db.Column(db.String(50)) 
