"""
Author: github.com/Ariocodes
This is a 4 digit password generator.
"""

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'
charsList = list(','.join(chars).split(','))
for a in charsList:
    for b in charsList:
        for c in charsList:
            for d in charsList:
                with open("passwords.txt", "a") as f:
                    f.write("{0}{1}{2}{3}\n".format(a, b, c, d))
                print("{0}{1}{2}{3}\n".format(a, b, c, d))
