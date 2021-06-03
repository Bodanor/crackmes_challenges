import random
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ""

def check_key(key):
    char_sum = 0
    for c in key[:-1]:
        char_sum += ord(c)
        char_sum = char_sum >>1
        char_sum = int(char_sum%0xf00) % 0xf00
        char_sum += 10
    return char_sum


while True:
    for i in range (0, 16):
        key += random.choice(alpha)

    check = check_key(key)
    if check == ord(key[-1]):
        print(key)
    else:
        key = ""
