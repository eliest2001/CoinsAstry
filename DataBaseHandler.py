import sqlite3



def coinsUser(user):
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute(f'''SELECT points FROM coins WHERE id=={user}''')
    coins = cur.fetchone()
    if coins is None:
        cur.execute(f'''INSERT INTO coins VALUES ('{user}','0','false','false','false')''')
        return 0
    else:
        return coins[0]


def addCoins(user, ncoins):
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute(f'''SELECT points FROM coins WHERE id=={user}''')
    coins = cur.fetchone()
    
    if coins is None:
        cur.execute(f'''INSERT INTO coins VALUES ('{user}','{ncoins}','false','false','false')''')
        con.commit()
        return int(ncoins)
    else:
        newcoins = int(coins[0]) + int(ncoins)
        cur.execute(f'''UPDATE coins SET points={newcoins} WHERE id=={user} ''')
        con.commit()
        return newcoins
    

def claimStickers(user):
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()    
    cur.execute(f'''SELECT points, stickers FROM coins WHERE id=={user}''')
    stickers = cur.fetchone()
    if stickers is None:
        cur.execute(f'''INSERT INTO coins VALUES ('{user}','0','false','false','false')''')           
    else:
        if(int(stickers[0]) >= 5 and stickers[1] != "true"):
            newcoins = int(stickers[0]) - 5
            cur.execute(f'''UPDATE coins SET points={newcoins}, stickers='true' WHERE id=={user} ''')
            con.commit()
            return newcoins
        else:
            if((int(stickers[0]) >= 5) == False):
                return -1
            else:
                return -2

def claimMonth(user):
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()    
    cur.execute(f'''SELECT points, month FROM coins WHERE id=={user}''')
    month = cur.fetchone()
    if month is None:
        cur.execute(f'''INSERT INTO coins VALUES ('{user}','0','false','false','false')''')           
    else:
        if(int(month[0]) >= 5 and month[1] != "true"):
            newcoins = int(month[0]) - 5
            cur.execute(f'''UPDATE coins SET points={newcoins}, month='true' WHERE id=={user} ''')
            con.commit()
            print("Free Month claimed successfully")
        else:
            if((int(month[0]) >= 5) == False):
                print("Not enough coins")
            else:
                print("Alredy claimed")

def claimHoodie(user):
    con = sqlite3.connect('DataBase.db')
    cur = con.cursor()
    cur.execute(f'''SELECT points, hoodie FROM coins WHERE id=={user}''')
    hoodie = cur.fetchone()
    if hoodie is None:
        cur.execute(f'''INSERT INTO coins VALUES ('{user}','0','false','false','false')''')           
    else:
        if(int(hoodie[0]) >= 5 and hoodie[1] != "true"):
            newcoins = int(hoodie[0]) - 5
            cur.execute(f'''UPDATE coins SET points={newcoins}, hoodie='true' WHERE id=={user} ''')
            con.commit()
            print("Hoodie claimed successfully")
        else:
            if((int(hoodie[0]) >= 5) == False):
                print("Not enough coins")
            else:
                print("Alredy claimed")

#cur.execute('''CREATE TABLE coins               (id text, points text, stickers text, month text, hoodie text )''')


#con = sqlite3.connect('DataBase.db')
    
#cur = con.cursor()
#cur.execute("INSERT INTO coins VALUES ('123','5','false','false','false')")
#con.commit()


