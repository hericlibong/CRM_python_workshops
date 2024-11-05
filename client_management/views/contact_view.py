from controllers.contact_controller import ContactController

contact_controller = ContactController()

def afficher_menu_contacts():
    print("\n=== Menu Contacts ===")
    print("1. Ajouter un contact")
    print("2. Consulter un contact")
    print("3. Mettre à jour un contact")
    print("4. Supprimer un contact")
    print("0. Retour au menu principal")


def ajouter_contact():
    print("\n=== Ajouter un contact ===")
    client_id = int(input("ID du client associé : "))
    nom = input("Nom du contact : ")
    date_contact = input("Date du contact (format YYYY-MM-DD) : ")
    notes = input("Notes : ")

    contact = contact_controller.add_contact(client_id, nom, date_contact, notes)
    if contact:
        print("Contact ajouté avec succès :", contact)
    else:
        print("Erreur lors de l'ajout du contact.")

def consulter_contact():
    print("\n=== Consulter un contact ===")
    contact_id = int(input("ID du contact à consulter : "))
    contact = contact_controller.get_contact(contact_id)
    if contact:
        print("Détails du contact :", contact)
    else:
        print("Contact non trouvé.")

def mettre_a_jour_contact():
    print("\n=== Mettre à jour un contact ===")
    contact_id = int(input("ID du contact à mettre à jour : "))
    nom = input("Nouveau nom du contact (laisser vide pour ne pas modifier) : ")
    date_contact = input("Nouvelle date du contact (laisser vide pour ne pas modifier) : ")
    notes = input("Nouvelles notes (laisser vide pour ne pas modifier) : ")

    kwargs = {}
    if nom:
        kwargs["nom"] = nom
    if date_contact:
        kwargs["date_contact"] = date_contact
    if notes:
        kwargs["notes"] = notes
    
    contact = contact_controller.update_contact(contact_id, **kwargs)
    if contact:
        print("Contact mis à jour avec succès :", contact)
    else:
        print("Erreur lors de la mise à jour du contact.")

def supprimer_contact():
    contact_id = int(input("ID du contact à supprimer : "))
    success = contact_controller.delete_contact(contact_id)
    if success:
        print("Contact supprimé avec succès.")
    else:
        print("Erreur lors de la suppression du contact.")