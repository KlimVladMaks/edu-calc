from database.base_database import BaseDatabase


class GroupsDatabase(BaseDatabase):
    """
    База данных для работы с данными учебных групп.
    """
    def __init__(self, parent_db):
        super().__init__(parent_db)
    
    def delete_by_calendar(self, calendar_name: str) -> None:
        self.load_data()
        groups = self.data.get("groups", [])
        for i, group in enumerate(groups):
            if group["calendar"] == calendar_name:
                del groups[i]
        self.save_data()
    
    def delete_by_program(self, program_name):
        self.load_data()
        groups = self.data.get("groups", [])
        for i, group in enumerate(groups):
            if group["program"] == program_name:
                del groups[i]
        self.save_data()

    def get_all_programs_names(self):
        self.load_data()
        groups_names = []
        for group in self.data.get("groups", []):
            groups_names.append(group["name"])
        return groups_names

    def get_group_data_dict(self, group_name):
        self.load_data()
        for group in self.data.get("groups", []):
            if group["name"] == group_name:
                return group






