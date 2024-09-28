from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

role = Table(
    'role', metadata,
    Column('id', Integer, primary_key=True),  # Правильное определение столбца id
    Column('name', String, nullable=False),
    Column('permissions', JSON),
    extend_existing=True
)

user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),  # Правильное определение столбца id
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('hashed_password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),  # Правильное использование datetime
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('is_active',Boolean, default=True, nullable=False),
    Column('is_superuser',Boolean, default=False, nullable=False),
    Column('is_verified',Boolean, default=False, nullable=False),
    extend_existing=True  # Добавьте эту опцию
)


