from brainflow.board_shim import BoardShim, NDArray
from pynput.keyboard import Listener, Key, HotKey
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED as cyton

def get_data(sampling_time: float = 10) -> NDArray[Float64]:

    cyton.prepare_session()

    if cyton.is_prepared():
        cyton.start_stream()
        sleep(sampling_time)
        data = cyton.get_board_data()
        cyton.stop_stream()
        cyton.release_session()

        return data

# Apenas uma ideia

def on_press(key: Key):
    
    if cyton.is_prepared():

        if key == 'p':
            cyton.stop_stream()
            print("fluxo de dados interrompido")
        elif key == 's':
            cyton.start_stream()
            print("fluxo de dados retomado")
        elif key == HotKey([Key.ctrl, Key.shift, 'c']):
            cyton.stop_stream()
            cyton.get_board_data()
            print("Fluxo interrompido e dados descartado")

def start_listener():
    
    listener = Listener(on_press=on_press)
    listener.join()