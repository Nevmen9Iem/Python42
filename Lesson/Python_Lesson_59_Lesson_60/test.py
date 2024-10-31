import pickle

l = []

with open('text.b', 'wb') as file:
    pickle.dump(l, file)

print('Done Write')

with open('text.b', 'rb') as file:
    print(pickle.load(file))

print('Done Read')
