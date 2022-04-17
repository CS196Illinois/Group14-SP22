# from curses import reset_prog_mode
from datetime import datetime
from os import stat_result
from sportsipy.nfl.teams import Teams
from sportsipy.nfl.roster import Player
from sportsipy.nfl.boxscore import Boxscore

teams = Teams()

class player_stock:    
    def __init__(self, shares, player_code, date):
        self.stat_key = { #keys to access stats
            1 : "rush yd",
            2 : "rush td",
            3 : "rec yd",
            4 : "rec td",
            5 : "rush broken",
            6 : "rec broken",
            7 : "rush yd contact",
            8 :  "rush att",
            9 : "recep",
            10 : "fumb"
        }    
        self.stat_multi = { #stat multiplier
            "rush yd" : 1,
            "rush td" : 1.5,
            "rec yd" : 0.8,
            "rec td" : 1.3,
            "rush broken" : 2,
            "rec broken" : 2,
            "rush yd contact" : 1,
            "rush att" : 1.5,
            "recep" : 1.5,
            "fumb" : -2
        } 
        self.stat_shares = { #amt of shares user has in each player stat
            "rush yd" : shares["rush yd"],
            "rush td" : shares["rush td"],
            "rec yd" : shares["rec yd"],
            "rec td" : shares["rec td"],
            "rush broken" : shares["rush broken"],
            "rec broken" : shares["rec broken"],
            "rush yd contact" : shares["rush yd contact"],
            "rush att" : shares["rush att"],
            "recep" : shares["recep"],
            "fumb" : shares["fumb"]
        }   

        #retrieves player code
        self.name = player_code
        self.player_season = Player(self.name)
        # self.position = self.name.position
        query = "{:04d}{:02d}{:02d}0{}".format(date.year, date.month, date.day, "CLT") # self.player_season.team_abbreviation
        print(query)
        #retrieves season stats
        self.player_game = Boxscore(query)
        # player_there = False;
        # for player in list(self.player_game.away_players) + list(self.player_game.home_players):
        #     if self.name == player.player_id: 
        #         self.bxp = player
        #         break

        self.ruyd = self.player_season.rush_yards_per_game
        self.rutd = self.player_season.rush_touchdowns
        self.reyd = self.player_season.receiving_yards_per_game
        self.retd = self.player_season.receiving_touchdowns
        self.rubr = self.player_season.rush_broken_tackles
        self.rebr = self.player_season.receiving_broken_tackles
        self.rucon = self.player_season.rush_yards_after_contact
        self.ruatt = self.player_season.rush_attempts_per_game
        self.reatt = self.player_season.receptions_per_game
        self.fum = self.player_season.fumbles
        self.gp = self.player_season.games
        #retrieves current game stats
        self.boxscore = {
            "rush yd" : self.bxp.rush_yards,
            "rush td" : self.bxp.rush_touchdowns,
            "rec yd" : self.bxp.receiving_yards,
            "rec td" : self.bxp.receiving_touchdowns,
            "rush broken" : self.bxp.rush_broken_tackles,
            "rec broken" : self.bxp.receiving_broken_tackles,
            "rush yd contact" : self.bxp.rush_yards_after_contact,
            "rush att" : self.bxp.rush_attempts,
            "recep" : self.bxp.receptions,
            "fumb" : self.bxp.fumbles
        }

    def per_game_stats(self): #generates per game stats of the player
        ruyd = self.ruyd
        rutd = self.rutd/self.gp
        reyd = self.reyd
        retd = self.retd/self.gp
        rubr = self.rubr/self.gp 
        rebr = self.rebr/self.gp 
        rucon = self.rucon/self.gp
        ruatt = self.ruatt
        reatt = self.reatt
        fum = self.fum/self.gp
        
        season_avg = {
            "rush yd" : ruyd,
            "rush td" : rutd,
            "rec yd" : reyd,
            "rec td" : retd,
            "rush broken" : rubr,
            "rec broken" : rebr,
            "rush yd contact" : rucon,
            "rush att" : ruatt,
            "recep" : reatt,
            "fumb" : fum
        }
        return season_avg
    
    def share_val(self): #cost of a single share of the player in coin
        stats = self.per_game_stats()
        javonte_williams = 30.01 #average player calculated based on Caris LeVert career averages
        player_avg = 0
        for key in self.stat_key:
            player_avg += stats[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
        multiplier = player_avg/javonte_williams
        return multiplier*javonte_williams

    def magic(self): #logic to determine stock
        stats = self.per_game_stats()
        initial_stock = 0
        game_stock = 0
        for key in self.stat_key:
            initial_stock += stats[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
            game_stock += self.boxscore[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
        diff = game_stock - initial_stock
        pct = diff/initial_stock
        print(pct)
        return pct

    def coin_diff(self): #net gain/loss of coin
        pct_diff = self.magic()
        return pct_diff * self.share_val()

d = datetime(2021, 11, 21)
test_stock = {
    "rush yd" : 1,
    "rush td" : 1,
    "rec yd" : 1,
    "rec td" : 1,
    "rush broken" : 1,
    "rec broken" : 1,
    "rush yd contact" : 1,
    "rush att" : 1,
    "recep" : 1,
    "fumb" : 1  
}
test_player = player_stock(test_stock, 'taylJo02', d)