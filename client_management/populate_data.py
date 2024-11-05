from db_session import get_session
from dao.client_dao import ClientDAO
from dao.contact_dao import ContactDAO

def populate_data():
    session = get_session()

    client_dao = ClientDAO(session)
    contact_dao = ContactDAO(session)

    client1 = client_dao.create_client(nom="Alice Dupont", email="alice@example.com", telephone="0102030405", adresse="123 Rue de Paris")
    client2 = client_dao.create_client(nom="Bob Martin", email="bob@exemple.com", telephone="0605040302", adresse="456 Rue de Lyon")

    print("Clients crées :", client1, client2)

    # Ajouter des contacts pour client1
    if client1:
        contact_dao.create_contact(client_id=client1.id, nom="Premier Contact Alice", date_contact="2023-11-01", notes="Premier suivi.")
        contact_dao.create_contact(client_id=client1.id, nom="Second Contact Alice", date_contact="2023-11-02", notes="Suivi complémentaire.")
    
    # Ajouter des contacts pour client2
    if client2:
        contact_dao.create_contact(client_id=client2.id, nom="Premier Contact Bob", date_contact="2023-11-03", notes="Présentation de produit.")
    
    session.close()
    print("Données d'exemple insérées avec succès.")

# Exécuter le script
if __name__ == "__main__":
    populate_data()