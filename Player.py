from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.engine import interfaces
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import cfg

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"
    id = Column('id', Integer, primary_key=True)
    player_id = Column('player_id', Integer, unique=True)
    player_name = Column('player_name', Text)

db = create_engine(f'mariadb+mariadbconnector://{cfg.DBUSER}:{cfg.DBPASSWORD}@127.0.0.1/{cfg.DATABASE}')
Base.metadata.create_all(bind=db)

Session = sessionmaker(bind=db)