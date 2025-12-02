#20.Function to remove spaces from string
def remove_spaces(string):
    new_string = ""
    for character in string:
        if character != " " and character != '\t' and character != '\n':
            new_string += character
    return new_string
#invocation
input = "hello world namaste bye"
output = remove_spaces(input)
print(f"After remove a spaces = {output}")