

""" 
x = 3
y = float(3)
print(x,y)
 """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """
"""values = [1,2.23,5,7,2,30,15]
print(values)
print(values[0])
print(values[6])"""

""" x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z) """

""" x = input("write a sentence")
def wordcount():
    count = x.split()
    wc = len(count)
    print(wc)
wordcount()  """

""" bill = float(input("how much was the bill"))
service = input("how was the service(bad, okay, good, great)")
if service == "bad":
    tip = 0
elif service == "okay":
    tip = .15 * bill
elif service == "good":
    tip = .20 * bill
elif service == "great":
    tip = .25 * bill

def total():
    total = float(bill + tip)
    print(total)
total() """

""" day_of_the_week = input("what day is it")
if day_of_the_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")  """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """

""" factors = []
num = int(input("input a number"))
def find_factors():
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            print(factors)
find_factors()   """

""" number = int(input("state a number"))
if number % 2 == 0 :
    print("the number is even")
else:
    print("the number is odd") """

factors_of_num = []
factors_of_num_2 = []
num = int(input("input a number"))
num_2 = int(input("input another number"))
def find_factors():
    for i in range(1, num + 1):
        if num % i == 0:
            factors_of_num.append(i)
            print(factors_of_num)
    for i in range(1, num_2 + 1):
        if num % i == 0:
            factors_of_num_2.append(i) 
            print(factors_of_num_2)
   
find_factors() 