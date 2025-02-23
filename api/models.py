from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey, UniqueConstraint, TIMESTAMP, func
)

# Base class for declarative models
Base = declarative_base()

class Tari(Base):
    __tablename__ = 'tari'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume_tara = Column(String(100), unique=True, nullable=False)
    latitudine = Column(Float, nullable=False)
    longitudine = Column(Float, nullable=False)

    # Relationship with Orase
    orase = relationship("Orase", back_populates="tara", cascade="all, delete")


class Orase(Base):
    __tablename__ = 'orase'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    idtara = Column(Integer, ForeignKey('tari.id', ondelete='CASCADE'), nullable=False)  
    nume_oras = Column(String(100), nullable=False)
    latitudine = Column(Float, nullable=False)
    longitudine = Column(Float, nullable=False)

    __table_args__ = (UniqueConstraint('idtara', 'nume_oras', name='uq_id_tara_nume_oras'),)

    tara = relationship("Tari", back_populates="orase") 
    temperaturi = relationship("Temperaturi", back_populates="oras", cascade="all, delete")


class Temperaturi(Base):
    __tablename__ = 'temperaturi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valoare = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    idoras = Column(Integer, ForeignKey('orase.id', ondelete='CASCADE'), nullable=False)

    __table_args__ = (UniqueConstraint('idoras', 'timestamp', name='uq_idoras_timestamp'),)


    oras = relationship("Orase", back_populates="temperaturi")
