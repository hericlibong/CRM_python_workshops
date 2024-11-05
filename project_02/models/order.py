from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    date_order = Column(Date, nullable=False)

    # Relation vers Client
    client = relationship("Client", back_populates="orders")

    # Relation vers OrderItems
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, date_order={self.date_order})>"