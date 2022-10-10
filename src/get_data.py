from brainflow.board_shim import NDArray
from pynput.keyboard import Listener
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED as cyton

# Possible file separation, too much definitions in a script file
class Controller():
    def __init__(self) -> None:
        self.main_loop_state = True
        self.connection_status = False

def set_timeout_for_operation(time: int = 3, operation: str = '[No operation defined]') -> None:
    print(f'{operation} sessão em:\n(Pressione [A] para abortar operação)')
    for i in range(time, 0, -1):
        sleep(1)
        print(f'{time}...')
        time -= 1

def quit_session_procedure(board: BoardShim) -> None:
    print('[Q]UIT --> Encerrando sessão')
    controller.main_loop_state = False

def reset_session_procedure(board: BoardShim) -> None:
    print('[R]ESET --> Reiniciando sessão')
    cyton.get_board_data()
    cyton.start_session()

def on_press(key) -> None:
    if key.char == 's':
        try:
            cyton.stop_stream()
            print("[S]TOP --> Interrompendo fluxo de dados")
        except Exception:
            print('[WARNING] FLUXO DE DADOS JÁ INTERROMPIDO')
    elif key.char == 'w':
        try:
            cyton.start_stream()
            print("[W]RITE --> Retomando fluxo de dados")
        except Exception:
            print('[WARNING] FLUXO DE DADOS JÁ EM OCORRÊNCIA')
    elif key.char == 'q':
        try:
            set_timeout_for_operation(operation='Encerrando')
            cyton.stop_stream()
            quit_session_procedure(cyton)
        except Exception:
            quit_session_procedure(cyton)
    # Missing test for this option
    # Check if start_session() really resets timestamps 
    elif key.char == 'r':
        try:
            set_timeout_for_operation(operation='Reiniciando')
            cyton.stop_stream()
            reset_session_procedure(cyton)
        except Exception:
            reset_session_procedure(cyton)
    # Not working properly
    elif key.char == 'a':
        print('[A]BORT --> Abortando operação')

# Initializing listeners and controllers
listener = Listener(on_press = on_press)
controller = Controller()

def get_data() -> NDArray[Float64]:
    # Missing test for this new loop
    while not controller.connection_status:
        try:
            cyton.prepare_session()
            controller.connection_status = True

            if cyton.is_prepared():
                cyton.start_stream()
                listener.start()
                while controller.main_loop_state:
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

