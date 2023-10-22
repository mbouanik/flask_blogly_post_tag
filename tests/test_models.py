from unittest import TestCase
from init import create_app, db
from models import User

app = create_app()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly_test"
app.config["SQlALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.config["TESTING"] = True

db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()


class Blogly_test(TestCase):
    def setUp(self):
        self.user = User(first_name="John", last_name="Wick")


    def test_full_name(self):
        with app.app_context():
            self.assertEqual(self.user.full_name, "John Wick")
