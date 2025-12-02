#18.Function to get count of words in a string
def getWordsCount(string):
    counter = 1
    if len(string) == 0:
        return 0
    for character in string:
        if character == " " or character == '\t' or character == '\n':
            counter += 1
    return counter
# input = "Hello world namaste"
input = " hello world namaste"
count = getWordsCount(input)
print(f"Number of words = {count}")