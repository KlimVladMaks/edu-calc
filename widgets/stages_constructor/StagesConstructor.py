import tkinter as tk
from tkinter import ttk
from widgets.stages_constructor.StageInput import StageInput


class StagesConstructor:
    """
    Конструктор этапов учебной программы.
    """
    def __init__(self, main_frame, canvas):
        self.main_frame = main_frame
        self.canvas = canvas
        self.sc_frame = ttk.Frame(main_frame)
        self.stages_list = []
        self.add_stage_button = ttk.Button()
        self.add_new_stage()
    
    def pack(self):
        self.sc_frame.pack(pady=10)
    
    def add_new_stage(self):
        self.add_stage_button.destroy()

        index = len(self.stages_list)
        new_stage = StageInput(self.sc_frame,
                               index, self.move_stage_up,
                               self.move_stage_down,
                               self.delete_stage, "", -1)
        new_stage.pack()
        self.stages_list.append(new_stage)

        self.add_stage_button = ttk.Button(self.sc_frame,
                                           text="+ Добавить этап",
                                           command=self.add_new_stage)
        self.add_stage_button.pack(pady=10)

        self.sc_frame.update_idletasks()
        self.canvas.yview_moveto(1)
    
    def delete_stage(self, index):
        self.stages_list.pop(index)
        new_index = 0
        for stage in self.stages_list:
            stage.update_index(new_index)
            new_index += 1
        if len(self.stages_list) == 0:
            self.add_new_stage()
    
    def move_stage_up(self, index):
        if index == 0:
            return
        
        stage = self.stages_list[index]
        name = str(stage.name_entry.get())
        days = str(stage.days_entry.get())

        upper_stage = self.stages_list[index - 1]
        u_name = str(upper_stage.name_entry.get())
        u_days = str(upper_stage.days_entry.get())

        upper_stage.name_entry.delete(0, tk.END)
        upper_stage.name_entry.insert(0, name)
        upper_stage.days_entry.delete(0, tk.END)
        upper_stage.days_entry.insert(0, days)

        stage.name_entry.delete(0, tk.END)
        stage.name_entry.insert(0, u_name)
        stage.days_entry.delete(0, tk.END)
        stage.days_entry.insert(0, u_days)
    
    def move_stage_down(self, index):
        if index == (len(self.stages_list) - 1):
            return

        stage = self.stages_list[index]
        name = str(stage.name_entry.get())
        days = str(stage.days_entry.get())

        lower_stage = self.stages_list[index + 1]
        l_name = str(lower_stage.name_entry.get())
        l_days = str(lower_stage.days_entry.get())

        lower_stage.name_entry.delete(0, tk.END)
        lower_stage.name_entry.insert(0, name)
        lower_stage.days_entry.delete(0, tk.END)
        lower_stage.days_entry.insert(0, days)

        stage.name_entry.delete(0, tk.END)
        stage.name_entry.insert(0, l_name)
        stage.days_entry.delete(0, tk.END)
        stage.days_entry.insert(0, l_days)
