#Random Module

import random

# random_integer = random.randint(1,100)
# print(random_integer)

# raslantisal_numaralar = random.random() * 10
# print(raslantisal_numaralar)

# raslatisal_float = random.uniform(1,10)
# print(raslatisal_float)

# yazi_tura = random.choice(["Heads", "Tails"])
# print(yazi_tura)

# List

#Question = Who will pay the bill?
#friends = ["Alice","Bob","Charlie", "David", "Emanuel"]

#First Options
# hesap_odetme = random.choice(["Alice","Bob","Charlie", "David", "Emanuel"])
# print(hesap_odetme)

# 2. Options
# bill = random.randint(0,4)
# if bill == 1 :
#     print("Alice")
# elif bill == 2 :
#     print("Bob")
# elif bill == 3 :
#     print("Charlie")
# elif bill == 4 :
#     print("David")
# elif bill == 5 :
#     print("Emanuel")

# 3. Options
#friends = ["Alice","Bob","Charlie", "David", "Emanuel"]
#print(random.choice(friends))

# state_names=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
#
# print(state_names[2])

# ROCK, PAPER; SCISSORS GAME

rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
table = [rock,paper,scissors]
# user = int(input("You can choise: 0 for rock, 1 for paper, 2 for scissors ?\n"))
# if user >= 0 and user <=2 :
#     print(table[user])
#
# computer = random.randint(0,2)
# print("computer")
# print(table[computer])
#
# if user >=  3 or user <0 :
#     print("You type invalid number, you lost")
# elif user == 0 and computer == 2 :
#     print("You win")
# elif computer == 0 and user == 2 :
#     print("You lose")
# elif user == computer :
#     print("its draw")
# elif user > computer :
#     print("You win")
# elif computer > user :
#     print("You lose")


user = int(input("Lütfen tas, kagit ve makas tan briini seciniz. tas icin 0, kagit icin 1, makas icin 2 ye basiniz\n"))
print("User")
print(table[user])
computer = random.randint(0,2)
print("Computer")
print(table[computer])

if user < 0 or user > 3 :
    print("You type invalid number, you lose!!")
elif user == 0 and computer == 2 :
    print("You win")
elif user == 2 and computer == 0 :
    print("You lose")
elif user > computer :
    print("You win")
elif computer > user :
    print("You lose")

elif user == computer :
    print("ITS DRAW")