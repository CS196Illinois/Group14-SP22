# from curses import reset_prog_mode
from datetime import datetime
from os import stat_result
from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player
from sportsipy.nba.boxscore import Boxscore
import pandas as pd

teams = Teams()

class player_stock:    
    def __init__(self, shares, player_code):
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

        self.ppg = self.player_season.points
        self.rpg = self.player_season.offensive_rebounds + self.player_season.defensive_rebounds
        self.apg = self.player_season.assists
        self.spg = self.player_season.steals
        self.bpg = self.player_season.blocks
        self.tpg = self.player_season.turnovers
        self.gp = self.player_season.games_played
        
    def box_score_stats(self, date):
        query = "{:04d}{:02d}{:02d}0{}".format(date.year, date.month, date.day, "CLE") # self.player_season.team_abbreviation
        print(query)
        #retrieves season stats
        self.player_game = Boxscore(query)
        player_there = False;
        for player in list(self.player_game.away_players) + list(self.player_game.home_players):
            if self.name == player.player_id:
                self.bxp = player
                break
        #retrieves current game stats
        pts = self.bxp.points
        reb = self.bxp.offensive_rebounds + self.bxp.defensive_rebounds
        ast = self.bxp.assists
        stl = self.bxp.steals
        blk = self.bxp.blocks
        tov = self.bxp.turnovers
        boxscore = {
            "pts" : pts,
            "reb" : reb,
            "ast" : ast,
            "stl" : stl,
            "blk" : blk,
            "tov" : tov
        }
        return boxscore

    def per_game_stats(self): #generates per game stats of the player
        ppg = self.ppg/self.gp
        rpg = self.rpg/self.gp
        apg = self.apg/self.gp
        spg = self.spg/self.gp
        bpg = self.bpg/self.gp
        tpg = self.tpg/self.gp
        
        season_avg = {
            "pts" : ppg,
            "reb" : rpg,
            "ast" : apg,
            "stl" : spg,
            "blk" : bpg,
            "tov" : tpg
        }
        return season_avg
    
    def share_val(self): #cost of a single share of the player in coin
        stats = self.per_game_stats()
        caris_levert = 30.01 #average player calculated based on Caris LeVert career averages
        player_avg = 0
        for key in self.stat_key:
            player_avg += stats[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
        multiplier = player_avg/caris_levert
        return multiplier*caris_levert

    def magic(self, date): #logic to determine stock
        bx = self.box_score_stats(date)
        stats = self.per_game_stats()
        initial_stock = 0
        game_stock = 0
        for key in self.stat_key:
            initial_stock += stats[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
            game_stock += bx[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
        diff = game_stock - initial_stock
        pct = diff/initial_stock
        print(pct)
        return pct

    def coin_diff(self): #net gain/loss of coin
        pct_diff = self.magic()
        return pct_diff * self.share_val()
        
# class team_stock:
#    def __init__(self, team_abbv, shares, date):
#        self.team_season = Teams(team_abbv)
#        query = "{:04d}{:02d}{:02d}0{}".format(date.year, date.month, date.day, "CLE") # self.player_season.team_abbreviation
#        print(query)
#        #retrieves season stats
#        self.team_game = Boxscore(query)
#     #    team_there = False;
#        if self.abbv == self.team_game.winning_abbr or self.abbv == self.team_game.losing_abbr:
#            self.bxp = self.team_game


#        self.ppg = self.team_season.points
#        self.rpg = self.team_season.offensive_rebounds + self.player_season.defensive_rebounds
#        self.apg = self.team_season.assists
#        self.spg = self.team_season.steals
#        self.bpg = self.team_season.blocks
#        self.tpg = self.team_season.turnovers
#        self.gp = self.team_season.games_played
#         #retrieves current game stats
#        self.boxscore = {
#             "pts" : self.bxp.points,
#             "reb" : self.bxp.offensive_rebounds + self.bxp.defensive_rebounds,
#             "ast" : self.bxp.assists,
#             "stl" : self.bxp.steals,
#             "blk" : self.bxp.blocks,
#             "tov" : self.bxp.turnovers
#        }
#         #shares user owns of team
#        self.shares = shares

#    def per_game_stats(self): #generates per game stats of the player
#        ppg = self.ppg/self.gp
#        rpg = self.rpg/self.gp
#        apg = self.apg/self.gp
#        spg = self.spg/self.gp
#        bpg = self.bpg/self.gp
#        tpg = self.tpg/self.gp
        
#        season_avg = {
#            "pts" : ppg,
#            "reb" : rpg,
#            "ast" : apg,
#            "stl" : spg,
#            "blk" : bpg,
#            "tov" : tpg
#        }
#        return season_avg

#    def magic(self): #logic to determine stock
#        stats = self.per_game_stats()
        
#        initial_stock = stats["Points"] + stats["Rebounds"]*1.2 + stats["Assists"]*1.5 + stats["Blocks"]*3 + stats["Steals"]*3 - stats["Turnovers"]
#        game_stock = self.pts + self.reb*1.2 + self.ast*1.5 + self.blk*3 + self.stl*3 - self.tov
#        diff = game_stock - initial_stock
#        pct = 1 + (diff/initial_stock)
#        print(pct)
#        return pct

d = datetime(2018, 6, 8)
test_stock = {
    "pts" : 1,
    "reb" : 1,
    "ast" : 1,
    "stl" : 1,
    "blk" : 1,
    "tov" : 1 
}
test_player = player_stock(test_stock, 'jamesle01')
# test_team = team_stock(teams("CLE"), 2, d)  #IDK why this isn't working
