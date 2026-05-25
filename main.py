from rich.prompt import Prompt, IntPrompt, Confirm
from rich.table import Table
from rich import box

from service import ContactService, FavoritesService
from repository import ContactRepository, FavoritesRepository

from service.menu import console, OPTIONS, show_contact, show_menu

def main() -> None:
    
    contact_repository = ContactRepository()
    contact_service = ContactService(contact_repository)
    
    favorites_repository = FavoritesRepository()
    favorites_service = FavoritesService(favorites_repository)
    
    int_prompt = IntPrompt(console=console)
    bool_prompt = Confirm(console=console)
    str_prompt = Prompt(console=console)
    
    while True:
        console.clear()
        show_menu(OPTIONS)
        choice = int_prompt.ask('\nEscolha uma opção', show_choices=False)       
        
        match choice:
            case 0:
                name = str_prompt.ask('Digite o nome do contato')
                number = str_prompt.ask(f'Digite o numero de {name}')
                
                try:
                    created_contact = contact_service.create_contact(name, number)
                    show_contact(created_contact)
                except Exception as e:
                    console.print(f"[red]Erro ao criar contato: {e}[/red]")
                
                if not bool_prompt.ask('\nVoltar para o menu?'):
                    break
                    
            case 1:
                contacts = contact_service.get_all()
                
                if not contacts:
                    console.print("[yellow]Não há contatos para deletar.[/yellow]")
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                
                contacts_table = Table(
                    'Index', 'Name', 'Number', 'Created At', 'Modified At', 
                    title='Meus Contatos', expand=True, box=box.HORIZONTALS
                )
                
                for i, contact in enumerate(contacts):
                    contacts_table.add_row(
                        str(i + 1),
                        str(contact.name), 
                        str(contact.number),
                        str(contact.created_at) if contact.created_at else "",
                        str(contact.modified_at) if contact.modified_at else ""
                    )
                console.print(contacts_table)
                
                if bool_prompt.ask('\nDeletar contato?'):
                    index = int_prompt.ask('Digite o index do contato')
                    
                    if index < 1 or index > len(contacts):
                        console.print(':warning: [bold red]ÍNDICE INVÁLIDO[/bold red]')
                        str_prompt.ask("\nPressione Enter para voltar")
                        continue
                    
                    current_contact = contacts[index-1]
                    
                    qtd_deleted = contact_service.delete_contact(current_contact.id) # type: ignore
                    
                    console.print(f'[bold magenta]Contatos apagados:[/bold magenta] [bold yellow]{qtd_deleted}[/bold yellow]')
                    str_prompt.ask("\nPressione Enter para continuar")
                    continue
                else:
                    continue
                    
            case 2:
                contacts = contact_service.get_all()
                
                if not contacts:
                    console.print("[yellow]Não há contatos na lista, crie um contato para listá-lo[/yellow]")
                    str_prompt.ask("\nPressione Enter para continuar")
                    continue
                
                contacts_table = Table(
                    'Index', 'Name', 'Number', 'Created At', 'Modified At', 
                    title='Meus Contatos', expand=True, box=box.HORIZONTALS
                )
                
                for i, contact in enumerate(contacts):
                    contacts_table.add_row(
                        str(i + 1),
                        str(contact.name), 
                        str(contact.number),
                        str(contact.created_at) if contact.created_at else "",
                        str(contact.modified_at) if contact.modified_at else ""
                    )
                console.print(contacts_table)
                
                if bool_prompt.ask('\nEditar contato?'):
                    index = int_prompt.ask('Digite o index')
                    
                    if index < 1 or index > len(contacts):
                        console.print(':warning: [bold red]ÍNDICE INVÁLIDO[/bold red]')
                        str_prompt.ask("\nPressione Enter para voltar")
                        continue
                    
                    current_contact = contacts[index-1]
                    
                    i_name = str_prompt.ask('Digite o novo nome do contato', default="")
                    i_number = str_prompt.ask(f'Digite o novo numero (Atual: {current_contact.number})', default="")
                    
                    new_name = i_name if i_name.strip() else None
                    new_number = i_number if i_number.strip() else None
                    
                    if new_name or new_number:
                        modified_contact = contact_service.update_contact(
                            current_contact.id, new_name, new_number # type: ignore
                        ) 
                        console.print("\n[green]Atualizado![/green]")
                        show_contact(modified_contact)
                    else:
                        console.print("\n[yellow]Nenhuma alteração realizada.[/yellow]")
                        
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                else:
                    continue
            
            case 3:
                contacts = contact_service.get_all()
                if not contacts:
                    console.print("[yellow]Não há contatos para favoritar.[/yellow]")
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                
                contacts_table = Table(
                    'Index', 'Name', 'Number', 'Created At', 'Modified At', 
                    title='Meus Contatos', expand=True, box=box.HORIZONTALS
                )
                
                for i, contact in enumerate(contacts):
                    contacts_table.add_row(
                        str(i + 1),
                        str(contact.name), 
                        str(contact.number),
                        str(contact.created_at) if contact.created_at else "",
                        str(contact.modified_at) if contact.modified_at else ""
                    )
                console.print(contacts_table)

                index = int_prompt.ask('Digite o index')
                    
                if index < 1 or index > len(contacts):
                    console.print(':warning: [bold red]ÍNDICE INVÁLIDO[/bold red]')
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                    
                current_contact = contacts[index-1]
                
                favorites_service.to_favorite(current_contact)
                
            case 4:
                favorites = favorites_service.list_all()
                if not favorites:
                    console.print("[yellow]Não há favoritos para deletar.[/yellow]")
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                
                favorites_table = Table(
                    'Index', 'Name', 'Number', 'Contact Created At', 'Favorited At','Modified At',
                    title='Meus Contatos', expand=True, box=box.HORIZONTALS
                )
                
                for i, favorite in enumerate(favorites):
                    favorites_table.add_row(
                        str(i + 1),
                        str(favorite.contact_id.name),
                        str(favorite.contact_id.number), 
                        str(favorite.contact_id.created_at),
                        str(favorite.created_at) if favorite.created_at else "",
                        str(favorite.modified_at) if favorite.modified_at else ""
                    )
                console.print(favorites_table)

                index = int_prompt.ask('Digite o index')
                    
                if index < 1 or index > len(favorites):
                    console.print(':warning: [bold red]ÍNDICE INVÁLIDO[/bold red]')
                    str_prompt.ask("\nPressione Enter para voltar")
                    continue
                    
                current_favorited = favorites[index-1]
                
                if current_favorited:
                    favorites_service.unfavorite(current_favorited.contact_id) # type: ignore
                    
            case 5:
                console.print('[bold green]Saindo de sua agenda de contatos [/bold green]')
                break
                
            case _:
                console.print("[red]Opção inválida.[/red]")
                str_prompt.ask("\nPressione Enter para continuar")
       
    console.clear()
    console.print("[bold green]Sessão Encerrada.[/bold green]")
    
if __name__ == '__main__':
    main()