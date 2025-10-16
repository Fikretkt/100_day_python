# Even number and modulo operator

# number = int(input("Please write a number"))
# modulo = int(input("please give a modulo number"))
#
# if number % modulo == 0 :
#     print("Even number")
# else:
#     print("Odd number")

#IF ELSE ELIF


# weight = 85
# height = 1.50
#
# bmi = weight / (height ** 2)
# print(bmi)
# # 🚨 Do not modify the values above
# # Write your code below 👇
# if bmi < 18.5 :
#     print("underweight")
# elif  18.5 <= bmi < 25 :
#     print("normal weight")
# elif 25 <= bmi < 29.9 :
#     print("overweight")

#Pizza Delivery
#
# print("Welcome to Fikret's Pizza House")
# size = input("Bitte geben Sie ihre Pizza Grösse: ( S, M, L)\n")
# pepperoni = input("Wollen Sie Pepperoni auf dem Pizza? y or n :\n")
# extra_cheese = input("Wollen Sie Extra Käse? y oder n :\n")
# kosten = 0
#
# if size == "S" :
#     kosten = 15
#     if pepperoni == "y" :
#         kosten += 2
# elif size == "M" :
#     kosten = 20
#     if pepperoni == "y" :
#         kosten += 3
# elif size == "L" :
#     kosten = 25
#     if pepperoni == "y" :
#         kosten += 3
#
#
# else:
#     pass
# if extra_cheese == "y" :
#     kosten += 1
# else:
#     pass
# print(f"Ihre pizza  kostet {kosten}€")


#  Rolercoaster
# print("Welcome to Rollercoaster!!!!!!!")
# grosse = float(input("Bitte geben Sie Ihre grösse:"))
# kosten = 0
#
# if grosse > 120 :
#     print("Herzlichen Glückwünsch")
#     age = int(input("Bitte geben Sie Ihre Alter: "))
#     if age < 12:
#         kosten = 5
#         print(f"Kinder kosten {kosten}")
#     elif age < 10 :
#         kosten = 7
#         print(f"Kleinkinder kostet {kosten}")
#     elif 45 <= age <= 55 :
#         kosten = 0
#     else:
#         kosten = 12
#         print(f"Erwachsene kosten {kosten}")
#     foto = input("Wollen Sie foto haben : y or n")
#     if foto == "y" :
#         kosten += 3
#     print(f"Ihre gesamt kosten {kosten}")
# else:
#     print("Ihre grösse ist nicht genug.Entschuldigung")

#  Treasure Island-----------------------------------
print('''
                     _
                    | \
                     '.|
     _-   _-    _-  _-||    _-    _-  _-   _-    _-    _-
       _-    _-   - __||___    _-       _-    _-    _-
    _-   _-    _-  |   _   |       _-   _-    _-
      _-    _-    /_) (_) (_\        _-    _-       _-
              _.-'           `-._      ________       _-
        _..--`                   `-..'       .'
    _.-'  o/o                     o/o`-..__.'        ~  ~
 .-'      o|o                     o|o      `.._.  // ~  ~
 `-._     o|o                     o|o        |||<|||~  ~
     `-.__o\o                     o|o       .'-'  \\ ~  ~
          `-.______________________\_...-``'.       ~  ~
                                    `._______`.
                                    ''')
print("Welcome to TREASURE ISLAND\n\n")
name = input("Please give your name")
print(f"In This Island you can find yourself {name}. Please follow the inscription\n")
left = input("You are at the forest and you have 2 way!! please say me, you want to go to left or right side?? l or r").lower()
if left == "l":
    print(f"A good choose {name}")
    swim = input("Do you wonna wait a boat or swimming? (Swimming is faster!!) b or s")
    if swim == "b":
        print(f"Du bist clever, but take care, everywhere so dangerus")
        door = input(f"Now we have 3 door. which one is right for living!!! red, blue or yellow... r,b or y ")
        if door == "y":
            print(f"{name} is Winner. Congratulation, you have all treasure!!!")
        else:
            print(f"Your are lost {name}")
    else:
        print(f"The Crocodile have a good dinner with {name}")

else:
    print(f"You are lost {name}")


