from database.base_database import BaseDatabase
from database.database import Database


class ProgramsDatabase(BaseDatabase):
    """
    База данных для работы с данными учебных программ.
    """
    def __init__(self, parent_db: Database) -> None:
        """
        Аргументы:
            parent_db: Родительская (общая) база данных.
        """
        super().__init__(parent_db)



