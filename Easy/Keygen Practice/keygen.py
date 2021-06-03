import random

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
key = ""

def check_key(key):
    previous_sum = 0
    i = 0
    strlen = len(key)
    while i < strlen:
        char_sum = ord(key[i])*strlen
        char_sum = char_sum*strlen
        previous_sum += char_sum
        i+=1
    return previous_sum

while True:
    key += random.choice(alpha)
    s = check_key(key)
    if s > 0xcdaa:
        key = ""
    elif s == 0xcdaa:
        print("Found Valid key : {0}".format(key))
        key = ""
