from africana import db

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True,nullable=False,unique=True)
    username=db.Column(db.String(20),nullable=False,unique=True)
    email=db.Column(db.String(20),nullable=False,unique=True)
    password=db.Column(db.String(20),nullable=False,unique=True)
    
    def __repr__(User) -> str: 
        return f"username = {User.username} ,email = {User.email};"