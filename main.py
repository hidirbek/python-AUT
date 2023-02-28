# 1
# def cubeVolume(sideLength):
#     volume = sideLength**3
#     return volume


# result1 = cubeVolume(2)
# result2 = cubeVolume(10)
# print(result1)
# print(result2)

# 2
# def main():
#     result = cubeVolume(2)
#     print("Acube with side length 2 has volume", result)


# def cubeVolume(sideLength):
#     volume = sideLength**3
#     return volume


# main()

# self check
# 1
# def main():
#     result1 = cubeVolume(3)
#     print("volume = ", result1)


# def cubeVolume(sideLength):
#     volume = sideLength**3
#     return volume


# main()

# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b: a * b
# print(x(5, 6))

# str1 = "hello world"
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str1))
#


# 14.02.2023
# 1

# input_list = [1, 2, 3, 4, 5, 6, 7, 7]

# output_list = []

# for var in input_list:
#     if var % 2 == 0:
#         output_list.append(var)
# print("output list osing for loop:", output_list)

# 2
# input_list = [1, 2, 3, 4, 5, 6, 7, 7]

# list_using_comp = [var for var in input_list if var % 2 == 0]
# print(list_using_comp)

# 3
# output_list = []
# for var in range(1, 10):
#     output_list.append(var**2)
# print(output_list)


# 4
# list_using_comprehensive = [var**2 for var in range(1, 10)]
# print(list_using_comprehensive)


# 5
# friends = []
# friends.append("Harry")
# friends.append("emily")
# friends.append("bob")
# friends.append("cari")
# print(friends)


# 6
# friends = ["harry", "emily", "bob", "cari"]
# friends.insert(1, "cindy")
# print(friends)


# 7
# friends = ["harry", "emily", "bob", "cari", "cindy"]

# if "cindy" in friends:
#     print("she's a friend")

# n = friends.index("emily")
# n2 = friends.index("emily", n + 1)


# 21.02.2023 lesson

# 1
# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7]

# output_set = set()

# for var in input_list:
#     if var % 2 == 0:
#         output_set.add(var)

# print(output_set)

# 2

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
# set_using_comp = {var for var in input_list if var % 2 == 0}
# print(set_using_comp)

# 3
# tags = {"Django", "Pandas", "Numpy"}

# lowecase_tags = set()
# for tag in tags:
#     lowecase_tags.add(tag.lower())

# print(lowecase_tags)

# 4
# tags = {"Django", "Pandas", "Numpy"}
# lowercase_tags = set(map(lambda tag: tag.lower(), tags))
# print(lowercase_tags)

# 5
# tags = {"Django", "Pandas", "Numpy"}
# lowercase_tags = {tag.lower() for tag in tags}
# print(lowercase_tags)

# 6

# tags = {"Django", "Pandas", "Numpy"}

# new_tags = {tag.lower() for tag in tags if tag != "Numpy"}
# print(new_tags)


# questions
# 1

# s = {1, 2, 3}
# t = {1, 2, 3, 4, 5}

# if s.issubset(t) and s != t:
#     print("s is a proper subset of t")
# else:
#     print("s is not a proper subset of t")


# 2
# s = {"apple", "banana", "cherry", "orange"}
# t = {"banana", "kiwi", "orange", "strawberry"}

# common_strings = s.intersection(t)

# for string in common_strings:
#     print(string)


# 3

# s = {"apple", "banana", "orange", "kiwi"}
# t = {"orange", "pear", "grape"}

# for string in s - t:
#     print(string)

# 4
# s = set()
# for i in range(1, 5):
#     s.add(i * i)
#     s.add(-i)

# print(s)

# 23.02.2023

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
# output_gen = (var for var in input_list if var % 2 == 0)
# print(end="")

# for var in output_gen:
#     print(var, end="")

# import contextlib


# @contextlib.contextmanager
# def make_context():
#     print("entering")
#     try:
#         yield {}
#     except RuntimeError as err:
#         print("ERROR:", err)
#     finally:
#         print("exiting")


# print("normal:")
# with make_context() as value:
#     print("inside with statement:", value)
# print("\nHandled error:")
# with make_context() as value:
#     raise RuntimeError("showing example")
# print("\nUNhandled error:")
# with make_context() as value:
#     raise ValueError("this exception is not handled")


# import contextlib


# @contextlib.contextmanager
# def make_context():
#     print("entering")
#     try:
#         yield
#     except RuntimeError as err:
#         print("error:", err)
#     finally:
#         print("exiting")


# @make_context()
# def normal():
#     print("inside with statement")


# @make_context()
# def throw_error(err):
#     raise err


# print("normal:")
# normal()
# print("\nhandled error:")
# throw_error(RuntimeError("showing example"))
# print("\nunhandled errror")
# print("\nunhanled error")
# throw_error(ValueError("this exception is not handled"))

# 28.02.2023
# def double(num):
#   return num*2;

# my_double = double(4)
# print(my_double)
# print(double)


# def plusOne(number):
#   return number+1


# def plusTwo(number):
#   return number+2


# def plusThree(number):
#   return number+3


# def plusFour(number):
#   return number+4

# func_list = [plusOne,plusTwo,plusThree, plusFour]

# for func in func_list:
#   print(func(10))


# def cube(number):
#     return number * number * number


# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result


# squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)


# def shout(text):
#     return text.upper()


# def whisper(text):
#     return text.lower()


# def greet(func):
#     greeting = func("hi there")
#     print(greeting)


# greet(whisper)

# 3

# def logger(msg):
#     def log_message():
#         print("Log:", msg)

#     return log_message


# loh_hi = logger("Hi!")
# loh_hi()


def plusOne(number):
    return number + 1


def plusTwo(number):
    return number + 2


def listModifier(li, func):
    result = []
    for el in li:
        result.append(func(el))
    return result


print(listModifier([1, 2, 3, 4, 5], plusTwo))
