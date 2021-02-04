from analyzer import analyze

# digest[map][round][round][ct/t] = wrate
# digest[map][pround] = wrate

buytypes = "5000 10000 15000 20000".split()

team1 = "Astralis"
team2 = "Liquid"
t1side = "ct"
t2side = "t"
eventid = {4889}

adata = analyze(team1, team2, eventid)
bdata = analyze(team2, team1, eventid)

print(adata)
print(bdata)

for e in adata:
    print(e)

print(" --- --- --- ")

for e in bdata:
    print(e)

map = "Nuke"

# pistol round winner

prating = {}

prating[team1] = adata[map]["pvp"]
prating[team2] = bdata[map]["pvp"]

presult = {}

presult[team1] = prating[team1] / (prating[team1] + prating[team2])
presult[team2] = prating[team2] / (prating[team1] + prating[team2])

print(presult)

# simulate the game

crate = []

crate.append(presult)

print(crate)

for i in range(1,15):

    ift1won = 0

    for b in buytypes:
        v = b
        while adata[map]["20000"][v][(t1side + "wrate")] == "nodata":
            v = str(int(v) + 5000)
            if int(v) == 25000:
                adata[map]["20000"]["20000"][(t1side + "wrate")] = prating[team1]
                v = "20000"
                print("caughtt1")
        ift1won += (adata[map]["20000"][v][(t1side + "wrate")] * bdata[map]["lossbuyprob"][b][t2side])

    ift2won = 0

    for b in buytypes:
        v = b
        while bdata[map]["20000"][v][(t2side + "wrate")] == "nodata":
            v = str(int(v) + 5000)
            if int(v) == 25000:
                bdata[map]["20000"]["20000"][(t2side + "wrate")] = prating[team2]
                v = "20000"
                print("caughtt2")
        ift2won += (bdata[map]["20000"][v][(t2side + "wrate")] * adata[map]["lossbuyprob"][b][t1side])

    rresult = {}
    rresult[team1] = ift1won * crate[i-1][team1] + (1-ift2won) * crate[i-1][team2]
    rresult[team2] = (1-ift1won) * crate[i-1][team1] + ift2won * crate[i-1][team2]

    crate.append(rresult)

for e in crate:
    print(e)

predictedscoremult = 0

if crate[14][team1] > crate[14][team2]:
    predictedscoremult = 16 / crate[14][team1]
if crate[14][team1] < crate[14][team2]:
    predictedscoremult = 16 / crate[14][team2]

print(map, "Predicted Score:", (crate[14][team1] * predictedscoremult), "to", (crate[14][team2] * predictedscoremult))