users = [
    {'id':12323, 'displayName':'Joe Smith', 'email':'joe.smith@here.com'},
    {'id':22312, 'displayName':'Bob Smith', 'email':'bob.smith@here.com'},
    {'id':37373, 'displayName':'Jane Smith', 'email':'jane.smith@here.com'},
]
# print(users)

def sorter(user):
    return user['displayName'].lower()

users.sort(key=sorter)
print(users)

reverseUsers = sorted(users, key=sorter, reverse=True)
print(reverseUsers)