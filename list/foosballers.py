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

# add an fake player in the middle of the list
foosballers.insert(median,"Average Player")
print(foosballers)

outOfTheLeague = [ "Johnson", "Trump", "Ronald", "Michael", "Elvis"]
foosballers.extend(outOfTheLeague)
print(foosballers)

# findPosition = foosballers.index("Average Player")
foosballers.remove("Average Player")
print(foosballers)

# median player index
median = len(foosballers)//2 #integer division
print(foosballers[median])

# add an fake player in the middle of the list
foosballers.insert(median,"Average Player")
print(foosballers)

"""
- Lacy is one spot ahead of Hubert

- Omar is one spot behind Rebecca

- Otto is 8th best in the league

- Chauncey is 10 spots from the bottom of the league
"""
first = 0
foosballers[first] = "Lacy"
findPosition = foosballers.index("Rebecca")
foosballers.insert(findPosition + 1, "Omar")
position = 8
realIndex = position - 1
foosballers.insert(realIndex, "Otto")
foosballers.insert(-10, "Chauncey")
print(foosballers)




