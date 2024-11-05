from sqlalchemy.orm import Session
from models.contact import Contact


class ContactDAO:
    def __init__(self, session: Session):
        self.session = session

    def create_contact(self, client_id, nom, date_contact, notes=None):
        try:
            new_contact = Contact(client_id=client_id, nom=nom, date_contact=date_contact, notes=notes)
            self.session.add(new_contact)
            self.session.commit()
            print("Contact créé avec succès")
            return new_contact
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la création du contact:{e}")
            return None
        
    def get_contact(self, contact_id):
        try:
            contact = self.session.query(Contact).filter_by(id=contact_id).first()
            if contact:
                return contact
            else:
                print("Contact non trouvé")
                return None
        except Exception as e:
            print(f"Erreur lors de la recherche du contact:{e}")
            return None
        
    def update_contact(self, contact_id, **kwargs):
        try:
            contact = self.get_contact(contact_id)
            if not contact:
                return None
            for key, value in kwargs.items():
                setattr(contact, key, value)
            self.session.commit()
            print("Contact mis à jour avec succès")
            return contact
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la mise à jour du contact:{e}")
            return None
        
    def delete_contact(self, contact_id):
        try:
            contact = self.get_contact(contact_id)
            if not contact:
                return False
            self.session.delete(contact)
            self.session.commit()
            print("Contact supprimé avec succès")
            return True
        except Exception as e:
            self.session.rollback()
            print(f"Erreur lors de la suppression du contact:{e}")
            return False