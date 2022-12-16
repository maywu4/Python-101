pond = dict(
    dept = 10,
    area = '210 square feet',
    fish = ['Mary', 'Bob', 'Billy']
)

print(pond)

alligator = dict([
    ('lifespan', 50),
    ('length', 3.4),
    ('lengthUnits', 'm')
])
print(alligator)

keys = ['name', 'home runs', 'strikeouts', 'rbi']
values = ['Babe Ruth', 7214, 1330, 2214]
player = dict(zip(keys, values))
print(player)