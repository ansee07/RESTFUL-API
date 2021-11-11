from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta
users = Table (
    'users', meta,
    Column('id',Integer,primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('Password', String(255)),
    Column('Date', int(255)),
    Column('Gender', String(255))
)