# Define the AngryBird class
# Define the __init__() method which sets the x and y instance variables to 0
# Define the move_up_by() method which accepts a delta value and adds it to the y instance variable
# Create an AngryBird object
# Print the object
# Print the object's y value
# Move the AngryBird object by some amount
# Print the object's y value, again, to see that it moved

class AngryBird:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up_by(self, delta):
        self.y += delta



bird1 = AngryBird()
print(bird1)
print(bird1.y)
bird1.move_up_by(2)
print(bird1.x, bird1.y)