# Agenda de Contatos CLI

Aplicacao de agenda de contatos executada pelo terminal, desenvolvida em Python como uma evolucao de um desafio do curso de Introducao ao Python da Rocketseat.

O projeto implementa um CRUD completo de contatos, com persistencia em banco SQLite, interface interativa no terminal usando Rich e organizacao em camadas para separar responsabilidades entre interface, regras de negocio, acesso a dados e modelos.

## Sumario

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Arquitetura](#arquitetura)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Modelagem do banco de dados](#modelagem-do-banco-de-dados)
- [Como executar](#como-executar)
- [Fluxo de uso](#fluxo-de-uso)
- [Camadas do projeto](#camadas-do-projeto)
- [Dependencias](#dependencias)
- [Aprendizados](#aprendizados)
- [Possiveis melhorias](#possiveis-melhorias)
- [Referencias](#referencias)

## Sobre o projeto

Este projeto foi criado como um laboratorio pratico para estudar Python, organizacao de codigo, leitura de documentacoes oficiais e uso de bibliotecas do ecossistema Python em uma aplicacao real de linha de comando.

A ideia principal e construir uma agenda simples, mas com uma estrutura mais proxima de um projeto organizado em camadas:

- a camada de apresentacao cuida do menu e da interacao com o usuario;
- a camada de servico concentra as regras de aplicacao;
- a camada de repositorio encapsula o acesso ao banco;
- a camada de modelos representa as tabelas e entidades persistidas.

Mesmo sendo uma aplicacao pequena, o projeto busca manter responsabilidades separadas para facilitar manutencao, leitura e evolucao.

## Funcionalidades

A aplicacao permite:

- criar novos contatos;
- listar todos os contatos cadastrados;
- editar nome e numero de um contato;
- deletar contatos;
- favoritar contatos;
- listar contatos favoritos;
- remover contatos da lista de favoritos;
- persistir dados localmente usando SQLite;
- exibir menus, tabelas e paineis formatados no terminal.

## Tecnologias utilizadas

- **Python**: linguagem principal da aplicacao.
- **Peewee ORM**: ORM utilizado para mapear classes Python para tabelas no SQLite.
- **SQLite**: banco de dados local usado para armazenar contatos e favoritos.
- **Rich**: biblioteca usada para criar uma experiencia visual melhor no terminal.
- **python-dotenv**: biblioteca usada para carregar variaveis de ambiente a partir do arquivo `.env`.

## Arquitetura

O projeto segue uma organizacao em camadas:

```text
Interface CLI
    |
    v
Services
    |
    v
Repositories
    |
    v
Models / Peewee ORM
    |
    v
SQLite
```

Essa separacao ajuda a evitar que o codigo de interface, regra de negocio e banco de dados fiquem misturados no mesmo lugar.

## Estrutura de pastas

```text
agenda_contatos/
├── init_db.py
├── main.py
├── README.md
├── requirements.txt
├── database.db
├── models/
│   ├── __init__.py
│   ├── basemodel.py
│   ├── contact.py
│   └── favorites.py
├── repository/
│   ├── __init__.py
│   ├── contact_repository.py
│   └── favorites_repository.py
└── service/
    ├── __init__.py
    ├── contact_service.py
    ├── favorites_service.py
    └── menu.py
```

### Arquivos principais

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Ponto de entrada da aplicacao. Controla o loop principal, menu, prompts e chamadas para os servicos. |
| `init_db.py` | Inicializa o banco de dados e cria as tabelas necessarias. |
| `requirements.txt` | Lista as dependencias Python do projeto. |
| `.env` | Define configuracoes de ambiente, como o caminho do banco de dados. |
| `database.db` | Arquivo SQLite onde os dados sao armazenados localmente. |

## Modelagem do banco de dados

O banco possui duas entidades principais: `Contact` e `Favorites`.

### Contact

Representa um contato salvo na agenda.

Campos principais:

| Campo | Tipo | Descricao |
| --- | --- | --- |
| `id` | `AutoField` | Identificador unico do contato. |
| `name` | `TextField` | Nome do contato. |
| `number` | `TextField` | Numero do contato. Deve ser unico. |
| `created_at` | `DateTimeField` | Data e hora de criacao do contato. |
| `modified_at` | `DateTimeField` | Data e hora da ultima modificacao. |

### Favorites

Representa um contato marcado como favorito.

Campos principais:

| Campo | Tipo | Descricao |
| --- | --- | --- |
| `id` | `AutoField` | Identificador unico do favorito. |
| `contact_id` | `ForeignKeyField` | Relacao com um registro da tabela `Contact`. |
| `created_at` | `DateTimeField` | Data e hora em que o favorito foi criado. |
| `modified_at` | `DateTimeField` | Data e hora da ultima modificacao. |

A relacao com `Contact` utiliza `on_delete='CASCADE'`. Isso significa que, ao remover um contato, o registro correspondente em favoritos tambem e removido automaticamente.

## Como executar

### 1. Clonar ou acessar o projeto

Entre na pasta do projeto:

```bash
cd agenda_contatos
```

### 2. Criar um ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar o ambiente virtual

No macOS ou Linux:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

### 4. Instalar as dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar o arquivo `.env`

Crie ou confira o arquivo `.env` na raiz do projeto com a variavel `DATABASE`:

```env
DATABASE=database.db
```

Essa variavel e usada pelo Peewee para saber qual arquivo SQLite deve ser utilizado.

### 6. Criar as tabelas no banco

```bash
python init_db.py
```

### 7. Executar a aplicacao

```bash
python main.py
```

## Fluxo de uso

Ao executar `main.py`, a aplicacao abre um menu interativo no terminal.

Opcoes disponiveis:

| Opcao | Acao |
| --- | --- |
| `0` | Criar contato |
| `1` | Deletar contato |
| `2` | Listar contatos e editar |
| `3` | Favoritar contato |
| `4` | Remover favoritos |
| `5` | Sair |

O menu recebe a opcao digitada pelo usuario e direciona o fluxo para a operacao correspondente.

## Camadas do projeto

### `main.py`

Responsavel por:

- criar as instancias dos repositorios;
- criar as instancias dos servicos;
- exibir o menu principal;
- receber entradas do usuario;
- chamar os metodos apropriados dos servicos;
- exibir tabelas, mensagens e paineis no terminal.

### `service/`

Contem a camada de servicos da aplicacao.

Essa camada funciona como intermediaria entre a interface e os repositorios.

Arquivos:

- `contact_service.py`: regras e operacoes relacionadas a contatos.
- `favorites_service.py`: regras e operacoes relacionadas a favoritos.
- `menu.py`: componentes visuais e utilitarios da interface no terminal.

### `repository/`

Contem a camada de acesso a dados.

Essa camada encapsula as chamadas diretas ao Peewee, evitando que a interface precise conhecer detalhes de consultas, criacao, atualizacao ou delecao no banco.

Arquivos:

- `contact_repository.py`: operacoes de banco para `Contact`.
- `favorites_repository.py`: operacoes de banco para `Favorites`.

### `models/`

Contem os modelos usados pelo Peewee.

Arquivos:

- `basemodel.py`: configura a conexao com o banco e define a classe base dos modelos.
- `contact.py`: define o modelo `Contact`.
- `favorites.py`: define o modelo `Favorites`.
- `__init__.py`: centraliza exportacoes usadas por outras camadas.

## Dependencias

As dependencias do projeto estao registradas em `requirements.txt`.

Principais pacotes:

```text
peewee
python-dotenv
rich
types-peewee
```

As demais dependencias listadas sao bibliotecas auxiliares instaladas junto com o Rich.

## Aprendizados

Este projeto explora conceitos importantes para evoluir em Python:

- criacao de aplicacoes CLI;
- organizacao de projeto em camadas;
- separacao de responsabilidades;
- uso de ORM com Peewee;
- criacao de modelos relacionais;
- persistencia com SQLite;
- uso de variaveis de ambiente;
- renderizacao de interfaces no terminal com Rich;
- tratamento de entradas do usuario;
- uso de relacionamento entre tabelas;
- delecao em cascata com chave estrangeira.

## Possiveis melhorias

Algumas evolucoes futuras possiveis:

- adicionar validacao mais forte para nome e numero;
- impedir duplicidade de favoritos;
- adicionar busca parcial por nome;
- adicionar testes automatizados;
- criar uma camada dedicada de controllers;
- melhorar tratamento de erros do banco;
- adicionar ordenacao na listagem de contatos;
- permitir desfazer operacoes sensiveis;
- criar comandos diretos via argumentos de terminal;
- separar melhor a camada de interface da regra de aplicacao.

## Referencias

- [Documentacao oficial do Rich](https://rich.readthedocs.io/en/stable/)
- [Documentacao oficial do Rich Prompt](https://rich.readthedocs.io/en/stable/prompt.html)
- [Documentacao oficial do Peewee ORM](https://docs.peewee-orm.com/en/latest/)
- [Documentacao oficial do SQLite](https://www.sqlite.org/docs.html)
- [Documentacao oficial do python-dotenv](https://saurabh-kumar.com/python-dotenv/)

## Observacao sobre nomes e evolucao do codigo

Este projeto tambem funciona como um espaco de aprendizado. Alguns nomes de metodos, variaveis ou estruturas podem evoluir com o tempo conforme a aplicacao crescer e novas responsabilidades ficarem mais claras.

A intencao principal e manter o codigo compreensivel, praticar leitura de documentacao tecnica e melhorar gradualmente a expressividade da arquitetura.
