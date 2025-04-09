import tkinter as tk
from tkinter import ttk
from frames.base_frame import BaseFrame
from database.database import Database
from widgets.back_button import BackButton


class AddCalendarFrame(BaseFrame):

    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.place()

        ttk.Label(self, text="Добавить производственный календарь").pack(pady=10)

        ttk.Label(self, text="Название:").pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self, width=50)
        self.name_entry.pack(pady=(0, 10))

        self.input_duration_frame = ttk.Frame(self)
        self.input_duration_frame.pack(pady=10)

        self.start_date_label = ttk.Label(self.input_duration_frame, text="Дата начала:")
        self.start_date_label.grid(row=0, column=0, padx=10)
        self.end_date_label = ttk.Label(self.input_duration_frame, text="Дата окончания:")
        self.end_date_label.grid(row=0, column=1, padx=10)

        self.start_date_entry = ttk.Entry(self.input_duration_frame)
        self.start_date_entry.grid(row=1, column=0, padx=10)
        self.end_date_entry = ttk.Entry(self.input_duration_frame)
        self.end_date_entry.grid(row=1, column=1, padx=10)

        self.days_off_label = ttk.Label(self, text="Даты нерабочих дней")
        self.days_off_label.pack(pady=(10, 0))
        self.days_off_entry = tk.Text(self, width=50, height=7)
        self.days_off_entry.pack(pady=(0, 10))

        ttk.Button(self, text="Сохранить производственный календарь", command=self.save_calendar).pack(pady=10)
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()

    def save_calendar(self):
        name = self.name_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        days_off_text = self.days_off_entry.get("1.0", tk.END)
        days_off_list = [line.strip() for line in days_off_text.splitlines() if line.strip()]
        new_calendar_data = [name, start_date, end_date, days_off_list]
        self.db.calendars.add_new_calendar(new_calendar_data)
        self.parent_frame.update_table()
        self.go_back()






