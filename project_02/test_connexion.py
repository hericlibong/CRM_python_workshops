# test connexion.py
from sqlalchemy import create_engine
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)


try:
    with engine.connect() as connection:
        print("Connexion réussie à la base de données")
except Exception as e:
    print(f"Erreur de connexion à la base de données: {e}")