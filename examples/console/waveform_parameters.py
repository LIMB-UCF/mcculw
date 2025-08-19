import numpy as np

def waveform_parameters_func(waveform_number):
    match waveform_number:
        case 1:
            return {
                'frequency': 5000,  # Frequency in Hz
                'rate': 1000000,  # Samples per second
                'points_per_channel': 100,  # Number of points per channel
                'waveform_type': 1,  # Sine wave
                'number_of_waveforms': 1,  # Number of waveforms
                'delay_time': 0.0001,  # Delay time in seconds
                'cathodic_time': 0.0002  # Cathodic time in
            }
        case 2:
            return {
                'frequency': 5000,  # Frequency in Hz
                'rate': 1000000,  # Samples per second
                'points_per_channel': 100,  # Number of points per channel
                'waveform_type': 2,  # Square wave
                'number_of_waveforms': 1,  # Number of waveforms
                'delay_time': 0.0001,  # Delay time in seconds
                'cathodic_time': 0.0002  # Cathodic time in seconds
            }
        case 3:
            return {
                'frequency': 5000,  # Frequency in Hz
                'rate': 1000000,  # Samples per second
                'points_per_channel': 100,  # Number of points per channel
                'waveform_type': 3,  # Triangle wave
                'number_of_waveforms': 1,  # Number of waveforms
                'delay_time': 0.0001,  # Delay time in seconds
                'cathodic_time': 0.0002  # Cathodic time in seconds
            }
        case 4:
            return {
                'frequency': 5000,  # Frequency in Hz
                'rate': 1000000,  # Samples per second
                'points_per_channel': 100,  # Number of points per channel
                'waveform_type': 4,  # Ramp up wave
                'number_of_waveforms': 1,  # Number of waveforms
                'delay_time': 0.0001,  # Delay time in seconds
                'cathodic_time': 0.0002  # Cathodic time in seconds
            }
        case 5:
            return {
                'frequency': 5000,  # Frequency in Hz
                'rate': 1000000,  # Samples per second
                'points_per_channel': 100,  # Number of points per channel
                'waveform_type': 5,  # Ramp down wave
                'number_of_waveforms': 1,  # Number of waveforms
                'delay_time': 0.0001,  # Delay time in seconds
                'cathodic_time': 0.0002  # Cathodic time in seconds
            }