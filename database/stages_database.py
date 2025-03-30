from database.base_database import BaseDatabase


class StagesDatabase(BaseDatabase):

    def __init__(self, parent_db):
        super().__init__(parent_db)
    
    def get_all_stages(self):
        self.load_data()
        stages = self.data.get("edu_stages", [])
        return stages
    




