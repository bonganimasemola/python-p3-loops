#!/usr/bin/env python3

def happy_new_year():
     count = 10 
     while count >= 1:
        print(count)
        count -= 1
     print("Happy New Year!")

def square_integers(int_list):
    square_list = []
    for i in int_list:
        square_list.append(i**2)
  
    return (square_list)

def fizzbuzz(num=100):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
