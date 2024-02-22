"""
Purpose: Simulate testing a name and password field, practice unittest

Username Requirement: First and Last name, one space, length greater than 5 (2 character fn, 2 charcter ln, 1 space)

Password Requirement: 10-20 characters, 1+ number, 1+ special character
"""

class Login():

    def __init__(self):
        self.name = ''
        self.password = ''
        self.specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '/', '?', ',', '.', '<', '>', ':', ';', '-', '_', '=', '+']
    
    def setName(self, name):
        self.name = name

    def setPassword(self, password):
        self.password = password

    def validateName(self):
        if self.name.count(' ') != 1:
            self.name = ''
            return False
        if len(self.name) <= 4:
            self.name = ''
            return False
        return True

    def validatePassword(self):
        if len(self.password) > 20 or len(self.password) < 10:
            self.password = ''
            return False
        numberCount = 0
        specialCount = 0
        for ch in self.password:
            if ch.isdigit():
                numberCount += 1
            if ch in self.specialChars:
                specialCount += 1
        if numberCount < 1 or specialCount < 1:
            self.password = ''
            return False
        return True