lst = [1, '2', 'three', True, None]

# new_lst = []
# for l in lst:
#     new_lst.append(l)

# print(new_lst)

new_lst = [l for l in lst]
print(new_lst)

#map
print('\nusing list comprehension to map thru list')
names = ['jerry', 'MARY', 'carrIE', 'larry']

# new_names = []
# for name in names:
#     new_names.append(name.title())

new_names=[name.title() for name in names]

print(new_names)

print('\nusing list comprehension to filter list')

nums = [1, 11, 12, 17, 19, 21, 27, 33, 40]
# new_nums = []
# for num in nums:
#     if num % 3 == 0:
#         new_nums.append(num)

new_nums = [num for num in nums if num % 3 == 0]
print(new_nums)

print('\nusing list comprehension instead of nested loops')

letters = ['a', 'b', 'c']
nums = [1,2]
# new_list1 = []
# for n in nums:
#     for l in letters:
#         new_list1.append((n, l))

# [value outer-for-loop inner-for-loop]
new_list1=[(n, l) 
                for n in nums 
                for l in letters]
print(new_list1)
