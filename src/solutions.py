
# Question 2
"""
operands = ["father", "mother"]
result = "parent"

sols = [
    {
        "p": "4",
        "h": "7",
        "n": "0",
        "f": "1",
        "m": "2",
        "e": "5",
        "o": "9",
        "a": "8",
        "t": "6",
        "r": "3",
    },
    {
        "p": "4",
        "h": "7",
        "n": "0",
        "f": "2",
        "m": "1",
        "e": "5",
        "o": "9",
        "a": "8",
        "t": "6",
        "r": "3",
    },
]
"""

# operands = ["one", "three", "four"]
# result = "eight"

# puzzle = " + ".join(operands) + " = " + result
# solver = Crypt_Solver()
# solutions = solver.solve(operands, result)


# for sol in solutions:
#     print(puzzle)
#     print(solver.apply_mapping(puzzle, sol))
#     print(sol)

"""
forty + ten + ten = sixty
29786 + 850 + 850 = 31486
{'x': '4', 's': '3', 'o': '9', 'e': '5', 'r': '7', 'f': '2', 'i': '1', 'y': '6', 't': '8', 'n': '0'}
"""

# from random import sample
# from pprint import pprint

# perms = [list(p) for p in permutations("0123456789")]
# sampled_right = (
#     sample(perms, 18)
#     + [
#         [
#             "0",
#             "2",
#             "9",
#             "5",
#             "4",
#             "1",
#             "7",
#             "6",
#             "8",
#             "3",
#         ]
#     ]  # 19
#     + sample(perms, 14)
#     + [
#         [
#             "0",
#             "8",
#             "6",
#             "4",
#             "3",
#             "7",
#             "1",
#             "9",
#             "2",
#             "5",
#         ]
#     ]  # 34
#     + sample(perms, 23)
#     + [
#         [
#             "3",
#             "0",
#             "8",
#             "9",
#             "6",
#             "7",
#             "1",
#             "4",
#             "2",
#             "5",
#         ]
#     ]  # 58
#     + sample(perms, 11)
#     + [
#         [
#             "7",
#             "2",
#             "3",
#             "6",
#             "4",
#             "0",
#             "8",
#             "5",
#             "9",
#             "1",
#         ]
#     ]  # 70
#     + sample(perms, 18)
#     + [
#         [
#             "9",
#             "5",
#             "6",
#             "8",
#             "0",
#             "7",
#             "1",
#             "4",
#             "2",
#             "3",
#         ]
#     ]  # 89
#     + sample(perms, 11)
# )

# pprint(sampled_right)
# print(len(sampled_right), all([type(i) == list for i in sampled_right]))

