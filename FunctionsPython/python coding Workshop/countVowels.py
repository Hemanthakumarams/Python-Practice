# 8.Function to count number of vowels present in a string
def countVowels(string):
    vowels = 0
    if string != None:
        for character in string:
            if (character == 'a' or 
                character == 'e' or 
                character == 'i' or 
                character == 'o' or 
                character == 'u' or
                character == 'A' or
                character == 'E' or
                character == 'I' or
                character == 'O' or
                character == 'U'):

                vowels += 1
    return vowels

#invokation
input1 = None
print(f"Number of vowels are in {input1} is {countVowels(input1)} ")

input2 = "Hemanth kumar"
print(f"Number of vowels are in {input2} is {countVowels(input2)} ")

input3 = "126./,"
print(f"Number of vowels are in {input3} is {countVowels(input3)} ")