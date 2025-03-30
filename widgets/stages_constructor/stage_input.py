from tkinter import ttk
from database.database import Database


class StageInput:

    def __init__(self, sc_frame, index):
        self.sc_frame = sc_frame
        self.index = index
        self.db = Database()
        self.frame = ttk.Frame(self.sc_frame)

        self.index_label = ttk.Label(self.frame, text=f"{str(self.index + 1)})")
        self.index_label.grid(row=0, column=0, padx=5)

        self.input_stage_frame = ttk.Frame(self.frame)
        self.input_stage_frame.grid(row=0, column=1, padx=5)
        ttk.Label(self.input_stage_frame, text="Название этапа:").pack()
        self.stages_list = self.db.edu_stages.get_all_stages()
        self.stage_combobox = ttk.Combobox(self.input_stage_frame, values=self.stages_list, state="readonly")
        self.stage_combobox.pack()
        self.stage_combobox.bind("<MouseWheel>", self.disable_mouse_wheel_scroll)

        self.input_days_frame = ttk.Frame(self.frame)
        self.input_days_frame.grid(row=0, column=2, padx=5)
        ttk.Label(self.input_days_frame, text="Число дней:").pack()
        self.days_entry = ttk.Entry(self.input_days_frame)
        self.days_entry.pack()

        ttk.Button(self.frame, text="↑", width=3, command=self.move_up).grid(row=0, column=3, padx=5)
        ttk.Button(self.frame, text="↓", width=3, command=self.move_down).grid(row=0, column=4, padx=5)
        ttk.Button(self.frame, text="-", width=3, command=self.delete).grid(row=0, column=5, padx=5)
    
    def pack(self, pady):
        self.frame.pack(pady=pady)
    
    def delete(self):
        pass

    def move_up(self):
        pass
    
    def move_down(self):
        pass

    def disable_mouse_wheel_scroll(self, event):
        return "break"




