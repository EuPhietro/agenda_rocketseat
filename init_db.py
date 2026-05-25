
# Importando o módulo 
from models import (db, Contact, Favorites)
# Iniciando uma conexão com o db
database = db

# Usando o statment de contexto para criar as tabelas necessárias
with database:
    database.create_tables([Contact, Favorites],safe=True)