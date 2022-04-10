from sportsipy.nba.teams import Teams
from sportsipy.nba.roster import Player

embiid_proj = {"points": 29.7, "rebounds": 11.1, "assists": 4.5, "blocks": 1.4, "steals": 1.0, "turnovers": 2.6}

def percent(stockf, stocki): #Finds the percentage up or down you are on the player
    pct = (stockf/stocki)
    pct = pct - 1
    return pct

def money(shares, percent): #returns the amount of money gained/lost
    return shares*percent

def stock(pts, reb, ast, blk, stl, tov, shares): #algorithm to determine stock
    i_stock = embiid_proj["points"] + embiid_proj["rebounds"]*1.2 + embiid_proj["assists"]*1.5 + embiid_proj["blocks"]*3 + embiid_proj["steals"]*3 - embiid_proj["turnovers"]
    f_stock = (pts-embiid_proj["points"]) + (reb-embiid_proj["rebounds"])*1.2 + (ast-embiid_proj["assists"])*1.5 + (blk-embiid_proj["blocks"])*3 + (stl-embiid_proj["steals"])*3 - (tov-embiid_proj["turnovers"])
    val = i_stock + (f_stock/i_stock)
    val = shares*val
    print(percent(f_stock, i_stock))
    print("Money: " + str(money(shares, percent(f_stock, i_stock))))
    return val

stock(20, 8, 2, 2, 1, 4, 20) #test case