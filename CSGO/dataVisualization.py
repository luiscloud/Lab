import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "archive/economy.csv",
    low_memory=False
)

headers = list(data.columns.values)

print(headers)
i = 0
for header in headers:
    print(i, " ", header)
    i += 1

dataList = data.values.tolist()

plt.plot(headers[9:24], dataList[0][9:24], color='green')
plt.plot(headers[24:39], dataList[0][24:39], color='green')
plt.plot(headers[9:24], dataList[0][39:54], color='red')
plt.plot(headers[24:39], dataList[0][54:69], color='red')

economy = []
veconomy = []
team = []
map = []
name = []
wins = []
teamnum = []

for row in dataList:
    if row[2] == 4901:
        if row[3] == "Natus Vincere" and row[4] != "G2":
            economy.append(row[9:39])
            veconomy.append(row[39:69])
            team.append(row[7] + row[8])
            map.append(row[6])
            name.append(row[3])
            wins.append(row[69:99])
            teamnum.append(1)
        if row[4] == "Natus Vincere" and row[3] != "G2":
            economy.append(row[39:69])
            veconomy.append(row[9:39])
            team.append(row[8] + row[7])
            map.append(row[6])
            name.append(row[4])
            wins.append(row[69:99])
            teamnum.append(2)


# plt.plot(headers[9:24], economy[0][0:15], color='red')
# plt.plot(headers[24:39], economy[0][15:30], color='red')
# print(team[0], map[0], name[0], teamnum[0])
# print(wins[0])
# print(len(name))

# pistol round win rate

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

# print(pwins)
###########
print(name[0])
for i in umaps:
    wrate = pwinspermap[i]/proundspermap[i]
    print(i, wrate)
#################################
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
            print(i, b, "vs", v, "CT", ctwrate, "T", twrate)

plt.show()