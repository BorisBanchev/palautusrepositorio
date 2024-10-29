from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    INVALID = 404
class StatisticsService:
    def __init__(self, p_reader: PlayerReader):
        self.p_reader = p_reader

        self._players = self.p_reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, SortBy = SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_key(player):
            if SortBy == SortBy.POINTS:
                return player.points
            elif SortBy == SortBy.GOALS:
                return player.goals
            elif SortBy == SortBy.ASSISTS:
                return player.assists
            else:
                raise ValueError
            
        sorted_players = sorted(
            self._players, 
            reverse=True, 
            key=sort_key)
        
        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
