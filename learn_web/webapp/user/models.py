from flask_login import UserMixin
from webapp.db import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    """
    Database Model for Users
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50), unique=True)

    def set_password(self, password):
        """
        Sets password for each user and generates password hash via werkzeug. \n
        Hash is saved to `password` class attribute.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks provided password with hash in database. \n
        Returns True or False
        """
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == "admin"

    def __repr__(self):
        return f"<User name: {self.username}, id: {self.id}>"
