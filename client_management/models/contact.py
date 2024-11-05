# models/contact.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base



class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    nom = Column(String(100), nullable=False)
    date_contact = Column(Date, nullable=False)
    notes = Column(String(255), nullable=True)

    # Relation avec le modèle Client
    client = relationship("Client", back_populates="contacts")

    def __repr__(self):
        return f"<Contact(id={self.id}, nom={self.nom}, date_contact={self.date_contact})>"
