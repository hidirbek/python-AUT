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
