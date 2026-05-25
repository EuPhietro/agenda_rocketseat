from datetime import datetime
from peewee import TextField, AutoField, DateTimeField
from models import BaseModel

class Contact(BaseModel):
    """
    Modelo representativo de um contato no banco de dados.
    """
    # Identificador único do registro
    id = AutoField(primary_key=True)
    
    # Nome completo ou de exibição do contato
    name = TextField(null=False)
    
    # Informação de contato (ex: email, telefone), deve ser única
    number = TextField(null=False, unique=True)
    
    # Data e hora exatas de criação do registro
    created_at = DateTimeField(
        formats='%Y-%m-%d %H:%M:%S.%f', 
        default=datetime.now
    )
    
    # Data e hora exatas da última modificação (precisão de milissegundos)
    modified_at = DateTimeField(
        formats='%Y-%m-%d %H:%M:%S.%f', 
        null=True
    )