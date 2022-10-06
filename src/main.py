from brainflow.data_filter import DataFilter
import pandas as pd
import numpy as np
from datetime import datetime

import interface as interf
import get_data as gd
from set_board import CYTON_BOARD_CONFIGURED, CYTON_ID


def main(): -> None
    interf.show_menu()
    session_number = interf.get_session_number()

    data = gd.get_data()

    # File writing raw
    DataFilter.write_file(data, f'data_raw/debug-session_{session_number}.csv', 'w')

    # Generating timestamp formatted
    timestamps: str = [] 
    for epoch in data[22, :]:
        timestamp_object = datetime.fromtimestamp(epoch)
        timestamps.append(timestamp_object.strftime("%Y-%m-%d %H:%M:%S.%f"))

    # Column naming
    columns_df = CYTON_BOARD_CONFIGURED.get_eeg_names(CYTON_ID)
    columns_df.insert(0, 'Index')
    for num in range(13):
        columns_df.append('other')
    columns_df.append('Timestamp')
    columns_df.append('other')

    # File writing with columns
    data_raw = np.genfromtxt(f'data_raw/debug-session_{session_number}.csv', delimiter='\t')
    data_df = pd.DataFrame(data_raw, columns=columns_df)
    data_df["Timestamp (Formatted)"] = timestamps
    data_df.to_csv(f'data_formatted/debug-session_{session_number}_formatted.csv', sep='\t')

if __name__ == '__main__':
    main()
