from brainflow.board_shim import BoardShim, NDArray
from nptyping import Float64
from time import sleep

from set_board import CYTON_BOARD_CONFIGURED

def get_data(board: BoardShim, sampling_time: float = 10) -> NDArray[Float64]:

    if board.is_prepared():
        board.start_stream()
        sleep(sampling_time)
        data = board.get_board_data()
        board.stop_stream()
        board.release_session()

        return data