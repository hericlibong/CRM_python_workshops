# models/client.py
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from .base import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telephone = Column(String(15), nullable=True)
    adresse = Column(String(255), nullable=True)

    # Relation avec les commandes
    orders = relationship("Order", back_populates="client", cascade="all, delete-orphan")

    
    def __repr__(self):
        return f"<Client(id={self.id}, nom={self.nom}, email={self.email})>"