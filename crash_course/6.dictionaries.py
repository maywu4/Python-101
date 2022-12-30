alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['color'])
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


# print(list(user_0.items()))