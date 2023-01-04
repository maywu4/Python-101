class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{(self.restaurant_name).title()} serves {(self.cuisine_type).title()} food.")

    def open_restaurant(self):
        print(f"{(self.restaurant_name).title()} is open.")


restaurant = Restaurant('Bobs Burgers', 'American')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


class User: 
    def __init__(self, first, last, username, age):    
        self.first_name = first
        self.last_name = last
        self.username = username
        self.age = age

    def describe_user(self):
        print(f"User {self.username} is named {self.first_name} {self.last_name} and is {self.age} years old.")


player_one = User('Keanu', 'Reeves', 'Neo', 28)
player_one.describe_user()