from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.console import Group
from rich import box
from rich.style import Style


from models import Contact


# O dunder all (__all__) é uma prática de arquitetura limpa em Python. 
# Ele restringe o que será exportado caso outro módulo faça um `from view import *`,
# garantindo que o encapsulamento desta camada seja respeitado.
__all__ = ['OPTIONS', 'console', 'show_menu', 'show_contact']

# CONSTANTES:
# Definimos as opções como uma lista estática. Isso facilita a manutenção e garante
# que a ordem e os textos do menu fiquem centralizados em um único lugar, 
# agindo como a "fonte da verdade" para o loop principal da aplicação.

# Menu Principal
OPTIONS = [
    'Criar contato',
    'Deletar Contato',
    'Listar Contatos / Editar',
    'Favoritar Contato',
    'Remover Favoritos',
    'Sair'
]





# Inicialização do motor de renderização da interface.
# O color_system='truecolor' garante renderização em alta fidelidade e 
# o force_terminal=True evita comportamentos inesperados em terminais embutidos (como os de IDEs).
console = Console(color_system='truecolor', force_terminal=True, style=Style(bgcolor='#282a36'))

# Definição das estruturas visuais de dados (Templates).
# Declaramos as tabelas globalmente para configurar os cabeçalhos (headers) e o estilo (box).
# O expand=True faz com que a tabela ocupe toda a largura disponível, dando uma aparência de "dashboard".

def show_menu(options: list[str]) -> None:
    """
    Renderiza o menu principal da aplicação encapsulado em um painel estilizado.
    """
    # O Group permite empilhar múltiplos elementos renderizáveis do Rich (como textos formatados)
    # antes de inseri-los em um contêiner (como o Panel).
    group = Group(fit=True)
    
    # Iteramos sobre as opções enumeradas para garantir que o número exibido
    # corresponda ao índice exato que o controlador (Controller) avaliará depois.
    for i, option in enumerate(options):
        # A sintaxe do Rich (ex: [i]...[/i]) injeta estilo diretamente nas strings.
        group.renderables.append(f'[i]{i}[/i] - [bold white]{option}[/bold white]')
        
    # Encapsulamos o grupo de opções em um Panel para criar uma borda visual ao redor do menu,
    # separando-o claramente de outras informações no terminal.
    panel = Panel(group, title='[bold red]My Contacts[/bold red]', title_align='left',subtitle='Digite uma opção: ', padding=1,)
    
    # O console consome o painel e o desenha na saída padrão (stdout).
    console.print(panel)
        
        
def show_contact(contact: Contact) -> None:
    """
    Extrai as informações de uma entidade Contact e as exibe 
    de forma destacada em um painel individual.
    """
    # Construímos a visualização do detalhe da entidade. O uso do Panel aqui 
    # cria um card focado no registro específico, separando títulos, subtítulos e conteúdo.
    panel = Panel(
        f'Contact: [bold red]{contact.number}[/bold red]',
        title=f"It's: [green bold]{contact.name}[/green bold]",
        subtitle=f'{contact.created_at}',
        title_align='left'
    )
    
    console.print(panel)