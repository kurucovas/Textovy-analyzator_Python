"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Simona Kurucová
email: kurucovas11@protonmail.com
discord: simona_21811
"""

# zadané hodnoty: registrovaní 4 užívatelia: 
# vytvorenie slovníku "users":
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"} 

# vyžiadanie prihlasovacieho mena a hesla od užívateľa: 
user_name = input("USER NAME:")
password = input("PASSWORD:")

# kontrola, či ide o registrovaného užívateľa: 
user_f = False
for user_name1 in users.keys(): 
    if user_name == user_name1:
        password1 = users.get(user_name1)
        if password1 == password:
             user_f = True
             break
if user_f:
    print("Welcome to the app,", user_name, "\nWe have 3 texts to be analyzed.")
else:    
    print("unregistered user, terminating the program")
    exit()

#  3 texty uložené v premennej TEXTS:      
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''  ]

# očíslovanie textov: 
enumerate(TEXTS, start=1)

line = "_" * 40
print(line)
print()

# užívateľ si vyberá medzi 3 textmi: 
number_of_text = input("Enter a number btw. 1 and 3 to select:")

print(line)

# kontrola vstupu zadaného užívateľom: 
if not number_of_text.isdigit():
    print("input is not a number, terminating the program")
    exit()
else:
    number_of_text1 = int(number_of_text) # preved string na integer

if not number_of_text1 in range(1, 4):
    print("number of text is not in asked range, terminating the program")
    exit()

vybrany_text = TEXTS [int(number_of_text)-1]

number_of_words_in_text = len(vybrany_text.split()) 
print()      
print("There are", number_of_words_in_text, "words in the selected text.")

count_titlecase = 0
number_of_words_in_text1 = vybrany_text.split()
for word in number_of_words_in_text1:
    if word.istitle():
        count_titlecase += 1
print("There are", count_titlecase , "titlecase words.")
print("There are", sum(1 for c in number_of_words_in_text1 if not c.startswith('3') if c.isupper()), "uppercase words.")
print("There are", sum(1 for d in number_of_words_in_text1 if d.islower()), "lowercase words.")
print("There are", sum(1 for e in number_of_words_in_text1 if e.isnumeric()), "numeric strings.")

# suma všetkých čísiel v texte: 
sum_of_numbers = 0
for word in number_of_words_in_text1:
    if word.isnumeric():
        sum_of_numbers += int(word) 
print("The sum of all the numbers", sum_of_numbers,)

lenght_of_words = []

vybrany_text1 = vybrany_text.replace(",", "")
vybrany_text = vybrany_text1.replace(".", "")
for f in vybrany_text.split():
    if f.isalnum():
        p = len(f)
        lenght_of_words.append(p)
 
 # četnost rôznych dĺžok slov v texte:
count_lenght1 = (lenght_of_words.count(1))
count_lenght2 = (lenght_of_words.count(2))
count_lenght3 = (lenght_of_words.count(3))
count_lenght4 = (lenght_of_words.count(4))
count_lenght5 = (lenght_of_words.count(5))
count_lenght6 = (lenght_of_words.count(6))
count_lenght7 = (lenght_of_words.count(7))
count_lenght8 = (lenght_of_words.count(8))
count_lenght9 = (lenght_of_words.count(9))
count_lenght10 = (lenght_of_words.count(10))
count_lenght11 = (lenght_of_words.count(11))

count_lenghts = {"1": count_lenght1,"2": count_lenght2, "3": count_lenght3,
            "4": count_lenght4, "5": count_lenght5, "6": count_lenght6, "7": count_lenght7,
            "8": count_lenght8, "9": count_lenght9, "10": count_lenght10, "11": count_lenght11}

print(line)
print()
print("LEN| "  " OCCURENCES  ""|NR.")
print(line)
print("  ", list(count_lenghts.keys())[0], "|", "*" * list(count_lenghts.values())[0],
"             ", "|",list(count_lenghts.values())[0],sep="")
print("  ", list(count_lenghts.keys())[1], "|", "*" * list(count_lenghts.values())[1],
"     ", "|",list(count_lenghts.values())[1],sep="")
print("  ", list(count_lenghts.keys())[2], "|", "*" * list(count_lenghts.values())[2],
"        ", "|",list(count_lenghts.values())[2],sep="")
print("  ", list(count_lenghts.keys())[3], "|", "*" * list(count_lenghts.values())[3],
"   ", "|",list(count_lenghts.values())[3],sep="")
print("  ", list(count_lenghts.keys())[4], "|", "*" * list(count_lenghts.values())[4],
"  ","|",list(count_lenghts.values())[4],sep="")
print("  ", list(count_lenghts.keys())[5], "|", "*" * list(count_lenghts.values())[5],
"           ", "|",list(count_lenghts.values())[5],sep="")
print("  ", list(count_lenghts.keys())[6], "|", "*" * list(count_lenghts.values())[6],
"          ", "|",list(count_lenghts.values())[6],sep="")
print("  ", list(count_lenghts.keys())[7], "|", "*" * list(count_lenghts.values())[7],
"         ", "|",list(count_lenghts.values())[7],sep="")
print("  ", list(count_lenghts.keys())[8], "|", "*" * list(count_lenghts.values())[8],
"             ", "|",list(count_lenghts.values())[8],sep="")
print(" ", list(count_lenghts.keys())[9], "|", "*" * list(count_lenghts.values())[9],
"             ", "|",list(count_lenghts.values())[9],sep="")
print(" ", list(count_lenghts.keys())[10], "|", "*" * list(count_lenghts.values())[10],
"             ", "|",list(count_lenghts.values())[10],sep="")


