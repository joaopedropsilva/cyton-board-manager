# Terminal interface procedure

from os import system

# Auxiliary

def clear_screen():
    system('cls || clear')

def get_input(text='Sua escolha: '):
    return input(text)

def check_int_type(arg):
    if (arg.isdigit()):
        return True
    
    return False

def validate_input(session_number):
    if (check_int_type(session_number)):
        return session_number
    else:
        while not check_int_type(session_number):
            session_number = get_input('Número da sessão inválido, tente novamente (tipo: int): ')
    return session_number

# Menu

def show_menu():
    clear_screen()
    print('=' * 45, '\n')
    print('\tOpenBCI Ultracortex Mark IV\n')
    print('=' * 45, '\n')
    input('Pressione enter para continuar...')

# Data acquisition

def get_session_name():
    return get_input('Nome da sessão: ')

def get_session_number():
    session_number = get_input('Número da sessão: ')
    return validate_input(session_number)
