from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter
import pandas as pd
import numpy as np

import interface as interf
import get_data as gd
from set_board import CYTON_BOARD_CONFIGURED, CYTON_ID


def main():
    interf.show_menu()
    interf.clear_screen()
    session_name = interf.get_session_name()
    session_number = interf.get_session_number()
    volunteer_name = interf.get_volunteer_name()
    volunteer_id = interf.get_volunteer_ID()

    BoardShim.enable_dev_board_logger()
    data = gd.get_data(sampling_time = 3)
    data = np.transpose(data)

    columns_df = CYTON_BOARD_CONFIGURED.get_eeg_names(CYTON_ID)
    columns_df.insert(0, 'Index')
    columns_df.append(['other'*15])

    data_df = pd.DataFrame(data, columns=columns_df)
    DataFilter.write_file(data, f'data/session_{session_name}-{session_number}.csv', 'w')


if __name__ == '__main__':
    main()
