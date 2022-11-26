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
    week1 = CharField()
    week2 = CharField()
    week3 = CharField()
    time_zone1 = CharField()
    time_zone2 = CharField()

    class Meta:
        database = db
        table_name = "User"


db.create_tables([User])


class Admin(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    password = IntegerField()
    email = CharField()

    class Meta:
        database = db
        table_name = "Admin"


db.create_tables([Admin])


class Program(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    content = CharField()
    strength = IntegerField()
    difficulty = IntegerField()
    minutes = IntegerField()
    capacity = IntegerField()
    images = CharField()

    class Meta:
        database = db
        table_name = "Program"


db.create_tables([Program])


class Schedule(UserMixin, Model):
    id = IntegerField(primary_key=True)
    # year = IntegerField()
    # month = IntegerField()
    week = CharField()
    time = CharField()
    program = CharField()
    ir = CharField()

    class Meta:
        database = db
        table_name = "Schedule"


db.create_tables([Schedule])


class Ir_register(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    program1 = CharField()
    fee1 = IntegerField()
    program2 = CharField()
    fee2 = IntegerField()
    program3 = CharField()
    fee3 = IntegerField()
    email = CharField()

    class Meta:
        database = db
        table_name = "Ir_register"


db.create_tables([Ir_register])


class Ir(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    password = IntegerField()
    email = CharField()

    class Meta:
        database = db
        table_name = "Ir"


db.create_tables([Ir])
