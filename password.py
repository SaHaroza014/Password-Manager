import random


# password should be long 15 spaces

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special = ["!", "@", '#', '%', "^", "&", '*', "(", ")", "-", "_", "+", "=", ";", ":", "'", ",", ".", "/", "?"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "x", "y", "z"]


def generate_pass():
    alpha_up = []  # upper letters of a alphabet
    for letter in range(len(alphabet)):
        x = alphabet[letter].upper()
        alpha_up.append(x)

    password = []
    for value in range(4):
        password.append(random.choice(numbers))
        password.append(random.choice(alphabet))
        password.append((random.choice(alpha_up)))

    for letter in range(2):
        password.append(random.choice(special))

    random.shuffle(password)
    password_as_string = ''.join([str(elem) for elem in password])  # transform list elements to a string

    return password_as_string
