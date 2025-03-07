import tkinter as tk
from tkinter import ttk
from frames.BaseFrame import BaseFrame
from database.Database import Database
from widgets.BackButton import BackButton
from widgets.Calculator import Calculator


class EditGroupFrame(BaseFrame):
    """
    Фрейм для изменения данный учебной группы.
    """
    def __init__(self, master, parent_frame, old_group_data):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.old_group_data = old_group_data
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)

        ttk.Label(self, text="Изменить данные учебной группы").pack(pady=10)

        ttk.Label(self, text="Название:").pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self, width=50)
        self.name_entry.insert(0, self.old_group_data[0])
        self.name_entry.pack(pady=(0, 10))

        self.comboboxes_frame = ttk.Frame(self)
        self.comboboxes_frame.pack(pady=10)

        ttk.Label(self.comboboxes_frame, text="Выберите календарь:").grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(self.comboboxes_frame, text="Выберите программу:").grid(row=0, column=1, padx=10, pady=5)

        self.calendars_names = self.get_calendars_names()
        self.programs_names = self.get_programs_names()

        self.calendar_combobox = ttk.Combobox(self.comboboxes_frame,
                                              values=self.calendars_names,
                                              state="readonly")
        self.calendar_combobox.set(self.old_group_data[1])
        self.calendar_combobox.grid(row=1, column=0, padx=10)
        self.calendar_combobox.bind("<<ComboboxSelected>>", self.update_labels)
        self.program_combobox = ttk.Combobox(self.comboboxes_frame,
                                             values=self.programs_names,
                                             state="readonly")
        self.program_combobox.set(self.old_group_data[2])
        self.program_combobox.grid(row=1, column=1, padx=10)
        self.program_combobox.bind("<<ComboboxSelected>>", self.update_labels)

        ttk.Label(self, text="Дата начала обучения:").pack(pady=(10, 0))
        self.start_date_entry = ttk.Entry(self)
        self.start_date_entry.insert(0, self.old_group_data[3])
        self.start_date_entry.pack(pady=(0, 10))
        self.start_date_entry.bind("<KeyRelease>", self.update_labels)

        self.total_days_label = ttk.Label(self, text="Обучение займёт (дней): -")
        self.total_days_label.pack(pady=10)
        self.end_date_label = ttk.Label(self, text="Дата окончания обучения: -")
        self.end_date_label.pack(pady=10)
        self.update_labels()

        ttk.Button(self, text="Обновить учебную группу", command=self.update_group).pack(pady=10)
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()
    
    def get_calendars_names(self):
        calendars_names = []
        calendars_data = self.db.calendars.get_all()
        for data in calendars_data:
            calendars_names.append(data[0])
        return calendars_names

    def get_programs_names(self):
        programs_names = []
        programs_data = self.db.programs.get_all()
        for data in programs_data:
            programs_names.append(data[0])
        return programs_names
    
    def update_labels(self, event=None):
        try:
            calendar_name = self.calendar_combobox.get()
            program_name = self.program_combobox.get()
            start_date = str(self.start_date_entry.get())
            if (calendar_name == "") or (program_name == ""):
                return
            end_date = Calculator.calculate_end_date(calendar_name, program_name, start_date)
            total_days = Calculator.count_days_between_dates(start_date, end_date)
            self.total_days_label.config(text=f"Обучение займёт (дней): {total_days}")
            self.end_date_label.config(text=f"Дата окончания обучения: {end_date}")
        except:
            self.total_days_label.config(text="Обучение займёт (дней): -")
            self.end_date_label.config(text="Дата окончания обучения: -")
    
    def update_group(self):
        updated_group_data = []

        name = str(self.name_entry.get())
        calendar = str(self.calendar_combobox.get())
        program = str(self.program_combobox.get())
        start_date = str(self.start_date_entry.get())

        updated_group_data.append(name)
        updated_group_data.append(calendar)
        updated_group_data.append(program)
        updated_group_data.append(start_date)

        group_id = (self.old_group_data[0], self.old_group_data[1], self.old_group_data[2])
        self.db.groups.update(group_id, updated_group_data)

        self.parent_frame.update()
        self.go_back()
