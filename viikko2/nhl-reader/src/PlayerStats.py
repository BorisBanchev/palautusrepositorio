from player import Player
from PlayerReader import PlayerReader
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()
    

    def top_scorers_by_nationality(self,nationality):
        players_sorted = sorted(self.players, key = lambda player: player.goals + player.assists, reverse=True)
        players_sorted_by_nationality = []
        for player in players_sorted:
            if player.nationality == nationality:
                players_sorted_by_nationality.append(player)
        return players_sorted_by_nationality