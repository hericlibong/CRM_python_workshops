# create_tables.py
from sqlalchemy import create_engine
from models.base import Base
from models.client import Client  # Assure-toi que ce chemin est correct
from models.contact import Contact  # Assure-toi que ce chemin est correct
from config import DATABASE_URL

# Créer le moteur de base de données
engine = create_engine(DATABASE_URL)

# Créer toutes les tables définies dans les modèles
Base.metadata.create_all(engine)

print("Tables créées avec succès.")
