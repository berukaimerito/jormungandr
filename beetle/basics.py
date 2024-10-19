# 1 - 9 lvl info. --> C
import random

# Python
# function(x) -> y
# what_is_snake_syntax
# folders-should-be-named-with-dashes
# [keyword][function name][function parameters in braces] --> method signature
#   [code]
# 7 x 7
# kareyi buluyorsun ve aldigin parametre de bu sayi.
# tanimla kareyi bul x 'in:
# x ile x i carp ve dondur


def find_square(x):  # method signature
    x**2  # ** (us)


# method calling
print(find_square(7))  # [method name][verilerin, variables, parameters etc.]
#############
# variables (degiskenler.)
# Data types.
# Integer
# String => 'Stortebeker' or '9exhexc2432'
# fonksiyon buyuk_harf f(x) -> X


def make_it_bigger(x):
    # x'i buyut.
    return x.upper()


# upper(), lower()


def make_it_lower(x):
    return x.lower()


# print(make_it_lower("ANNEN"))
# print(make_it_bigger("titanic"))
def make_it_opposite(x):
    # if (condition):
    #  == iki esittir esitlik durumunu check eder.
    #  = tek esittir ise tanimlar
    z = 10
    q = "ANNEN"

    # print(f"Iste Z diye tanimladigimiz degisken burada: {z}")
    # print(f"bu format cok karsilasilacak {q}")
    if x.lower() == x:
        return x.upper()
    if x.upper() == x:
        return x.lower()

    # RETURN NONE


print(make_it_opposite("MARKET"))
print(make_it_opposite("pokemon"))
print(
    make_it_opposite(
        "Pepsi, Coca-Cola'dan daha iyidir. Aksini iddia eden maldir."
    )
)
# print( x --> make_it_opposite (x --> String --> "Pepsi, ...")  )


def divide_two_numbers(x: int, y: int):
    even_division = x // y
    fractional_division = x / y
    # type() methodu bir verinin data type ni verir
    return f"tam bolme: {type(even_division)}, kesirli bolme: {type(fractional_division)}"


print(divide_two_numbers(12, 3))

# PYTHON
# INTEGER: -Max , +Max 8, 10, -15
# String: "Pepsi", "Texas"
# Float: 8.13
# Boolean: True or False

# Java Primitive
# Boolean, [char], byte, [int, short, long, float, and double]


# print(type(int("darkell64")))
# f(x: str) -> str
# int, str, bool
def make_it_opposite_advanced(x: str) -> str:
    result = ""
    if x.upper() == x:
        return x.lower()
    if x.lower() == x:
        return x.upper()
    else:
        # `xFxYq98ELMcuk` --> `XfXyQ98elmCUK`
        for char in x:
            if char.lower() == char:
                result += char.upper()
            elif char.upper() == char:
                result += char.lower()
            else:
                result += char
    return result


# print(make_it_opposite_advanced("98"))
print(make_it_opposite_advanced("xFxYq9>>8ELMcuk"))

# NON PRIMITIVE TYPES list
#     ^  ^  ^  ^
#      +7 +3 +2, +0 ...
twod_list = [[], [], []]
char_list = ["P", "e", "p", "s", "i"]
print(char_list[0])

li = [7, 3, 2, "Pepsi", 8.0, True]

print(sum(x for x in li if isinstance(x, (int, float))))
example_string = "Carnivore"
example_number = 11
print(type(example_string))

# for char in example_string:
#     print(char, end=" ")

# for item in example_number:
#     print(item)

# for i in twod_list:
#     print(f"This is i in the 2D list: {i}", end=" ")

# for item in li:
#     print(f"This is item: {item} in variable li.")

# for i in example_string:
#     print(f"This is {i}", end=" ")
#


# DO THIS IN C
def generate_list(n):
    # Fill the list with random numbers betwen 80-180
    speed_li = []
    for _ in range(n):
        speed_li.append(random.randint(60, 185))
    return speed_li


def speed_check():
    highway_cars = generate_list(13)
    for car in highway_cars:
        if car > 120:
            print("This is Leonida Police Departmant, stop the vehicle now.")
        else:
            print("Have a nice trip.")


def speed_check_advanced():
    pass


# Dictionary a.k.a HashMap

# { key: value, key1: value1, key2: value, key3: value}
#  key1 --> value1

protagonists = {
    3: "Cluade",
    "Vice City": "Tommy Vercetti",
    "San Andreas": "C.J",
    "VCS": "Victor Vance",
    4: "Niko Bellic",
    5: ["Franklin", "Trevor", "Micheal"],
}

print(type(protagonists))
print(protagonists[3])
print(protagonists[5])
print(protagonists["VCS"])


def weapon_layout(user_selection):
    weapons = {"SMG": ["Micro-SMG", "Assault-SMG", "MP5"]}

    if user_selection == "SMG":
        return weapons["SMG"]


print(weapon_layout("SMG"))

z = 180
y = 90.23


def weapon_layout_advanced(user_selection):
    pass


another_list = [random.randint(69, 420) for _ in range(20)]

print(len(another_list))
