from database.base_database import BaseDatabase


class CalendarsDatabase(BaseDatabase):
    """
    База данных для работы с данными производственных календарей.
    """
    def __init__(self, parent_db) -> None:
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

    def delete_calendar(self, calendar_name: str):
        self.load_data()
        calendars = self.data.get("calendars", [])
        for i, calendar in enumerate(calendars):
            if calendar["name"] == calendar_name:
                del calendars[i]
                break
        self.save_data()
        self.db.groups.delete_by_calendar(calendar_name)

    def get_days_off_list(self, calendar_name):
        self.load_data()
        for calendar in self.data.get("calendars", []):
            if calendar["name"] == calendar_name:
                return calendar["days_off_list"]


