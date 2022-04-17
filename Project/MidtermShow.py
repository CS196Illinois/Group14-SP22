from stock import *
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
test_stock = {
    "pts" : 1,
    "reb" : 1,
    "ast" : 1,
    "stl" : 1,
    "blk" : 1,
    "tov" : 1 
}
stock = player_stock(test_stock, 'jamesle01')

cle = Schedule("CLE", year=2018)
sdate = datetime(2018, 6, 1)   # start date
edate = datetime(2018,6,9)   # end date
prices = [stock.share_val()]
xs = pd.date_range(sdate, edate-timedelta(days=1), freq='d')

for i, d in enumerate(xs[1:]):
    print(i)
    if cle.dataframe['datetime'].isin([d]).any() :
        print(d, type(d))
        pct_change = stock.magic(d)
        prev_value = prices[-1]
        next_value = (prev_value * (pct_change)) + prev_value
        prices.append(next_value)
    else :
        prices.append(prices[-1])



test_player = player_stock(test_stock, 'jamesle01')
plt.plot(xs, prices)
plt.show()