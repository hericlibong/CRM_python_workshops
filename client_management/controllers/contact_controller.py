# controllers/contact_controller.py
from dao.contact_dao import ContactDAO
from db_session import get_session

class ContactController:
    def __init__(self):
        self.session = get_session()
        self.contact_dao = ContactDAO(self.session)

    def add_contact(self, client_id, nom, date_contact, notes=None):
        contact = self.contact_dao.create_contact(client_id=client_id, nom=nom, date_contact=date_contact, notes=notes)
        return contact

    def get_contact(self, contact_id):
        contact = self.contact_dao.get_contact(contact_id)
        return contact

    def update_contact(self, contact_id, **kwargs):
        contact = self.contact_dao.update_contact(contact_id, **kwargs)
        return contact

    def delete_contact(self, contact_id):
        success = self.contact_dao.delete_contact(contact_id)
        return success

    def close_session(self):
        self.session.close()
