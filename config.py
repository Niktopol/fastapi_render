from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://user:qO8WGcxbV0pfsir1ttjHOx8vCsf3ySUt@dpg-ctha8elumphs73fm56ag-a.frankfurt-postgres.render.com/fastapi_database_7fn6'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()
