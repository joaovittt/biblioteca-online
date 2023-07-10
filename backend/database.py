import sqlalchemy as sql 
import sqlalchemy.ext.declarative as declarative 
import sqlalchemy.orm as orm 


db_endpoint = 'database-1.clllywvqw34m.us-east-2.rds.amazonaws.com'
db_port = 5432
db_name = 'postgres'
db_user = 'postgres'
db_password = 'biblio123'


DATABASE_URL = f'postgresql://{db_user}:{db_password}@{db_endpoint}:{db_port}/{db_name}'


engine = sql.create_engine(DATABASE_URL)

sessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative.declarative_base()