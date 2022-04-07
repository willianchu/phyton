import math

foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

# median player index
median = len(foosballers)//2 #integer division
print(foosballers[median])

# 5 median players index
numberOfPlayers = 6
numberOfPlayersLessMedian = numberOfPlayers - 1
if (numberOfPlayersLessMedian) % 2 == 0:
  medianStart = int(median - (numberOfPlayersLessMedian/2))
  medianEnd = int(median + (numberOfPlayersLessMedian/2)) + 1
else:
  medianStart = int(median - math.ceil(numberOfPlayersLessMedian/2))
  medianEnd = int(median + math.floor(numberOfPlayersLessMedian/2)) + 1
print(medianStart)
print(medianEnd)
print(foosballers[medianStart:medianEnd])

#





