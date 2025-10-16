print("fikret"[2])

#String
print("123"+"456")

#Integer = Whole Number
print(123 + 345)

#Float = Floating Point Number
print(3.14)

#Boolean
print(True)
print(False)

#Type
print(type("hello"))
print(type(12345))
print(type(True))
print(type(3.14))

print(int("123") + int("345"))

#concatunate str and integer with variable
# isim = len(input("ismini gir"))
# print("Senin isminde " + str(isim) + " harf var")

#Mathematical Operations
print(3*4)
print(4-2)
print(5 / 3)
print(5 // 3) # double division dont take rest only count , how much it can
print(5**3)

# PEMDAS ( Prantheses, Exponents, multiplication, Division, Addition, Subtraction)
# ()
# **
# * or /
# + or -
# print(3 * (3 + 3) / 3 - 3)
#
# pw = 1.65
# ph= 85
# bmi = (ph / pw ** 2)
# print(round(bmi, 2))
# print(int(bmi))

#Final Project Tip Calculator

#what was the total bill? 124.56$
#How much tip whould you like to give? 10, 12 or 15%
#How many people split the bill?
#Each person schould pay:
print("Welcome To Tip Calcuator\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip whould you like to give? 10, 12 or 15%\n"))
people = int(input("How many people split the bill?\n"))
eachPerson = ((bill * tip/10) / people)
print(f"Each person should pay: {eachPerson}")





