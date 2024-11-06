from dao.client_dao import ClientDAO

class ClientController:
    def __init__(self):
        self.client_dao = ClientDAO()

    def add_client(self, nom, email, telephone=None, adresse=None):
        # Ajouter un client en utilisant le DAO
        return self.client_dao.create_client(nom, email, telephone, adresse)
    
    def get_client(self, id_client):
        # Récupérer un client en utilisant le DAO
        return self.client_dao.get_client(id_client)
    
    def list_clients(self):
        # Lister les clients en utilisant le DAO
        return self.client_dao.get_all_clients()
    
    def update_client(self, id_client, **kwargs):
        # Mettre à jour un client en utilisant le DAO
        return self.client_dao.update_client(id_client, **kwargs)
    
    def delete_client(self, id_client):
        # Supprimer un client en utilisant le DAO
        return self.client_dao.delete_client(id_client)
    
