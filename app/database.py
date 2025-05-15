from .models import Base, engine

# Initialize the database
def init_db():
    Base.metadata.create_all(bind=engine)
