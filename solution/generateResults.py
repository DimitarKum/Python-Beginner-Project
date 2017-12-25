# WARNING: THIS IS THE SOLUTION
# DO NOT LOOK AT THIS CODE BEFORE ATTEMPTING TO SOLVE THE PROBLEM!

def createTable(players):
    table = dict()
    for player in players:
        table[player] = list()
    return table

def getWinLossTies(fileName, players):
    fileIn = open(fileName, "r")

    # Advance file pointer after line 1 to start reading games data
    headerRow = fileIn.readline()

    winTable, lossTable, tieTable = createTable(players), createTable(players), createTable(players)

    for line in fileIn:
        data = line.split(",")

        homePlayer = data[0].strip()
        awayPlayer = data[1].strip()
        homeScore = int(data[2])
        awayScore = int(data[3])

        if homeScore > awayScore:
            # Home team is winner, away team is loser
            winTable[homePlayer].append(awayPlayer)
            lossTable[awayPlayer].append(homePlayer)
        elif homeScore < awayScore:
            # Home team is loser, away team is winner
            winTable[awayPlayer].append(homePlayer)
            lossTable[homePlayer].append(awayPlayer)
        elif homeScore == awayScore:
            # Game is tie
            tieTable[homePlayer].append(awayPlayer)
            tieTable[awayPlayer].append(homePlayer)

    fileIn.close()
    return winTable, lossTable, tieTable

def generateResults(players, winTable, lossTable, tieTable, fileName):
    fileOut = open(fileName, "w")
    fileOut.write("Player, Win Indices, Loss Indices, Tie Indices\n")
    for player in players:
        playersWonAgainst = winTable[player]
        playersLossAgainst = lossTable[player]
        playersTiedAgainst = tieTable[player]

        winStartIndex = 5
        winEndIndex = winStartIndex + len(playersWonAgainst)
        lossStartIndex = winEndIndex + 1
        lossEndIndex = lossStartIndex + len(playersLossAgainst)
        tieStartIndex = lossEndIndex + 1
        tieEndIndex = tieStartIndex + len(playersTiedAgainst)

        winIndices = str(winStartIndex) + " - " + str(winEndIndex)
        lossIndices = str(lossStartIndex) + " - " + str(lossEndIndex)
        tieIndices = str(tieStartIndex) + " - " + str(tieEndIndex)

        fileOut.write(
            "{}, {}, {}, {}, {}, {}, {}\n".format(
                player,
                winIndices,
                lossIndices,
                tieIndices,
                ", ".join(playersWonAgainst),
                ", ".join(playersLossAgainst),
                ", ".join(playersTiedAgainst)
                )
             )

    fileOut.close()

def main():
    players = [
        "Grace Hopper", "Alan Turing", "Marie Curie",
        "Charles Darwin", "Nikola Tesla", "Gregor Mendel",
        "John von Neumann", "Ada Lovelace", "Georg Cantor",
        "David Hilbert"
        ]
    winTable, lossTable, tieTable = getWinLossTies("matches.csv", players)
    generateResults(players, winTable, lossTable, tieTable, "results.csv")

main()