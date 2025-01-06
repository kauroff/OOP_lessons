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

print(dict_of_products)
print(dict_of_products[0].name)
print(dict_of_products[1].price)
print(dict_of_products[2].desc)
print(dict_of_products[3].quantity)
print(dict_of_categoryes)
print(dict_of_categoryes[0].name)
print(dict_of_categoryes[1].desc)
print(dict_of_categoryes[2].products)
print(data)
print(dict_of_products[3])
print(dict_of_categoryes[0].count_category)
print(dict_of_categoryes[0].uniq_products)
# Product.add_product({'name': 'Яблоко', 'description': 'Вкусное', 'price': 50.0, 'quantity': 17})
