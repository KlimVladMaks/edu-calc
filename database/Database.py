import os
import json
from database.CalendarsDatabase import CalendarsDatabase
from database.EduTypesDatabase import EduTypesDatabase
from database.EduStagesDatabase import EduStagesDatabase
from database.ProgramsDatabase import ProgramsDatabase
from database.GroupsDatabase import GroupsDatabase


class Database:
    """
    Общая база данных.
    Является обёрткой для других баз данных.
    """

    def __init__(self):
        self.file_path = 'database.json'
        self._check_and_create_database_file()

        self.calendars = CalendarsDatabase(self)
        self.edu_types = EduTypesDatabase(self)
        self.edu_stages = EduStagesDatabase(self)
        self.programs = ProgramsDatabase(self)
        self.groups = GroupsDatabase()

    def _check_and_create_database_file(self):
        if not os.path.exists(self.file_path):
            initial_data = {
                "calendars": [],
                "edu_types": [],
                "edu_stages": [],
                "programs": [],
                "groups": []
            }
            with open(self.file_path, 'w') as json_file:
                json.dump(initial_data, json_file, indent=4)
