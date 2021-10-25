from sqlalchemy import create_engine, Column, Integer, BigInteger, Text, Boolean, ForeignKey
from sqlalchemy.engine import interfaces
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import cfg

Base = declarative_base()

class Player(Base):
    __tablename__ = "player"
    player_id = Column('player_id', BigInteger, primary_key=True)
    player_name = Column('player_name', Text)
    current_health = Column('current_health', Integer)
    maximum_health = Column('maximum_health', Integer)
    current_experience = Column('current_experience', Integer)
    maximum_experience = Column('maximum_experience', Integer)
    base_damage = Column('base_damage', Integer)

    def __init__(self, user_id, user_name):
        self.player_id = user_id
        self.player_name = user_name
        self.current_health = 10
        self.maximum_health = 10
        self.current_experience = 0
        self.maximum_experience = 100
        self.base_damage = 5

class Mob(Base):
    __tablename__ = "mob"
    mob_id = Column('id', Integer, primary_key=True)
    mob_name = Column('player_name', Text)
    current_health = Column('current_health', Integer)
    maximum_health = Column('maximum_health', Integer)
    base_experience_value = Column('base_experience_value', Integer)
    base_damage = Column('base_damage', Integer)

    def __init__(self, mob_name):
        self.mob_name = mob_name
        self.current_health = 10
        self.maximum_health = 10
        self.base_experience_value = 5
        self.base_damage = 2

db = create_engine(f'mariadb+mariadbconnector://{cfg.DBUSER}:{cfg.DBPASSWORD}@127.0.0.1/{cfg.DATABASE}')
Base.metadata.create_all(bind=db)

Session = sessionmaker(bind=db)