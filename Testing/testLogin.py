"""
Purpose: Simulate testing a name and password field, practice unittest

Username Requirement: First and Last name, one space, length greater than 5 (2 character fn, 2 charcter ln, 1 space)

Password Requirement: 10-20 characters, 1+ number, 1+ special character
"""

import unittest
import login

class testLogin(unittest.TestCase):

    def setUp(self):
        self.validUsernames = ["Corey Comish", "Gary Oak", "Ash Ketchum", "Jo Li"]
        self.invalidUsernames = ["Coreycomish", "Gary O ak", "Ash", "as h"]
        self.validPasswords = ["password123*", "password1!", "passwordpassword123*"]
        self.invalidPasswords = ["password", "passw0rd!", "passwordpassword1234*", "password123", "password***", "passwrd*1"]
        self.login = login.Login()

    def tearDown(self):
        pass

    def testValidUsernames(self):
        for name in self.validUsernames:
            self.login.setName(name)
            assert self.login.validateName() == True
    
    def testInvalidUsernames(self):
        for name in self.invalidUsernames:
            self.login.setName(name)
            assert self.login.validateName() == False

    def testValidPasswords(self):
        for pw in self.validPasswords:
            self.login.setPassword(pw)
            assert self.login.validatePassword() == True
    
    def testInvalidPasswords(self):
        for pw in self.invalidPasswords:
            self.login.setPassword(pw)
            assert self.login.validatePassword() == False

if __name__ == "__main__":
    unittest.main()