import typing as tp
import tkinter as tk
from tkinter import ttk
from frames.base_frame import BaseFrame


class Table:
    """
    Таблица для отображения данных.
    """
    def __init__(self, frame: BaseFrame, columns: list[list[tp.Union[str, int]]], height: int):
        """
        Параметры:
            - frame: Фрейм, на котором должна размещаться таблица.
            - columns: Список с названиями и начальной шириной столбцов таблицы.
            Должен иметь следующий формат: columns = [["Название 1", 150], ["Название 2", 100]].
            - height: Высота таблицы (число отображаемых строк).
        """
        self.frame = frame
        self.columns = columns

        self.current_sort_column: tp.Union[str, None] = None
        self.sort_order: bool = True
        
        self.column_names: list[str] = []
        for column in columns:
            self.column_names.append(column[0])
        
        self.column_widths: list[int] = []
        for column in columns:
            self.column_widths.append(column[1])
        
        self.table_frame = ttk.Frame(self.frame)
        self.tree = ttk.Treeview(self.table_frame, columns=self.column_names, height=height, show="headings")

        for name in self.column_names:
            self.tree.heading(name, text=name, command=lambda name=name: self.sort_column(name))
        for column in self.columns:
            self.tree.column(column[0], width=column[1], stretch=False)

        self.scroll_x = ttk.Scrollbar(self.table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=self.scroll_x.set)

        self.scroll_y = ttk.Scrollbar(self.table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scroll_y.set)

        self.scroll_x.pack(side="bottom", fill="x")
        self.scroll_y.pack(side="right", fill="y")
        self.tree.pack(side="left")

        self.tree.bind("<Button-1>", self.on_table_click)

        self.menu = tk.Menu(self.table_frame, tearoff=0)
        self.tree.bind("<Button-3>", self.show_menu)

    def pack(self, pady=0) -> None:
        """
        Располагает (отображает) таблицу на фрейме.

        Параметры:
            - pady: Отступы таблицы по оси Y.
        """
        self.table_frame.pack(pady=pady)

    def add_rows(self, rows: list[list[str]]) -> None:
        """
        Добавляет в таблицу заданные строки.

        Параметры:
            - rows: Список со значениями строк в формате:
            [[<1-е значение 1-й строки>, <2-е значение 1-й строки>, ...], [<1-е значение 2-й строки>, ...], ...].
        """
        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def update_rows(self, new_rows: list) -> None:
        """
        Удаляет все старые строки и заменяет их на новые.

        Параметры:
            - new_rows: Список со значениями новых строк в формате:
            [[<1-е значение 1-й строки>, <2-е значение 1-й строки>, ...], [<1-е значение 2-й строки>, ...], ...].
        """
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.add_rows(new_rows)  

    def sort_column(self, column_name: str) -> None:
        """
        Сортирует заданный столбец таблицы.
        Использует отдельную переменную для хранения порядка сортировки
        (Сначала сортирует по возрастанию, при повторном вызове - по убыванию).

        Параметры:
            column_name: Название столбца, который нужно отсортировать.
        """
        if self.current_sort_column == column_name:
            self.sort_order = not self.sort_order
        else:
            self.sort_order = True
            self.current_sort_column = column_name
        
        column_index = self.tree["columns"].index(column_name)
        
        data = []
        for item in self.tree.get_children():
            values = self.tree.item(item)["values"]
            data.append((item, values))
        
        is_numeric = True
        for _, values in data:
            try:
                float(values[column_index])
            except:
                is_numeric = False
                break
        
        if is_numeric:
            def sort_key(x):
                return x[1][column_index]
        else:
            def sort_key(x):
                return str(x[1][column_index])
        
        data.sort(key=sort_key, reverse=not self.sort_order)

        self.tree.delete(*self.tree.get_children())
        for item, values in data:
            self.tree.insert("", tk.END, iid=item, values=values)
        
        self.update_sorting_arrow()
    
    def update_sorting_arrow(self) -> None:
        """
        Устанавливает в заголовке столбца стрелочку, соответствующую порядку сортировки. 
        """
        for col in self.tree["columns"]:
            current_title = self.tree.heading(col)["text"].strip("↑↓ ")
            if col == self.current_sort_column:
                arrow = "↑ " if self.sort_order else "↓ "
                self.tree.heading(col, text=arrow + current_title)
            else:
                self.tree.heading(col, text=current_title)
    
    def destroy(self) -> None:
        """
        Уничтожает таблицу.
        """
        self.table_frame.destroy()

    def on_table_click(self, event) -> None:
        region = self.tree.identify_region(event.x, event.y)
        if region == "nothing":
            self.tree.selection_remove(self.tree.selection())

    def show_menu(self, event):
        row_id = self.tree.identify_row(event.y)
        if row_id:
            self.tree.selection_set(row_id)
            self.menu.post(event.x_root, event.y_root)

    def add_menu_command(self, label, command):
        self.menu.add_command(label=label, command=command)

    def delete_selected(self):
        selected_items = self.tree.selection()
        selected_item = selected_items[0]
        self.tree.delete(selected_item)

    def get_selected_row(self):
        selected_items = self.tree.selection()
        selected_item = selected_items[0]
        item_data = self.tree.item(selected_item)
        return item_data["values"]


