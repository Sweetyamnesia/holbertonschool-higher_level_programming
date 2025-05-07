#!/usr/bin/python3
def uppercase(str):
	new_string = ""
for i in str:
    if ord(i) >= 97 and ord(i) <= 122:  # Vérifie si le caractère est une lettre minuscule
        new_string += chr(ord(i) - 32)  # Convertit la lettre en majuscule
    else:
        new_string += i  # Ajoute le caractère tel quel si ce n'est pas une lettre minuscule
print(new_string)