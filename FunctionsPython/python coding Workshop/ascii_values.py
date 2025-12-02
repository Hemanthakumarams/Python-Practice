#6.Function to print the ASCII values of character
def print_ascii_value(string):
    for character in string:
        ascii_value = ord(character)     # ord() is used to find the Ascii value of single character
        print(f"ASCII value of {character} --> {ascii_value}")
    
#invocation
print_ascii_value("EFG")
print_ascii_value("ghi")
print_ascii_value("123")
print_ascii_value("1.2/()*,';")