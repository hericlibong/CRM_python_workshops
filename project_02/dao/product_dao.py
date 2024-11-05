# dao/product_dao.py
from .base_dao import BaseDAO
from models.product import Product

class ProductDAO(BaseDAO):
    def create_product(self, nom, prix, description=None, stock=0):
        product = Product(nom=nom, prix=prix, description=description, stock=stock)
        self.session.add(product)
        self.commit()
        return product
    
    def get_product(self, product_id):
        return self.session.query(Product).get(product_id)
    
    def get_all_products(self):
        return self.session.query(Product).all()
    
    def update_product(self, product_id, **kwargs):
        product = self.get_product(product_id)
        if not product:
            return None
        for key, value in kwargs.items():
            setattr(product, key, value)
        self.commit()
        return product
    
    def delete_product(self, product_id):
        product = self.get_product(product_id)
        if product:
            self.session.delete(product)
            self.commit()
            return True
        return False