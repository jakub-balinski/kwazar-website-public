from kwazar_website import db
from kwazar_website.models import User
from flask_bcrypt import Bcrypt

db.drop_all()
db.create_all()
bcrypt = Bcrypt()
user = User(login='your_login', password=bcrypt.generate_password_hash('your_pwd').decode('utf-8'))
db.session.add(user)
db.session.commit()
