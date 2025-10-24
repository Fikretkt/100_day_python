# def create(isim):
#     print(f"gel {isim}")
#     print(f"gör {isim}")
#     print(f"git  {isim}"  )

# create("fikret")

# def ikili_parameter(name, location):
#     print(f"Merhaba {name}")
#     print(f"Sen  {location} dan geliyorsun")

# ikili_parameter("Fikret","Istanbul")

# treu = ("T","R","U","E")
# love = ("L","O","V","E")
# true_love = ""
# def calculate_love_score(name1, name2):
#     for i in calculate_love_score:
#         if i == treu :
#             true_love = i
#             print(true_love)
#         else:
#             print("yok")

# calculate_love_score("Angela Yu", "Jack Bauer".upper)

# TRUE ve LOVE kelimesindeki harfler
# true = ("T","R","U","E")
# love = ("L","O","V","E")

# def calculate_love_score(name1, name2):
#     # Tüm harfleri BÜYÜK harfe çevir ve birleştir
#     combined_names = (name1 + name2).upper()
#     print("Birleştirilmiş ve büyük harfe çevrilmiş isimler:", combined_names)  # Debug

#     true_score = 0
#     love_score = 0

#     # TRUE harflerini döngüyle isimde kaç tane var bakılır
#     for letter in true:
#         count = combined_names.count(letter)
#         true_score += count
#         print(f"TRUE harfi [{letter}] sayısı: {count}")

#     # LOVE harflerini döngüyle isimde kaç tane var bakılır
#     for letter in love:
#         count = combined_names.count(letter)
#         love_score += count
#         print(f"LOVE harfi [{letter}] sayısı: {count}")

#     # Sonunda sonucu birleştir ve duyur
#     print(f"TRUE toplamı: {true_score}, LOVE toplamı: {love_score}")
#     love_score_total = int(str(true_score) + str(love_score))
#     print(f"Aşk skoru: {love_score_total}")

#     return love_score_total

# # Fonksiyonu çalıştırıyoruz
# calculate_love_score("Angela Yu", "Jack Bauer")


#Cheesar Cipher

logo = '''
        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           

'''
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(" Sifrelemek icin 'encode', sifre cozmek icin 'decode' yazin.\n")
text = input("Lütfen mesajinizi yaziniz:\n")
kaydirma = int(input("Kaydirma numarasini yaziniz\n"))


def encrypt(text, kaydirma):

    encrypt = ""

    for letter in text:
        if letter in alphabet:
            eski_index = alphabet.index(letter)
            yeni_index = (eski_index + kaydirma) %26
            encrypt += alphabet[yeni_index]
        else:
            encrypt += letter
    return encrypt
encode = encrypt(text, kaydirma)
print("sifreli mesaj :" , encode)

def decrypt(text,kaydirma):
    
    decrypt = ""

    for letter in text:
        if letter in alphabet:
            eski_index = alphabet.index(letter)
            yeni_index = (eski_index - kaydirma) 
            decrypt += alphabet[yeni_index]
        else:
            decrypt += letter
    return decrypt

decode = decrypt(text,kaydirma)
print("sifreli mesaj: ", decode)

def ceaser(text, kaydirma, direction):
    if direction == "encode":
        return encrypt(text, kaydirma)
    elif direction == "decode":
        return decrypt(text,kaydirma)
    else:
        return "Gecersiz islem"