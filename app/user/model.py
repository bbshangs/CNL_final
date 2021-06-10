from app import db

class UserRegister(db.Model):
    __tablename__ = 'UserRegisters'
    __bind_key__ = 'user_db'
    count = 27
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    favorite = db.Column(db.String(count*100))

    def check_password(self, password):
        if self.password == password:
            return True
        return False
    
    def get_id(self):
        return self.id

    def is_favorite(self, place_id):
        id_list = self.favorite.split()
        for id in id_list:
            print(place_id == id)
        if place_id in id_list:
            return True
        return False

    def add_favorite(self, place_id):
        self.favorite += place_id
        self.favorite += " "
        db.session.commit()

    def remove_favorite(self, place_id):
        remove_str = place_id + " "
        self.favorite = self.favorite.replace(remove_str, "")
        db.session.commit()

    def get_favorite(self):
        return self.favorite

    def __repr__(self):
        return 'username:%s' % self.username
 
