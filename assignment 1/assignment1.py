# Name: Geeta
 
# Roll no: 2501060160

# Course: BCA(H)(AI &DS)
# Semester: 1
# Subject: Problem Solving With Python
# Assignment: Unit-1 Mini Project
# Title: Student Profile Console App
# Date: 12th November 2025
print('''Welcome To Python Programming! \n Python is a very easy to use coding language preferred by many beginners as their first programming language
      because of it's vast libraries and ease of use many developers prefer python as their main language
      Python can be used with lots of IDE's which we can use with python like PYcharm but here we are using VS CODE''')

# TASK 2
name=str(input("Student Full Name: "))
roll_no=int(input("Roll no: "))
program=str(input("Program name: "))
uni_name=str(input("University Name: "))
city=str(input("City: "))
age=int(input("Age: "))
hobby=str(input("Hobby: "))


#TASK 3
number_1=int(input("Enter number 1: "))
number_2=int(input("ENter Number 2: "))
#Arithmetic operators
print("addition: ",number_1+number_2)
print("subtraction: ",number_1-number_2)
print("Multiplication: ",number_1*number_2)
print("Division: ",number_1/number_2)
print("Modulo: ",number_1%number_2)
print("Square of number 1: ",number_1**2)
print("Square of number 2: ",number_2**2)
#Assignment Operators 
a = number_1
a+=12
print(a)
a-=23
print(a)
a*=34
print(a)
a/=53
print(a)
#Comparision OPerators
if number_1<number_2:
    print("NUMBER 1 < NUMBER 2")
elif number_1>number_2:
    print("NUMBER 1 > NUMBER 3")
elif number_1==number_2:
    print("NUMBER 1 = NUMBER 2")
#Logical Operators
print("\nLogical Operators:")
print(f"({number_1} > 0) and ({number_2} > 0) → {(number_1 > 0) and (number_2 > 0)}")
print(f"({number_1} > 0) or ({number_2} < 0) → {(number_1 > 0) or (number_2 < 0)}")
print(f"not({number_1} > {number_2}) → {not(number_1 > number_2)}")

# Identity Operators
print("\nIdentity Operators:")
print(f"num1 is num2 → {number_1 is number_2}")
print(f"num1 is not num2 → {number_1 is not number_2}")

# Membership Operators
sample_str = "python programming"
print("\nMembership Operators:")
print(f"'py' in '{sample_str}' → {'py' in sample_str}") 
print(f"'java' not in '{sample_str}' → {'java' not in sample_str}")

# Task 4
print("\n===== String Operations & Formatting =====")

# Concatenation
full_intro = "My name is " + name + " and I study in " + uni_name + "."
print(full_intro)

# f-string
print(f"Hello, {name.title()}! Welcome to {uni_name}.")

# Escape characters
print("Using escape characters:\n\tName:", name, "\n\tProgram:", program)

# String Methods
print("\nApplying String Methods:")
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())
print("Replacing letters:", name.replace("a", "@"))
print("Count of 'a':", name.count("a"))


# TASK 5
print('''\t----------------------\n
        Student Profile System\n
        -----------------------
      Name:\t       Geeta

      Roll no:\t       2501060160

      Course:\t       BCA
      University:\tK.R. Mangalam University
      City:\t       New Delhi
      Age:\t       19
      Hobby:\t       Coding
        -----------------------''')