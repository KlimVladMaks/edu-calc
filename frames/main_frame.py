import tkinter as tk
from frames.base_frame import BaseFrame


class MainFrame(BaseFrame):
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
        pass
