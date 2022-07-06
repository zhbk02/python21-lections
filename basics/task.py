import json

with open('HarryPotterBooks.json') as my_file:
    dictionary = json.load(my_file)
    data = dictionary['books']
    for book in data:
        book['author'] = 'J.K Rowling'

with open('HarryPotterBooks', 'w') as my_file:
    json.dump(dictionary, my_file)