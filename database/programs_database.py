from database.base_database import BaseDatabase


class ProgramsDatabase(BaseDatabase):
    """
    База данных для работы с данными учебных программ.
    """
    def __init__(self, parent_db: 'database.database.Database') -> None:
        """
        Аргументы:
            parent_db: Родительская (общая) база данных.
        """
        super().__init__(parent_db)



