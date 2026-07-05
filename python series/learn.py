# print("hello world")

# Comments--

'''single line comments(#)
multi line commnets (''' ''' and """ """)'''

# Module--

''' 1.Built-in Module
 2.External module'''


# Escape Sequences--

# \\	Backslash (\)
# \'	Single quote (')
# \"	Double quote (")
# \n	New line
# \t	Horizontal tab
# \r	Carriage return
# \b	Backspace
# \f	Form feed
# \v	Vertical tab
# \a	Alert/Bell sound
# \0	Null character
# \ooo	Character with octal value
# \xhh	Character with hexadecimal value
# \uXXXX	Unicode character (16-bit)
# \UXXXXXXXX	Unicode character (32-bit)
# \N{name}	Unicode character by name


# VARIABLE & DATA TYPES--

# Variable->
'''a = 1 #here a and b are the variable 
b = 3
c = "kuldeep" #c is the string value 
print(a+b)
print(c)'''

# Data Types->
'''- int (1,2,3 etc.)
   - float (5.2,5.1 etc.)
   - strings ("harry","kuldeep"etc.)
   - boolean (True,False)
   - None (none)'''


# Strings--  strings are immutable (cannot be changed) and ordered (indexing is possible)
# a = 'kuldeep'
# a = "kuldeep"
# a = '''kuldeep'''

# String slicing-> 

'''a = "kuldeep goswami"
print(a[0:11])
print(a[-12:-1])
print(a[0:13:2])
print(a[:8])
print(a[2:])'''

# String Functions->

'''name = "Kuldeep"
print(len(name))
print(name.upper())
print(name.lower())
print(name.strip())
print(name.capitalize())
print(name.replace("Kuldeep", "Kuldeep Goswami"))
print(name.endswith("eep"))
print(name.startswith("Kul"))
print(name.count("Kuldeep"))
print(name.find("deep"))
'''


# Lists-- lists are mutable (can be changed) and ordered (indexing is possible)

'''name =["kuldeep","goswami","born","2004","student","Engineering"]
print(name[0])
print(name[3])

name[0] = "kundan"
print(name[0])

name[3] = "2010"
print(name[3])

print(name[0:5])
print(name[-2:-1])
print(name[0:4:2])
print(name[:3])
print(name[0:])'''

#List methods->

'''l1 = [1, 34,62, 2, 6, 11]

l1.append("Harry")
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
# l1.pop(3)
# l1.remove(6)
print(l1)'''


#Tuples-- tuples are immutable (cannot be changed) and ordered (indexing is possible)

'''t = (1, 2, 3, 2, 2, 4)
print(t.count(2))

t = (10, 20, 30, 40)
print(t.index(30))

# Operations on tuples->

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(t1 + t2)

# repetition
print(t1 * 3)

# Indexing
print(t1[0])
print(t1[-1])

# Slicing
t = (10, 20, 30, 40, 50)
print(t[1:4])

# Membership operators 
print(2 in t1)
print(10 not in t1)

# Iteration
for item in t1:
    print(item)

# Length 
print(len(t1))

# Finding Maximum and Minimum
t = (10, 50, 20, 5)
print(max(t))
print(min(t))

#Sum of Elements
t = (10, 20, 30)
print(sum(t))

#Tuple Packing and Unpacking
t = (10, 20, 30)
a, b, c = t
print(a, b, c)'''


# Dictionaries-- dictionaries are mutable (can be changed) and unordered (indexing is not possible)

'''d = {} # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
     0: "kuldeep"
    
}
# print(marks, type(marks))
# print(marks["Harry"])

# Methods of dictionary->
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Shubham": 90, "Rohan":50, "Kelly": 75})
print(marks)
print(marks.get("Shubham"))
print(marks["Shubham"])

print(marks.get("Shubham2")) # It return none if key is not present in dictionary
print(marks["Shubham2"]) # It will give error if key is not present in dictionary
'''


# Sets-- sets are mutable (can be changed) and unordered (indexing is not possible)
# sets is a collection of unique elements # sets cannot have duplicate elements 

