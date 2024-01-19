num1 = [10, 20, 30, 40, 50]
num2 = [50, 60, 70, 80, 90]

"""
Value 70 is not present in the list num1 so, by removing value 70 from 
    list num1 gives an error,
so its a runtime error.
"""
num1.remove(70)
print(num1)
print(num2)

"""
There are two assignment operator(==), only one needed. its a syntax error
"""
sum1 == sum(num1)
print(sum1)
sum2 = sum(num2)
print(sum2)

"""
Colon missing in if statement, its a syntax error,
and below in elif statment 'sum of num2' is bigger comparison of 'sum of num1', 
but its printing 'sum of num1' is bigger and answer is 'True' (which actually False), 
so its logical error.
"""
if sum1>sum2
    print(f"Num1 is bigger num1={sum1}> num2={sum2}: {sum1>=sum2}")
elif sum2>sum1:
    print(f"Num1 is bigger, num1={sum1}> num2={sum2}: {sum2>=sum1}")
else:
    print("None")