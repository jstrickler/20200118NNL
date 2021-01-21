#!/usr/bin/python3

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]


# business logic
def cleanup(s):
    return ???

# user interface
for s in spam:
    new_s = cleanup(s)
    print(s, new_s)
