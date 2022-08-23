from brainflow.board_shim import BoardShim, NDArray
from pynput.keyboard import Listener, Key, HotKey
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED as cyton

def on_press(key: Key):
    if key.char == 'p':
        cyton.stop_stream()
        print("fluxo de dados interrompido")
    elif key.char == 's':
        cyton.start_stream()
        print("fluxo de dados retomado")

def start_listener():
    listener = Listener(on_press = on_press)
    listener.start()

def get_data(sampling_time: float = 10) -> NDArray[Float64]:

    cyton.prepare_session()

    if cyton.is_prepared():
        cyton.start_stream()
        start_listener()
        sleep(sampling_time)
        data = cyton.get_board_data()
        # TODO: tratar exceção do cyton.stop_stream
        cyton.stop_stream()
        cyton.release_session()

        return data
