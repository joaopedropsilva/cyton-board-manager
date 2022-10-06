# Cyton Board Manager

This software is responsible to capture EEG signals from <a href="https://docs.openbci.com/AddOns/Headwear/MarkIV/" target="_blank">Ultracortex Mark IV</a> an <a href="https://openbci.com" target="_blank">OpenBCI</a> headgear

## Project structure

:white_check_mark: `set_board.py` configures the cyton board correctly<br>
:white_check_mark:  `get_data.py` gets all data from the hardware<br>
:white_check_mark: `interface.py` sets a collection of functions to run the application on terminal mode<br>
:white_check_mark: `main.py` uses the other files to generate the formatted file outputs

## Upcoming features

:pushpin: Pre-filtering and data denoising with BrainFlow<br>
:pushpin: Fancier terminal interface

## Used technologies

<div style="display: flex; justify-content: flex-start">
<a href="https://python.org" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="45px" height="45px"/></a>
<a href="https://numpy.org" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="45px" height="45px"/></a>
<a href="https://pandas.pydata.org" target="_blank"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" width="45px" height="45px"/></a>
</div>

## Other featured technologies

:wrench: <a href="https://brainflow.org" target="_blank">BrainFlow</a>
:wrench: <a href="https://pynput.readthedocs.io/en/latest/#" target="_blank">pynput</a>
