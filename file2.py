#file2

import file1

with open('file1','r') as f:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    num1_squared = num1 ** 2
    num2_squared = num2 ** 2
    sum_squares = float(f.addition(num1_squared,num2_squared))
    
output = "The sum of squares of numbers",num1,"and",num2,"equals",sum_squares

with open('file3','w') as f:
    f.writeline(output)
    
 
