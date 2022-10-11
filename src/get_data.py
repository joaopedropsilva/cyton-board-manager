from brainflow.board_shim import NDArray
from pynput.keyboard import Listener
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED as cyton


# Possible file separation, too much definitions in a script file
class Flags():
    def __init__(self) -> None:
        self.main_loop_state = True
        self.connection_status = False
        self.exec_permission = True
        self.abort_permission = False


def set_timeout_for_operation(time: int = 3, operation: str = '[No operation defined]') -> None:
    print(f'{operation} sessão em: {time} segundos\n(Pressione [A] para abortar operação)')

    for _ in range(time, 0, -1):
        sleep(1)
        time -= 1

def stop_stream_procedure() -> None:
    try:
        cyton.stop_stream()
        print("[S]TOP --> Interrompendo fluxo de dados")
    except Exception:
        print('[WARNING] FLUXO DE DADOS JÁ INTERROMPIDO')

def restart_stream_procedure() -> None:
    try:
        cyton.start_stream()
        print("[W]RITE --> Retomando fluxo de dados")
    except Exception:
        print('[WARNING] FLUXO DE DADOS JÁ EM OCORRÊNCIA')


def quit_session_procedure() -> None:
    try:
        flags.abort_permission = True
        set_timeout_for_operation(operation='Encerrando')
        if flags.exec_permission:
            cyton.stop_stream()
            print('[Q]UIT --> Encerrando sessão')
            flags.main_loop_state = False
        else:
            flags.abort_permission = False
            flags.exec_permission = True
    except Exception:
        print('[Q]UIT --> Encerrando sessão')
        flags.main_loop_state = False


def init_new_session() -> None:
    cyton.get_board_data()
    cyton.release_session()
    cyton.prepare_session()

    if cyton.is_prepared():
        cyton.start_stream()
        flags.abort_permission = False
        flags.exec_permission = True


def reset_session_procedure() -> None:
    try:
        flags.abort_permission = True
        set_timeout_for_operation(operation='Reiniciando')
        if flags.exec_permission:
            cyton.stop_stream()
            print('[R]ESET --> Reiniciando sessão')
            init_new_session()
        else:
            flags.abort_permission = False
            flags.exec_permission = True
    except Exception:
        print('[R]ESET --> Reiniciando sessão')
        init_new_session()


def abort_procedure() -> None:
    if flags.abort_permission:
        flags.exec_permission = False
        print('[A]BORT --> Abortando operação')


def on_press(key) -> None:
    if key.char == 's':
        stop_stream_procedure()
    elif key.char == 'w':
        restart_stream_procedure()
    elif key.char == 'q':
        quit_session_procedure()
    elif key.char == 'r':
        reset_session_procedure()


def on_press_abort(key): 
  if key.char == 'a':
    abort_procedure()


# Initializing listeners and flagss
regular_listener = Listener(on_press = on_press)
abort_listener = Listener(on_press = on_press_abort)
flags = Flags()


def get_data() -> NDArray[Float64]:
    while not flags.connection_status:
        try:
            cyton.prepare_session()
            flags.connection_status = True

            if cyton.is_prepared():
                cyton.start_stream()
                regular_listener.start()
                abort_listener.start()

                while flags.main_loop_state:
                    sleep(1)
                    
                data = cyton.get_board_data()
                cyton.release_session()

                return data
        except Exception:
            print('[WARNING] CONEXÃO COM A PLACA INDISPONÍVEL')
            print('[WARNING] Verifique o estado do equipamento')

            for time in range(5, 0, -1):
                print(f'TENTANDO RECONEXÃO EM {time}...')
                sleep(1)

