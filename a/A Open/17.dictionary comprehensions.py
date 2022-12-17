keys = ['age', 'name', 'height']
values = [32, "Corina", 1.4]
# d = dict()
# for i in range(len(keys)):
#     d[keys[i].title()] = values[i]

#{key: value for-loop}
# d = {keys[i].title(): values[i] for i in range(len(keys))}


d = {key: value for key, value in zip(keys, values)}
print(d)