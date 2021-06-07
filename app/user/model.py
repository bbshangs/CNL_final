from app import db

class UserRegister(db.Model):
    __tablename__ = 'UserRegisters'
    __bind_key__ = 'user_db'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    favorite = db.Column(db.String(27*10))

    def check_password(self, password):
        if self.password == password:
            return True
        return False
    
    def get_id(self):
        return self.id

    def add_favorite(self, place_id):
        self.favorite += place_id
        db.session.commit()

    def get_favorite(self):
        return self.favorite

    def __repr__(self):
        return 'username:%s' % self.username
 
