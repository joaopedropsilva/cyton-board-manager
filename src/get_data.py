from brainflow.board_shim import NDArray
from pynput.keyboard import Listener, Key, KeyCode
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED as cyton

class LoopController():
    def __init__(self) -> None:
        self.state = True

loop_controller = LoopController()

def on_press(key) -> None:
    if type(key) is KeyCode:
        if key.char == 'p':
            try:
                cyton.stop_stream()
                print("--> Interrompendo fluxo de dados")
            except Exception:
                print('[WARNING] FLUXO DE DADOS JÁ INTERROMPIDO')
        elif key.char == 's':
            try:
                cyton.start_stream()
                print("--> Retomando fluxo de dados")
            except Exception:
                print('[WARNING] FLUXO DE DADOS JÁ EM OCORRÊNCIA')
    elif type(key) is Key:
        if key == Key.esc:
            try:
                cyton.stop_stream()
                print('--> Encerrando sessão')
                loop_controller.state = False
            except Exception:
                print('--> Encerrando sessão')
                loop_controller.state = False

listener = Listener(on_press = on_press)

def get_data() -> NDArray[Float64]:
    try:
        cyton.prepare_session()
    except Exception:
        print('[WARNING] CONEXÃO COM A PLACA INDISPONÍVEL')
        print('[WARNING] Verifique o estado do equipamento')

        for time in range(10, 0, -1):
            print(f'ENCERRANDO PROGRAMA EM {time}...')
            sleep(1)
        
        exit(1)

    if cyton.is_prepared():

        cyton.start_stream()
        listener.start()
        while loop_controller.state:
            sleep(1)
            
        data = cyton.get_board_data()
        cyton.release_session()

        return data
