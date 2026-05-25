from datetime import datetime

from peewee import ForeignKeyField, AutoField, DateTimeField

from models import BaseModel
from models import Contact


class Favorites(BaseModel):
    """
    Modelo que representa a relação de contatos favoritos no banco de dados.
    """
    
    # Identificador único do registro de favorito (Chave Primária)
    id = AutoField(primary_key=True)
    
    # Relação com o modelo Contact. 
    # O on_delete='CASCADE' garante que, se o contato for apagado, o favorito também será.
    contact_id = ForeignKeyField(Contact, field=Contact.id, on_delete='CASCADE', backref='favorites')
    
    # Data e hora exatas da criação do registro de favorito (precisão de milissegundos)
    created_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S.%f', null=False, default=datetime.now)
    
    # Data e hora exatas da última modificação, preenchida automaticamente com o momento atual
    modified_at = DateTimeField(formats='%Y-%m-%d %H:%M:%S.%f')