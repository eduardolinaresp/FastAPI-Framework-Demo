from sqlalchemy import Table,Column
from config.db import meta

user = Table("users", metadata, Column("id", Integer, primary_key=True))