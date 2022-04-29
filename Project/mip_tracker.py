from datetime import datetime
from os import stat_result
from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player
from sportsipy.nba.boxscore import Boxscore

#track the most improved and most regressed players/teams of the season

all_teams = Teams()

class mip:
    leap_score = [0, 0, 0, 0, 0]
    fall_score = [0, 0, 0, 0, 0]
    leap_players = [" ", " ", " ", " ", " "]
    fall_players = [" ", " ", " ", " ", " "]
    def __init__(self, shares, player_code, date):
        
        self.stat_key = { #keys to access stats
            1 : "pts",
            2 : "reb",
            3 : "ast",
            4 : "stl",
            5 : "blk",
            6 : "tov"
        }    
        self.stat_multi = { #stat multiplier
            "pts" : 1,
            "reb" : 1.2,
            "ast" : 1.5,
            "stl" : 3,
            "blk" : 3,
            "tov" : -1
        } 
        self.stat_shares = { #amt of shares user has in each player stat
            "pts" : shares["pts"],
            "reb" : shares["reb"],
            "ast" : shares["ast"],
            "stl" : shares["stl"],
            "blk" : shares["blk"],
            "tov" : shares["tov"]
        }   

        # for i in self.stat_shares:
        #     if self.stat_shares[stat_key[i]] <= 0:
        #         self.stat_shares.pop(stat_key[i])

        #retrieves player code
        self.name = player_code
        self.player_season = Player(self.name)
        query = "{:04d}{:02d}{:02d}0{}".format(date.year, date.month, date.day, "CLE") # self.player_season.team_abbreviation
        print(query)
        #retrieves season stats
        self.player_game = Boxscore(query)
        player_there = False;
        for player in list(self.player_game.away_players) + list(self.player_game.home_players):
            if self.name == player.player_id:
                self.bxp = player
                break

        self.ppg = self.player_season.points
        self.rpg = self.player_season.offensive_rebounds + self.player_season.defensive_rebounds
        self.apg = self.player_season.assists
        self.spg = self.player_season.steals
        self.bpg = self.player_season.blocks
        self.tpg = self.player_season.turnovers
        self.gp = self.player_season.games_played
        #retrieves current game stats
        self.pts = self.bxp.points
        self.reb = self.bxp.offensive_rebounds + self.bxp.defensive_rebounds
        self.ast = self.bxp.assists
        self.stl = self.bxp.steals
        self.blk = self.bxp.blocks
        self.tov = self.bxp.turnovers
        self.boxscore = {
            "pts" : self.pts,
            "reb" : self.reb,
            "ast" : self.ast,
            "stl" : self.stl,
            "blk" : self.blk,
            "tov" : self.tov
        }