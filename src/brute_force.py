from itertools import permutations


class Crypt_Solver:
    def __init__(self) -> None:
        self.digits = "0123456789"
        self.perms = permutations(self.digits)

    def construct_letter_digit_mapping(self, letters, permutation):
        mapping = {letter: permutation[i] for i, letter in enumerate(letters)}
        return mapping

    def apply_mapping(self, term, mapping):
        replaced = "".join([mapping[c] if c in mapping else c for c in term])
        return replaced

    def attempt_solution(self, mapping, operands, result):
        mapped_ops = [self.apply_mapping(op, mapping) for op in operands]
        mapped_res = self.apply_mapping(result, mapping)

        leading_zeros = any([op[0] == "0" for op in mapped_ops]) or mapped_res[0] == "0"

        if not leading_zeros:
            puzzle = "+".join(mapped_ops) + "==" + mapped_res
            return eval(puzzle)

        return False

    def solve(self, operands, result):
        unique_letters = list(set("".join(operands) + result))

        solutions = []
        for perm in self.perms:
            mapping = self.construct_letter_digit_mapping(unique_letters, perm)

            if self.attempt_solution(mapping, operands, result):
                solutions.append(mapping)

        return solutions