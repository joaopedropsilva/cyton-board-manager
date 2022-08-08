from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter
import pandas as pd

import interface as interf
from set_board import CYTON_BOARD_CONFIGURED, CYTON_ID

def main():
    interf.show_menu()
    interf.clear_screen()
    session_name = interf.get_session_name()
    session_number = interf.get_session_number()

    BoardShim.enable_dev_board_logger()
    CYTON_BOARD_CONFIGURED.prepare_session()

    # TODO: check how the data is returned; official doc uses time.sleep
    if (CYTON_BOARD_CONFIGURED.is_prepared()):
        CYTON_BOARD_CONFIGURED.start_stream()
        #Tempo de leitura (A definir)
        data = CYTON_BOARD_CONFIGURED.get_board_data()
        CYTON_BOARD_CONFIGURED.stop_stream()
        CYTON_BOARD_CONFIGURED.release_session()

    channels_names = CYTON_BOARD_CONFIGURED.get_eeg_names(CYTON_ID)
    data_df = pd.DataFrame(data,columns=channels_names)
    #Arquivo com colunas, mas sem indexação
    data_df.to_csv(f'../data/session_{session_name}-{session_number}.csv', index=False)
    #Arquivo com dados puramente
    DataFilter.write_file(data, f'../data/session_{session_name}-{session_number}.csv', 'w')


if __name__ == '__main__':
    main()
