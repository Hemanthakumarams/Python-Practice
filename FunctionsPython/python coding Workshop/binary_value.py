#19.Function print binary value of integer also perform shift operator on integer
def print_binary_value(number):
    no_of_bits = number.bit_length()
    print(f"Number of bits = {no_of_bits}")
    mask = 1
    mask = mask << no_of_bits - 1
    for _ in range(no_of_bits):
        if number & mask :
            print("1",end="")
        else:
            print("0",end="")
        mask = mask >> 1
#invoke
print_binary_value(100)