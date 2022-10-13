import pyqtgraph as pg
from brainflow.board_shim import BoardShim, NDArray
from pyqtgraph.Qt import QtGui, QtCore
import pandas as pd
import numpy as np
from nptyping import Float64
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

from set_board import CYTON_ID
from filter import default_filtering
from filter import CYTON_SAMPLING_RATE

# Real time plot

class Graph:
    def __init__(self, board_shim, session_number) -> None:
        self.board_shim = board_shim
        self.board_id = CYTON_ID
        self.exg_channels = BoardShim.get_exg_channels(CYTON_ID)
        self.sampling_rate = CYTON_SAMPLING_RATE
        self.update_speed_ms = 50
        self.window_size = 4
        self.num_points = self.window_size * self.sampling_rate

        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title = f'Session {session_number}', size=(800, 600))

        self._init_timeseries()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(self.update_speed_ms)
        QtGui.QGuiApplication.instance().exec_()

    def _init_timeseries(self):
        self.plots = list()
        self.curves = list()
        for i in range(len(self.exg_channels)):
            p = self.win.addPlot(row=i, col=0)
            p.showAxis('left', False)
            p.setMenuEnabled('left', False)
            p.showAxis('bottom', False)
            p.setMenuEnabled('bottom', False)
            if i == 0:
                p.setTitle('TimeSeries Plot')
            self.plots.append(p)
            curve = p.plot()
            self.curves.append(curve)

    def update(self):
        data = self.board_shim.get_current_board_data(self.num_points)
        
        default_filtering(data)

        self.app.processEvents()

# Visualize data

def plot_data_png(data: NDArray[Float64], figure_name: str = "data") -> None:
    eeg_channels = BoardShim.get_eeg_channels(CYTON_ID)
    df = pd.DataFrame(np.transpose(data))
    plt.figure()
    df[eeg_channels].plot(subplots=True)
    plt.savefig(f'{figure_name}.png')
