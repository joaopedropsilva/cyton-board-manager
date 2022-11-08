from brainflow.data_filter import DataFilter, FilterTypes, NoiseTypes
from brainflow.board_shim import NDArray

from set_board import CYTON_SAMPLING_RATE, CYTON_ID, CYTON_BOARD_CONFIGURED as cyton
from nptyping import Float64

# cyton.get_eeg_channels(CYTON_ID)

# Filters:
def envi_noise(data: NDArray[Float64]) -> None:
    for channel in cyton.get_eeg_channels(CYTON_ID):
        DataFilter.remove_environmental_noise(data[channel], CYTON_SAMPLING_RATE, NoiseTypes.FIFTY.value)

def bandpass(data: NDArray[Float64], start_freq: float, stop_freq: float, order: int = 4) -> None:
    for channel in range(4):
        DataFilter.perform_bandpass(data[channel], CYTON_SAMPLING_RATE, start_freq, stop_freq, order, FilterTypes.BESSEL.value, 0)

def bandstop(data: NDArray[Float64], start_freq: float = 50, stop_freq: float = 70, order: int = 4) -> None:
    for channel in range(4):
        DataFilter.perform_bandstop(data[channel], CYTON_SAMPLING_RATE, start_freq, stop_freq, order, FilterTypes.BUTTERWORTH.value, 0)

# Apply filters
def default_filtering(data: NDArray[Float64]) -> None:
    envi_noise(data)
    #bandstop(data)
