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

        self.canvas = tk.Canvas(self, highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((150, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        ttk.Label(self.scrollable_frame, text="Добавить учебную программу").pack(pady=10)
        
        ttk.Label(self.scrollable_frame, text="Название программы:").pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self.scrollable_frame, width=50)
        self.name_entry.pack(pady=(0, 10))

        self.stages_constructor = StagesConstructor(self.scrollable_frame)
        self.stages_constructor.pack(pady=10)

        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)
    
    def on_mouse_wheel(self, event):
        start, end = self.scrollbar.get()
        if (start > 0.0) or (end < 1.0):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def go_back(self):
        self.back_button.destroy()
        self.canvas.unbind_all("<MouseWheel>")
        self.destroy()
        self.parent_frame.display_frame()
    






