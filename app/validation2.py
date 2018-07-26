"""validation class with regular expressions"""
import re


class Validate2():
    """valiation class for diary inputs"""
    def __init__(self, title, body):
        self.title = title
        self.body = body

    def validate_empty(self):
        """method to validate my input """
        result = ""
        if(not re.search("[a-zA-Z0-9]", self.title) or not
           re.search("^(\s|\S)*(\S)+(\s|\S)*$", self.body)):
            result = "wrong data"
        else:
            result = True
        return result
