# Terminal interface procedure

from os import system

## Auxiliary

def clear_screen() -> None:
    system('cls || clear')

def get_input(text: str = 'Sua escolha: ') -> str:
    return input(text)

# Menu

def show_menu():
    clear_screen()
    print('=' * 45, '\n')
    print('\tOpenBCI Ultracortex Mark IV\n')
    print('=' * 45, '\n')
    input('Pressione enter para continuar...')

## Data acquisition

#Lê o nome da sessão
def get_session_name() -> str:
    while True:
        session_name = get_input('Nome da sessão: ')
        confirm = get_input('Confirme [y/n]: ')
        if confirm.lower() == 'y': break

    return session_name

#Lê o número da sessão
def get_session_number() -> int:
    user_input = get_input('Número da sessão: ')

    while True:
        try:
            #Se não for possível converter para int, significa que a entrada é inválida.
            #Nesse caso, um erro é gerado e o loop continua.
            session_number = int(user_input)
            break
        except:
            user_input = get_input('Número da sessão inválido, tente novamente (tipo: int): ')
    
    return session_number

# Volunteers

#Lê o nome da pessoa
def get_volunteer_name() -> str:
    while True:
        vol_name = get_input('Nome do voluntário: ')
        confirm = get_input('Confirme [y/n]: ')
        if confirm.lower() == 'y': break
    
    return vol_name

#Lê o ID da pessoa
def get_volunteer_ID() -> int:
    user_input = get_input('Número da pessoa: ')

    while True:
        try:
            vol_ID = int(user_input)
            break
        except:
            user_input = get_input('Número da pessoa inválido, tente novamente (tipo: int): ')
    
    return vol_ID
