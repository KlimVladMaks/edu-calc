import tkinter as tk
from frames.main_frame import MainFrame


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Образовательный калькулятор")
    root.geometry("700x400")
    root.resizable(False, False)
    main_frame = MainFrame(root)
    main_frame.display_frame()
    root.mainloop()
