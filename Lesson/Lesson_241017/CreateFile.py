import pickle

l = []

with open('text.b', 'wb') as file:
    pickle.dump(l, file)

print('Done Write')
