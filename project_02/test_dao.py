# from datetime import date
# from dao.client_dao import ClientDAO
# from dao.order_dao import OrderDAO
# from dao.order_item_dao import OrderItemDAO
# from dao.product_dao import ProductDAO

# # Instancier les DAO
# client_dao = ClientDAO()
# order_dao = OrderDAO()
# order_item_dao = OrderItemDAO()
# product_dao = ProductDAO()

# # 1. Tester ClientDAO

# print("== TEST ClientDAO ==")
# # Créer un client
# client = client_dao.create_client(
#     nom="Paul O.",
#     email="paulO@example.com",
#     telephone="25458732",
#     adresse="123 rue du phare, 75001 Paris"
# )
# print("Client créé:", client)

# # Lire un client
# client_retrieved = client_dao.get_client(client.id)
# print("Client lu:", client_retrieved)

# # Modifier un client
# client_updated = client_dao.update_client(client.id, nom="Paul O. Updated")
# print("Client modifié:", client_updated)

# # Supprimer un client
# client_deleted = client_dao.delete_client(client.id)
# print("Client supprimé:", client_deleted)

# # 2. Tester ProductDAO
# print("\n== TEST ProductDAO ==")
# # Créer des produits
# product1 = product_dao.create_product(nom="Tabouret en fer", prix=50.0, stock=15)
# product2 = product_dao.create_product(nom="Table en bois", prix=150.0, stock=5)
# print("Produits créés:", product1, product2)

# # Lire un produit
# product_retrieved = product_dao.get_product(product1.id)
# print("Produit lu:", product_retrieved)

# # Modifier un produit
# product_updated = product_dao.update_product(product1.id, prix=55.0)
# print("Produit modifié:", product_updated)

# # Supprimer un produit
# product_deleted = product_dao.delete_product(product2.id)
# print("Produit supprimé:", product_deleted)

# # 3. Tester OrderDAO et OrderItemDAO
# print("\n=== Test OrderDAO et OrderItemDAO ===")
# # Créer une commande pour le client
# order = order_dao.create_order(client_retrieved.id, date.today())
# print("Commande ajoutée :", order)