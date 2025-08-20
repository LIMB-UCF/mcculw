import numpy as np

def waveform_parameters_func(waveform_number, stimtime, repetitions):
    match waveform_number:
        case 1:
            if stimtime == 100:
                return {
                    'frequency': 5000,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in
                }
            elif stimtime == 300:
                return {
                    'frequency': 1667,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 300,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 400:
                return {
                    'frequency': 1250,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 400,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 600:
                return {
                    'frequency': 833.4,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 600,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 900:
                return {
                    'frequency': 555.5,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 900,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
        case 2:
            if stimtime == 100:
                return {
                    'frequency': 5000,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 2,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in
                }
            elif stimtime == 300:
                return {
                    'frequency': 1667,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 300,  # Number of points per channel
                    'waveform_type': 2,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 400:
                return {
                    'frequency': 1250,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 400,  # Number of points per channel
                    'waveform_type': 2,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 600:
                return {
                    'frequency': 833.4,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 600,  # Number of points per channel
                    'waveform_type': 2,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 900:
                return {
                    'frequency': 555.5,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 900,  # Number of points per channel
                    'waveform_type': 2,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
        case 3:
            if stimtime == 100:
                return {
                    'frequency': 5000,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 3,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in
                }
            elif stimtime == 300:
                return {
                    'frequency': 1667,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 300,  # Number of points per channel
                    'waveform_type': 3,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 400:
                return {
                    'frequency': 1250,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 400,  # Number of points per channel
                    'waveform_type': 3,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 600:
                return {
                    'frequency': 833.4,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 600,  # Number of points per channel
                    'waveform_type': 3,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 900:
                return {
                    'frequency': 555.5,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 900,  # Number of points per channel
                    'waveform_type': 3,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
        case 4:
            if stimtime == 100:
                return {
                    'frequency': 5000,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 4,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in
                }
            elif stimtime == 300:
                return {
                    'frequency': 1667,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 300,  # Number of points per channel
                    'waveform_type': 4,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 400:
                return {
                    'frequency': 1250,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 400,  # Number of points per channel
                    'waveform_type': 4,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 600:
                return {
                    'frequency': 833.4,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 600,  # Number of points per channel
                    'waveform_type': 4,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 900:
                return {
                    'frequency': 555.5,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 900,  # Number of points per channel
                    'waveform_type': 4,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
        case 5:
            if stimtime == 100:
                return {
                    'frequency': 5000,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 5,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in
                }
            elif stimtime == 300:
                return {
                    'frequency': 1667,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 300,  # Number of points per channel
                    'waveform_type': 5,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 400:
                return {
                    'frequency': 1250,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 400,  # Number of points per channel
                    'waveform_type': 5,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 600:
                return {
                    'frequency': 833.4,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 600,  # Number of points per channel
                    'waveform_type': 5,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
            elif stimtime == 900:
                return {
                    'frequency': 555.5,  # Frequency in Hz
                    'rate': 1000000,  # Samples per second
                    'points_per_channel': 900,  # Number of points per channel
                    'waveform_type': 5,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.0001,  # Delay time in seconds
                    'cathodic_time': 0.0002  # Cathodic time in seconds
                }
        case 6: # for testing purposes only
                return {
                    'frequency': 1,  # Frequency in Hz
                    'rate': 200,  # Samples per second
                    'points_per_channel': 100,  # Number of points per channel
                    'waveform_type': 1,  # Sine wave
                    'number_of_waveforms': repetitions,  # Number of waveforms
                    'delay_time': 0.1,  # Delay time in seconds
                    'cathodic_time': 0.2  # Cathodic time in seconds
                }