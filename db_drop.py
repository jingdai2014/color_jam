from application import db
from application.models import Colors

db.drop_all()

print("DB dropped.")
