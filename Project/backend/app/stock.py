# from curses import reset_prog_mode
from datetime import datetime
from os import stat_result
from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player
from sportsipy.nba.boxscore import Boxscore
from sportsipy.nba.schedule import Schedule
import numpy as np
import pandas as pd

teams = Teams()

class player_stock:    
    def __init__(self, shares, player_code, team, s):
        self.team = team
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
        self.player_season = self.player_season(s)

        self.ppg = self.player_season.points
        self.rpg = self.player_season.offensive_rebounds + self.player_season.defensive_rebounds
        self.apg = self.player_season.assists
        self.spg = self.player_season.steals
        self.bpg = self.player_season.blocks
        self.tpg = self.player_season.turnovers
        self.gp = self.player_season.games_played
    

    def box_score_stats(self, date):
        tm = Schedule(self.team, year=str(date.year))
        
        parse_date = "{}-{:02}-{:02}".format(date.year, date.month, date.day)
        df = tm.dataframe
        index = np.argwhere(df.datetime.to_numpy() < np.datetime64(parse_date))
        
        game_box = index[-1][0]
        self.player_game = tm[game_box].boxscore

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
            incr = stats[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
            initial_stock += incr
            g_incr = bx[self.stat_key[key]]*self.stat_multi[self.stat_key[key]]*self.stat_shares[self.stat_key[key]]
            game_stock += g_incr
        diff = game_stock - initial_stock
        pct = diff/initial_stock
        if pct < .8:
            return pct**3
        else:
            return .8

    def coin_diff(self): #net gain/loss of coin
        pct_diff = self.magic()
        return pct_diff * self.share_val()
        
def season(date):
    if d.year == 2020:
        if d.month < 11:
            return "{}-{}".format(date.year - 1, str(date.year)[-2:])
    if d.month < 8:
        return "{}-{}".format(date.year - 1, str(date.year)[-2:])
    else:
        return "{}-{}".format(date.year, str(date.year + 1)[-2:])

d = datetime(2019, 3, 23)

test_stock = {
    "pts" : 1,
    "reb" : 1,
    "ast" : 1,
    "stl" : 1,
    "blk" : 1,
    "tov" : 1
}
test_player = player_stock(test_stock, 'mcgeeja01', 'LAL', season(d))