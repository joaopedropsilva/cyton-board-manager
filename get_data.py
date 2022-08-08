from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter

from set_board import CYTON_BOARD_CONFIGURED

BoardShim.enable_dev_board_logger()
CYTON_BOARD_CONFIGURED.prepare_session()
active_channels = CYTON_BOARD_CONFIGURED.get_eeg_channels(BoardIds.CYTON_BOARD.value)

# TODO: check how the data is returned; official doc uses time.sleep
if (CYTON_BOARD_CONFIGURED.is_prepared()):
    CYTON_BOARD_CONFIGURED.start_stream()
    data = CYTON_BOARD_CONFIGURED.get_board_data()
    CYTON_BOARD_CONFIGURED.stop_stream()
    CYTON_BOARD_CONFIGURED.release_session()

DataFilter.write_file(data, f'./data/session_{session_name}.csv', 'w')