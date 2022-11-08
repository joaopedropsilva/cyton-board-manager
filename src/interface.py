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

def get_session_number() -> int:
    user_input = get_input('Número da sessão: ')

    while True:
        try:
            session_number = int(user_input)
            break
        except ValueError:
            user_input = get_input('Número da sessão inválido, tente novamente (tipo: int): ')
    
    return session_number

