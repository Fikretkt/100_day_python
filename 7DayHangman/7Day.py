import random
from Hangman_words import words
from Hangman_arts import hangman_logo, hangmanpics

print(hangman_logo)


health = 6
generatedWords = random.choice(words).upper()
blankLetter = "_"
display = (blankLetter * (len(generatedWords)))


game_over = False
update_words = []


while not game_over:
    print(f"******************** {health} LIVES LEFT **************************") 
    user = input("lütfen kelimeyi tahmin ediniz?").upper()
    display = ""
    for letter in generatedWords:
        if letter == user:
            display += letter
            update_words.append(user)
            print ("evet süpersin, böyle devam et")
        elif letter in update_words:
            display += letter
            
        else:
            display += "_"
    print(display)

    if user not in generatedWords:
        health -= 1
        print(f" Siz {user} tahmin ettiniz, fakat bu yanlis. bir hakkinizi kaybettiniz!!! ")

        if health == 0:
            game_over == True
            print(f"Aradiginiz kelime {generatedWords} idi")
            print("*************************  YOU LOSE  **************************")
        

    

    if "_" not in display: 
        game_over = True
        print("Kazandiniz")
        print("*************************  YOU WINNNNNNN  **************************")


    print(hangmanpics[health])

    






# def getRandomWord(wordList):
#     # This function returns a random string from the passed list of strings.
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]

# def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
#     print(hangmanPics[len(missedLetters)])
#     print()

#     print('Missed letters:', end=' ')
#     for letter in missedLetters:
#         print(letter, end=' ')
#     print()

#     blanks = '_' * len(secretWord)

#     for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

#     for letter in blanks:  # show the secret word with spaces in between each letter
#         print(letter, end=' ')
#     print()

# def getGuess(alreadyGuessed):
#     # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
#     while True:
#         print('Guess a letter.')
#         guess = input().lower()
#         if len(guess) != 1:
#             print('Please enter a single letter.')
#         elif guess in alreadyGuessed:
#             print('You have already guessed that letter. Choose again.')
#         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#             print('Please enter a LETTER.')
#         else:
#             return guess

# def playAgain():
#     # This function returns True if the player wants to play again; otherwise, it returns False.
#     print('Do you want to play again? (yes or no)')
#     return input().lower().startswith('y')

# print("Welcome to Hangman! Try to guess the animal I'm thinking of.")

# missedLetters = ''
# correctLetters = ''
# secretWord = getRandomWord(words)
# gameIsDone = False

# while True:
#     displayBoard(hangmanpics, missedLetters, correctLetters, secretWord)

#     # Let the player enter a letter.
#     guess = getGuess(missedLetters + correctLetters)

#     if guess in secretWord:
#         correctLetters += guess

#         # Check if the player has won
#         foundAllLetters = True
#         for i in range(len(secretWord)):
#             if secretWord[i] not in correctLetters:
#                 foundAllLetters = False
#                 break
#         if foundAllLetters:
#             print(f'Yes! The secret word is "){secretWord}"! You have won!')
#             gameIsDone = True


import random                                     # Rastgele seçim için
from Hangman_words import words                   # Kelime listesi olan modül
from Hangman_arts import hangman_logo, hangmanpics # Logo ve çizimler

print(hangman_logo)                              # Oyun logosunu yazdırır

health = 6                                       # Başlangıç can hakları
# Kelime rastgele seçilip büyük harfe çevrilir
generatedWord = random.choice(words).upper()    
blankLetter = "_"                               # Harflerin yerine kullanılacak boşluk karakteri

display = [blankLetter] * len(generatedWord)     # Örneğin: ['_', '_', '_', ...]
guessed_letters = []                             # Daha önce tahmin edilen harfler tutulur

game_over = False                                # Oyun bitiş durumunu kontrol eder

print(" ".join(display))                         # İlk başta boşluklu gösterim yapar

while not game_over:                             # Oyun bitene kadar döngü
    print(f"\n******************** {health} LIVES LEFT **************************")
    print(" ".join(display))                    # Güncel kelime durumu gösterilir
    user = input("Lütfen bir harf tahmin edin: ").upper()   # Kullanıcıdan harf alınır

    if not user.isalpha() or len(user) != 1:
        print("Lütfen sadece tek bir harf girin.")   # Sadece harf ve tek karakter kontrolü
        continue

    if user in guessed_letters:
        print("Bu harfi zaten denediniz.")          # Aynı harfi iki kez denemeyi engeller
        continue

    guessed_letters.append(user)                  # Yeni harfi tahmin listesine ekler

    if user in generatedWord:                     # Doğru harf ise...
        print("Evet, süpersin, böyle devam et!")
        for idx, letter in enumerate(generatedWord):
            if letter == user:
                display[idx] = user               # Doğru harf, uygun yerlere eklenir
    else:
        health -= 1                              # Yanlış tahmin, can bir azalır
        print(f"Siz [{user}] tahmin ettiniz, fakat bu yanlış. Bir hakkınızı kaybettiniz!")

    print(hangmanpics[health])                   # Kalan cana göre asma adam çizimi

    # Oyun bitti mi?
    if "_" not in display:                       # Tüm harfler bulunduysa
        print("Kazandiniz!")
        print("*************************  YOU WINNNNNNN  **************************")
        game_over = True

    elif health == 0:                            # Canlar biterse
        print(f"Aradiğiniz kelime {generatedWord} idi")
        print("*************************  YOU LOSE  **************************")
        game_over = True

