from curses import reset_prog_mode
from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player
from sportsipy.nba.boxscore import BoxscorePlayer

#teams = Teams()

class player_stock: 
    def __init__(self, player_code, shares):
        #retrieves player code
        self.name = player_code
        self.player_season = Player(self.name)
        self.player_game = BoxscorePlayer(self.name)
        #retrieves season stats
        self.ppg = self.player_season.points
        self.rpg = self.player_season.offensive_rebounds + self.player_season.defensive_rebounds
        self.apg = self.player_season.assists
        self.spg = self.player_season.steals
        self.bpg = self.player_season.blocks
        self.tpg = self.player_season.turnovers
        self.gp = self.player_season.games_played
        #retrieves current game stats
        self.pts = self.player_game.points
        self.reb = self.player_game.offensive_rebounds + self.player_game.defensive_rebounds
        self.ast = self.player_game.assists
        self.stl = self.player_game.steals
        self.blk = self.player_game.blocks
        self.tov = self.player_game.turnovers
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

    def magic(self): #algorithm to determine stock
        stats = self.per_game_stats()
        
        initial_stock = stats["Points"] + stats["Rebounds"]*1.2 + stats["Assists"]*1.5 + stats["Blocks"]*3 + stats["Steals"]*3 - stats["Turnovers"]
        game_stock = self.pts + self.reb*1.2 + self.ast*1.5 + self.blk*3 + self.stl*3 - self.tov
        diff = game_stock - initial_stock
        pct = initial_stock + (diff/initial_stock)
        print(pct)
        return pct

test_player = player_stock(bridgmi01, 1)
print(test_player)