'''s = {1, 2, 3, 4, 5, 2, 2, 1, 3, 1} #sets are not repetitive and unordered
# print(s, type(s))
# e = set() # empty set 
#print(s)

# Methods of sets->

#s.len()
#s.add(6)
#s.remove(3)
#s.discard(4)
#s.pop()
#s.clear()
print(s)
'''
'''s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(s1.union(s2))
print(s1.intersection(s2))'''


# Conditional Expressions--

# if - else statements->

'''a = int(input("Enter your age: "))

if (a>=18):
    print("You are eligible to vote")
    print("You have rights to choose your leader")

else:
    print("You are not eligible to vote")
    print("You do not have the right to choose your leader")

print("Thank you for using our service")'''

# elif statements->

'''a = int(input("Enter your age: "))

if (a>=18):
    print("You are eligible to vote")
    print("You have rights to choose your leader")

elif(a<0):
    print("You have entered invalid age\nPlease enter again!")

else:
    print("You are not eligible to vote")
    print("You do not have the right to choose your leader")

print("Thank you for using our service")'''


# Short Hand if-else statements->

'''a = int(input("Enter any number: "))
print("Enter number: ",a)

b = int(input("Enter any number: "))
print("Enter number: ",b)

print("A") if a>b else print("==") if a==b else print("B")

c = "True" if a>b else ""
print(c)
'''

# Match case statements--

'''x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    # case with if condition
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)'''


# LOOPS--

# For loops->

'''for i in range(10,100,2):
    print(i)'''

'''for k in range(1,2000):
        print(k)
        '''

'''colors =["red","green","blue","purple","yellow"]
for color in colors:
    print(color)
    for i  in color:
        print(i)'''

# For loop with string->
'''s="ABC"
for c in s:
    print(c) '''

# For loop with list->
'''numbers=[10,-3,5,100,0]
for num in numbers:
    if num >= 0:
     print(num)'''

#For loop with tuple->
'''t = (1,5,2,8,9)
for i in t:
    print(i)'''

# For loop with dictionries->
'''d={'UP':'Lucknow','Delhi':'New Delhi'}
for key in d:
    print(key,d[key])'''

# For loop with else->
'''l = [1,7,8]
for i in l:
    print(i)
else:
    print("done")'''

# While Loop->

'''i = 0
while(i<=5):
    print(i)
    i += 1
print("Done with the loop")'''

# while loop with else->

'''n = 5
while n >= 0:
    print(n)
    n = n-1
else:
    print("I am inside the code")'''

'''i = int(input("Enter the number: "))
while(i<=30):
    i = int(input("Enter the number: "))
    print(i)
else:
    print("The code is end")'''


# Break statement--

'''for i in range (1,12):
    if(i == 11):
        break
    print("5 X",i,"=",5 * i)
print("Exit the Loop")'''

'''for i in range(1,101,1):
    print(i, end=" ")
    if(i == 50):
        break
    else:
        print("missippi")
print("Thank you")'''

# Continue statement--
'''for i in range (1,15):
    if(i == 11):
        print("Skip the iteration")
        continue
    print("5 X",i,"=",5 * i)'''

'''for i in [2,3,4,5,6,7]:
    if(i%2!=0):
        continue
    print(i)'''


# Function and Recursion--

'''def Calculategmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreaternumber(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def islessernumber(a,b):
    pass

a = 9
b = 5
isGreaternumber(a,b)
Calculategmean(a,b)

c = 12
d = 15
isGreaternumber(c,d)
Calculategmean(c,d)'''


# Types of Functions--

''' 1 Built in function
    2 User defined function'''

# Function Arguments-> Function arguments are the values that are passed to a function when it is called. These arguments can be of any data type, such as integers, strings, lists, or even other functions. The function can then use these arguments to perform its operations and return a result.

'''def goodday(name,ending):
    print("Good Day," + name )
    print(ending)
goodday("Kuldeep","Have a nice day")'''

# 1.Default Arguments--A parameter has a default value. If no value is passed, the default is used.
    
'''def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")'''

# 2.Keyword Arguments--We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
    
'''def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")'''

# 3.Variable length Arguments--Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments. There are two types of variable-length arguments: *args (non-keyword variable-length arguments) and **kwargs (keyword variable-length arguments).

