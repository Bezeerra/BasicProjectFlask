from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# criacao dentro da tabela


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement =True, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(350), nullable=False)
    
    def __init__(self, name , email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password) #criptografa a senha 
   
    def verify_password(self, pwd): 
        return check_password_hash(self.password, pwd) #vai checar se a senha esta correta
   
    def __repr__(self): 
        return '<User %r>' %self.name
