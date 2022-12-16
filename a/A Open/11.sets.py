a = {1,2,3}
b = {3,4,5}
# print(a)
# print(b)

# print(a | b) #union of two sets
# print(a & b) #intersection/overlap
# print(a - b) #the difference
# print(b - a)
# print(a ^ b) #semmetric difference


c = set('banana')
d = set('scarab')

# print(c.union(d))
# print(c.intersection(d))
# print(c.symmetric_difference(d))
# print(c.difference(d))

basket = ['apple', 'banana', 'apple', 'orange', 'pear', 'apple', 'banana']
# print(basket)
# print(list(set(basket)))

purchasingEmails = ('bob@gmail.com', 'sam@yahoo.com', 'riley@rileymail.org')
helpEmails = ('jo@josbilling.com', 'bob@gmail.com', 'sam@yahoo.com')
print(set(purchasingEmails) & set(helpEmails))
