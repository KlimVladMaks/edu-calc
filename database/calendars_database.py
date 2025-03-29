from database.base_database import BaseDatabase
from widgets.calculator import Calculator


class CalendarsDatabase(BaseDatabase):
    """
    База данных для работы с данными производственных календарей.
    """
    def __init__(self, parent_db: 'database.database.Database') -> None:
        """
        Параметры:
            parent_db: Родительская (общая) база данных.
        """
        super().__init__(parent_db)
    
    def get_all_calendars_names(self) -> list[str]:
        """
        Получить список с названиями всех производственных календарей.

        Возвращаемое значение: Список с названиями всех производственных календарей.
        """
        self.load_data()
        calendars_names: list[str] = []
        for calendar in self.data.get("calendars", []):
            calendars_names.append(calendar["name"])
        return calendars_names

    def get_calendar_data_dict(self, calendar_name: str) -> dict:
        self.load_data()
        for calendar in self.data.get("calendars", []):
            if calendar["name"] == calendar_name:
                return calendar




