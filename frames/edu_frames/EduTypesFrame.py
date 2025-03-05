import tkinter as tk
from tkinter import ttk
from frames.BaseFrame import BaseFrame
from frames.edu_frames.InputWidget import InputWidget
from database.Database import Database
from widgets.BackButton import BackButton
from widgets.Table import Table


class EduTypesFrame(BaseFrame):
    """
    Фрейм для работы с видами обучения.
    """
    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.pack()
    
        ttk.Label(self, text="Виды обучения").pack(pady=5)
        self.create_table()

        self.add_button = ttk.Button(self, text="Добавить вид обучения", command=self.open_add_widget)
        self.add_button.pack(pady=10)
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()
    
    def create_table(self):
        columns = [
            ("Вид обучения", 300)
        ]
        self.table = Table(self, columns)
        table_rows = self.get_table_rows()
        self.table.add_rows(table_rows)
        self.table.pack()
        self.create_context_menu()
    
    def get_table_rows(self):
        table_rows = []
        for edu_type in self.db.edu_types.get_all():
            table_rows.append([edu_type])
        return table_rows
    
    def create_context_menu(self):
        self.menu = tk.Menu(self, tearoff=0)
        self.menu.add_command(label="Удалить", command=self.delete_selected)
        self.table.tree.bind("<Button-3>", self.show_context_menu)
    
    def delete_selected(self):
        selected_items = self.table.tree.selection()
        item = selected_items[0]
        item_data = self.table.tree.item(item)
        values = item_data['values']
        self.db.edu_types.delete(values[0])
        self.table.tree.delete(item)
    
    def show_context_menu(self, event):
        row_id = self.table.tree.identify_row(event.y)
        if row_id:
            self.table.tree.selection_set(row_id)
            self.menu.post(event.x_root, event.y_root)
    
    def open_add_widget(self):
        self.add_button.pack_forget()
        self.add_widget = InputWidget(self, "Название:", "Добавить", self.add_edu_type, self.cancel_add)
        self.add_widget.pack()
    
    def add_edu_type(self):
        new_edu_type = self.add_widget.entry.get()
        self.db.edu_types.add(new_edu_type)
        self.update_table()
        self.add_widget.destroy()
        self.add_button.pack(pady=5)
    
    def update_table(self):
        new_table_rows = self.get_table_rows()
        self.table.update(new_table_rows)
    
    def cancel_add(self):
        self.add_widget.destroy()
        self.add_button.pack(pady=5)
