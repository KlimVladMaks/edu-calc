import typing as tp
from frames.base_frame import BaseFrame


class Table:
    """
    Таблица для отображения данных.
    """
    def __init__(self, frame: BaseFrame, columns: list[list[tp.Union[str, int]]]):
        """
        Аргументы:
            - frame: Фрейм, на котором должна размещаться таблица.
            - columns: Список с названиями и начальной шириной столбцов таблицы.
            Должен иметь следующий формат: columns = [["Название 1", 150], ["Название 2", 100]].
        """
        self.frame = frame
        
        self.columns_name = []
        for column in columns:
            self.columns_name.append(column[0])
        
        self.column_widths = []
        for column in columns:
            self.column_widths.append(column[1])
