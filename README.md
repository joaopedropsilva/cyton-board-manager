# Cyton Board Manager

This software is responsible to capture EEG signals from [Ultracortex Mark IV](https://docs.openbci.com/AddOns/Headwear/MarkIV/) an [OpenBCI](https://openbci.com) headgear

## Project structure

:white_check_mark: `set_board.py` configures the cyton board correctly
:white_check_mark:  `get_data.py` gets all data from the hardware
:white_check_mark: `interface.py` sets a collection of functions to run the application on terminal mode
:white_check_mark: `main.py` uses the other files to generate the formatted file outputs

## Upcoming features

:pushpin: Pre-filtering and data denoising with BrainFlow
:pushpin: Fancier terminal interface

## Used technologies

<div style="display: flex; justify-content: flex-start">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" />
<img src="httpscdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" />
</div>

## Other featured technologies

:wrench: [BrainFlow](https://brainflow.org)
:wrench: [pynput](https://pynput.readthedocs.io/en/latest/#)
