# 1.'''Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000.
#  Otherwise, return their sum.'''
# def function(a,b):
#     c = a * b   
#     if c <= 1000:
#         return c
#     else:
#         return a+b
# result = function(20,30)
# print("result is", result)
# result = function(40,60)
# print("result is", result)
# 2.'''Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number'''
# previous_number = 0
# for i in range(0,11):
#     sum = previous_number + i
#     print(f"current number",i,"previous no", previous_number, "sum is :", sum)
#     previous_number = i
# 3.'''Write a Python code to accept a string from the user and display characters present at an even index number.'''
# n = input("enter a string: ")
# size = len(n)
# for i in range(0,size-1,2):
#     print(n[i])
# 4.'''Write a Python code to remove characters from a string from 0 to n and return a new string.'''
# text = input("Enter string: ")
# n = int(input("Enter the number of characters to remove: "))
# result = text[n:]
# print("new string: ", result)
# 5.'''Write a code to return True if the lists first and last numbers are the same. If the numbers are different, return False.'''
# def check_first_last(numbers):
#     if numbers[0] == numbers[-1]:
#         return True
#     else:
#         return False

# my_list = [1, 5, 6, 7, 16]
# result = check_first_last(my_list)
# print("Result:", result)
# 6.'''Write a Python code to display numbers from a list divisible by 5'''
# num = [10, 20, 33, 46, 55]
# for i in num:
#     if i%5==0:
#         print(i)
# 7.'''Write a Python code to find how often the substring “Emma” appears in the given string.'''
# given_string="Emma is good developer. Emma is a writer"
# sub_string = "Emma"
# result = given_string.count(sub_string)
# print(result)
# 8.''' Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5'''
# for i in range (1,6):
#     print(" ".join([str(i)]* i))
# 9.'''Write a Python code to check if the given number is palindrome. A palindrome number is a number that is the same after reverse.'''
# number = int(input("enter number: "))
# s = str(number)
# if s == s[::-1]:
#     print("True")
# else:
#     print("False")
# 10.'''Given two lists of numbers, write a Python code to create a new list such that
#  the latest list should contain odd numbers from the first list and even numbers from the second list'''
# def total_list(list1,list2):
#     result_list = []
#     for i in list1:
#         if i % 2 != 0:
#             result_list.append(i)
#     for i in list2:
#         if i % 2 == 0:
#             result_list.append(i)
#     return result_list
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result list is :", total_list(list1,list2))
# 11.'''For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.'''
# n = 7536
# s = str(n)
# s1 = s[::-1]
# print(" ".join(s1))




#13. # Print multiplication table from 1 to 10
# n = int(input())
# for i in range(0,n+1):
#     for j in range(0,n+1):
#         print(i*j , end = " ")
#     print()

# 14.Print a downward half-pyramid pattern of stars
# n = int(input())
# for i in range(n,0,-1):
#     print(i*'*')
# 15.# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base,exp):
#     return base ** exp
# print(exponent(5,4))
# 16.#Write a program to accept two numbers from the user and calculate multiplication
# n = int(input("no1"))
# n2 = int(input("no2"))
# c = n *n2
# print(c)
# 17.#Convert Decimal number to octal using print() output formatting
# num = 21
# print("%o"% num)
#18.Display float number with 2 decimal places using print()
# n = float(input())
# print(f"{n:.2f}")
#19.Accept a list of 5 float numbers as an input from the user.
# float_numbers = []
# for i in range(5):
#     num = float(input("enter number: "))
#     float_numbers.append(num)
# print("list= ",float_numbers)
#20.Accept any three string from one input() call
# str1 ,str2, str3 = input("enter string: ").split()
# print("1=",str1)
# print("2=",str2)
# print('3=',str3)
#21.Format variables using a string.format() method.
# totalMoney = 1000
# quantity = 3
# price = 450
# Expected Output:

# 22.I have 1000 dollars so I can buy 3 football for 450.00 dollars.
# total_money = int(input("enter:"))
# quantity = int(input("quantity:"))
# price = float(input("price: "))
# print(f"i have {total_money} so I can buy {quantity} football for {price:.2f} dollars")
# 23.Check file is empty or not
# import os
# file_name = 'text.txt'
# try:
#     size = os.stat('text.txt').st_size
#     if size == 0:
#         print('empty')
#     else:
#         print("error")
# except FileNotFoundError:
#     print("no data")
#Print first 10 natural numbers using while loop
# n = int(input("enter number: "))
# while n <= 10:
#     print(n)
#     n += 1
#Print the following pattern
# n = int(input("enter number: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end= " ")
#     print()
#Calculate sum of all numbers from 1 to a given number
# n = int(input("enter number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print("sum is", sum)
#Print multiplication table of a given number
# num = int(input('enter number: '))
# for i in range(1,11):
#     result = num * i
#     print(result)
#Display numbers from a list using a loop
# list = [12, 75, 150, 180, 145, 525, 50]
# for i in list:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i % 5 == 0:
#         print(i)
#Count the total number of digits in a number
# num = 75869 
# count = 0 
# while num != 0:
#     num // 10
#     count += 1
# print(count)
# Write a Python program to print the reverse number pattern using a for loop.
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# num = int(input('enter: '))
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(j, end = " ")
#     print() 
# #Print list in reverse order using a loop
