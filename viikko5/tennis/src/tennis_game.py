class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_types = ["Love","Fifteen","Thirty","Forty"]

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""
        if self.player1_score == self.player2_score:
            score = self.get_tie_score()
            
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_last_point_score()
        else:
            score = self.get_normal_score()
            
        return score
    
    def get_tie_score(self):
        if self.player1_score < 3:
            return f"{self.score_types[self.player1_score]}-All"
        return f"Deuce"

    def get_last_point_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        
        return "Win for player2"
    
    def get_normal_score(self):
        return f"{self.score_types[self.player1_score]}-{self.score_types[self.player2_score]}"
    
