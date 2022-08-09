from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter
import pandas as pd
import numpy as np
from time import sleep

import interface as interf
from set_board import CYTON_BOARD_CONFIGURED, CYTON_ID

def main():
    interf.show_menu()
    interf.clear_screen()
    session_name = interf.get_session_name()
    session_number = interf.get_session_number()
    volunteer_name = interf.get_volunteer_name()
    volunteer_id = interf.get_volunteer_ID()

    BoardShim.enable_dev_board_logger()
    CYTON_BOARD_CONFIGURED.prepare_session()

    # TODO: check how the data is returned; official doc uses time.sleep
    if (CYTON_BOARD_CONFIGURED.is_prepared()):
        CYTON_BOARD_CONFIGURED.start_stream()
        sleep(3)
        data = CYTON_BOARD_CONFIGURED.get_board_data()
        CYTON_BOARD_CONFIGURED.stop_stream()
        CYTON_BOARD_CONFIGURED.release_session()

    columns_df = CYTON_BOARD_CONFIGURED.get_eeg_names(CYTON_ID)
    columns_df.insert(0, 'Index')
    data_df = pd.DataFrame(np.transpose(data)[: , :9], columns=columns_df)
    DataFilter.write_file(data, f'data/session_{session_name}-{session_number}.csv', 'w')


if __name__ == '__main__':
    main()
