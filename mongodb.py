from pymongo import MongoClient, errors
import json
from itertools import cycle
from pprint import pprint

#метод присваивания id по наименованию книги
def encode(text) -> str:
    return '_'.join([str(ord(i)) for i in text])

#загрузил список словарей с книгами
with open('books.json', 'r') as f:
    list_dict = json.load(f)

pprint(list_dict)

client = MongoClient('localhost', 27017)
db = client['toscrape']
books = db.books
duplicate = db.duplicate

for dict_ in list_dict:
    dict_['_id'] = encode(dict_['name']) 
    try:
        books.insert_one(dict_)
    except errors.DuplicateKeyError as e:
        print(e, dict_['_id'])
        duplicate.insert_one(dict_)

#запросы
for book in books.find({'name': "1st to Die (Women's ..."}):
    print(book)

for book in books.find({'amount': 0}):
    print(book)

for book in books.find({'amount': 0}):
    print(book)

for book in books.find({"$or": [{'amount': 0}, {'price': 53.98}]}):
    print(book)

for book in books.find({'amount': {'$gt': 5}}):
    print(book)