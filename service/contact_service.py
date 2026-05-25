from typing import Optional
from datetime import datetime


from peewee import  DoesNotExist

from repository import ContactRepository

from models import Contact


class ContactService:
    
    def __init__(self, contact_repo: ContactRepository):
        self.contact_repo = contact_repo
    
    def create_contact(self, name: str, number: str) -> Contact:
        
        new_contact = self.contact_repo.save(name,number)
        
        return new_contact
    
    def update_contact(
        self,
        id: int,
        new_name: Optional[str] = None,
        new_number: Optional[str] = None) -> Contact:
        
        contact = self.contact_repo.get(id)
        
        if not contact:
            raise DoesNotExist
        
        if new_name is not None:
            contact.name = new_name  # type: ignore
        if new_number is not None:
            contact.number = new_number  # type: ignore
        contact.modified_at = datetime.now()  # type: ignore
        
        return self.contact_repo.update(contact)
    
    def delete_contact(self,contact_id:int) ->int:
        return self.contact_repo.delete(contact_id)
    
    def get_by_id(self, contact_id: int) -> Optional[Contact]:
        
        return self.contact_repo.get(contact_id)
    
    
    def get_all(self) -> list[Contact]:
        contacts = self.contact_repo.list_all()
        return  contacts if len(contacts) > 0 else []
    
    def get_by_name(self, name:str) -> list[Contact]:
        return self.contact_repo.query_by_name(name)
    
    


