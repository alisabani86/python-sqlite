#List Manipulation:
# a function to return even numbers from a list in descending order.
def list_manipulation(numbers):
    even = []
    for i in numbers:
        if i%2 == 0:
            even.append(i)
    even.sort(reverse=True)
    return even
#testing for function
print(list_manipulation([1,2,3,4,5,6,7,8,9,10]))

#Dictionary Handling:
# Turn a list of tuples (name, age) into a dictionary with names as keys.
def list_to_dict(peoples):
    dictionary_peoples = {people[0]: people[1] for people in peoples}
    return dictionary_peoples

#testing for dictionary handling
people = [("John", 25), ("Jane", 30), ("Alice", 22), ("Bob", 27)]
print(list_to_dict(people))

#Range Sum Function:
# a function to sum all numbers between two integers,inclusive.
def range_sum(start, end):
    return sum(range(start, end + 1))
#testing for range sum function
print(range_sum(1, 5))


#Data Filter:
#  filter a list of products (name, price, category), return those in a given category with a price over 20.
def filter_products(products, category):
    filtered_products = [product for product in products if product['category'] == category and product['price'] > 20]
    return filtered_products


products = [
    {"name": "Product 1", "price": 25, "category": "Electronics"},
    {"name": "Product 2", "price": 15, "category": "Electronics"},
    {"name": "Product 3", "price": 30, "category": "Books"},
    {"name": "Product 4", "price": 50, "category": "Books"}
]
print(filter_products(products, "Books"))

