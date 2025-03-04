import tkinter as tk
from tkinter import ttk
from frames.BaseFrame import BaseFrame
from database.Database import Database
from widgets.BackButton import BackButton
from widgets.Table import Table


class EduTypesFrame(BaseFrame):
    """
    Фрейм для работы с видами обучения.
    """
    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.pack()
    
        ttk.Label(self, text="Виды обучения").pack(pady=10)
        self.create_table()
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()
    
    def create_table(self):
        columns = [
            ("Вид обучения", 300)
        ]
        self.table = Table(self, columns)
        table_rows = self.get_table_rows()
        self.table.add_rows(table_rows)
        self.table.pack()
    
    def get_table_rows(self):
        table_rows = []
        for edu_type in self.db.edu_types.get_all():
            table_rows.append([edu_type])
        return table_rows
    