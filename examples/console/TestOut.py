"""
File:                       a_out_scan.py

Library Call Demonstrated:  mcculw.ul.a_out_scan()

Purpose:                    Writes to a range of D/A Output Channels.

Demonstration:              Sends a digital output to the D/A channels

Other Library Calls:        mcculw.ul.win_buf_alloc()
                            mcculw.ul.win_buf_free()
                            mcculw.ul.get_status()
                            mcculw.ul.release_daq_device()

Special Requirements:       Device must have D/A converter(s).
                            This function is designed for boards that
                            support timed analog output.  It can be used
                            for polled output boards but only for values
                            of NumPoints up to the number of channels
                            that the board supports (i.e., NumPoints =
                            6 maximum for the six channel CIO-DDA06).
"""
from __future__ import absolute_import, division, print_function
from builtins import *  # @UnusedWildImport

from ctypes import cast, POINTER, c_ushort
from math import pi, sin
from signal import signal
from time import sleep

import numpy as np

from mcculw import ul
from mcculw.enums import ScanOptions, FunctionType, Status
from mcculw.device_info import DaqDeviceInfo, ai_info

try:
    from console_examples_util import config_first_detected_device
except ImportError:
    from .console_examples_util import config_first_detected_device

import time
import matplotlib.pyplot as plt
import csv

def run_example(amplitude, freq, rate, points_per_channel, delaycount, numwaveform, WaveID,trialnum):
    # By default, the example detects and displays all available devices and
    # selects the first device listed. Use the dev_id_list variable to filter
    # detected devices by device ID (see UL documentation for device IDs).
    # If use_device_detection is set to False, the board_num variable needs to
    # match the desired board number configured with Instacal.
    use_device_detection = True
    dev_id_list = []
    board_num = 0
    memhandle = None
    value_list = []
    try:
        if use_device_detection:
            config_first_detected_device(board_num, dev_id_list)

        daq_dev_info = DaqDeviceInfo(board_num)
        if not daq_dev_info.supports_analog_output:
            raise Exception('Error: The DAQ device does not support '
                            'analog output')

        print('\nActive DAQ device: ', daq_dev_info.product_name, ' (',
              daq_dev_info.unique_id, ')\n', sep='')

        ao_info = daq_dev_info.get_ao_info()
        ai_info = daq_dev_info.get_ai_info()
        ai_range = ai_info.supported_ranges[0]
        chan = 0
        low_chan = chan
        high_chan = chan
        num_chans = 1
        # IMPORTANT: RATE MUST BE 2 * N THE POINTS SO THAT WE GET HALF THE PHASE OF SINE (changes with frequency, currently 1Hz)
        EndZeroTime = 0.1
        EndZerocount = int(EndZeroTime * rate)
        cathodic_amplitude = 0.5
        params1 = calc_cathodic_time(amplitude, freq, rate, points_per_channel, WaveID, cathodic_amplitude)
        CathodiccountCalculated = params1['CathodiccountCalculated']
        print('Calculated Cathodic Count:', CathodiccountCalculated)
        total_count = int((points_per_channel * num_chans) + delaycount + CathodiccountCalculated + EndZerocount) # total number of data points to output, important for timing
        ao_range = ao_info.supported_ranges[0]
        # Allocate a buffer for the scan
        memhandle = ul.win_buf_alloc(total_count)
        # Convert the memhandle to a ctypes array
        # Note: the ctypes array will no longer be valid after win_buf_free
        # is called.
        # A copy of the buffer can be created using win_buf_to_array
        # before the memory is freed. The copy can be used at any time.
        ctypes_array = cast(memhandle, POINTER(c_ushort))

        # Check if the buffer was successfully allocated
        if not memhandle:
            raise Exception('Error: Failed to allocate memory')

        add_example_data(board_num, ctypes_array, ao_range,
                                    num_chans, freq, rate, points_per_channel,
                                    amplitude, WaveID, delaycount, EndZerocount, CathodiccountCalculated, cathodic_amplitude)

        # these two lines dont completely work. shortens the negative pulse but causes a delay
        first_code = ul.from_eng_units(board_num, ao_range, 0)
        ul.a_out(board_num, 0, ao_range, first_code)
        # Start the scan
        
        for i in range(0, numwaveform): 
            ul.a_out_scan(board_num, low_chan, high_chan, total_count, rate,
                        ao_range, memhandle, ScanOptions.BACKGROUND)

            # Wait for the scan to complete
            print('Waiting for output scan to complete...', end='')
            status = Status.RUNNING
            while status != Status.IDLE:
                if ai_info.resolution <= 16:
                    # Use the a_in method for devices with a resolution <= 16
                    value = ul.a_in(board_num, 0, ai_range) # for some reason this is working for A1
                    value = ul.to_eng_units(board_num, ai_range, value)
                    value = value # negate the value to match the true output due to flipping polarity at input
                    value_list.append(value)
                sleep(1/rate)
                status, _, _ = ul.get_status(board_num, FunctionType.AOFUNCTION)
            print('')

            print('Scan completed successfully')
            with open('output_dataGUI_%d.csv' % trialnum, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['Index', 'Value'])
                for i, val in enumerate(value_list):
                    csv_writer.writerow([i, val])
    except Exception as e:
        print('\n', e)
    finally:
        if memhandle:
            # Free the buffer in a finally block to prevent a memory leak.
            ul.win_buf_free(memhandle)
        if use_device_detection:
            ul.release_daq_device(board_num)
        # plt.plot(value_list, marker='o', linestyle='-', color='b')

        # # Add labels and title
        # plt.xlabel("Index")
        # plt.ylabel("Value")
        # plt.title("Array Plot")

        # # Show grid
        # plt.grid(True)

        # # Display the plot
        # plt.show()


