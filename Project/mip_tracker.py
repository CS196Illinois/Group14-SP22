from asyncio.windows_events import NULL
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
    
    teams = Teams()
    d = datetime(2019, 3, 23)

    # for team in teams:
    #     for player in team:
    #         if != NULL &&  != 0