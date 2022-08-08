import argparse
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds

parser = argparse.ArgumentParser(description='Cyton Board Parser Setup')

parser.add_argument('-sp', '--serial-port', type=str, help='serial port to connect board, usually COM3 from dongle (our case)', required=False, default='COM3')
parser.add_argument('-id', '--board-id', type=int, help='board id', required=False, default=BoardIds.CYTON_BOARD.value)
args = parser.parse_args()

params = BrainFlowInputParams()
params.serial_port = args.serial_port

CYTON_BOARD_CONFIGURED = BoardShim(args.board_id, params)
CYTON_ID = BoardIds.CYTON_BOARD.value
