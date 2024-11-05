# dao/dao_client.py
from .base_dao import BaseDAO
from models.client import Client

class ClientDAO(BaseDAO):
    def create_client(self, nom, email, telephone=None, adresse=None):
        client = Client(nom=nom, email=email, telephone=telephone, adresse=adresse)
        self.session.add(client)
        self.commit()
        return client
    
    def get_client(self, client_id):
        return self.session.query(Client).get(client_id)
    
    def get_all_clients(self):
        return self.session.query(Client).all()
    
    def update_client(self, client_id, **kwargs):
        client = self.get_client(client_id)
        if not client:
            return None
        for key, value in kwargs.items():
            setattr(client, key, value)
        self.commit()
        return client
    
    def delete_client(self, client_id):
        client = self.get_client(client_id)
        if client:
            self.session.delete(client)
            self.commit()
            return True
        return False