from application import db

class Colors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True, unique=False)
    time = db.Column(db.String(128), index=True, unique=False)
    color = db.Column(db.String(128), index=True, unique=False)
    valence = db.Column(db.Integer, index=True, unique=False)
    
    def __init__(self, uid, time, color, valence):
        self.uid = uid
        self.time = time
        self.color = color
        self.valence = valence

    def __repr__(self):
        return '<Colors %r>' % self.uid