from database.base_database import BaseDatabase


class ProgramsDatabase(BaseDatabase):
    """
    База данных для работы с данными учебных программ.
    """
    def __init__(self, parent_db) -> None:
        """
        Аргументы:
            parent_db: Родительская (общая) база данных.
        """
        super().__init__(parent_db)

    def get_unique_stages_names(self):
        self.load_data()
        unique_stages_names = []
        for program in self.data.get("programs", []):
            for stage in program.get("stages", []):
                stage_name = stage[0]
                if stage_name not in unique_stages_names:
                    unique_stages_names.append(stage_name)
        return sorted(unique_stages_names)

    def get_all_programs_names(self):
        self.load_data()
        programs_names = []
        for program in self.data.get("programs", []):
            programs_names.append(program["name"])
        return programs_names

    def get_program_duration(self, program_name):
        self.load_data()
        for program in self.data.get("programs", []):
            if program["name"] == program_name:
                program_duration = sum(stage[1] for stage in program["stages"])
                return program_duration

    def get_program_stage_duration(self, program_name, stage_name):
        self.load_data()
        for program in self.data.get("programs", []):
            if program["name"] == program_name:
                stage_duration = 0
                for stage in program["stages"]:
                    if stage[0] == stage_name:
                        stage_duration += stage[1]
                return stage_duration

    def delete_program(self, program_name):
        self.load_data()
        programs = self.data.get("programs", [])
        for i, program in enumerate(programs):
            if program["name"] == program_name:
                del programs[i]
                break
        self.save_data()
        self.db.groups.delete_by_program(program_name)




