#numbers
num1 = 42
num2 = 2.3
#Boolean
boolean = True
#strings
string = 'Hello World'
#List 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#Dictionaries
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#Tuples
fruit = ('blueberry', 'strawberry', 'banana')
#type check
print(type(fruit))
#List access value
print(pizza_toppings[1])
#List  ADD VALUE
pizza_toppings.append('Mushrooms')
#Dictionary  access value
print(person['name'])
#Dictionary change value
person['name'] = 'George'
#Dictionary ADD VALUE
person['eye_color'] = 'blue'
#Tuples access value
print(fruit[2])
#conditional
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#if else if else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#For loop
# 5 is stop
for x in range(5):
    print(x)
#2 is start and 5 is stop
for x in range(2,5):
    print(x)
#2 is start and 10 is stop and 3 is step    
for x in range(2,10,3):
    print(x)
#while loop start from 0 stop at 5 increment 1
x = 0
while(x < 5):
    print(x)
    x += 1
#list delete value
pizza_toppings.pop()
pizza_toppings.pop(1)
#Dictionary delete value
print(person)
person.pop('eye_color')
print(person)
#for loop continue and break
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#function name : print_hello_ten_times
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#function argument
print_hello_ten_times()
#function name : print_hello_x_times parameter : x
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#function argument 
print_hello_x_times(4)
#function name : print_hello_x_or_ten_times parameter : x= 10 
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""
# NameError: name <variable name> is not defined
#print(num3)

#num3 = 72

#TypeError: 'tuple' object does not support item assignment
#fruit[0] = 'cranberry'

#KeyError: 'favorite_team'
#print(person['favorite_team'])

#IndexError: list index out of range
#print(pizza_toppings[7])

#IndentationError: unexpected indent
#   print(boolean)

#AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')

#AttributeError: 'tuple' object has no attribute 'pop'
#fruit.pop(1)