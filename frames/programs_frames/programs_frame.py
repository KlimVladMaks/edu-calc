import tkinter as tk
from tkinter import ttk
from frames.base_frame import BaseFrame
from database.database import Database
from widgets.back_button import BackButton


class ProgramsFrame(BaseFrame):
    """
    Фрейм для работы с учебными программами.
    """
    def __init__(self, master: tk.Tk, parent_frame: BaseFrame) -> None:
        """
        Аргументы:
            master: Окно приложения.
            parent_frame: Родительский фрейм.
        """
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()

    def create_frame(self) -> None:
        """
        Создаёт фрейм (добавляет и настраивает все необходимые компоненты).
        """
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.place()
        ttk.Label(self, text="Учебные программы").pack(pady=10)
        self.create_table()
    
    def create_table(self) -> None:
        """
        Создаёт таблицу с учебными программами.
        """
        pass
    
    def go_back(self) -> None:
        """
        Уничтожает текущий фрейм и открывает предыдущий.
        """
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()








