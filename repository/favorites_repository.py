# Internal libraries
from datetime import datetime
from typing import Optional

# Third Part Libraries
from peewee import DoesNotExist, JOIN

# Internal Libraries 
from models.contact import Contact
from models.favorites import Favorites


class FavoritesRepository:
    """
    Repositório de acesso a dados responsável por isolar a lógica 
    de consultas do Peewee para a entidade Favorites.
    """
    
    def save(self, contact: Contact) -> Favorites:
        """
        Cria e persiste um novo registro de favorito associado a um contato.
        """
        return Favorites.create(
            contact_id=contact.id, 
            modified_at=datetime.now()
        )
    
    def get_by_id(self, contact_id: int) -> Optional[Favorites]:
        """
        Busca um favorito específico através do ID do contato.
        Retorna a instância do favorito ou None caso não seja encontrado.
        """
        try:
            return Favorites.get(Favorites.contact_id == contact_id)
        except DoesNotExist:
            return None
            
    def delete(self, contact_id: int) -> int:
        """
        Remove o favorito através do ID do contato.
        Retorna a quantidade de registros deletados.
        """
        query = Favorites.delete().where(Favorites.contact_id == contact_id)
        return query.execute()
       
    def list_all(self) -> list[Favorites]:
        """
        Lista todos os favoritos registrados no banco de dados,
        realizando um JOIN automático com a tabela Contact.
        """
        # O Peewee monta o objeto Favorites com o Contact embutido
        query = Favorites.select(Favorites, Contact).join(
            dest=Contact,
            join_type=JOIN.INNER,
            on=(Favorites.contact_id == Contact.id)
            )
        
        
        
        return list(query)