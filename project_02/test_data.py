# Code pour ajouter des donnees de test dans la base de donnees
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models.client import Client
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from datetime import date

# Créer le moteur de base de données et congiurer la session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Etape 1: Ajouter un client
client = Client(nom="Alice B.", email="alice@example.com", telephone="0203060507", adresse="12 rue des fleurs, 75002 Paris")
session.add(client)
session.commit()
print("Client ajouté avec succès : ", client)

# Etape 2: Ajouter des produits
product1 = Product(nom="Chaise en bois", prix=45.99, description="Chaise en bois de chêne", stock=10)
product2 = Product(nom="Table en verre", prix=99.99, description="Table en verre trempé", stock=5)
session.add_all([product1, product2])
session.commit()
print("Produits ajoutés avec succès : ", product1, product2)


# Etape 3: Ajouter une commande pour le client
order = Order(client_id=client.id, date_order=date.today())
session.add(order)
session.commit()
print("Commande ajoutée avec succès : ", order)

# Etape 4: Ajouter des articles de commande
order_item1 = OrderItem(order_id=order.id, product_id=product1.id, quantity=2)
order_item2 = OrderItem(order_id=order.id, product_id=product2.id, quantity=1)
session.add_all([order_item1, order_item2])
session.commit()
print("Articles de commande ajoutés avec succès : ", order_item1, order_item2)

# vérificationdes relations
print("Client de la commande : ", order.client)
print("Produits de la commande : ")
for item in order.order_items:
    print(f"Produit : {item.product}, Quantité : {item.quantity}; Prix unitaire : {item.product.prix}")

# Fermer la session
session.close()