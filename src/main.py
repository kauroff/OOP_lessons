from func import Category, Product
import json

dict_of_categoryes = {}
dict_of_products = {}

with open('products.json', encoding='utf-8') as file:
    data = json.load(file)
for i in range(len(data)):
    name = data[i]['name']
    desc = data[i]['description']
    products = data[i]['products']
    dict_of_categoryes[i] = Category(name, desc, products)

count = 0
for i in range(len(data)):
    for n in range(len(data[i]['products'])):
        name = data[i]['products'][n]['name']
        desc = data[i]['products'][n]['description']
        price = data[i]['products'][n]['price']
        quantity = data[i]['products'][n]['quantity']
        dict_of_products[count] = Product(name, desc, price, quantity)
        count += 1
