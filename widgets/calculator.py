from datetime import datetime


class Calculator:
    """
    Калькулятор для расчётов, требующихся при работе программы.
    """

    def count_days_between_dates(start_date: str, end_date: str) -> int:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = (end - start).days + 1
        return delta
