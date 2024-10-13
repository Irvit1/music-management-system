""" Implement a USER class having following fields
• Email ID
• Password
• First N a m e
• Last N a m e
• Age
"""
class User():
    def __init__(self, email, password, fname, lname, age):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname
        self.age = age 