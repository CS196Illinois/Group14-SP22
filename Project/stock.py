# from curses import reset_prog_mode
from datetime import datetime
from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player
from sportsipy.nba.boxscore import Boxscore

#teams = Teams()

class player_stock: 
    def __init__(self, player_code, shares, date):
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
        #shares user owns of player
        self.shares = shares

    def per_game_stats(self): #generates per game stats of the player
        ppg = self.ppg/self.gp
        rpg = self.rpg/self.gp
        apg = self.apg/self.gp
        spg = self.spg/self.gp
        bpg = self.bpg/self.gp
        tpg = self.tpg/self.gp
        
        season_avg = {
            "Points" : ppg,
            "Rebounds" : rpg,
            "Assists" : apg,
            "Steals" : spg,
            "Blocks" : bpg,
            "Turnovers" : tpg
        }
        return season_avg

    def magic(self): #logic to determine stock
        stats = self.per_game_stats()
        
        initial_stock = stats["Points"] + stats["Rebounds"]*1.2 + stats["Assists"]*1.5 + stats["Blocks"]*3 + stats["Steals"]*3 - stats["Turnovers"]
        game_stock = self.pts + self.reb*1.2 + self.ast*1.5 + self.blk*3 + self.stl*3 - self.tov
        diff = game_stock - initial_stock
        pct = 1 + (diff/initial_stock)
        pct -= 1
        return pct*10
class team_stock:
   def __init__(self, team_abbv, shares, date):
       self.team_season = Teams(team_abbv)
       query = "{:04d}{:02d}{:02d}0{}".format(date.year, date.month, date.day, "CLE") # self.player_season.team_abbreviation
       print(query)
       #retrieves season stats
       self.team_game = Boxscore(query)
    #    team_there = False;
       if self.abbv == self.team_game.winning_abbr or self.abbv == self.team_game.losing_abbr:
           self.bxp = self.team_game


       self.ppg = self.team_season.points
       self.rpg = self.team_season.offensive_rebounds + self.player_season.defensive_rebounds
       self.apg = self.team_season.assists
       self.spg = self.team_season.steals
       self.bpg = self.team_season.blocks
       self.tpg = self.team_season.turnovers
       self.gp = self.team_season.games_played
        #retrieves current game stats
       self.pts = self.bxp.points
       self.reb = self.bxp.offensive_rebounds + self.bxp.defensive_rebounds
       self.ast = self.bxp.assists
       self.stl = self.bxp.steals
       self.blk = self.bxp.blocks
       self.tov = self.bxp.turnovers
        #shares user owns of team
       self.shares = shares

   def per_game_stats(self): #generates per game stats of the player
       ppg = self.ppg/self.gp
       rpg = self.rpg/self.gp
       apg = self.apg/self.gp
       spg = self.spg/self.gp
       bpg = self.bpg/self.gp
       tpg = self.tpg/self.gp
        
       season_avg = {
           "Points" : ppg,
           "Rebounds" : rpg,
           "Assists" : apg,
           "Steals" : spg,
           "Blocks" : bpg,
           "Turnovers" : tpg
       }
       return season_avg

   def magic(self): #logic to determine stock
       stats = self.per_game_stats()
        
       initial_stock = stats["Points"] + stats["Rebounds"]*1.2 + stats["Assists"]*1.5 + stats["Blocks"]*3 + stats["Steals"]*3 - stats["Turnovers"]
       game_stock = self.pts + self.reb*1.2 + self.ast*1.5 + self.blk*3 + self.stl*3 - self.tov
       diff = game_stock - initial_stock
       pct = 1 + (diff/initial_stock)
       print(pct)
       return pct

d = datetime(2018, 6, 8)
test_player = player_stock('jamesle01', 1, d)
# test_team = team_stock("CLE", 2, d)  IDK why this isn't working