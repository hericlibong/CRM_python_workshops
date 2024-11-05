from controllers.client_controller import ClientController

client_controller = ClientController()

def afficher_menu_client():
    print("\n=== Menu Client ===")
    print("1. Ajouter un client")
    print("2. consulter un client")
    print("3. Mettre à jour un client")
    print("4. Supprimer un client")
    print("0. Retour au menu principal")


def ajouter_client():
    print("\n=== Ajouter un client ===")
    nom = input("Nom du client : ")
    email = input("Email du client : ")
    telephone = input("Téléphone du client : ")
    adresse = input("Adresse du client : ")

    client = client_controller.add_client(nom, email, telephone, adresse)
    if client:
        print("Client ajouté avec succès :", client)
    else:
        print("Erreur lors de l'ajout du client.")


def consulter_client():
    print("\n=== Consulter un client ===")
    client_id = int(input("ID du client à consulter : "))
    client = client_controller.get_client(client_id)
    if client:
        print("Détails du client :", client)
    else:
        print("Client non trouvé.")

def mettre_a_jour_client():
    print("\n=== Mettre à jour un client ===")
    client_id = int(input("ID du client à mettre à jour : "))
    nom = input("Nouveau nom du client (laisser vide pour ne pas modifier) : ")
    email = input("Nouvel email du client (laisser vide pour ne pas modifier) : ")
    telephone = input("Nouveau téléphone du client (laisser vide pour ne pas modifier) : ")
    adresse = input("Nouvelle adresse du client (laisser vide pour ne pas modifier) : ")

    kwargs = {}
    if nom:
        kwargs["nom"] = nom
    if email:
        kwargs["email"] = email
    if telephone:
        kwargs["telephone"] = telephone
    if adresse:
        kwargs["adresse"] = adresse
    
    client = client_controller.update_client(client_id, **kwargs)
    if client:
        print("Client mis à jour avec succès :", client)
    else:
        print("Erreur lors de la mise à jour du client.")

def supprimer_client():
    print("\n=== Supprimer un client ===")
    client_id = int(input("ID du client à supprimer : "))
    success = client_controller.delete_client(client_id)
    if success:
        print("Client supprimé avec succès.")
    else:
        print("Erreur lors de la suppression du client.")

    