def add_example_data(board_num, data_array, ao_range, num_chans, freq, rate,
                     points_per_channel, amplitude, waveform_type, delaycount, EndZerocount, CathodiccountCalculated, cathodic_amplitude):

    # Fill the array with sine wave data at the calculated frequencies.
    # Note that since we are using the SCALEDATA option, the values
    # added to data_array are the actual voltage values that the device
    # will output
    data1_array = [0] * (points_per_channel)
    data_index = 0
    if waveform_type == 1:
        for point_num in range(points_per_channel): #points_per_channel,freq and rate dictate how long the output will run
    #        for channel_num in range(num_chans):
            value = -amplitude * sin(2 * pi * freq * point_num / rate) + 0
            raw_value = ul.from_eng_units(board_num, ao_range, value)
            data1_array[data_index] = value
            data_array[data_index] = raw_value
            data_index += 1
    elif waveform_type == 2:
        for point_num in range(points_per_channel):
            value = -amplitude * np.sign(sin(2 * pi * freq * point_num / rate)) + 0
            raw_value = ul.from_eng_units(board_num, ao_range, value)
            data1_array[data_index] = value
            data_array[data_index] = raw_value
            data_index += 1
    elif waveform_type == 3:
        for point_num in range(points_per_channel):
            value = -amplitude * np.arcsin(np.sin(2 * np.pi * freq * point_num / rate)) * 2 / np.pi
            raw_value = ul.from_eng_units(board_num, ao_range, value)
            data1_array[data_index] = value
            data_array[data_index] = raw_value
            data_index += 1
    elif waveform_type == 4:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(0, 1, points_per_channel)[point_num]
            raw_value = ul.from_eng_units(board_num, ao_range, value)
            data1_array[data_index] = value
            data_array[data_index] = raw_value
            data_index += 1
    elif waveform_type == 5:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(1, 0, points_per_channel)[point_num]
            data1_array[data_index] = value
            raw_value = ul.from_eng_units(board_num, ao_range, value)
            data_array[data_index] = raw_value
            data_index += 1

    for i in range(0, delaycount): # delay period, output 0v
        raw_value = ul.from_eng_units(board_num, ao_range, 0)
        data_array[data_index] = raw_value
        data_index += 1
    for i in range(0, CathodiccountCalculated): # Cathodic period, output 0v
        raw_value = ul.from_eng_units(board_num, ao_range, cathodic_amplitude)
        data_array[data_index] = raw_value
        data_index += 1
    for i in range(0, EndZerocount): # End Zero period, output 0v
        raw_value = ul.from_eng_units(board_num, ao_range, 0)
        data_array[data_index] = raw_value
        data_index += 1
    return time.time()

def calc_cathodic_time(amplitude, freq, rate, points_per_channel, WaveID, cathodic_amplitude):
    waveform_type = WaveID
    data2_array = [0] * (points_per_channel)
    data_index1 = 0
    if waveform_type == 1:
        for point_num in range(points_per_channel): #points_per_channel,freq and rate dictate how long the output will run
    #        for channel_num in range(num_chans):
            value = -amplitude * sin(2 * pi * freq * point_num / rate) + 0
            data2_array[data_index1] = value
            data_index1 += 1
    elif waveform_type == 2:
        for point_num in range(points_per_channel):
            value = -amplitude * np.sign(sin(2 * pi * freq * point_num / rate)) + 0
            data2_array[data_index1] = value
            data_index1 += 1
    elif waveform_type == 3:
        for point_num in range(points_per_channel):
            value = -amplitude * np.arcsin(np.sin(2 * np.pi * freq * point_num / rate)) * 2 / np.pi
            data2_array[data_index1] = value
            data_index1 += 1
    elif waveform_type == 4:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(0, 1, points_per_channel)[point_num]
            data2_array[data_index1] = value
            data_index1 += 1
    elif waveform_type == 5:
        for point_num in range(points_per_channel):
            value = -amplitude * np.linspace(1, 0, points_per_channel)[point_num]
            data2_array[data_index1] = value
            data_index1 += 1
    x = np.arange(points_per_channel)
    area = abs(np.trapz(data2_array, x))
    CathodiccountCalculated = int(area/cathodic_amplitude)
    print('Cathodic Count:', CathodiccountCalculated)
    print('Area under curve:', area)
    print('Rate:', rate)
    return {'CathodiccountCalculated': CathodiccountCalculated}

if __name__ == '__main__':
    run_example()
