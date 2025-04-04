import tkinter as tk
from tkinter import ttk
from frames.base_frame import BaseFrame
from frames.calendars_frames.calendars_frame import CalendarsFrame
from frames.programs_frames.programs_frame import ProgramsFrame
from frames.groups_frames.groups_frame import GroupsFrame


class MainMenuFrame(BaseFrame):
    """
    Фрейм с главным меню приложения.
    """
    def __init__(self, master: tk.Tk) -> None:
        """
        Аргументы:
            master: Окно приложения.
        """
        super().__init__(master)
        self.create_frame()
    
    def create_frame(self) -> None:
        """
        Создаёт фрейм (добавляет и настраивает все необходимые компоненты).
        """
        button_width = 60
        button_height = 10
        padding_between_buttons = 8

        ttk.Button(self,
                   text="Производственные календари",
                   command=self.open_calendars_frame,
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)
        
        ttk.Button(self,
                   text="Учебные программы",
                   command=self.open_programs_frame,
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)
        
        ttk.Button(self,
                   text="Учебные группы",
                   command=self.open_groups_frame,
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)
        
        ttk.Button(self,
                   text="Этапы обучения",
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)
        
        ttk.Button(self,
                   text="Виды обучения",
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)
        
        ttk.Button(self,
                   text="Выгрузить данные",
                   width=button_width,
                   padding=(0, button_height)).pack(pady=padding_between_buttons)

    def open_calendars_frame(self) -> None:
        calendars_frame = CalendarsFrame(self.master, self)
        calendars_frame.display_frame()

    def open_programs_frame(self):
        programs_frame = ProgramsFrame(self.master, self)
        programs_frame.display_frame()
    
    def open_groups_frame(self):
        groups_frame = GroupsFrame(self.master, self)
        groups_frame.display_frame()





