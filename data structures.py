# list
employees = [ 'John','Smith', 'Andrew', 'Jane' ]
print(employees)
print(employees[2])
print(employees[1:3])
employees[3] = 'Reuben'
print(employees)
employees.append('Stephen')
print(employees)
employees.insert(2, 'Juliana')
print(employees)
employees.extend(['Paul', 'Erick', 'Allan'])
print(employees)
# tuple
products = ('apple', 'banana', 'orange', 'strawberry')
print(products)
print(products[2])
print(products[1:3])
# products[0] = 'Mango'
print(products)
# set
students = {'peter','Esther','Ann','Oduor'}
students.add('Dennis')
print(students)
students.update(['Kimani'])
print(students)
students.remove('Ann')
print(students)
# dictionary
book = {
    'title': 'Book Title',
    'author': 'Ali',
    'publisher': 'Philadelphia',
}
print(book)
book['Year published'] = 2006
print(book)
print(book['author'])
print(book['title'])

if 'author' in book:
    print('author is in the book')
else:
    print('author is not present')


