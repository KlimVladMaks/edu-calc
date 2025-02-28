import tkinter as tk
from tkinter import ttk
from frames.BaseFrame import BaseFrame
from widgets.Table import Table
from database.Database import Database
from widgets.BackButton import BackButton

class ProgramsFrame(BaseFrame):
    """
    Фрейм для работы с учебными программами.
    """
    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        ttk.Label(self, text="Учебные программы").pack(pady=10)
        self.create_table()
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()
    
    def create_table(self):
        columns = [
            ["Название", 150],
            ["Всего дней", 100]
        ]
        unique_stages_names = self.db.programs.get_unique_stages_names()
        for stage_name in unique_stages_names:
            column = []
            column.append(stage_name)
            column.append(100)
            columns.append(column)
        self.table = Table(self, columns)

        table_rows = []
        programs_names = self.db.programs.get_all_programs_names()
        for program_name in programs_names:
            table_row = []
            table_row.append(program_name)
            total_days = self.db.programs.get_total_days(program_name)
            table_row.append(total_days)
            for stage_name in unique_stages_names:
                number_of_days = self.db.programs.get_number_of_days_for_stage(program_name, stage_name)
                table_row.append(number_of_days)

            table_rows.append(table_row)

        self.table.add_rows(table_rows)

        self.table.pack()
