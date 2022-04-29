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
    return dtrg_value(impact_value + reb_value)

def total_value(pts, ast, tos, per, ts, stls, blks, reb, dtrg):
    return offensive_value(pts, ast, tos, per, ts) + defensive_value(stls, blks, reb, dtrg)

# updated after game... total value with game stats not season averages
def net_change(pts, ast, tos, per, ts, stls, blks, reb, dtrg):
    avg_player = 809
    gm_value = (total_value(pts, ast, tos, per, ts, stls, blks, reb, dtrg) - avg_player)/ 82 
    return gm_value

# total val. w/szn avg

prices = [total_value(pts, ast, tos, per, ts, stls, blks, reb, dtrg)]
xs = pd.date_range(sdate, edate-timedelta(days=1), freq='d')

for d in xs:
    prev_value = prices[-1]
    next = prev_value + net_change(pts, ast, tos, per, ts, stls, blks, reb, dtrg)
    prices.append(next)

import matplotlib.pyplot as plt
import pandas as pd
from datetime import date, timedelta
import random

sdate = date(2019,3,22)   # start date
edate = date(2019,4,9)   # end date

ys = [random.random() for _ in range(18)]

plt.plot(xs, ys)
plt.show()