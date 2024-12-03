from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, HasFewerThan, Not, Or
from query_builder import QueryBuilder
def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)


    # return every player
    query = QueryBuilder()
    matcher = query.build()

    for player in stats.matches(matcher):
        print(player)
    
    #return players that play in "NYR"
    query = QueryBuilder()
    matcher = query.plays_in("NYR").build()

    for player in stats.matches(matcher):
        print(player)
    
    #return player that play in "NYR" and have at least 10 but fewer than 20 goals
    query = QueryBuilder()
    matcher = query.plays_in("NYR").has_at_least(10, "goals").has_fewer_than(20, "goals").build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
