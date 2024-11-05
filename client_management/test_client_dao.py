# # test_client_dao.py
# from dao.client_dao import ClientDAO
# from db_session import get_session

# class TestClientDAO:
#     def __init__(self):
#         self.session = get_session()
#         self.client_dao = ClientDAO(self.session)

#     def test_create_client(self):
#         print("\nTest de création de client...")
#         # Utilise un email unique pour chaque test
#         unique_email = "testuser_unique@example.com"
        
#         # Vérifie si le client existe déjà et le supprime si nécessaire
#         existing_client = self.client_dao.get_client_by_email(unique_email)
#         if existing_client:
#             self.client_dao.delete_client(existing_client.id)

#         client = self.client_dao.create_client(
#             nom="Test User", 
#             email=unique_email, 
#             telephone="0123456789", 
#             adresse="123 Test Street"
#         )
#         assert client is not None, "Échec de la création du client."
#         assert client.nom == "Test User", "Le nom du client ne correspond pas."
#         print("Création de client réussie :", client)

#         # Suppression du client de test pour rendre le test répétable
#         self.client_dao.delete_client(client.id)

#     def test_get_client(self, client_id):
#         print("\nTest de récupération de client...")
#         client = self.client_dao.get_client(client_id)
#         assert client is not None, f"Client avec l'ID {client_id} non trouvé."
#         print("Récupération de client réussie :", client)

#     def test_update_client(self, client_id):
#         print("\nTest de mise à jour de client...")
#         client = self.client_dao.update_client(client_id, nom="Updated User")
#         assert client is not None, "Échec de la mise à jour du client."
#         assert client.nom == "Updated User", "Le nom du client n'a pas été mis à jour."
#         print("Mise à jour de client réussie :", client)

#     def test_delete_client(self, client_id):
#         print("\nTest de suppression de client...")
#         success = self.client_dao.delete_client(client_id)
#         assert success, f"Échec de la suppression du client avec l'ID {client_id}."
#         print(f"Suppression de client avec l'ID {client_id} réussie.")

#     def close_session(self):
#         self.session.close()

# # Exécution des tests
# if __name__ == "__main__":
#     test_dao = TestClientDAO()
    
#     # Créer un client
#     test_dao.test_create_client()

#     # Obtenir un client (Remplace 1 par l'ID du client créé précédemment)
#     test_dao.test_get_client(1)

#     # Mettre à jour un client (Remplace 1 par l'ID du client créé précédemment)
#     test_dao.test_update_client(1)

#     # Supprimer un client (Remplace 1 par l'ID du client créé précédemment)
#     test_dao.test_delete_client(1)
    
#     # Fermer la session
#     test_dao.close_session()
