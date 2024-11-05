# controllers/client_controller.py
from dao.client_dao import ClientDAO
from db_session import get_session

class ClientController:
    def __init__(self):
        self.session = get_session()
        self.client_dao = ClientDAO(self.session)

    def add_client(self, nom, email, telephone=None, adresse=None):
        client = self.client_dao.create_client(nom=nom, email=email, telephone=telephone, adresse=adresse)
        return client

    def get_client(self, client_id):
        client = self.client_dao.get_client(client_id)
        return client

    def update_client(self, client_id, **kwargs):
        client = self.client_dao.update_client(client_id, **kwargs)
        return client

    def delete_client(self, client_id):
        success = self.client_dao.delete_client(client_id)
        return success

    def close_session(self):
        self.session.close()
