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
from time import sleep

from mcculw import ul
from mcculw.enums import ScanOptions, FunctionType, Status
from mcculw.device_info import DaqDeviceInfo
from LoadWaveform import generate_waveform_dataarray

try:
    from console_examples_util import config_first_detected_device
except ImportError:
    from .console_examples_util import config_first_detected_device

import time
import csv

def run_example():
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
        chanin = 0
        low_chan = chan
        high_chan = chan
        num_chans = 1
        # rate = 100
        # points_per_channel = 1000
        # total_count = points_per_channel * num_chans # total number of data points to output, important for timing

        ao_range = ao_info.supported_ranges[0]


        # Adding variables for my own function
        time_stim = 10 # seconds to run the output
        amplitude2 = 1
        frequency = 1
        Limit = 1 * 10**6  # 1 million points per second
        points_per_channel = int(time_stim * Limit)
        rate = int(points_per_channel / time_stim)
        waveform_type = 'sine'  # 'sine' or 'square'
        total_count = points_per_channel * num_chans

        
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
                                        num_chans, rate, points_per_channel)

        #generate_waveform_dataarray(board_num, ao_range, ctypes_array, points_per_channel, rate, time_stim, amplitude2, frequency, waveform_type)

        # Start the scan
        print('Time start', time.time())
        ul.a_out_scan(board_num, low_chan, high_chan, total_count, rate,
                      ao_range, memhandle, ScanOptions.BACKGROUND)

        # Wait for the scan to complete
        print('Waiting for output scan to complete...', end='')
        status = Status.RUNNING
        print('Time read loop', time.time())
        while status != Status.IDLE:
            if ai_info.resolution <= 16:
                # Use the a_in method for devices with a resolution <= 16
                value = ul.a_in(board_num, chanin, ai_range)
                value = ul.to_eng_units(board_num, ai_range, value)
                value_list.append(value)
                #print('Time read loop', time.time())
                #print('AI Value: ', ul.to_eng_units(board_num, ai_range, value))
            # Slow down the status check so as not to flood the CPU
            sleep(1/rate)

            status, _, _ = ul.get_status(board_num, FunctionType.AOFUNCTION)
        print('')

        print('Scan completed successfully')
        print('Time end', time.time())
        # Save the data to a CSV file
        with open('output_data1.csv', 'w', newline='') as csvfile:
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


def add_example_data(board_num, data_array, ao_range, num_chans, rate,
                     points_per_channel):
    # Calculate frequencies that will work well with the size of the array

    # Calculate an amplitude and y-offset for the signal
    # to fill the analog output range
    amplitude = (ao_range.range_max - ao_range.range_min) / 2
    y_offset = (amplitude + ao_range.range_min) / 2

    # Fill the array with sine wave data at the calculated frequencies.
    # Note that since we are using the SCALEDATA option, the values
    # added to data_array are the actual voltage values that the device
    # will output
    data_index = 0
    for point_num in range(points_per_channel): #points_per_channel,freq and rate dictate how long the output will run
#        for channel_num in range(num_chans):
        freq = 1
        value = amplitude/10 * sin(2 * pi * freq * point_num / rate) + y_offset # amplitude = 10v
        raw_value = ul.from_eng_units(board_num, ao_range, value)
        data_array[data_index] = raw_value
        data_index += 1
        #print('Time write loop', time.time())
        print('Value written: ', value, 'Raw Value: ', raw_value)
        
        

    return time.time()


if __name__ == '__main__':
    run_example()
