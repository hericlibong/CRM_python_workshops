# # models/client.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base



class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telephone = Column(String(15), nullable=True)
    adresse = Column(String(255), nullable=True)

    # Relation avec le modèle Contact
    contacts = relationship("Contact", back_populates="client")

    # def __repr__(self):
    #     return f"<Client(id={self.id}, nom={self.nom}, email={self.email})>"

    def __str__(self):
        return f"ID: {self.id}, Nom: {self.nom}, Email: {self.email}, Téléphone: {self.telephone}, Adresse: {self.adresse}"

