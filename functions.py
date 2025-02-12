def my_function():
    print("Hello World")
    print("Hello World")

my_function()
my_function()
my_function()

def my_function2():
    salute = "Hello World"
    print(salute)

my_function2()

def customers(salute):
    print(salute)
customers("Hello World")
customers("Hello Ken")
customers("Hello Anjela")

def employees(first_name, last_name,age):
    print(f'Hello {first_name} {last_name}you are {age} years old')

employees("Omar","kiptoo",13)
employees("Hillary","Njeri",20)
employees("William","Marsa",19)

def numbers(first_number, second_number):
   print(f'first_number is {first_number}, second_number is {second_number}')
   print(f'summation is {first_number + second_number}')
   print(f'subtraction is {first_number * second_number}')
numbers(1, 2)
numbers(2, 21)
numbers(10, 8)

def numbers2(first_number, second_number):
   total=first_number+second_number
   return total

def arithmetic(first_number, second_number):
   total = first_number+second_number
   product = first_number*second_number
   return (f'The product of {first_number} and {second_number} is :'
           f'{product} and the total is {total}')

print(arithmetic(5, 5))
print(arithmetic(55, 6))

def age_calculator(current_age):
   new_age = current_age+36
   return new_age
print(age_calculator(18))

def bet_bonus (name,correct_score):
   if correct_score >=9 and correct_score <=13:
      return f'{name}your bonus is 5000'
   elif correct_score >=6 and correct_score <=9:
      return f'{name}your bonus is 3000'
   elif correct_score >=4 and correct_score <=6:
      return f'{name}your bonus is 2000'
   else:
      return f'{name}your bonus is 0'
   print(bet_bonus('paul',2))
   print(bet_bonus('ken',13))


def greeting(name):
   if name == 'Alice':
      return f'Hello, {name} have a great day'
   elif name == 'Bob':
      return f'Hello, Bob have a great day'
   else:
      return f'Hello, {name}!'


print(greeting('Bob'))
print(greeting('Alice'))
print(greeting('Bob'))
print(greeting('harry'))





