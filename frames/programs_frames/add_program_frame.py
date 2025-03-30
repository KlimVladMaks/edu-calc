import tkinter as tk
from tkinter import ttk
from frames.base_frame import BaseFrame
from database.database import Database
from widgets.back_button import BackButton
from widgets.stages_constructor.stages_constructor import StagesConstructor


class AddProgramFrame(BaseFrame):

    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.place()

        ttk.Label(self, text="Добавить учебную программу").pack(pady=10)
        
        ttk.Label(self, text="Название программы:").pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self, width=50)
        self.name_entry.pack(pady=(0, 10))

        self.stages_constructor = StagesConstructor(self)
        self.stages_constructor.pack(pady=10)

    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()





