# arithmetic operators(+,-,/,%/*)
a = 23
c = 14
total = a + c
print( "The total is ",total)
print(f'The total is {total}')
subtract = a - c
print("The subtract is ",subtract)
print(f'The subtract is {subtract}')

multiplication = a * c
print(f'The multiplication is {multiplication}')
division = a / c
print(f'The division is {division}')

remainder = a % c
print("The remainder is ",remainder)

# comparison operators(=,>,<.>=,<=,!=)
age1 = 25
age2 = 12
print(f'Is age1 equal to age2? {age1==age2}')
print(f'Is age1 greater than age2? {age1>age2}')
print(f'Is age1 less than age2? {age1<age2}')
print(age1>=age2)
print(age1<=age2)
print(age1!=age2)
# logical operators(and,or,not)
math = 67
science = 56
swahili = 78
french = 59
print(math>science and swahili>french)
print(math<science and swahili<french)
print(math>=science and swahili<=french)
print(math>science or swahili>french)
print(math>=science or swahili<french)
print(not(math>=science or swahili<=french))

num1 = float(input("enter the first number"))
num2 =float(input("enter the second number"))
num3 =float(input("enter the third number"))
num4 =float(input("the fourth number"))
result1=num1/num2
result2=num3/num4
result1 > result2
print(f"{result1} is grater than {result2}")
result1 < result2
print(f"{result1} is less than {result2}")
print(f"{result1} is equal to {result2}" )

result1 > 0 and result2 > 0
print("both results are positive.")
result1 < 0 and result2 < 0
print("both results are negative.")
result1== 0 or result2== 0
print("at least one result is zero.")
print("results are mixed(one positive one negative).")

username = input("enter your username")
password = input("enter your password")
username = "admin"
password = "secure123"

print(f'true if both are correct? {username == password}')
