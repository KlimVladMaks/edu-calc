import os
import json
from database.programs_database import ProgramsDatabase

class Database:
    """
    Общая база данных приложения.
    Служит обёрткой для специализированных баз данных.
    """
    def __init__(self) -> None:
        self.file_path = "database.json"
        self.check_and_create_database_file()

        self.programs = ProgramsDatabase(self)
    
    def check_and_create_database_file(self) -> None:
        """
        Проверяет наличие и при отсутствии создаёт JSON-файл для базы данных.
        """
        if not os.path.exists(self.file_path):
            initial_data = {
                "calendars": [],
                "programs": [],
                "groups": [],
                "edu_stages": [],
                "edu_types": []
            }
            with open(self.file_path, 'w') as json_file:
                json.dump(initial_data, json_file, indent=4)
