#  arithmetic operator
print(10 + 6) #addition
print(10 - 5) #subtraction
print(5 * 7) #multiplication
print(9 / 4) #division
print(17 // 5)  #floor division
print(-17 // 5) #floor division
print(17 % 5) #modulus
print(2 ** 10) # Exponentiation

# Relational (comparison operator)
# Basic comparisons
print(10 == 10) 
print(10 != 5) 
print(10 > 20) 
#chained comparison 
x=5 
print(1 < x < 10) 
print(0 <= x <= 5) 
#string comparision 
print("apple" < "banana") 
print("Python" == "python")
# Comparing booleans with numbers
print(1 == True) 
print(0 == False) 
print(1 == "1") 


#assignment operator 
# Compound assignment operators
score = 40
score += 5
score *= 2 
score -= 10
print(score) 
# Multiple assignment 
a = b = c = 0 
print(a, b, c) 
x, y, z = 1, 2, 3
print(x, y, z) 
a, b = 10, 20
#swap variables
a, b = b, a 
print(a, b) 

#logical operator 
age = 20
has_id = True
print(age >= 18 and has_id)

is_student = True
is_teacher = False
print(is_student or is_teacher)

print(not True)
print(not False)

print(False and 1/0)

print(True or 1/0)

marks = 72
print(marks >= 40 and marks <= 100)
print(marks < 40 or marks > 100)

#bitwise operator 
print(bin(10))
#AND
print(10 & 6)
#OR
print(10 | 6)
#XOR
print(10 ^ 6)
#LEFT SHIFT
print(10 << 1)
#RIGHT SHIFT
print(40 >> 2)

#MEMBERSHIP & IDENTITY OPERATOR 
a=[2,3,4]
b=[2,3,4]
c=a
print(a is b)
print(a is c)
print(a==b)
print(a==c)
print(id(a))
print(id(b))
print(id(c))