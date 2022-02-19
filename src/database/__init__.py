from .database import engine, metadata
from .tables import staff, order, food

metadata.create_all(bind=engine)



