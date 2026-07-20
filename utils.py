import re

def valid_phone(phone):
    pattern = r"^[6-9]\d{9}$"
    return re.match(pattern, phone)

def valid_pincode(pincode):
    pattern = r"^\d{6}$"
    return re.match(pattern, pincode)