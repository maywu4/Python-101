#like lists but immutable
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = ('a', 'b', 'c', 'd', 'e')
c = 10, 20, 30

# print(a)
# print(b)
# print(c)

# a.append(10)
# print(a) #AttributeError: 'tuple' object has no attribute 'append'

# a.sort() #AttributeError: 'tuple' object has no attribute 'sort'

#.sort() modifies original vs sorted() makes a sorted copy
shopping = ('apples', 'milk', 'bread')
alphaShopping = sorted(shopping)
# print(alphaShopping)

shoppingStops = (
    ['bread', 'milk', 'eggs'], 
    ['picture hooks', 'extension cord'],
)
# print(shoppingStops[0])
shoppingStops[0].append('apples')
# print(shoppingStops)

users = [
    (1, 'user_a'),
    (2, 'user_b'),
]

# print(users)

scores = (15, 66, 34, 99, 29, 54, 12)
# print(scores)
# print(max(scores))
# print(min(scores))
# print(sum(scores) / len(scores))
# print(tuple(sorted(scores)))

def minmax(numbers):
    return min(numbers), max(numbers)

myNums = (1 , 4, -2, 3.3, -8, 25, 9, 0)
# print(minmax(myNums)) #returns tuple: (-8, 25)

(lowest, highest) = minmax(myNums)
# print(lowest)
# print(highest)

#empty tuple
empty = ()
print(empty)

single = (1)
print(single) #shows 1 not tuple of single item

single = ('a',)
print(single)