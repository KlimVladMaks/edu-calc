from tkinter import ttk
from widgets.stages_constructor.stage_input import StageInput


class StagesConstructor:
    
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.frame = ttk.Frame(main_frame)
        self.stages_list = []
        self.add_stage_button = ttk.Button()
        self.add_new_stage()
    
    def pack(self, pady):
        self.frame.pack(pady=pady)
    
    def add_new_stage(self):
        self.add_stage_button.destroy()

        index = len(self.stages_list)
        new_stage = StageInput(self.frame, index)
        new_stage.pack(pady=5)
        self.stages_list.append(new_stage)

        self.add_stage_button = ttk.Button(self.frame, text="+ Добавить этап", command=self.add_new_stage)
        self.add_stage_button.pack(pady=(10, 0))

        self.main_frame.update_idletasks()
        self.main_frame.master.yview_moveto(1)







