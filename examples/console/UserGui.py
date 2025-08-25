from tkinter import *
from tkinter import messagebox
from customtkinter import CTk, CTkLabel, CTkButton, set_appearance_mode, CTkImage
import customtkinter
import datetime
import os
from PIL import Image
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
        self.window = CTk()
        self.window.geometry('600x800')
        set_appearance_mode("dark")
        CTkLabel(master=self.window, text="Press this button when you experience stimulation", font=("Arial Bold", 20), text_color="#FFFFFF").pack(anchor="nw", padx=(50,0))
        CTkButton(master=self.window, text="This is the button!!!! :-)", font=("Arial Bold", 20), command = self.show_hand, hover_color="#299039", fg_color="#35B248").pack(fill="x", ipady=15, pady=(50, 0), padx=50)

        self.movies_img_data = Image.open("examples/console/Ucf-Logo-PNG-Pic.png")
        self.movies_img = CTkImage(light_image=self.movies_img_data, dark_image=self.movies_img_data, size=(234,234))
        CTkLabel(master=self.window, text="", image=self.movies_img,corner_radius=8).pack(fill="x", ipady=25, pady=(75, 0), padx=75)

        self.LIMB_data = Image.open("examples/console/LIMB-logo.png")
        self.LIMB_img = CTkImage(light_image=self.LIMB_data, dark_image=self.LIMB_data, size=(184,234))
        CTkLabel(master=self.window, text="", image=self.LIMB_img,corner_radius=8).pack(fill="x", ipady=25, pady=(75, 0), padx=75)
        self.after_id = self.window.after(3000, self.sendwaveformincrease)

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
            run_example(self.amplitude, freq, rate, points_per_channel, delaycount, numwaveform, WaveID, self.trialnum)
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
            run_example(self.amplitude, freq, rate, points_per_channel, delaycount, numwaveform, WaveID, self.trialnum)
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
        run_example(self.amplitude, freq, rate, points_per_channel, delaycount, numwaveform, WaveID, self.trialnum)
        self.after_id = self.window.after(3000, self.sendwaveformincrease)