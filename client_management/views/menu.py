from views.client_view import (
    afficher_menu_client,
    ajouter_client,
    consulter_client,
    mettre_a_jour_client,
    supprimer_client
)
from views.contact_view import (
    afficher_menu_contacts,
    ajouter_contact,
    consulter_contact,
    mettre_a_jour_contact,
    supprimer_contact
)

def afficher_menu_principal():
    print("\n=== Menu Principal ===")
    print("1. Gestion des clients")
    print("2. Gestion des contacts")
    print("0. Quitter")

def menu_principal():
    while True:
        afficher_menu_principal()
        choix = input("Choisissez votre option : ")

        if choix == "1":
            menu_client()
        elif choix == "2":
            menu_contacts()
        elif choix == "0":
            print("Au revoir !")
            break   
        else:
            print("Option invalide. Veuillez réessayer.")

def menu_client():
    while True:
        afficher_menu_client()
        choix = input("Choisissez votre option : ")

        if choix == "1":
            ajouter_client()
        elif choix == "2":
            consulter_client()
        elif choix == "3":
            mettre_a_jour_client()
        elif choix == "4":
            supprimer_client()
        elif choix == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

def menu_contacts():
    while True:
        afficher_menu_contacts()
        choix = input("Choisissez votre option : ")

        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            consulter_contact()
        elif choix == "3":
            mettre_a_jour_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")