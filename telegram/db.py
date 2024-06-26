from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database setup
DATABASE_URL = 'mysql+pymysql://root:@localhost/db_tele'  # Ganti dengan URL database Anda

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Model untuk tb_inbox
class Inbox(Base):
    __tablename__ = 'tb_inbox'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Model untuk tb_outbox
class Outbox(Base):
    __tablename__ = 'tb_outbox'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Model untuk tb_cerita_rakyat
class CeritaRakyat(Base):
    __tablename__ = 'tb_cerita_rakyat'
    id = Column(Integer, primary_key=True, autoincrement=True)
    judul = Column(String(255), nullable=False)
    isi = Column(Text, nullable=False)

# Model untuk tb_querylog
class QueryLog(Base):
    __tablename__ = 'tb_querylog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(100), nullable=False)
    query_type = Column(String(50), nullable=False)  # Ubah bagian ini
    query = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)