#/usr/bin/env python
# -*- coding: utf-8 -*-
# Emoji encryptor
from sys import argv, exit

def intify(string, alphabet):
    number = sum([len(alphabet)**i for i in range(len(string))])
    combinations = len(alphabet)**(len(string))
    for letter in string:
        combinations /= len(alphabet)
        number += alphabet.index(letter) * combinations
    return number

def wordify(number, alphabet):
    out = []
    while 1:
        if number <= len(alphabet):
            out.insert(0, alphabet[number-1])
            break
        loc = number % len(alphabet)
        loc += len(alphabet) * (loc == 0)
        out.insert(0, alphabet[loc-1])
        number = (number - loc) / len(alphabet)
    return out


def encipher(string):
    integer = intify(string, alphabet1)
    return wordify(integer, alphabet2)

def decipher(string):
    integer = intify(string, alphabet2)
    return wordify(integer, alphabet1)

alphabet1 = list("abcdefghijklmnopqrstuvwxyz ")


with open("emojilist") as f:
    emojilist = f.read().splitlines()
alphabet2 = [emoji.split("|")[0] for emoji in emojilist]


string1 = " ".join(argv[1:]).lower()


if not any(letter not in alphabet1 for letter in string1):
    print " ".join(encipher(string1))
else:
    string1 = string1.split()
    if not any(letter not in alphabet2 for letter in string1):
        print "".join(decipher(string1))
    else:
        print "Invalid input."
