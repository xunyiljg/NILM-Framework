# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 15:04:36 2015

@author: thibaut
"""
from __future__ import print_function, division
import pandas as pd
import numpy as np


def simple_edge(meter, edge_threshold=30):
    # PART I: t to delta t
    columns = ['delta P', 'delta Q']

    meter_t1 = meter.values[1:]
    meter_t0 = meter.values[:-1]
    meter_dt = meter_t1-meter_t0
    index_dt = meter.index[1:]
    events = pd.DataFrame(meter_dt, columns=columns, index=index_dt)
    # PART II: Application of edge_threshold
    events = events[np.abs(events[columns[0]]) > edge_threshold]
    return events