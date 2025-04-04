from tkinter import ttk
from frames.base_frame import BaseFrame
from database.database import Database
from widgets.back_button import BackButton
from widgets.table import Table
from widgets.calculator import Calculator


class GroupsFrame(BaseFrame):
    """
    Фрейм для работы с учебными группами.
    """
    def __init__(self, master, parent_frame):
        super().__init__(master)
        self.parent_frame = parent_frame
        self.db = Database()
        self.create_frame()
    
    def create_frame(self):
        self.back_button = BackButton(self.master, command=self.go_back)
        self.back_button.place()
        ttk.Label(self, text="Учебные группы").pack(pady=10)
        self.create_table()
    
    def go_back(self):
        self.back_button.destroy()
        self.destroy()
        self.parent_frame.display_frame()

    def create_table(self):
        columns = [
            ("Название", 150),
            ("Календарь", 100),
            ("Программа", 100),
            ("Вид обучения", 100),
            ("Дата начала", 100),
            ("Дата окончания", 100),
            ("Дней обучения", 100),
            ("Выходных дней", 100),
            ("Всего дней", 100)
        ]
        self.table = Table(self, columns, height=11)
        table_rows = self.get_table_rows()
        self.table.add_rows(table_rows)
        self.table.pack(pady=10)

        self.table.add_menu_command(label="Календарь", command=self.open_calendar_app)
        self.table.add_menu_command(label="Изменить", command=self.open_edit_group_frame)
        self.table.add_menu_command(label="Удалить", command=self.delete_group)
    
    def get_table_rows(self):
        table_rows = []
        groups_names = self.db.groups.get_all_programs_names()
        for group_name in groups_names:
            table_row = [group_name]
            group_data_dict = self.db.groups.get_group_data_dict(group_name)
            calendar = group_data_dict["calendar"]
            program = group_data_dict["program"]
            edu_type = group_data_dict["edu_type"]
            start_date = group_data_dict["start_date"]
            end_date = Calculator.calculate_end_date(calendar, program, start_date)
            total_days = Calculator.count_days_between_dates(start_date, end_date)
            study_days = self.db.programs.get_total_days(program)
            days_off = total_days - study_days
            table_row.append(calendar)
            table_row.append(program)
            table_row.append(edu_type)
            table_row.append(start_date)
            table_row.append(end_date)
            table_row.append(study_days)
            table_row.append(days_off)
            table_row.append(total_days)
            table_rows.append(table_row)
        return table_rows

    def open_edit_group_frame(self):
        pass

    def delete_group(self):
        pass

    def open_calendar_app(self):
        pass







