from os import system

## Auxiliary

def clear_screen() -> None:
    system('cls || clear')

def get_input(text: str = 'Sua escolha: ') -> str:
    return input(text)

# Menu

def show_menu() -> None:
    clear_screen()
    print('=' * 37, '\n')
    print('\tCyton Board Manager\n')
    print('=' * 37, '\n')
    input('Pressione enter para continuar...')

## Data acquisition

def get_session_name() -> int:
   return get_input('Nome da sessão: ')

