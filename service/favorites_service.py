# Build-in Libraries
from datetime import datetime
from typing import Optional

# Third Part Libraries
from peewee import DoesNotExist

# Internal Libraries
from models import Favorites, Contact
from repository import FavoritesRepository



class FavoritesService:
    
    def __init__(self, favorites_repo:FavoritesRepository):
        self.favorites_repo = favorites_repo
            
    def to_favorite(self, contact: Contact) -> Favorites:
        return self.favorites_repo.save(contact)
        
    def unfavorite(self, contact_id: int) -> int:
        return self.favorites_repo.delete(contact_id=contact_id) #type: ignore
    
    def get_favorited(self, id: int) -> Optional[Favorites]:
        return self.favorites_repo.get_by_id(id)
    # Retorna uma lista de contatos favoritos
    def list_all(self) -> list[Favorites]:
        
        return self.favorites_repo.list_all()