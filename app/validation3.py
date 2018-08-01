"""regular expressions validation"""
import re

def validate_userfields(data):
    """method to update other data fields"""
    result = ""
    lst = list(data)
    for char in lst:
        if not re.search("[a-zA-Z]", char):
            result = False
            break
        else:
            result = True
    return result

def validate_username(data):
    """method to validate username"""
    result = ""
    lst = list(data)
    for char in lst:
        if not re.search("[a-zA-Z0-9]", char):
            result = False
            break
        else:
            result = True
    return result
