from tkinter import *
from tkinter import messagebox
import datetime
import os
from Test import testingIntegral
from Test import add_example_data
from TestOut import run_example
from HandGUI import draw_on_image_and_save
from waveform_parameters import waveform_parameters_func
import time


class UserGUI:
    WIDTH = 500
    HEIGHT = 600
    def __init__(self):
        # Initialize
        print('Initializing')
        self.amplitude = 0
        self.trialnum = 0
        self.waveform_number = 6 # used for waveform_parameters_func
        self.stimtime = 900 #microseconds
        self.repetitions = 1 # 1 or 15
        self.current_report = 0
        self.last_report = 0
        #self.params = ['# trial', 'amplitude (V)','frequency (Hz)','Rate','Samples','Waveform type', 'Delay Time', 'Cathodic Time','# waves']
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

        # Text in Frame
        self.buttontextlabel = Label(self.general_frame, text = "Please press this button when you experience sensation!")
        self.buttontextlabel.grid(column=0,row=0)
        self.detectionbutton = Button(self.general_frame, text='button :-)', command=self.show_hand)
        self.detectionbutton.grid(column=0,row=1, padx=5,pady=5)
        self.exitbuttonlabel = Label(self.general_frame, text = "Press this button to exit the app")
        self.exitbuttonlabel.grid(column=0,row=2)
        self.exitbutton = Button(self.general_frame, text='Exit', command=self.window.quit)
        self.exitbutton.grid(column=0,row=3, padx=5,pady=5)

        #wait x seconds then send another waveform
        self.after_id = self.window.after(3000, self.sendwaveformincrease)

        #keeps window up, keep at end of this function
        self.window.mainloop()

    def show_hand(self):
        if self.after_id is not None:
            self.window.after_cancel(self.after_id)
            self.after_id = None
            print("Waveform loop ended!")
        self.current_report = 1
        draw_on_image_and_save('output_hand_model', 1, self.amplitude, self.trialnum)
        if self.last_report == 1:
            self.after_id = self.window.after(3000, self.sendwaveformdecrease)
        elif self.last_report == 0 and self.current_report == 1:
            self.after_id = self.window.after(3000, self.sendwaveformNoChange)
        else:
            self.after_id = self.window.after(3000, self.sendwaveformincrease)

    def sendwaveformincrease(self):
        params = waveform_parameters_func(self.waveform_number, self.stimtime, self.repetitions)
        self.last_report = self.current_report
        self.current_report = 0
        self.amplitude += 1
        self.trialnum +=1
        if self.amplitude > 8:
            messagebox.showinfo("Warning", "Amplitude is too high, resetting to 0")
            self.amplitude = 0
            self.sendwaveformincrease()
        else:
            freq = params['frequency']
            rate = params['rate']
            points_per_channel = params['points_per_channel']
            numwaveform = params['number_of_waveforms']
            WaveID = params['waveform_type']
            delaytime = params['delay_time']
            delaycount = int(delaytime * rate)
            Cathodictime = params['cathodic_time']
            Cathodiccount = int(Cathodictime * rate)
            run_example(self.amplitude, freq, rate, points_per_channel, delaycount, Cathodiccount, numwaveform, WaveID,self.trialnum)
            self.after_id = self.window.after(3000, self.sendwaveformincrease)

    def sendwaveformdecrease(self):
        params = waveform_parameters_func(self.waveform_number, self.stimtime, self.repetitions)
        self.last_report = self.current_report
        self.current_report = 0
        self.amplitude -= 1
        self.trialnum +=1
        if self.amplitude < 0:
            messagebox.showinfo("Warning", "Amplitude is too low, resetting to 0 and increasing")
            self.amplitude = 0
            self.sendwaveformincrease()
        else:
            freq = params['frequency']
            rate = params['rate']
            points_per_channel = params['points_per_channel']
            numwaveform = params['number_of_waveforms']
            WaveID = params['waveform_type']
            delaytime = params['delay_time']
            delaycount = int(delaytime * rate)
            Cathodictime = params['cathodic_time']
            Cathodiccount = int(Cathodictime * rate)
            run_example(self.amplitude, freq, rate, points_per_channel, delaycount, Cathodiccount, numwaveform, WaveID,self.trialnum)
            self.after_id = self.window.after(3000, self.sendwaveformincrease)


    def sendwaveformNoChange(self):
        params = waveform_parameters_func(self.waveform_number, self.stimtime, self.repetitions)
        self.last_report = self.current_report
        self.current_report = 0
        self.trialnum +=1
        freq = params['frequency']
        rate = params['rate']
        points_per_channel = params['points_per_channel']
        numwaveform = params['number_of_waveforms']
        WaveID = params['waveform_type']
        delaytime = params['delay_time']
        delaycount = int(delaytime * rate)
        Cathodictime = params['cathodic_time']
        Cathodiccount = int(Cathodictime * rate)
        run_example(self.amplitude, freq, rate, points_per_channel, delaycount, Cathodiccount, numwaveform, WaveID,self.trialnum)
        self.after_id = self.window.after(3000, self.sendwaveformincrease)