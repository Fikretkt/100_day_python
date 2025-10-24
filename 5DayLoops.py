
#Max score rechnen, ohne max funktion

# max_score = 0
# student_score = [11,22,33,44,55,66,77,88,99,123,12344]
# for score in student_score:
#     if score > max_score :
#         max_score = score
# print(max_score)
#
# # Gauss probleme
#
# total = 0
# for number in range( 1,101):
#     total += number
# print(total)


# FizzBuzz spiel

# for i in range(1,101):
#     if i % 3 == 0:
#         print("Fizz")
#
#     elif i % 5 == 0:
#         print("Buzz")
#
#
#     elif i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#
#     else:
#         print(i)
import random

# Password generator

#Easy Pass

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ["0","1","2","3","4","5","6","72","8","9"]
symbols = ["!", "#","$","%","&","*","+"]

nr_letters = int(input("Wie viele buchstaben wollen Sie: "))
nr_numbers = int(input("Wie viele nummer wollen Sie: "))
nr_symbols = int(input("Wie viele symbole wollen Sie haben :"))

# password =""
# for char in range(0,nr_letters):
#     password += random.choice(letters)
#
# for char in range(0,nr_numbers):
#     password += random.choice(numbers)
#
# for char in range(0,nr_symbols):
#     password += random.choice(symbols)

#print(password)

#Hard Pass

password = []
for char in range(0,nr_letters):
    password.append(random.choice(letters))

for char in range(0,nr_numbers):
    password.append(random.choice(numbers))

for char in range(0,nr_symbols):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(f"Your new pass : {password}")

passw = ""
for i in password:
    passw += i
print(passw)

sirali_sayi = ""
for x in range(len(numbers)):
    for sirali_sayi in x:
        sirali_sayi += x
        print(sirali_sayi)
