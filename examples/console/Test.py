from __future__ import absolute_import, division, print_function
from builtins import *  # @UnusedWildImport

from ctypes import cast, POINTER, c_ushort
from math import pi, sin
from signal import signal
from time import sleep

import numpy as np
import matplotlib.pyplot as plt

import time

def testingIntegral(amplitude, freq, rate, points_per_channel, delaycount, Cathodiccount, numwaveform, waveform_type):

    chan = 0
    low_chan = chan
    high_chan = chan
    num_chans = 1
    # IMPORTANT: RATE MUST BE 2 * N THE POINTS SO THAT WE GET HALF THE PHASE OF SINE (changes with frequency, currently 1Hz)
    delaycount = int(delaycount)
    Cathodiccount = int(Cathodiccount)
    EndZeroTime = 0.1
    EndZerocount = int(EndZeroTime * rate)
    total_count = (points_per_channel * num_chans) + delaycount + Cathodiccount + EndZerocount # total number of data points to output, important for timing
    data_array = [0] * total_count
    add_example_data( data_array,
                                num_chans, freq, rate, points_per_channel,
                                amplitude, waveform_type, delaycount, Cathodiccount, EndZerocount)
    plt.plot(data_array, marker='o', linestyle='-', color='b')

    # Add labels and title
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Array Plot")

    # Show grid
    plt.grid(True)

    # Display the plot
    plt.show()
    return 1






def add_example_data(data_array, num_chans, freq, rate,
                     points_per_channel, amplitude, waveform_type, delaycount, Cathodiccount, EndZerocount):

    # Fill the array with sine wave data at the calculated frequencies.
    # Note that since we are using the SCALEDATA option, the values
    # added to data_array are the actual voltage values that the device
    # will output
    data_index = 0
    if waveform_type == 1:
        for point_num in range(points_per_channel): #points_per_channel,freq and rate dictate how long the output will run
    #        for channel_num in range(num_chans):
            value = -amplitude * sin(2 * pi * freq * point_num / rate) + 0
            data_array[data_index] = value
            data_index += 1
    elif waveform_type == 2:
        for point_num in range(points_per_channel):
            value = -amplitude * np.sign(sin(2 * pi * freq * point_num / rate)) + 0
            data_array[data_index] = value
            data_index += 1
    elif waveform_type == 3:
        for point_num in range(points_per_channel):
            value = -amplitude * np.arcsin(np.sin(2 * np.pi * freq * point_num / rate)) * 2 / np.pi
            data_array[data_index] = value
            data_index += 1
    elif waveform_type == 4:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(0, 1, points_per_channel)[point_num]
            data_array[data_index] = value
            data_index += 1
    elif waveform_type == 5:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(1, 0, points_per_channel)[point_num]
            data_array[data_index] = value
            data_index += 1
    x = np.arange(len(data_array))
    area = abs(np.trapz(data_array,x))
    cathodicamplitude = area/Cathodiccount
    for i in range(0, delaycount): # delay period, output 0v
        value = 0
        data_array[data_index] = value
        data_index += 1
    for i in range(0, Cathodiccount): # Cathodic period
        value = cathodicamplitude
        data_array[data_index] = value
        data_index += 1
    for i in range(0, EndZerocount): # End Zero period, output 0v
        value = 0
        data_array[data_index] = value
        data_index += 1
    return time.time()

if __name__ == '__main__':
    testingIntegral()