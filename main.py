import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class Class:
    def __init__(self, name, time, duration, importance):
        self.name = name
        self.time = time
        self.duration = duration
        self.importance = importance

class Scheduler:
    def __init__(self):
        self.classes = []

    def add_class(self, name, time, duration, importance):
        new_class = Class(name, time, duration, importance)
        self.classes.append(new_class)

    def schedule(self):
        sorted_classes = sorted(self.classes, key=lambda x: x.time)
        schedule = []
        current_day = None
        for c in sorted_classes:
            if current_day is None or c.time.date() != current_day:
                current_day = c.time.date()
                schedule.append([])
            schedule[-1].append(c)
        return schedule

    def total_hours(self):
        total_duration = timedelta()
        total_classes = len(self.classes)
        for c in self.classes:
            total_duration += c.duration
        return total_duration, total_classes

    def study_hours(self, intensity):
        study_hours = {}
        for c in self.classes:
            if c.importance not in study_hours:
                study_hours[c.importance] = timedelta()
            study_hours[c.importance] += c.duration
        total_study_hours = sum(study_hours.values(), timedelta())
        for k, v in study_hours.items():
            study_hours[k] = v / total_study_hours * intensity
        return study_hours

class ScheduleGUI:
    def __init__(self):
        self.scheduler = Scheduler()
        self.window = tk.Tk()
        self.window.title("Class Scheduler")
        self.create_widgets()

    def create_widgets(self):
        # Class input
        class_frame = ttk.LabelFrame(self.window, text="Add Class")
        class_frame.grid(column=0, row=0, padx=10, pady=5)

        name_label = ttk.Label(class_frame, text="Name:")
        name_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
        self.name_entry = ttk.Entry(class_frame)
        self.name_entry.grid(column=1, row=0, padx=5, pady=5)

        time_label = ttk.Label(class_frame, text="Time (YYYY-MM-DD HH:MM):")
        time_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
        self.time_entry = ttk.Entry(class_frame)
        self.time_entry.grid(column=1, row=1, padx=5, pady=5)

        duration_label = ttk.Label(class_frame, text="Duration (HH:MM):")
        duration_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
        self.duration_entry = ttk.Entry(class_frame)
        self.duration_entry.grid(column=1, row=2, padx=5, pady=5)

        importance_label = ttk.Label(class_frame, text="Importance:")
        importance_label.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
        self.importance_var = tk.StringVar(self.window)
        self.importance_var.set("Low")
        self.importance_dropdown = ttk.OptionMenu(class_frame, self.importance_var, "Low", "Medium", "High")
        self.importance_dropdown.grid(column=1, row=3, padx=5, pady=5)

        add_button = ttk.Button(class_frame, text="Add Class", command=self.add_class)
        add_button.grid(column=1, row=4, padx=5, pady=5)

        # Schedule output
        schedule_frame = ttk.LabelFrame(self.window, text="Schedule")
        schedule_frame.grid(column=0, row=1, padx=10, pady=5)

        schedule_button = ttk.Button(schedule_frame, text="Generate Schedule", command=self.generate_schedule)
        schedule_button.grid(column=0, row=0, padx=5, pady=5)

        total_hours_label = ttk.Label(schedule_frame, text="Total Class Hours:")
        total_hours_label.grid(column=0, row=1, padx=5, pady=5)
        self.total_hours_var = tk.StringVar(self.window)
        self.total_hours_var.set("")
        total_hours_output = ttk.Label(schedule_frame, textvariable=self.total_hours_var)
        total_hours_output.grid(column=1, row=1, padx=5, pady=5)

        study_intensity_label = ttk.Label(schedule_frame, text="Selected Study Intensity:")
        study_intensity_label.grid(column=0, row=2, padx=5, pady=5)
        self.study_intensity_var = tk.StringVar(self.window)
        self.study_intensity_var.set("Low")
        study_intensity_dropdown = ttk.OptionMenu(schedule_frame, self.study_intensity_var, "Low", "Medium", "High")
        study_intensity_dropdown.grid(column=1, row=2, padx=5, pady=5)

        study_hours_button = ttk.Button(schedule_frame, text="Calculate Study Hours", command=self.calculate_study_hours)
        study_hours_button.grid(column=0, row=3, padx=5, pady=5)
        self.study_hours_var = tk.StringVar(self.window)
        self.study_hours_var.set("")
        study_hours_output = ttk.Label(schedule_frame, textvariable=self.study_hours_var)
        study_hours_output.grid(column=1, row=3, padx=5, pady=5)

    def add_class(self):
        name = self.name_entry.get()
        time_str = self.time_entry.get()
        duration_str = self.duration_entry.get()
        importance = self.importance_var.get()
        try:
            time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
            duration = timedelta(hours=int(duration_str.split(":")[0]), minutes=int(duration_str.split(":")[1]))
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input")
            return
        self.scheduler.add_class(name, time, duration, importance)
        self.name_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)

    def generate_schedule(self):
        schedule = self.scheduler.schedule()
        schedule_str = ""
        for i, day in enumerate(schedule):
            day_str = f"Day {i+1}:\n"
            for c in day:
                day_str += f"{c.name} at {c.time.strftime('%H:%M')} for {c.duration.seconds//3600} hours\n"
            schedule_str += day_str + "\n"
        self.total_hours_var.set(str(self.scheduler.total_hours()[1]) + " classes, " + str(self.scheduler.total_hours()[0].seconds//3600) + " hours")
        tk.messagebox.showinfo("Schedule", schedule_str)

    def calculate_study_hours(self):
        intensity = {"Low": 1, "Medium": 2, "High": 3}[self.study_intensity_var.get()]
        study_hours = self.scheduler.study_hours(intensity)
        study_hours_str = ""
        for k, v in study_hours.items():
            study_hours_str += f"{k}: {v.seconds//3600} hours\n"
        self.study_hours_var.set(study_hours_str)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ScheduleGUI()
    gui.run()
