class Sport:
    def __init__(self, team_size: int, name: str, equipment_type: str):
        self.team_size = team_size
        self.name = name
        self.equipment_type = equipment_type


class BallSport(Sport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.equipment_type = "ball"


class RacketSport(Sport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.equipment_type = "racket"


class AthleticSport(Sport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.equipment_type = None


class Football(BallSport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.team_size = 11


class Tennis(RacketSport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.team_size = 1


class Badminton(RacketSport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.team_size = 1


class Running(AthleticSport):
    def __init__(self, team_size: int, name: str, equipment_type: str):
        super().__init__(team_size, name, equipment_type)
        self.team_size = 1
        self.equipment_type = "shoes"


running = Running(1, "running", "meow")

print(running.equipment_type)
