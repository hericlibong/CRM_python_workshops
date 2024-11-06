from dao.product_dao import ProductDAO

class ProductController:
    def __init__(self):
        self.product_dao = ProductDAO()

    def add_product(self, nom, prix, description=None, stock=0):
        # Ajouter un produit en utilisant le DAO
        return self.product_dao.create_product(nom, prix, description, stock)
    
    def get_product(self, id_product):
        # Récupérer un produit en utilisant le DAO
        return self.product_dao.get_product(id_product)
    
    def list_products(self):
        # Lister les produits en utilisant le DAO
        return self.product_dao.get_all_products()
    
    def update_product(self, id_product, **kwargs):
        # Mettre à jour un produit en utilisant le DAO
        return self.product_dao.update_product(id_product, **kwargs)
    
    def delete_product(self, id_product):
        # Supprimer un produit en utilisant le DAO
        return self.product_dao.delete_product(id_product)
    
    def check_stock(self, id_product, quantity):
        # Vérifier si le stock d'un produit est suffisant pour une quantité donnée
        product = self.product_dao.get_product(id_product)
        if product and product.stock >= quantity:
            return True
        return False