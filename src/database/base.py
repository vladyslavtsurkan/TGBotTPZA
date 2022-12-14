from typing import TypeAlias
from sqlalchemy.ext.declarative import declarative_base

from config_loader import load_config_db, DatabaseConfig

sqlalchemy_url: TypeAlias = str

Base = declarative_base()


def get_sqlalchemy_url() -> sqlalchemy_url:
    """Get SQLAlchemy URL for work with database from config"""
    config_db: DatabaseConfig = load_config_db()
    return (
        f'postgresql+asyncpg://{config_db.user}:{config_db.password}@'
        f'{config_db.host}/{config_db.db_name}'
    )
