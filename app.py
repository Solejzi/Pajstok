import numpy as np
import pandas as pd

import plotly.graph_objs as go

import matplotlib.pyplot as plt

from static import StaticInfo
from dataframe_maker import DataMaker





if __name__ == '__main__':
    data = DataMaker().last_30_days('High')


    plt.figure()
    plt.style.use('classic')
    data.plot()
    plt.show()
    data = data.to_numpy()

    rounded = data.round(0)


