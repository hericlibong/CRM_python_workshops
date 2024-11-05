# from controllers.client_controller import ClientController
# from controllers.contact_controller import ContactController


# # Initialisation des controllers
# client_controller = ClientController()
# contact_controller = ContactController()

# # Test des operations client
# print("=== Test Client ===")
# client = client_controller.add_client("Alice Dupont", "alice2@example.com", "0102030405", "123 Rue de Paris")
# print("Client ajouté :", client)

# client = client_controller.get_client(client.id)
# print("Client récupéré :", client)

# client = client_controller.update_client(client.id, nom="Alice D.")
# print("Client mis à jour :", client)

# success = client_controller.delete_client(client.id)
# print("Client supprimé :", success)

# # Test des opérations Contact (si un client existe)
# print("\n=== Test Contact ===")
# client = client_controller.add_client("Bob Martin", "bob3@example.com", "0607080910", "456 Boulevard Saint-Germain")
# contact = contact_controller.add_contact(client.id, "Premier Contact", "2023-11-01", "Premier suivi.")
# print("Contact ajouté :", contact)

# contact = contact_controller.get_contact(contact.id)
# print("Contact récupéré :", contact)

# contact = contact_controller.update_contact(contact.id, notes="Suivi complémentaire.")
# print("Contact mis à jour :", contact)

# success = contact_controller.delete_contact(contact.id)
# print("Contact supprimé :", success)

# # Fermeture des sessions
# client_controller.close_session()
# contact_controller.close_session()
