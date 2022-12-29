magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician)
    pass


pizzas = ['cheese', 'artichoke', 'hawaiian']
for pizza in pizzas:
    # print(f"My favorite pizza is {pizza} pizza.")
    pass

# print('Pizza is my favorite meal.')

animals = ['cat', 'dog', 'goldfish']
for animal in animals:
    # print(f"A {animal} would make a great pet.")
    pass

# print("Any of these animals would make a great pet.")

# print(list(range(1,5)))
even_numbers = list(range(2,11,2))
# print(even_numbers)

squares = [value**2 for value in range(1, 11)]
# print(squares)

#4-3
for n in range(1, 21):
    # print(n)
    pass

#4-5
till_a_mill = list(range(1, 1_000_001))
# print(min(till_a_mill))
# print(max(till_a_mill))
# print(sum(till_a_mill))

#4-6
for odd in range(1,21,2):
    # print(odd)
    pass

#4-7
for three in range(3,31,3):
    # print(three)
    pass

#4-8
# cubes = []
# for i in range(1,11):
#     cubes.append(i**3)

# for cube in cubes:
#     print(cube)

#4-9
cubes = [num**3 for num in range(1,11)]
# print(cubes)

#4-10
pizzas.append('pepperoni')
pizzas.append('vegetarian')
pizzas.append('buffalo chicken')
pizzas.sort()
print(pizzas)
print(f"The first three items in the list are {pizzas[:3]}.")
print(f"The two middle items in the list are {pizzas[2:4]}.")
print(f"The last three items in the list are {pizzas[-3:]}.")