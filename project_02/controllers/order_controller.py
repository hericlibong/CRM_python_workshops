from dao.order_dao import OrderDAO
from dao.product_dao import ProductDAO
from dao.client_dao import ClientDAO
from dao.order_item_dao import OrderItemDAO
from datetime import date

class OrderController:
    def __init__(self):
        self.order_dao = OrderDAO()
        self.product_dao = ProductDAO()
        self.client_dao = ClientDAO()
        self.order_item_dao = OrderItemDAO()

    
    def create_order(self, client_id, items):
        """
        Créer une commande pour un client donné avec des produits.
        `items` est une liste de dictionnaires avec `product_id` et `quantity`.
        """
        client = self.client_dao.get_client(client_id)
        if not client:
            raise ValueError("Client introuvable")

        # Vérifier le stock pour chaque produit
        for item in items:
            product = self.product_dao.get_product(item["product_id"])
            if not product or product.stock < item["quantity"]:
                raise ValueError(f"Stock insuffisant pour le produit {product.nom}")

        # Créer la commande
        order = self.order_dao.create_order(client_id, date.today())

        # Créer chaque OrderItem et réduire le stock du produit
        for item in items:
            # Créer l'item de commande
            self.order_item_dao.create_order_item(order.id, item["product_id"], item["quantity"])
            
            # Réduire le stock du produit et le synchroniser avec la base de données
            new_stock = product.stock - item["quantity"]
            updated_product = self.product_dao.update_product(item["product_id"], stock=new_stock)

            # Utiliser flush pour forcer la synchronisation, et refresh pour actualiser l’objet
            self.product_dao.session.flush()
            self.product_dao.session.refresh(updated_product)

        return order

   
    
    def get_order(self, id_order):
        # Récupérer une commande par son id
        return self.order_dao.get_order(id_order)
    
    def list_orders(self):
        # Lister toutes les commandes
        return self.order_dao.get_all_orders()
    
    def delete_order(self, id_order):
        # Supprimer une commande et ses items associés
        order_items = self.order_item_dao.get_all_order_items()
        for item in order_items:
            if item.order_id == id_order:
                self.order_item_dao.delete_order_item(item.id)    
        return self.order_dao.delete_order(id_order)