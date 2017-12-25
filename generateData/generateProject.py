import random as rnd

# This is the code that was used to produce the matches.csv file.
# The code can be rerun to generate different matches data since the games are randomized.
def main():
    scientists = [
        "Grace Hopper", "Alan Turing", "Marie Curie",
        "Charles Darwin", "Nikola Tesla", "Gregor Mendel",
        "John von Neumann", "Ada Lovelace", "Georg Cantor",
        "David Hilbert"
        ]

    fileOut = open("matches.csv", "w")

    matchesCount = 200
    maxScore = 4

    fileOut.write("HomePlayer, AwayPlayer, HomeScore, AwayScore\n")
    for i in range(matchesCount):
        homePlayer = rnd.randint(0, len(scientists) - 1)
        awayPlayer = rnd.randint(0, len(scientists) - 2)
        if awayPlayer >= homePlayer:
            awayPlayer += 1
        homeScore = rnd.randint(0, maxScore)
        awayScore = rnd.randint(0, maxScore)
        fileOut.write("{}, {}, {}, {}\n".format(scientists[homePlayer], scientists[awayPlayer], homeScore, awayScore))

    fileOut.close()

main()