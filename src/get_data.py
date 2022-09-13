from brainflow.board_shim import BoardShim, NDArray
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
            cyton.stop_stream()
            print("Fluxo de dados interrompido")
        elif key.char == 's':
            cyton.start_stream()
            print("Fluxo de dados retomado")
    elif type(key) is Key:
        if key == Key.esc:
            cyton.stop_stream()
            loop_controller.state = False

listener = Listener(on_press = on_press)

def get_data() -> NDArray[Float64]:
    cyton.prepare_session()

    if cyton.is_prepared():

        cyton.start_stream()
        listener.start()
        while loop_controller.state:
            sleep(1)
            
        data = cyton.get_board_data()
        cyton.release_session()

        return data