# Arbitrary Arguments:

'''def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")'''

# Keyword Arbitrary Arguments:

'''def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")'''

# 4.Required Arguments---These are the arguments that are required to be passed to a function when it is called. If any of the required arguments are missing, the function will raise an error. Required arguments are defined in the function signature and must be provided in the correct order when calling the function.

'''def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill", "Korven")'''

# Return value from function->

'''def goodday(name,ending):
    print("Good Day," + name )
    print(ending)
    return "sir"

a = goodday("Kuldeep","Have a nice day")
print(a)'''

# Default parameter values->

'''def goodday(name,ending = "Have a nice day"):
    print("Good Day," + name )
    print(ending)

goodday("Kuldeep")
goodday("lily","you are lucky today")'''

# Enumerate function->

'''marks = [90, 80, 70, 60, 50]

for index,mark in enumerate(marks, start =1):
    print(mark)
    if(index == 3):
        print("Kuldeep is awesome!")'''


# Recursion--Recursion is a programming technique where a function calls itself in order to solve a problem. It is often used to solve problems that can be broken down into smaller subproblems of the same type. A recursive function typically has a base case that stops the recursion and prevents infinite loops.

'''factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X (n-1) X ........ X 3 X 2 X 1
factorial(n) = n*factorial(n-1)'''

'''def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)

i = int(input("Enter the number:"))
print("The factorial of",i,"is",factorial(i))'''


# File I/O-- File I/O (Input/Output) is a way to read and write data to files in a computer's file system. It allows programs to store and retrieve data from files, which can be useful for persisting data between program runs or for sharing data with other programs.

'''f = open("file.txt") # "r" is the default mode for opening a file, which means that the file is opened in read-only mode. This means that you can read the contents of the file, but you cannot modify or write to it. If you want to write to a file, you need to open it in write mode ("w") or append mode ("a").
data = f.read()
print(data)
f.close()'''

'''f = open("file.txt", "r")
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line ,type(line))
        break'''

# Types of File->
# 1. Text files (.txt, .csv, .json, etc.)
# 2. Binary files (.bin, .dat, .jpg, .png, etc.)
# 3. Log files (.log)

#Opening a file in different modes->

# 1. Read mode ("r") - Opens a file for reading (default mode).

'''f = open("file.txt", "r")
data = f.read()
print(data)
f.close()'''

# 2. Write mode ("w") - Opens a file for writing. If the file already exists, it will be overwritten. If the file does not exist, a new file will be created.

'''st ="Hey will you marry me?"

f = open("myfile.txt","w")
f.write(st)
f.close()'''

# 3. Append mode ("a") - Opens a file for writing, but appends new data to the end of the file instead of overwriting it. If the file does not exist, a new file will be created.

'''st = "\nHey, How are you doing?"

f = open("myfile.txt","a")
f.write(st)
f.close()
'''

# 4. Read and Write mode ("r+") - Opens a file for both reading and writing. The file pointer is placed at the beginning of the file.

# 5. Binary mode ("b") - Opens a file in binary mode, which is used for reading and writing binary data (e.g., images, audio files, etc.). This mode can be combined with other modes (e.g., "rb" for reading a binary file).

# 6. Exclusive creation mode ("x") - Creates a new file, but raises an error if the file already exists. This mode is used to ensure that a new file is created and that existing files are not accidentally overwritten.

# 7. Text mode ("t") - Opens a file in text mode, which is used for reading and writing text data. This is the default mode for opening files in Python. This mode can be combined with other modes (e.g., "rt" for reading a text file).

# 8. Context manager ("with") - A context manager is a way to automatically manage resources, such as files, in Python. When you use a context manager to open a file, the file is automatically closed when the block of code is exited, even if an error occurs. This can help prevent resource leaks and make your code more robust. The syntax for using a context manager to open a file is as follows:

'''with open("file.txt","r") as f:
    print(f.read())'''

# readlines() function---

# f = open("file.txt","r")

'''lines =f.readlines()
print(lines, type(lines))'''

'''line1 = f.readlines()
print(line1, type(line1))

line2 = f.readlines()
print(line2, type(line2))

line3 = f.readlines()
print(line3, type(line3))

line4 = f.readlines()
print(line4 == "")'''

