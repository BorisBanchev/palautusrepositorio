class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.goals+self.assists}"
