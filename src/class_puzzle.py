class Puzzle:
    def __init__(self, terms, result) -> None:
        self.terms = terms
        self.result = result

    def get_unique_letters(self):
        all_letters = "".join(self.terms) + self.result
        unique_letters = set(all_letters)

        return unique_letters


from itertools import permutations


class Solver:
    def __init__(self, puzzle) -> None:
        self.puzzle = puzzle

    def generate_permutations(self):
        return permutations("0123456789")

    def permutation_to_solution(self, permutation):
        solution = {}
        letters = self.puzzle.get_unique_letters()

        for letter, number in zip(letters, permutation):
            solution[letter] = number

        return solution

    def try_solution(self, solution):
        def apply_mapping(term):
            new_term = ""
            for letter in term:
                new_term += solution[letter]

            return new_term

        replaced_terms = [apply_mapping(term) for term in self.puzzle.terms]
        replaced_result = apply_mapping(self.puzzle.result)
        replaced_puzzle = replaced_terms + [replaced_result]

        leading_zeros = any([term[0] == "0" for term in replaced_puzzle])
        if leading_zeros:
            return False

        puzzle = "+".join(replaced_terms) + "==" + replaced_result
        return eval(puzzle)

    def solve(self):
        solutions = []
        perms = self.generate_permutations()

        for perm in perms:
            possible_solution = self.permutation_to_solution(perm)
            if self.try_solution(possible_solution):
                solutions.append(possible_solution)

        return solutions


if __name__ == "__main__":
    terms = ["one", "three", "four"]
    result = "eight"

    puzzle = Puzzle(terms, result)
    steve = Solver(puzzle)

    solutions = steve.solve()
    print(len(solutions))
