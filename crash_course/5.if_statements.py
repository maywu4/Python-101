cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        # print(car.upper())
        pass
    else:
        # print(car.title())
        pass

requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")