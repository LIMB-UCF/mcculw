from tkinter import *
from tkinter import messagebox
import datetime
import os
from Test import testingIntegral
from Test import add_example_data
from TestOut import run_example
from TestOut import add_example_data

class GUI:
    WIDTH = 500
    HEIGHT = 600

    def __init__(self):
        # Initialize
        print('Initializing')
        self.trialcount = 0
        self.params = ['# trial', 'amplitude (V)','frequency (Hz)','Rate','Samples','Waveform type', 'Delay Time', 'Cathodic Time','# waves']
        self.createWindow()

    def wave_Selection(self):
        selection = "you selected the option"

    def createWindow(self):
        self.window = Tk()
        self.window.geometry('600x800')
        self.window.title('Welcome to the wrist stimulator app')

        # Frames
        self.general_frame= LabelFrame(self.window, bd = 10,   text = 'General')
        self.general_frame.pack(side = 'top', fill='x',expand=TRUE)
        self.settings_frame = LabelFrame(self.window, bd = 10, text = 'Waveform Settings')
        self.settings_frame.pack(side = 'top', fill ='x',expand = TRUE)
        self.stim_frame = LabelFrame(self.window, bd = 10, text = 'Stim Settings')
        self.stim_frame.pack(side = 'top', fill ='x',expand = TRUE)
        self.logging_frame = LabelFrame(self.window, bd=10, text = 'log file')
        self.logging_frame.pack(side='top',padx=5, pady=5, ipady=5, expand= True, fill='x')

        # Widgets
        self.amplitude_label = Label(self.settings_frame, text="Waveform amplitude (V)")
        self.amplitude_label.grid(column=0,row=3)
        self.freq_label = Label(self.settings_frame, text="Frequency (Hz)")
        self.freq_label.grid(column=3,row=3)
        self.rate_label = Label(self.settings_frame, text="Rate (samples/sec)")
        self.rate_label.grid(column=0,row=4)
        self.samples_label = Label(self.settings_frame, text="Number of samples")
        self.samples_label.grid(column=0,row=5)
        self.delay_label = Label(self.settings_frame, text="Intra-phase delay")
        self.delay_label.grid(column=0,row=6)
        self.cathodic_label = Label(self.settings_frame, text="Cathodic period time")
        self.cathodic_label.grid(column=3,row=6)
        self.numwave_label = Label(self.settings_frame, text="Number of waves")
        self.numwave_label.grid(column=3,row=4)

        self.amplitude_entry = Entry(self.settings_frame,width=10, state='normal')
        self.amplitude_entry.grid(column=1, row=3)
        self.freq_entry = Entry(self.settings_frame,width=10, state='normal')
        self.freq_entry.grid(column=4, row=3)
        self.rate_entry = Entry(self.settings_frame,width=10, state='normal')
        self.rate_entry.grid(column=1, row=4)
        self.samples_entry = Entry(self.settings_frame,width=10, state='normal')
        self.samples_entry.grid(column=1, row=5)
        self.delay_entry = Entry(self.settings_frame,width=10, state='normal')
        self.delay_entry.grid(column=1, row=6)
        self.cathodic_entry = Entry(self.settings_frame,width=10, state='normal')
        self.cathodic_entry.grid(column=4, row=6)
        self.numwave_entry = Entry(self.settings_frame,width=10, state='normal')
        self.numwave_entry.grid(column=4, row=4)

        # General Window
        self.waveSelection = IntVar()
        self.title_waveSelection = Label(self.general_frame, text="Select Stim type")
        self.title_waveSelection.grid(column=0, row=1)
        self.SineRadio = Radiobutton(self.general_frame,text='Sine', value=1, variable = self.waveSelection,  command = self.wave_Selection())
        self.SquareRadio = Radiobutton(self.general_frame,text='Square', value=2, variable = self.waveSelection, command = self.wave_Selection())
        self.triangleRadio = Radiobutton(self.general_frame,text='Triangle', value=3, variable = self.waveSelection, command = self.wave_Selection())
        self.linINCRadio = Radiobutton(self.general_frame,text='Linear Increase', value=4, variable = self.waveSelection, command = self.wave_Selection())
        self.linDECRadio = Radiobutton(self.general_frame,text='Linear Decrease', value=5, variable = self.waveSelection, command = self.wave_Selection())

        self.SineRadio.grid(column=1, row=1)
        self.SquareRadio.grid(column=2, row=1)
        self.triangleRadio.grid(column=3, row=1)
        self.linINCRadio.grid(column=4, row=1)
        self.linDECRadio.grid(column=5,row=1)
        self.general_frame.grid_columnconfigure(2, minsize=15)

        # Stim Window
        self.start_button = Button(self.stim_frame, text="Send Stimulation", command=self.start_stim)
        self.start_button.grid(column=0, row=0, padx=5, pady=5)
        self.title_trialcount = Label(self.stim_frame, text="Trial count")
        self.title_trialcount.grid(column=4, row=1)
        self.trialcount_entryvar =  StringVar(value='0')
        self.trialcount_entry = Entry( self.stim_frame, textvariable= self.trialcount_entryvar)
        self.trialcount_entry.grid(column=5, row=1)

        # initialize values
        self.amplitude_entry.insert(END,'1')
        self.freq_entry.insert(END,'1')
        self.rate_entry.insert(END,'200')
        self.samples_entry.insert(END,'100')
        self.delay_entry.insert(END,'0.1')
        self.cathodic_entry.insert(END,'0.2')
        self.numwave_entry.insert(END,'1')

        self.window.mainloop()

    def start_stim(self):
        # Get values from entries
        amplitude = int(self.amplitude_entry.get())
        frequency = int(self.freq_entry.get())
        rate = int(self.rate_entry.get())
        points_per_channel = int(self.samples_entry.get())
        delaytime = float(self.delay_entry.get())
        delaycount = int(delaytime * rate)
        CathodicTime = float(self.cathodic_entry.get())
        Cathodiccount = int(CathodicTime * rate)
        numwaveform = int(self.numwave_entry.get())
        WaveID = self.waveSelection.get()
        trialnum = self.trialcount

        # Update trial count
        self.trialcount += 1
        self.trialcount_entryvar.set(str(self.trialcount))

        # Call the function to run the example
        run_example(amplitude, frequency, rate, points_per_channel, delaycount, Cathodiccount, numwaveform, WaveID,trialnum)