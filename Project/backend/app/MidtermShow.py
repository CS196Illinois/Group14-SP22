from app.stock import *
# w/szn averages
def offensive_value(pts, ast, tos, per, ts):
    pts_value = pts * 10
    ast_value = ast * 6.5
    tos_value = tos * -4.5
    ts_value = ts / 2
    return per * ts_value * (pts_value + ast_value + tos_value)

def defensive_value(stls, blks, reb, dtrg):
    impact_value = (stls + blks) * 8
    reb_value = reb * 5
    dtrg_value = 1000 / dtrg
    return dtrg_value * (impact_value + reb_value)

def total_value(pts, ast, tos, per, ts, stls, blks, reb, dtrg):
    return offensive_value(pts, ast, tos, per, ts) + defensive_value(stls, blks, reb, dtrg)

# updated after game... total value with game stats not season averages
def net_change(pts, ast, tos, per, ts, stls, blks, reb, dtrg):
    avg_player = 809
    gm_value = (total_value(pts, ast, tos, per, ts, stls, blks, reb, dtrg) - avg_player)/ 82 
    return gm_value

# total val. w/szn avg
import matplotlib.pyplot as plt
import pandas as pd
from sportsipy.nba.teams import Teams
from sportsipy.nba.schedule import Schedule
from datetime import datetime, timedelta
import random
def player_chart(player_name, player_team, sdate, edate):
    test_stock = {
        "pts" : 1,
        "reb" : 1,
        "ast" : 1,
        "stl" : 1,
        "blk" : 1,
        "tov" : 1 
    }
    #player_name= 'butleji01'
    s = season(edate)
    stock = player_stock(test_stock, player_name, player_team, s)

    team_games = Schedule(player_team, year=str(sdate.year))
    #sdate = datetime(2020, 9, 30)   # start date
    #edate = datetime(2020,10, 11)   # end date
    prices = [stock.share_val()]
    xs = pd.date_range(sdate-timedelta(days=1), edate-timedelta(days=1), freq='d')

    for i, d in enumerate(xs[1:]):
        if team_games.dataframe['datetime'].isin([d]).any() :
            
            try:
                pct_change = stock.magic(d)
                prev_value = prices[-1]
                next_value = (prev_value * (pct_change)) + prev_value
                prices.append(next_value)
            except TypeError:
                prices.append(prices[-1])
        else :
            prices.append(prices[-1])

    plt.switch_backend('Agg')
    plt.plot(xs, prices)
    plt.savefig(player_name + '.png')

# player_chart('adebaba01', 'MIA', datetime(2020, 9, 30), datetime(2020,10, 11))