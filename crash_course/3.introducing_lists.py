motorcycles = ['honda', 'yamaha','suzuki']
motorcycles.append('ducati')
# print(motorcycles)

motorcycles = ['honda', 'yamaha','suzuki']
motorcycles.insert(0, 'ducati')
# print(motorcycles)

del motorcycles[3]
# print(motorcycles)

#3-4 Guest List

guests = ['guest 1', 'guest 2', 'guest 3']
for guest in guests:
    # print(f"Invitation for {guest.title()}.")
    pass

busy_guest = guests[1]
print(f'{busy_guest.title()}')

#3-5
guests.pop(1)
# print(guests)
guests.insert(1, 'new guest 2')
# print(guests)
for guest in guests:
    # print(f"New Invitation for {guest.title()}.")
    pass

#permanently sorting a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

#temporarily sorting a list
print('Here is the original list:')
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again")
print(cars)