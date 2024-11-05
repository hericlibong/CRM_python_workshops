# create_tables.py
from sqlalchemy import create_engine
from models.base import Base
from models.client import Client 
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from config import DATABASE_URL

# Créer le moteur de base de données
engine = create_engine(DATABASE_URL)

# Créer toutes les tables définies dans les modèles
Base.metadata.create_all(engine)

print("Tables créées avec succès.")
