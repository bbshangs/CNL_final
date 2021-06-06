from app import db

class UserRegister(db.Model):
    __tablename__ = 'UserRegisters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def check_password(self, password):
        if self.password == password:
            return True
        return False

    def __repr__(self):
        return 'username:%s' % self.username
