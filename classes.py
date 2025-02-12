class person:
    first_name = "Alex"
    last_name = "Kibunja"
    gender = "female"
    age = 19

class Employee:
    def __init__(self, name, gender, basic_salary, age, position):
        self.name = name
        self.gender = gender
        self.basic_salary = basic_salary
        self.age = age
        self.position = position

    def display_employees(self):
        return f"Name: {self.name}, Gender: {self.gender},"

    def full_salary(self):
        full_salary = self.basic_salary + 25000
        return full_salary




class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class Rectangle:
    def __init__(self, length, width):
        # Initialize the length and width of the rectangle
        self.length = length
        self.width = width

    def perimeter(self):
        # Calculate and return the perimeter of the rectangle
        return 2 * (self.length + self.width)

    def area(self):
        # Calculate and return the area of the rectangle
        return self.length * self.width

    def display(self):
        # Display the length and width of the rectangle
        print(f"Length: {self.length}, Width: {self.width}")

class Emobilis_Employee:
    def __init__(self, name, gender, salary, age, qualification):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.age = age
        self.qualification = qualification

    def promotion(self):
        if self.qualification == "Degree":
            return "You are promoted"
        else:
            return "You are not promoted"

class Developer(Emobilis_Employee):
    def __init__(self, name, gender, salary, age, qualification,specialization,prog_language):
        super().__init__(name,gender,salary,age,qualification)
        self.specialization = specialization
        self.prog_language = prog_language

class Teacher(Emobilis_Employee):
    def __init__(self,name,salary,gender,age,prog_language,experience,rewards):
        super().__init__(name,gender,age)
        self.prog_language = prog_language
        self.experience = experience
        self.rewards = rewards


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        # """Method to deposit money into the bank account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # """Method to withdraw money from the bank account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        # """Method to display the account details."""
        print(f"Account holder: {self.account_holder}")
        print(f"Account balance: {self.balance}")

# Child class 1: CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # """Override withdraw method to consider overdraft limit."""
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                print(f"Withdrew {amount} with overdraft. New balance: {self.balance}")
            else:
                print("Exceeds overdraft limit and available funds.")
        else:
            print("Withdrawal amount must be positive.")

# Child class 2: SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # """Method to apply interest to the balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: {interest}. New balance: {self.balance}")

