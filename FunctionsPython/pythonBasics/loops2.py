def print_stars(MaxCount):
    for star in range(MaxCount):
        print("*",end="")

# print_stars(1000)

def print_star_grid(MaxCount):
    for row in range(MaxCount):
        for col  in range(MaxCount):
            print("*",end="")
        print("*")

# print_star_grid(5)

def print_star_list(list):
    for number in list:
        print(number * "*")

list = [4,3,2,6,5,4,8]
# print_star_list(list)

def print_star_list_v2(numbers):
    for number in numbers:
        for star in range(number):
            print("*",end="")
        print("")
numbers = [4,3,2,6,5,4,8]

# print_star_list_v2(numbers)


def append_and_print_stars(gridSize):
    for row in range(gridSize):
        list = []
        for col in range(gridSize):
            list.append("*")         # append '*' to the list
        print("".join(list))         

# append_and_print_stars(5)


def print_even_stars(gridSize):
    for row in range(gridSize):
        for col in range(gridSize):
            # if col % 2 == 0:
            #     print("*",end="")
            # else:
            #     print("  ",end="")
            print("*" if col % 2 == 0 else " ",end="")
        print("")

# print_even_stars(5)


def print_stars_only_border(gridSize):
    for row in range(1,gridSize+1):
        for col in range(1,gridSize+1):
            # if col == 1 or col == gridSize or row == 1 or row == gridSize:
            #     print("* ",end="")
            # else:
            #     print("  ",end="")
            print("* " if col == 1 or col == gridSize or row == 1 or row == gridSize else "  " , end="")
        print("")

# print_stars_only_border(5)


def print_stars_only_border_v2(gridSize):
    for row in range(1,gridSize+1):
        list = []
        for col in range(1,gridSize+1):
            # if col == 1 or col == gridSize or row == 1 or row == gridSize:
            #     list.append("* ")
            # else:
            #     list.append("  ")
            list.append(("* ") if col == 1 or col == gridSize or row == 1 or row == gridSize else "  ")

        print("".join(list))

# print_stars_only_border_v2(5)


def append_and_print_stars(gridSize):
    for row in range(1,gridSize+1):
        list = []
        for col in range(1,gridSize+1):
            list.append(str(row) + "," + str(col))         # append '*' to the list
        print("  ".join(list))  
# append_and_print_stars(5)

def print_pyramid_stars(height):
    no_of_stars = 1
    for level in range(1,height+1):
        no_of_spaces = height - level
        print(no_of_spaces * " " + no_of_stars * "*")
        no_of_stars += 2
# print_pyramid_stars(10)

def print_inverted_pyramid_stars(height):
    no_of_stars = height * 2 - 1
    for level in range(1, height+1):
        no_of_spaces = level - 1
        print(no_of_spaces * " " + no_of_stars * "*")
        no_of_stars -= 2
# print_inverted_pyramid_stars(10)

def print_inverted_pyramid_stars_v2(height):
    for level in range(1, height+1):
        no_of_spaces = level - 1
        no_of_stars = (height - level) * 2 + 1
        print(no_of_spaces * " " + no_of_stars * "*")
print_inverted_pyramid_stars_v2(10)