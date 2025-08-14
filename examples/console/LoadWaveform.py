"""
File:                       LoadWaveform.py

Purpose:                    Creates a waveform from given parameters.

Demonstration:              check data array to ensure correct values are sent to the D/A channels.
"""
from __future__ import absolute_import, division, print_function
from builtins import *  # @UnusedWildImport

from ctypes import cast, POINTER, c_ushort

import numpy as np
from time import sleep

from mcculw import ul
from mcculw.enums import ScanOptions, FunctionType, Status
from mcculw.device_info import DaqDeviceInfo
from scipy import signal

try:
    from console_examples_util import config_first_detected_device
except ImportError:
    from .console_examples_util import config_first_detected_device

import time
import csv

def generate_waveform_dataarray(board_num, ao_range, data_array, points_per_channel, rate, time_stim, amplitude2, frequency, waveform_type):
    points_per_channel = int(points_per_channel)
    rate = int(rate)
    data_index = 0
    for point_num in range(points_per_channel):
        match waveform_type:
            case 'sine':
                value = -amplitude2 * np.sin(2 * np.pi * frequency * point_num / rate)
            case 'square':
                value = -amplitude2 * signal.square(2 * np.pi * frequency * point_num / rate)
        raw_value = ul.from_eng_units(board_num, ao_range, value)
        data_array[data_index] = raw_value
        data_index += 1
    return 1