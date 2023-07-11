import database as db

def create_database():
    print(db.SessionLocal)
    return db.Base.metadata.create_all(bind=db.engine)

create_database()