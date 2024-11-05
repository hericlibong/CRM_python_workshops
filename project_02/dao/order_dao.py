# dao/order_dao.py
from .base_dao import BaseDAO
from models.order import Order

class OrderDAO(BaseDAO):
    def create_order(self, client_id, date_order):
        order = Order(client_id=client_id, date_order=date_order)
        self.session.add(order)
        self.commit()
        return order
    
def get_order(self, order_id):
    return self.session.query(Order).get(order_id)

def get_all_orders(self):
    return self.session.query(Order).all()

def update_order(self, order_id, **kwargs):
    order = self.get_order(order_id)
    if not order:
        return None
    for key, value in kwargs.items():
        setattr(order, key, value)
    self.commit()
    return order

def delete_order(self, order_id):
    order = self.get_order(order_id)
    if order:
        self.session.delete(order)
        self.commit()
        return True
    return False