"""
one + three + four = eight
948 + 75188 + 6921 = 83057
{'g': '0', 'u': '2', 'o': '9', 'h': '5', 'n': '4', 'r': '1', 't': '7', 'f': '6', 'e': '8', 'i': '3'}
one + three + four = eight
682 + 14722 + 9637 = 25041
{'g': '0', 'u': '3', 'o': '6', 'h': '4', 'n': '8', 'r': '7', 't': '1', 'f': '9', 'e': '2', 'i': '5'}
one + three + four = eight
928 + 75188 + 6941 = 83057
{'g': '0', 'u': '4', 'o': '9', 'h': '5', 'n': '2', 'r': '1', 't': '7', 'f': '6', 'e': '8', 'i': '3'}
one + three + four = eight
784 + 39544 + 1765 = 42093
{'g': '0', 'u': '6', 'o': '7', 'h': '9', 'n': '8', 'r': '5', 't': '3', 'f': '1', 'e': '4', 'i': '2'}
one + three + four = eight
632 + 14722 + 9687 = 25041
{'g': '0', 'u': '8', 'o': '6', 'h': '4', 'n': '3', 'r': '7', 't': '1', 'f': '9', 'e': '2', 'i': '5'}
one + three + four = eight
764 + 39544 + 1785 = 42093
{'g': '0', 'u': '8', 'o': '7', 'h': '9', 'n': '6', 'r': '5', 't': '3', 'f': '1', 'e': '4', 'i': '2'}
one + three + four = eight
794 + 32544 + 6785 = 40123
{'g': '1', 'u': '8', 'o': '7', 'h': '2', 'n': '9', 'r': '5', 't': '3', 'f': '6', 'e': '4', 'i': '0'}
one + three + four = eight
784 + 32544 + 6795 = 40123
{'g': '1', 'u': '9', 'o': '7', 'h': '2', 'n': '8', 'r': '5', 't': '3', 'f': '6', 'e': '4', 'i': '0'}
one + three + four = eight
862 + 19722 + 4807 = 25391
{'g': '3', 'u': '0', 'o': '8', 'h': '9', 'n': '6', 'r': '7', 't': '1', 'f': '4', 'e': '2', 'i': '5'}
one + three + four = eight
802 + 19722 + 4867 = 25391
{'g': '3', 'u': '6', 'o': '8', 'h': '9', 'n': '0', 'r': '7', 't': '1', 'f': '4', 'e': '2', 'i': '5'}
one + three + four = eight
258 + 74188 + 9201 = 83647
{'g': '6', 'u': '0', 'o': '2', 'h': '4', 'n': '5', 'r': '1', 't': '7', 'f': '9', 'e': '8', 'i': '3'}
one + three + four = eight
982 + 15722 + 3947 = 20651
{'g': '6', 'u': '4', 'o': '9', 'h': '5', 'n': '8', 'r': '7', 't': '1', 'f': '3', 'e': '2', 'i': '0'}
one + three + four = eight
208 + 74188 + 9251 = 83647
{'g': '6', 'u': '5', 'o': '2', 'h': '4', 'n': '0', 'r': '1', 't': '7', 'f': '9', 'e': '8', 'i': '3'}
one + three + four = eight
942 + 15722 + 3987 = 20651
{'g': '6', 'u': '8', 'o': '9', 'h': '5', 'n': '4', 'r': '7', 't': '1', 'f': '3', 'e': '2', 'i': '0'}
one + three + four = eight
349 + 86099 + 5320 = 91768
{'g': '7', 'u': '2', 'o': '3', 'h': '6', 'n': '4', 'r': '0', 't': '8', 'f': '5', 'e': '9', 'i': '1'}
one + three + four = eight
329 + 86099 + 5340 = 91768
{'g': '7', 'u': '4', 'o': '3', 'h': '6', 'n': '2', 'r': '0', 't': '8', 'f': '5', 'e': '9', 'i': '1'}
one + three + four = eight
317 + 69277 + 5302 = 74896
{'g': '8', 'u': '0', 'o': '3', 'h': '9', 'n': '1', 'r': '2', 't': '6', 'f': '5', 'e': '7', 'i': '4'}
one + three + four = eight
307 + 69277 + 5312 = 74896
{'g': '8', 'u': '1', 'o': '3', 'h': '9', 'n': '0', 'r': '2', 't': '6', 'f': '5', 'e': '7', 'i': '4'}
one + three + four = eight
592 + 16722 + 3547 = 20861
{'g': '8', 'u': '4', 'o': '5', 'h': '6', 'n': '9', 'r': '7', 't': '1', 'f': '3', 'e': '2', 'i': '0'}
one + three + four = eight
542 + 16722 + 3597 = 20861
{'g': '8', 'u': '9', 'o': '5', 'h': '6', 'n': '4', 'r': '7', 't': '1', 'f': '3', 'e': '2', 'i': '0'}
one + three + four = eight
652 + 18722 + 4607 = 23981
{'g': '9', 'u': '0', 'o': '6', 'h': '8', 'n': '5', 'r': '7', 't': '1', 'f': '4', 'e': '2', 'i': '3'}
one + three + four = eight
602 + 18722 + 4657 = 23981
{'g': '9', 'u': '5', 'o': '6', 'h': '8', 'n': '0', 'r': '7', 't': '1', 'f': '4', 'e': '2', 'i': '3'}
"""