'''line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()'''

# f.close()

'''f = open("file.txt", "r")
i = 0

while True:
    i += 1
    line = f.readline()
    
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Marks of student {i} in Maths is: {m1+2}")
    print(f"Marks of student {i} in Phsyics is: {m2+2}")
    print(f"Marks of student {i} in Chemistry is: {m3+2}")

print(line)'''

# seek() and tell() function->

'''with open("myfile.txt","r") as f:
    print(type(f))

    f.seek(10)

    print(f.tell())
    data = f.read(7)
    print(data)'''

# truncate() function->

'''with open("sample.txt","w") as f:
    f.write("Hello world!")
    f.truncate(5)

with open("sample.txt","r") as f:
    print(f.read())'''


# Exceptions and Error Handling-- In Python, exceptions are errors that occur during the execution of a program. When an exception occurs, the normal flow of the program is interrupted, and the program may terminate or produce unexpected results. To handle exceptions and prevent program crashes, Python provides a mechanism called error handling.

'''a = input("Enter a number: ")
print(f"Multiplacation table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")

except ValueError:
    print("Please enter a valid number.")
print("End of program")'''


# Finally block-- The finally block is a part of the try-except statement in Python that is used to define a block of code that will always be executed, regardless of whether an exception was raised or not. The finally block is typically used to perform cleanup operations, such as closing files or releasing resources, that need to be executed regardless of whether an exception occurred.

'''def func1():
    try:
        l = [1,2,3,4,5,6]
        i = int(input("Enter a index value: "))
        print(l[i])
        
        return 1
    
    except:
        print("Please enter a valid index value.")

        return 0
    
    finally:
        print("End of program")

    # print("End of program")

a = func1()
print(a)'''


#  Raise Custom errors-- In Python, you can create your own custom exceptions by defining a new class that inherits from the built-in Exception class. This allows you to create specific error types that are relevant to your application or domain.

'''a = int(input("Enter any value between 3 to 10: "))

if(a<3 or a>10):
    raise ValueError("Please enter a valid value between 3 to 10")'''


# Local and Global variables--

'''x = 10 

def myfunc(): 
    x = 5
    y = 7
    print(x)  
    print(y)

myfunc()
print(x)'''
#print(y) #its make error due to y variable is a local variable of myfunc
    

# Lambda function--

'''def double(x):
    return x*2'''

'''def appl(fx, value):
    return 22 + fx(value)

print(appl(lambda x : x*x*x,165))'''

'''double = lambda x : x*2
cube = lambda y : y*y*y
avg = lambda x,y : (x+y)/2

a = int(input("Enetr the number:"))
print(double(a))

b = int(input("Enter the number:"))
print(cube(b))

print(avg(8,9))'''


#Map, Filter and Reduce--

#Map

'''def square(x):
    return x*x

print(square(8))

l = [2,5,8,10,12,14,15]
newl = []
for item in l:
    newl.append(square(item))

print(newl)'''

'''def square(x):
    return x*x

print(square(8))

l = [2,5,8,10,12,14,15]

newl = list(map(square,l))
print(newl)'''


# Filter

'''l = [12,5,8,10,12,4,6]

def filter_fun(a):
    return a>5

newl = list(filter(filter_fun,l))
print(newl)'''

# Reduce

'''from functools import reduce

num = [2,5,4,7,8,3,5]

def mysum(x,y):
    return x+y

sum = reduce(mysum,num)

print(sum)'''


# 'is' vs '==' --

'''a = 8 
b = 8

print(a is b) # exact location of object in memory 
print(a == b) # value of object '''

'''a = 8 
b = "8"

print(a is b) # exact location of object in memory 
print(a == b) '''

'''a = "kuldeep" 
b = "kuldeep"

print(a is b) # exact location of object in memory 
print(a == b) '''

'''a = [1,2,3] 
b = [1,2,3]

print(a is b) # exact location of object in memory 
print(a == b) '''

'''a = (1,2,3) 
b = (1,2,3)

print(a is b) # exact location of object in memory 
print(a == b) 
'''
