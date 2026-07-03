# Practice set 03
#1
'''name = input("Enter your name:")
print(f"Good Morning, {name}")'''

#2

'''s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(len(s))'''

'''nums = [1, 2, 3, 4, 5]
nums.remove(3)
nums.pop(2)
print(nums)'''

'''a1 = int(input("Enter number1: "))
a2 = int(input("Enter number2: "))
a3 = int(input("Enter number3: "))
a4 = int(input("Enter number4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is:", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is:", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is:", a3)
else:
    print("Greatest number is:", a4)'''

# Function and Recursion--

#1
'''def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    else:
        return "All numbers are equal"

a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
c = int(input("Enter number3: "))
print("Greatest number is:", greatest(a,b,c))'''

#2
'''def f_to_c(f):
    c = (f-32)*5/9
    return c

f = int(input("Enter temperature in Fahrenheit: "))
c = f_to_c(f)
print(f"Temperature {f}°F in Celsius is: {round(c,2)}°C")'''

#3
'''print("a")
print("b")
print("c", end="")
print("d")
'''

#4
'''
sum(1) = 1
sum(2) = 1 + 2 = 3
sum(3) = 1 + 2 + 3 = 6
sum(4) = 1 + 2 + 3 + 4 = 10
sum(5) = 1 + 2 + 3 + 4 + 5 = 15
sum(n) = 1 + 2 + 3 + ... + (n-1) + n = (n*(n+1))/2
'''

'''def sum(n):
    if (n==1):
        return 1
    return (n*(n+1))/2

print("Sum of first n natural numbers is:", sum(5))'''

'''def sum(n):
    if (n==1):
        return 1
    return sum(n-1) + n

print("Sum of first n natural numbers is:", sum(5))'''

#5
'''def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)
   

n = int(input("Enter number of rows:"))
print(pattern(n))'''

#
'''f = open("file.txt","r")
line1 = f.readlines()
print(line1, type(line1))

line2 = f.readlines()
print(line2, type(line2))

line3 = f.readlines()
print(line3, type(line3))

line4 = f.readlines()
print(line4 == [])

f.close()'''

#sum of all digit 
'''a = 85476921
sum = 0

while a > 0:
    digit = a % 10     # Get the last digit
    sum = sum + digit   # Add the digit to sum
    a = a // 10    # Remove the last digit

print("Sum of digits =", sum)
'''

# reverse number
'''a = 9843

reverse = 0

while a > 0:
    digit = a % 10
    reverse = reverse * 10 + digit
    a = a // 10

print("Reversed number =", reverse)'''

