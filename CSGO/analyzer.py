import pandas as pd
import numpy as np

def analyze(teamname, opponent, eventid):

    eventid = set(eventid)

    data = pd.read_csv(
        "archive/economy.csv",
        low_memory=False
    )

    dataList = data.values.tolist()

    economy = []
    veconomy = []
    team = []
    map = []
    name = []
    wins = []
    teamnum = []

    for row in dataList:
        if row[2] in eventid:
            if row[3] == teamname and row[4] != opponent:
                economy.append(row[9:39])
                veconomy.append(row[39:69])
                team.append(row[7] + row[8])
                map.append(row[6])
                name.append(row[3])
                wins.append(row[69:99])
                teamnum.append(1)
            if row[4] == teamname and row[3] != opponent:
                economy.append(row[39:69])
                veconomy.append(row[9:39])
                team.append(row[8] + row[7])
                map.append(row[6])
                name.append(row[4])
                wins.append(row[69:99])
                teamnum.append(2)

    pwins = 0
    prounds = 0
    umaps = list(set(map))
    pwinspermap = {}
    proundspermap = {}

    for m in umaps:
        pwinspermap[m] = 0
    for m in umaps:
        proundspermap[m] = 0

    for i in range(len(name)):
        if wins[i][0] == teamnum[i]:
            pwins += 1
            pwinspermap[map[i]] += 1
        if wins[i][15] == teamnum[i]:
            pwins += 1
            pwinspermap[map[i]] += 1

        proundspermap[map[i]] += 2

    buytypes = "5000 10000 15000 20000".split()

    ctwinspermap = {}
    ctroundspermap = {}

    twinspermap = {}
    troundspermap = {}

    for m in umaps:
        twinspermap[m] = {}
        for b in buytypes:
            twinspermap[m][b] = {}
            for v in buytypes:
                twinspermap[m][b][v] = 0

    for m in umaps:
        troundspermap[m] = {}
        for b in buytypes:
            troundspermap[m][b] = {}
            for v in buytypes:
                troundspermap[m][b][v] = 0


    for m in umaps:
        ctwinspermap[m] = {}
        for b in buytypes:
            ctwinspermap[m][b] = {}
            for v in buytypes:
                ctwinspermap[m][b][v] = 0

    for m in umaps:
        ctroundspermap[m] = {}
        for b in buytypes:
            ctroundspermap[m][b] = {}
            for v in buytypes:
                ctroundspermap[m][b][v] = 0

    nonp = list(range(1,15)) + list(range(16,30))

    for i in range(len(name)):
        for c in nonp:
            eco = 0
            veco = 0
            if economy[i][c] >= 20000:
                eco = "20000"
            elif economy[i][c] >= 15000:
                eco = "15000"
            elif economy[i][c] >= 10000:
                eco = "10000"
            elif economy[i][c] < 10000:
                eco = "5000"

            if veconomy[i][c] >= 20000:
                veco = "20000"
            elif veconomy[i][c] >= 15000:
                veco = "15000"
            elif veconomy[i][c] >= 10000:
                veco = "10000"
            elif veconomy[i][c] < 10000:
                veco = "5000"

            if c < 15:
                if wins[i][c] == teamnum[i]:
                    if team[i][0] == 'c':
                        ctwinspermap[map[i]][eco][veco] += 1
                    elif team[i][1] == 'c':
                        twinspermap[map[i]][eco][veco] += 1
            elif c > 15:
                if wins[i][c] == teamnum[i]:
                    if team[i][0] == 'c':
                        twinspermap[map[i]][eco][veco] += 1
                    elif team[i][1] == 'c':
                        ctwinspermap[map[i]][eco][veco] += 1
                elif wins[i][c] != 3 - teamnum[i]:
                    break

            if c < 15:
                if team[i][0] == 'c':
                    ctroundspermap[map[i]][eco][veco] += 1
                elif team[i][1] == 'c':
                    troundspermap[map[i]][eco][veco] += 1
            elif c > 15:
                if team[i][0] == 'c':
                    troundspermap[map[i]][eco][veco] += 1
                elif team[i][1] == 'c':
                    ctroundspermap[map[i]][eco][veco] += 1

    digest = {}

    for m in umaps:
        digest[m] = {}
        for b in buytypes:
            digest[m][b] = {}
            for v in buytypes:
                digest[m][b][v] = {}

    for i in umaps:
        for b in buytypes:
            for v in buytypes:
                if ctroundspermap[i][b][v] != 0:
                    ctwrate = ctwinspermap[i][b][v] / ctroundspermap[i][b][v]
                else:
                    ctwrate = "nodata"
                if troundspermap[i][b][v] != 0:
                    twrate = twinspermap[i][b][v] / troundspermap[i][b][v]
                else:
                    twrate = "nodata"
                digest[i][b][v]["ctwrate"] = ctwrate
                digest[i][b][v]["twrate"] = twrate

    for i in umaps:
        wrate = pwinspermap[i] / proundspermap[i]
        digest[i]["pvp"] = wrate

    #####

    ctbuyspermap = {}
    ctlosspermap = {}

    tbuyspermap = {}
    tlosspermap = {}

    for m in umaps:
        tbuyspermap[m] = {}
        for b in buytypes:
            tbuyspermap[m][b] = 0

    for m in umaps:
        tlosspermap[m] = 0

    for m in umaps:
        ctbuyspermap[m] = {}
        for b in buytypes:
            ctbuyspermap[m][b] = 0

    for m in umaps:
        ctlosspermap[m] = 0

    for i in range(len(name)):
        for c in nonp:
            eco = 0
            if economy[i][c] >= 20000:
                eco = "20000"
            elif economy[i][c] >= 15000:
                eco = "15000"
            elif economy[i][c] >= 10000:
                eco = "10000"
            elif economy[i][c] < 10000:
                eco = "5000"

            if np.isnan(wins[i][c]):
                break

            if c < 15:
                if wins[i][c-1] == 3 - teamnum[i]:
                    if team[i][0] == 'c':
                        ctlosspermap[map[i]] += 1
                        ctbuyspermap[map[i]][eco] += 1
                    elif team[i][1] == 'c':
                        tlosspermap[map[i]] += 1
                        tbuyspermap[map[i]][eco] += 1
            elif c > 15:
                if wins[i][c-1] == 3 - teamnum[i]:
                    if team[i][0] == 'c':
                        tlosspermap[map[i]] += 1
                        tbuyspermap[map[i]][eco] += 1
                    elif team[i][1] == 'c':
                        ctlosspermap[map[i]] += 1
                        ctbuyspermap[map[i]][eco] += 1

    # print(ctbuyspermap)
    # print(ctlosspermap)
    # print(tbuyspermap)
    # print(tlosspermap)

    for i in umaps:
        digest[i]["lossbuyprob"] = {}
        for b in buytypes:
            digest[i]["lossbuyprob"][b] = {}

    for i in umaps:
        for b in buytypes:
            if ctlosspermap[i] != 0:
                digest[i]["lossbuyprob"][b]["ct"] = ctbuyspermap[i][b] / ctlosspermap[i]
                # print(i, b, "ct",str(ctbuyspermap[i][b] / ctlosspermap[i]))
            else:
                digest[i]["lossbuyprob"][b]["ct"] = 0.25
            if tlosspermap[i] != 0:
                digest[i]["lossbuyprob"][b]["t"] = tbuyspermap[i][b] / tlosspermap[i]
                # print(i, b, "t",str(tbuyspermap[i][b] / tlosspermap[i]))
            else:
                digest[i]["lossbuyprob"][b]["t"] = 0.25

    #####

    return digest

team1 = "Natus Vincere"
team2 = "G2"
t1side = "ct"
t2side = "t"
eventid = {4901}

adata = analyze(team1, team2, eventid)
# bdata = analyze(team2, team1, eventid)

print(adata["Nuke"]["pvp"])
# print(bdata["Nuke"]["pvp"])
# print("Pistol Navi Win", str(adata["Nuke"]["pvp"]/(adata["Nuke"]["pvp"]+bdata["Nuke"]["pvp"])), "Pistol G2 Win", str(bdata["Nuke"]["pvp"]/(adata["Nuke"]["pvp"]+bdata["Nuke"]["pvp"])))
print(adata["Mirage"]["20000"]["20000"]["twrate"])