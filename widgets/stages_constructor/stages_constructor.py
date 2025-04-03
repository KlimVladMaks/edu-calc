import tkinter as tk
from tkinter import ttk
from widgets.stages_constructor.stage_input import StageInput


class StagesConstructor:
    
    def __init__(self, main_frame, scroll_func):
        self.main_frame = main_frame
        self.scroll_func = scroll_func
        self.frame = ttk.Frame(main_frame)
        self.stages_list: list[StageInput] = []
        self.add_stage_button = ttk.Button()
        self.add_new_stage()
    
    def pack(self, pady):
        self.frame.pack(pady=pady)
    
    def add_new_stage(self):
        self.add_stage_button.destroy()

        index = len(self.stages_list)
        new_stage = StageInput(self.frame, index,
                               self.scroll_func, self.delete_stage,
                               self.move_stage_up, self.move_stage_down)
        new_stage.pack(pady=5)
        self.stages_list.append(new_stage)

        self.add_stage_button = ttk.Button(self.frame, text="+ Добавить этап", command=self.add_new_stage)
        self.add_stage_button.pack(pady=(10, 0))

        self.main_frame.update_idletasks()
        self.main_frame.master.yview_moveto(1)

    def delete_stage(self, index: int):
        self.stages_list.pop(index)
        new_index = 0
        for stage in self.stages_list:
            stage.update_index(new_index)
            new_index += 1
        if len(self.stages_list) == 0:
            self.add_new_stage()
    
    def move_stage_up(self, index: int):
        if index == 0:
            return
        else:
            self.swap_two_stages(index, index - 1)
    
    def move_stage_down(self, index: int):
        if index == (len(self.stages_list) - 1):
            return
        else:
            self.swap_two_stages(index, index + 1)

    def swap_two_stages(self, index_1: int, index_2: int):
        stage_1 = self.stages_list[index_1]
        stage_2 = self.stages_list[index_2]
        data_1 = [stage_1.stage_combobox.get(), stage_1.days_entry.get()]
        data_2 = [stage_2.stage_combobox.get(), stage_2.days_entry.get()]

        stage_1.stage_combobox.set(data_2[0])
        stage_1.days_entry.delete(0, tk.END)
        stage_1.days_entry.insert(0, data_2[1])

        stage_2.stage_combobox.set(data_1[0])
        stage_2.days_entry.delete(0, tk.END)
        stage_2.days_entry.insert(0, data_1[1])
        






