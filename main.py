import customtkinter
import numpy as np
import matplotlib.pyplot as plt

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

# Add event handlers for clicking to select or deselect a rectangle
def select_rectangle(event, canvas):
    item = canvas.find_closest(event.x, event.y)[0]
    if canvas.itemcget(item, "fill") == "gray":
        canvas.itemconfig(item, fill="dark blue")
    else:
        canvas.itemconfig(item, fill="gray")

def get_selected_time_ranges():
    selected_ranges = []
    start_time = None
    for rectangle in rectangles:
        if canvas.itemcget(rectangle, "fill") == "dark blue":
            if start_time is None:
                start_time = rectangles[rectangle]
        else:
            if start_time is not None:
                end_time = rectangles[rectangle-1]
                selected_ranges.append((start_time, end_time))
                start_time = None
    if start_time is not None:
        end_time = rectangles[rectangle]
        selected_ranges.append((start_time, end_time))
    return selected_ranges

# Add a button to submit the selected times
def submit():
    selected_ranges = get_selected_time_ranges()
    print("Selected time ranges:", selected_ranges)
    # VisualizeTimes(selected_ranges)

submit_button = customtkinter.CTkButton(inputframe, text="Submit", command=submit)
submit_button.grid(row=17, column=2, sticky="W")

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

# Create time labels for each day of the week
mon_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
mon_label_canvas.grid(row=3, column=1, sticky="W")
tue_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
tue_label_canvas.grid(row=5, column=1, sticky="W")
wed_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
wed_label_canvas.grid(row=7, column=1, sticky="W")
thu_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
thu_label_canvas.grid(row=9, column=1, sticky="W")
fri_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
fri_label_canvas.grid(row=11, column=1, sticky="W")
sat_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
sat_label_canvas.grid(row=13, column=1, sticky="W")
sun_label_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=30, background="dark gray", highlightthickness=0)
sun_label_canvas.grid(row=15, column=1, sticky="W")

# Create a canvas to hold the time slots for each day of the week
# Monday
customtkinter.CTkLabel(master=inputframe, text="Mon", font=("Roboto", 12)).grid(row=4, column=0)
mon_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
mon_widget_canvas.grid(row=4, column=1, sticky="W")
# Tuesday
customtkinter.CTkLabel(master=inputframe, text="Tue", font=("Roboto", 12)).grid(row=6, column=0)
tue_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
tue_widget_canvas.grid(row=6, column=1, sticky="W")
# Wednesday
customtkinter.CTkLabel(master=inputframe, text="Wed", font=("Roboto", 12)).grid(row=8, column=0)
wed_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
wed_widget_canvas.grid(row=8, column=1, sticky="W")
# Thursday
customtkinter.CTkLabel(master=inputframe, text="Thu", font=("Roboto", 12)).grid(row=10, column=0)
thu_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
thu_widget_canvas.grid(row=10, column=1, sticky="W")
# Friday
customtkinter.CTkLabel(master=inputframe, text="Fri", font=("Roboto", 12)).grid(row=12, column=0)
fri_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
fri_widget_canvas.grid(row=12, column=1, sticky="W")
# Saturday
customtkinter.CTkLabel(master=inputframe, text="Sat", font=("Roboto", 12)).grid(row=14, column=0)
sat_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
sat_widget_canvas.grid(row=14, column=1, sticky="W")
# Sunday
customtkinter.CTkLabel(master=inputframe, text="Sun", font=("Roboto", 12)).grid(row=16, column=0)
sun_widget_canvas = customtkinter.CTkCanvas(inputframe, width=960, height=25, highlightbackground="black")
sun_widget_canvas.grid(row=16, column=1, sticky="W")

# Define the available time slots
times = []
for hour in range(0, 24):
    for minute in range(0, 60, 15):
        times.append(f"{hour:02}{minute:02}")

# Create a rectangle for each time slot
rectangles = {}
for i, time in enumerate(times):
    x0 = i * 10
    y0 = 0
    x1 = (i + 1) * 10
    y1 = 25
    mon_rectangle = mon_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[mon_rectangle] = time
    tue_rectangle = tue_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[tue_rectangle] = time
    wed_rectangle = wed_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[wed_rectangle] = time
    thu_rectangle = thu_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[thu_rectangle] = time
    fri_rectangle = fri_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[fri_rectangle] = time
    sat_rectangle = sat_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[sat_rectangle] = time
    sun_rectangle = sun_widget_canvas.create_rectangle(x0, y0, x1, y1, fill="gray", outline="black")
    rectangles[sun_rectangle] = time

    # Label every 4th rectangle
    labelcanvases = [mon_label_canvas, tue_label_canvas, wed_label_canvas, thu_label_canvas, fri_label_canvas, sat_label_canvas, sun_label_canvas]
    for labelcanvas in labelcanvases:
        if i % 4 == 0:
            labelcanvas.create_text((i + 0.5) * 10, 5, text=f"{i // 4}\n|", anchor="n")

# Handle button presses
mon_widget_canvas.bind("<Button-1>",lambda event, arg=mon_widget_canvas: select_rectangle(event, arg))
tue_widget_canvas.bind("<Button-1>",lambda event, arg=tue_widget_canvas: select_rectangle(event, arg))
wed_widget_canvas.bind("<Button-1>",lambda event, arg=wed_widget_canvas: select_rectangle(event, arg))
thu_widget_canvas.bind("<Button-1>",lambda event, arg=thu_widget_canvas: select_rectangle(event, arg))
fri_widget_canvas.bind("<Button-1>",lambda event, arg=fri_widget_canvas: select_rectangle(event, arg))
sat_widget_canvas.bind("<Button-1>",lambda event, arg=sat_widget_canvas: select_rectangle(event, arg))
sun_widget_canvas.bind("<Button-1>",lambda event, arg=sun_widget_canvas: select_rectangle(event, arg))

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
    # print(name_entry.get())
    # MonTimeVector = VectorizeInputStream(mon_entry.get("1.0",'end-1c'))
    VisualizeTimes(MonTimeVector)

# create a button to submit the form
submit_button = customtkinter.CTkButton(inputframe, text="Calculate", command=input)
submit_button.grid(row=17, column=1, sticky="W")

#run main window loop
inputwindow.geometry("1400x700")
inputwindow.mainloop()