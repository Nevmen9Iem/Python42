import pickle

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('text.b', 'wb') as file:
    pickle.dump(l, file)

print('Done')

with open('text.b', 'rb') as file:
    print(pickle.load(file))

print('Done Read')
