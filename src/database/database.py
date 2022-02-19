from ..core.settings import settings

from databases import Database
from sqlalchemy import create_engine, MetaData


database = Database(settings.DATABASE_URL)
engine = create_engine(settings.DATABASE_URL)
metadata = MetaData()


