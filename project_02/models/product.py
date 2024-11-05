# modèle du produit
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prix = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    
    # Relation vers OrderItem
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Product(id={self.id}, nom={self.nom}, prix={self.prix})>"