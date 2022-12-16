titles1 = ['Mr', 'Mrs', 'Ms']
titles2 = ['Mr', 'Mrs', 'Ms', '']
titles3 = []
print(all(titles1))
print(all(titles2))
print(all(titles3)) #looking for any false items - no items = no false items


print('\nany()') #looking for any item to be true
feedback1 = ['', '', '', '']
feedback2 = ['So much fun!', '', '', '']
feedback3 = []
print(any(feedback1))
print(any(feedback2))
print(any(feedback3))