# dao/client_dao.py
from sqlalchemy.orm import Session
from models.client import Client

class ClientDAO:
    def __init__(self, session: Session):
        self.session = session

    def create_client(self, nom, email, telephone=None, adresse=None):
        try:
            new_client = Client(nom=nom, email=email, telephone=telephone, adresse=adresse)
            self.session.add(new_client)
            self.session.commit()
            print("Client créé avec succès.")
            return new_client
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la création du client : {e}")
            return None

    def get_client(self, client_id):
        try:
            client = self.session.query(Client).filter_by(id=client_id).first()
            if client:
                return client
            else:
                print("Client non trouvé.")
                return None
        except Exception as e:
            print(f"Erreur lors de la récupération du client : {e}")
            return None

    def update_client(self, client_id, **kwargs):
        try:
            client = self.get_client(client_id)
            if not client:
                return None
            for key, value in kwargs.items():
                setattr(client, key, value)
            self.session.commit()
            print("Client mis à jour avec succès.")
            return client
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la mise à jour du client : {e}")
            return None

    def delete_client(self, client_id):
        try:
            client = self.get_client(client_id)
            if not client:
                return False
            self.session.delete(client)
            self.session.commit()
            print("Client supprimé avec succès.")
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la suppression du client : {e}")
            return False
