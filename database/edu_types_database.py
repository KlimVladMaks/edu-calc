from database.base_database import BaseDatabase


class EduTypesDatabase(BaseDatabase):

    def __init__(self, parent_db):
        super().__init__(parent_db)
    
    def get_all_edu_types(self):
        self.load_data()
        edu_types = self.data.get("edu_types", [])
        return edu_types








