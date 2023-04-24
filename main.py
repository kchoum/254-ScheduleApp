import tkinter as tk
from tkinter import ttk
import datetime
import numpy as np
import matplotlib.pyplot as plt
import customtkinter

# Define custom tkinter theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Student Info Screen Functionality***********************************
# create a Tkinter window
inputwindow = customtkinter.CTk()
inputwindow.title("User Info")

# Define input frame
inputframe = customtkinter.CTkFrame(master=inputwindow)
inputframe.pack(fill="both", expand=True)

# create student entry fields
customtkinter.CTkLabel(master=inputframe,
text="Student Name",
font=("Roboto", 12)).grid(row=0, column=0)
name_entry = customtkinter.CTkEntry(master=inputframe, placeholder_text="Student Name")
name_entry.grid(row=0, column=1, sticky="W")

# create intensity entry dropdown
def optionmenu_callback(choice):
print("optionmenu dropdown clicked:", choice)

customtkinter.CTkLabel(master=inputframe,
text="Study Intensity",
font=("Roboto", 12)).grid(row=1, column=0)
optionmenu_var = customtkinter.StringVar(value="low")
level_entry = customtkinter.CTkOptionMenu(master=inputframe,
values=["low", "medium", "high"],
command=optionmenu_callback, variable=optionmenu_var)
level_entry.grid(row=1, column=1, sticky="W")

# create daily hours entry
customtkinter.CTkLabel(master=inputframe, text="Monday Hours", font=("Roboto", 12)).grid(row=2, column=0)
mon_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
mon_entry.grid(row=2, column=1)

customtkinter.CTkLabel(master=inputframe, text="Tuesday Hours", font=("Roboto", 12)).grid(row=3, column=0)
tues_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
tues_entry.grid(row=3, column=1)

customtkinter.CTkLabel(master=inputframe, text="Wednesday Hours", font=("Roboto", 12)).grid(row=4, column=0)
weds_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
weds_entry.grid(row=4, column=1)

customtkinter.CTkLabel(master=inputframe, text="Thursday Hours", font=("Roboto", 12)).grid(row=5, column=0)
thurs_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
thurs_entry.grid(row=5, column=1)

customtkinter.CTkLabel(master=inputframe, text="Friday Hours", font=("Roboto", 12)).grid(row=6, column=0)
fri_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
fri_entry.grid(row=6, column=1)

customtkinter.CTkLabel(master=inputframe, text="Saturday Hours", font=("Roboto", 12)).grid(row=7, column=0)
sat_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
sat_entry.grid(row=7, column=1)

customtkinter.CTkLabel(master=inputframe, text="Sunday Hours", font=("Roboto", 12)).grid(row=8, column=0)
sun_entry = customtkinter.CTkTextbox(master=inputframe, width=500, height=50)
sun_entry.grid(row=8, column=1)

# get the information from the entry fields
name = name_entry.get()

def VectorizeInputStream(time_intervals_str):
    time_intervals_list = time_intervals_str.replace("(", "").replace(")", "").split(", ")
    vectorized_time_intervals = np.empty((len(time_intervals_list), 2), dtype=int)

    for i, interval in enumerate(time_intervals_list):
        start_time_str, end_time_str = interval.split("-")
        start_time = int(start_time_str)
        end_time = int(end_time_str)
        vectorized_time_intervals[i] = [start_time, end_time]

    return vectorized_time_intervals

def VisualizeTimes(army_time_intervals):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 1)
    ax.set_yticks([])

    for interval in army_time_intervals:
        start_time, end_time = interval
        ax.hlines(y=0.5, xmin=start_time, xmax=end_time, linewidth=10)

    ax.set_xlim(0, 2400)
    xtick_values = np.arange(0, 2500, 100)
    xtick_labels = [f"{x:04d}" for x in xtick_values]
    ax.set_xticks(xtick_values)
    ax.set_xticklabels(xtick_labels)

    ax.set_xlabel("Time (Military format)")
    ax.set_title("Army Time Intervals")

    plt.show()

def input():
    print(name_entry.get())
    MonTimeVector = VectorizeInputStream(mon_entry.get("1.0",'end-1c'))
    VisualizeTimes(MonTimeVector)

# create a button to submit the form
submit_button = customtkinter.CTkButton(inputframe, text="Calculate", command=input)
submit_button.grid(row=10, column=1, sticky="W")

#run main window loop
inputwindow.geometry("700x500")
inputwindow.mainloop()
