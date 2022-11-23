from playhouse.db_url import connect
from peewee import Model
from peewee import IntegerField
from peewee import CharField
from peewee import DateField
from flask_login import UserMixin

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("接続NG")
    exit()
print("接続OK")

class User(UserMixin, Model):
    id = IntegerField(primary_key=True)
    membership_number = IntegerField()
    name = CharField()
    password = IntegerField()
    birthday = DateField()
    gender = CharField()
    week = CharField()
    time_zone = CharField()
    class Meta:
        database = db
        table_name = "User"

db.create_tables([User])   

