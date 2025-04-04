from datetime import datetime, timedelta
from database.database import Database


class Calculator:
    """
    Калькулятор для расчётов, требующихся при работе программы.
    """

    def count_days_between_dates(start_date: str, end_date: str) -> int:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = (end - start).days + 1
        return delta

    def calculate_end_date(calendar_name, program_name, start_date_str):
        db = Database()
        days_off_list = db.calendars.get_days_off_list(calendar_name)
        study_days = db.programs.get_total_days(program_name)
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        days_off_dates = {datetime.strptime(date, "%Y-%m-%d") for date in days_off_list}
        current_date = start_date
        days_counter = 0
        while days_counter < study_days:
            if current_date not in days_off_dates:
                days_counter += 1
            current_date += timedelta(days=1)
        current_date -= timedelta(days=1)
        return current_date.strftime("%Y-%m-%d")



