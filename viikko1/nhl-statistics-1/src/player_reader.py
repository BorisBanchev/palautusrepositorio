from urllib import request
from player import Player

class PlayerReader:
    def __init__(self, url_for_players: str):
        self.url_for_players = url_for_players

    def get_players(self):
        players_file = request.urlopen(self.url_for_players)
        players = []

        for line in players_file:
            decoded_line = line.decode("utf-8")
            parts = decoded_line.split(";")

            if len(parts) > 3:
                player = Player(
                    parts[0].strip(),
                    parts[1].strip(),
                    int(parts[3].strip()),
                    int(parts[4].strip())
                )

                players.append(player)

        return players
