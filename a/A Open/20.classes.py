class Invoice:
    __slots__ = ['_number', '_items']

    def __init__(self, number):
        self._number = number
        self._items = []

    def add_items(self, item):
        self._items.append(item)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value is not None:
            self._number = value
    
    #make method into getter property when its one line method that just returns value without changing the state of the object
    @property #takes total method into a property/can be invoked without parentheses
    def total(self):
        # t = 0
        # for item in self._items:
        #     t += item.total()
        # change the list of items to a list of totals(map)
        # add up all the items(totals)
        #return value
        return sum([item.total for item in self._items])


    def __repr__(self):
        return f"Invoice {self._number} ${self.total:.2f}"

class LineItem:
    __slots__ = ['_amount', '_description']
    def __init__(self, amount, description):
        self._amount = amount
        self._description = description


class FeeItem(LineItem):
    __slots__ = ['_rate']
    def __init__(self, rate, amount, description):
        super().__init__(amount, description)
        self._rate = rate

    @property
    def total(self):
        return self._rate * self._amount

class ExpenseItem(LineItem):
    __slots__ = ['_number', '_items']
    def __init__(self, amount, description):
        super().__init__(amount, description)

    @property
    def total(self):
        return self._amount

invoice = Invoice('A12345')
fee = FeeItem(100, 1.5, "Phone conversation")
expense = ExpenseItem(200, 'Copies')

invoice.add_items(fee)
invoice.add_items(expense)

# print(invoice.total)

print(invoice)
# print(fee.total)
# print(expense.total)

print(invoice.number)
invoice.number = 'B23456'
print(invoice.number)


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
# print(bird1)
# print(bird1.y)
bird1.move_up_by(2)
# print(bird1.x, bird1.y)

