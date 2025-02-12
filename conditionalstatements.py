# if.....else....
# loops
votes = 500
if votes > 10000:
    print(f"You got {votes} and therefore you win!")
else:
    print(f"You got {votes} and therefore you lose!")





marks = 100
if marks > 80 and marks <= 100 :
    print(f"You got {marks} and you have grade A")
elif marks > 70 and marks <= 80 :
    print(f"You got {marks} and you have grade B")
elif marks > 60 and marks <= 70 :
    print(f"You got {marks} and you have grade C")
elif marks > 40 and marks <= 60 :
    print(f"You got {marks} and you have grade D")
elif marks > 40 and marks <= 40 :
    print(f"You got {marks} and you have grade E")
else:
    print('Please enter a number between 0 and 100')


age = 55
if age > 2:
    print(f"You are {age} you are a baby")
elif age >= 2 and age <= 3:
    print(f"You are {age} you are a toddler")
elif age >= 4 and age <= 12:
    print(f"You are {age} you are a child")
elif age >= 13 and age <= 19:
    print(f"You are {age} you are a teenager")
elif age >= 20 and age <= 34:
    print(f"You are {age} you are a young adult")
elif age >= 35 and age <= 59:
    print(f"You are {age} you are a middle-aged adult")

else:
    print(f'you are a senior citizen')
    print('Age is just a number, enjoy life !')

current_temperature = float(input("Enter your current temperature: "))
if current_temperature> 30:
    print(f"You are {current_temperature} it is a hot day")
elif current_temperature > 20 and current_temperature <= 30:
    print(f"You are {current_temperature} it is a cold day")
elif current_temperature <=20 and current_temperature <= 30:
    print(f"You are {current_temperature} it is a cold day")
else:
    print(f'invalid temperature')

amount = float(input("Enter your amount: "))
if amount > 15000:
    print(f'your total amount withdrawal is: {10/100}')
elif amount < 5000:
    print(f'your total amount withdrawal is: {5/100}')
else:
    print(f'invalid amount')



