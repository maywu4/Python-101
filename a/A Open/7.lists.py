# ordered, mutable

# empty = []
# print(empty)

# friends = ['Monica', 'Chandler', 'Joey', 'Phoebe', 'Rachel', 'Ross']
# print(friends)

# print(friends[0])
# # print(friends[15])

# print(friends[-1]) #returns 1 item
# print(friends[1:-1]) #returns items in list
# print(friends[-1:]) #returns 1 item in list
# print(friends[1::2]) #returns every other item starting at idx 1 til end of list


# print(len(friends))
# print('Joey' in friends)

# scores = [159, 210, 188, 76]
# print(scores)

# teamScore = sum(scores)
# print(teamScore)

# highestScore = max(scores)
# print(highestScore)

# lowestScore = min(scores)
# print(lowestScore)

# average = sum(scores)/len(scores)
# print(average)

# rankedScores = sorted(scores, reverse=True)
# print(rankedScores)

# supplies = ['crayons', 'pencils', 'paper', 'Kleenex', 'eraser']
# print(supplies)

# supplies.append('markers')
# print(supplies)

# supplies.remove('crayons')
# print(supplies)

# supplies.sort()
# print(supplies)

# supplies.sort(key=str.lower)
# print(supplies)

colors = ['red', 'orange', 'blue', 'pink']
alphabetical = sorted(colors)
print(colors)
print(alphabetical)

alphabetical = sorted(colors, reverse=True)
print(alphabetical)

reversedColors = reversed(colors)
reverseAlpha = reversed(alphabetical)
print(reversedColors)
print(reverseAlpha)
print(list(reversedColors))
print(list(reverseAlpha))
