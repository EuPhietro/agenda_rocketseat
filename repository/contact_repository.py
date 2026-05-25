from typing import Optional

from peewee import DoesNotExist

from models import Contact


class ContactRepository:
    """
    Repositório de acesso a dados (DAO) responsável por abstrair 
    e encapsular as operações de banco de dados para a entidade Contact.
    """
    
    def get(self, contact_id: int) -> Optional[Contact]:
        """
        Recupera um contato específico pelo seu ID.
        Retorna a instância do contato ou None caso não exista.
        """

        try:

            return Contact.get_by_id(contact_id)
        except DoesNotExist:
            return None
        
    def save(self, name: str, number: str) -> Contact:
        """
        Cria e persiste um novo contato no banco de dados.
        """

        return Contact.create(name=name, number=number)

    def update(self, contact: Contact) -> Contact:
        """
        Sincroniza as alterações feitas na instância do contato com o banco de dados.
        """
        contact.save()
        return contact
    
    def delete(self, contact_id: int) -> int:
        """
        Deleta um contato pelo seu ID e retorna a quantidade de linhas afetadas.
        """

        return Contact.delete_by_id(contact_id)
    
    def list_all(self) -> list[Contact]:
        """
        Recupera todos os contatos armazenados.
        """

        
        return list(Contact.select())
    
    def query_by_name(self, name: str) -> list[Contact]:
        """
        Busca contatos cujo nome corresponda ao valor exato informado.
        """

        return list(Contact.filter(Contact.name == name))