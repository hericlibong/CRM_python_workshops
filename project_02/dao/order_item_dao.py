# dao/order_item_dao.py
from .base_dao import BaseDAO
from models.order_item import OrderItem

class OrderItemDAO(BaseDAO):
    def create_order_item(self, order_id, product_id, quantity):
        order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity)
        self.session.add(order_item)
        self.commit()
        return order_item
    
    def get_order_item(self, order_item_id):
        return self.session.query(OrderItem).get(order_item_id)
    
    def get_all_order_items(self):
        return self.session.query(OrderItem).all()
    
    def update_order_item(self, order_item_id, **kwargs):
        order_item = self.get_order_item(order_item_id)
        if not order_item:
            return None
        for key, value in kwargs.items():
            setattr(order_item, key, value)
        self.commit()
        return order_item
    
    def delete_order_item(self, order_item_id):
        order_item = self.get_order_item(order_item_id)
        if order_item:
            self.session.delete(order_item)
            self.commit()
            return True
        return False