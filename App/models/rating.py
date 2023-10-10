from App.database import db

class Rating(db.Model):
    ratingID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    
    def __init__(self, title, description, date):
        self.title = title
        self.description = description
        self.date = date
    
    def get_json(self):
        return{
            'ratingID': self.ratingID,
            'studentID': self.studentID,
            'userID': self.userID,
            'title': self.title,
            'description': self.description,
            'date': self.date
        }