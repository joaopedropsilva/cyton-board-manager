from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter
import pandas as pd
import numpy as np

import interface as interf
import get_data as gd
from set_board import CYTON_BOARD_CONFIGURED, CYTON_ID


def debug():
    session_number = interf.get_session_number()
    BoardShim.enable_dev_board_logger()
    data = gd.get_data(sampling_time = 3)

    # File writing raw
    DataFilter.write_file(data, f'data/debug-session_{session_number}.csv', 'w')

    # Column naming
    columns_df = CYTON_BOARD_CONFIGURED.get_eeg_names(CYTON_ID)
    columns_df.insert(0, 'Index')
    for num in range(12):
        columns_df.append('other')
    columns_df.append('Timestamp')
    columns_df.append('other')
    columns_df.append('Timestamp (Formatted)')

    # File writing with columns
    data_raw = pd.read_csv(f'data/debug-session_{session_number}.csv')
    print(columns_df)
    input()
    data_raw.to_csv(f'data_view/debug-session_{session_number}_formatted.csv', columns=columns_df)

if __name__ == '__main__':
    debug()
