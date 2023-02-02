from sys import base_exec_prefix
from manim import *

from random import seed, sample
from itertools import permutations
from pprint import pprint

from numpy import greater

seed(42)


class Test(Scene):
    def construct(self):
        terms_right = {"one": 2, "three": 3, "four": 1, "eight": 4}
        letters = ["G", "U", "O", "H", "N", "R", "T", "F", "E", "I"]
        solutions = [
            [
                "0",
                "2",
                "9",
                "5",
                "4",
                "1",
                "7",
                "6",
                "8",
                "3",
            ],
            [
                "0",
                "8",
                "6",
                "4",
                "3",
                "7",
                "1",
                "9",
                "2",
                "5",
            ],
            [
                "3",
                "0",
                "8",
                "9",
                "6",
                "7",
                "1",
                "4",
                "2",
                "5",
            ],
            [
                "7",
                "2",
                "3",
                "6",
                "4",
                "0",
                "8",
                "5",
                "9",
                "1",
            ],
            [
                "9",
                "5",
                "6",
                "8",
                "0",
                "7",
                "1",
                "4",
                "2",
                "3",
            ],
        ]

        def update_text_right(target, term):
            if term == 1:
                target.next_to(three, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(three, aligned_edge=RIGHT, direction=UP)
                )

            elif term == 2:
                target.next_to(four, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(four, aligned_edge=RIGHT, direction=UP)
                )

            elif term == 3:
                target.next_to(line_right, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        line_right, aligned_edge=RIGHT, direction=UP
                    )
                )

            else:
                target.next_to(operator_right, aligned_edge=RIGHT, direction=DOWN)
                target.add_updater(
                    lambda x: target.next_to(
                        operator_right, aligned_edge=RIGHT, direction=DOWN
                    )
                )

            return target

        line_right = Line(stroke_width=2).set_length(4)
        plus_right = Tex("+")
        operator_right = VGroup(line_right, plus_right).arrange(UP, aligned_edge=LEFT)

        three = update_text_right(
            Tex("T\phantom{--}H\phantom{--}R\phantom{--}E\phantom{--}E"), 3
        )
        four = update_text_right(Tex("F\phantom{--}O\phantom{--}U\phantom{--}R"), 1)
        one = update_text_right(Tex("O\phantom{--}N\phantom{--}E"), 2)
        eight = update_text_right(
            Tex("E\phantom{--}I\phantom{--}G\phantom{--}H\phantom{--}T"), 4
        )

        right_puzzle = VGroup(operator_right, one, three, four, eight).shift(
            (DOWN) + (RIGHT * 3)
        )

        self.play(FadeIn(right_puzzle))

        blank = [" " for _ in range(10)]
        table_right = (
            Table(
                [letters, blank],
                row_labels=[
                    Text("Letters", color=GREEN),
                    Text("Digits", color=RED),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.5},
            )
            .scale(0.25)
            .shift(2 * UP + 3 * RIGHT)
        )
        self.play(FadeIn(table_right))
        self.wait()

        pos_to_letter_right = {idx: val for idx, val in enumerate(letters)}

        def update_puzzle(perm, color=RED):
            three_template = "T\phantom{--}H\phantom{--}R\phantom{--}E\phantom{--}E"
            four_template = "F\phantom{--}O\phantom{--}U\phantom{--}R"
            one_template = "O\phantom{--}N\phantom{--}E"
            eight_template = "E\phantom{--}I\phantom{--}G\phantom{--}H\phantom{--}T"

            mapping = {
                pos_to_letter_right[index]: value for index, value in enumerate(perm)
            }

            three_updated = "".join(
                [mapping[c] if c in mapping else c for c in three_template]
            )
            four_updated = "".join(
                [mapping[c] if c in mapping else c for c in four_template]
            )
            one_updated = "".join(
                [mapping[c] if c in mapping else c for c in one_template]
            )
            eight_updated = "".join(
                [mapping[c] if c in mapping else c for c in eight_template]
            )

            three_updated = update_text_right(
                Tex(three_updated, color=color), terms_right["three"]
            )
            four_updated = update_text_right(
                Tex(four_updated, color=color), terms_right["four"]
            )
            one_updated = update_text_right(
                Tex(one_updated, color=color), terms_right["one"]
            )
            eight_updated = update_text_right(
                Tex(eight_updated, color=color), terms_right["eight"]
            )

            puzzle_updated = (
                three_updated,
                four_updated,
                one_updated,
                eight_updated,
            )

            return puzzle_updated

        def update_table(perm):
            updated = (
                Table(
                    [letters, perm],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                    line_config={"stroke_width": 1.5},
                )
                .scale(0.25)
                .shift(2 * UP + 3 * RIGHT)
            )

            return updated

        def apply_permutation(perm_right, speed=0.2, color_right=RED):
            new_table_right = update_table(perm_right)
            (
                three_temp,
                four_temp,
                one_temp,
                eight_temp,
            ) = update_puzzle(perm_right, color_right)

            self.play(
                Transform(three, three_temp),
                Transform(four, four_temp),
                Transform(one, one_temp),
                Transform(eight, eight_temp),
                Transform(table_right, new_table_right),
                run_time=speed,
            )

        for s in solutions:
            apply_permutation(
                s,
                speed=1,
                color_right=GREEN,
            )

        self.wait()


class SimulSolve(Scene):
    def construct(self):
        terms_left = {"mother": 1, "father": 2, "parent": 3}
        terms_right = {"one": 2, "three": 3, "four": 1, "eight": 4}

        def update_text_left(target, term):
            if term == 1:
                target.next_to(father, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(father, aligned_edge=RIGHT, direction=UP)
                )

            elif term == 2:
                target.next_to(line_left, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        line_left, aligned_edge=RIGHT, direction=UP
                    )
                )

            else:
                target.next_to(operator_left, aligned_edge=RIGHT, direction=DOWN)
                target.add_updater(
                    lambda x: target.next_to(
                        operator_left, aligned_edge=RIGHT, direction=DOWN
                    )
                )

            return target

        def update_text_right(target, term):
            if term == 1:
                target.next_to(three, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(three, aligned_edge=RIGHT, direction=UP)
                )

            elif term == 2:
                target.next_to(four, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(four, aligned_edge=RIGHT, direction=UP)
                )

            elif term == 3:
                target.next_to(line_right, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        line_right, aligned_edge=RIGHT, direction=UP
                    )
                )

            else:
                target.next_to(operator_right, aligned_edge=RIGHT, direction=DOWN)
                target.add_updater(
                    lambda x: target.next_to(
                        operator_right, aligned_edge=RIGHT, direction=DOWN
                    )
                )

            return target

        line_left = Line(stroke_width=2).set_length(5)
        plus_left = Tex("+")
        operator_left = VGroup(line_left, plus_left).arrange(UP, aligned_edge=LEFT)

        father = update_text_left(
            Tex("F\phantom{--}A\phantom{--}T\phantom{--}H\phantom{--}E\phantom{--}R"), 2
        )
        mother = update_text_left(
            Tex("M\phantom{--}O\phantom{--}T\phantom{--}H\phantom{--}E\phantom{--}R"), 1
        )
        parent = update_text_left(
            Tex("P\phantom{--}A\phantom{--}R\phantom{--}E\phantom{--}N\phantom{--}T"), 3
        )

        left_puzzle = VGroup(operator_left, mother, father, parent).shift(
            (DOWN) + (LEFT * 3)
        )

        line_right = Line(stroke_width=2).set_length(4)
        plus_right = Tex("+")
        operator_right = VGroup(line_right, plus_right).arrange(UP, aligned_edge=LEFT)

        three = update_text_right(
            Tex("T\phantom{--}H\phantom{--}R\phantom{--}E\phantom{--}E"), 3
        )
        four = update_text_right(Tex("F\phantom{--}O\phantom{--}U\phantom{--}R"), 1)
        one = update_text_right(Tex("O\phantom{--}N\phantom{--}E"), 2)
        eight = update_text_right(
            Tex("E\phantom{--}I\phantom{--}G\phantom{--}H\phantom{--}T"), 4
        )

        right_puzzle = VGroup(operator_right, one, three, four, eight).shift(
            (DOWN) + (RIGHT * 3)
        )

        self.play(FadeIn(left_puzzle, right_puzzle))

        letters_left = ["P", "H", "N", "F", "M", "E", "O", "A", "T", "R"]
        blank = [" " for _ in range(10)]

        table_left = (
            Table(
                [letters_left, blank],
                row_labels=[
                    Text("Letters", color=GREEN),
                    Text("Digits", color=RED),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.5},
            )
            .scale(0.25)
            .shift(2 * UP + 3 * LEFT)
        )

        letters_right = ["G", "U", "O", "H", "N", "R", "T", "F", "E", "I"]

        table_right = (
            Table(
                [letters_right, blank],
                row_labels=[
                    Text("Letters", color=GREEN),
                    Text("Digits", color=RED),
                ],
                include_outer_lines=True,
                line_config={"stroke_width": 1.5},
            )
            .scale(0.25)
            .shift(2 * UP + 3 * RIGHT)
        )
        self.play(FadeIn(table_left, table_right))
        self.wait()

        pos_to_letter_left = {idx: val for idx, val in enumerate(letters_left)}
        pos_to_letter_right = {idx: val for idx, val in enumerate(letters_right)}

        def update_puzzle_left(perm, color=RED):
            father_template = (
                "F\phantom{--}A\phantom{--}T\phantom{--}H\phantom{--}E\phantom{--}R"
            )
            mother_template = (
                "M\phantom{--}O\phantom{--}T\phantom{--}H\phantom{--}E\phantom{--}R"
            )
            parent_template = (
                "P\phantom{--}A\phantom{--}R\phantom{--}E\phantom{--}N\phantom{--}T"
            )

            mapping = {
                pos_to_letter_left[index]: value for index, value in enumerate(perm)
            }

            father_updated = "".join(
                [mapping[c] if c in mapping else c for c in father_template]
            )
            mother_updated = "".join(
                [mapping[c] if c in mapping else c for c in mother_template]
            )
            parent_updated = "".join(
                [mapping[c] if c in mapping else c for c in parent_template]
            )

            father_updated = update_text_left(
                Tex(father_updated, color=color), terms_left["father"]
            )
            mother_updated = update_text_left(
                Tex(mother_updated, color=color), terms_left["mother"]
            )
            parent_updated = update_text_left(
                Tex(parent_updated, color=color), terms_left["parent"]
            )

            puzzle_updated = (
                father_updated,
                mother_updated,
                parent_updated,
            )

            return puzzle_updated

        def update_table_left(perm):
            updated = (
                Table(
                    [letters_left, perm],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                    line_config={"stroke_width": 1.5},
                )
                .scale(0.25)
                .shift(2 * UP + 3 * LEFT)
            )

            return updated

        def update_puzzle_right(perm, color=RED):
            three_template = "T\phantom{--}H\phantom{--}R\phantom{--}E\phantom{--}E"
            four_template = "F\phantom{--}O\phantom{--}U\phantom{--}R"
            one_template = "O\phantom{--}N\phantom{--}E"
            eight_template = "E\phantom{--}I\phantom{--}G\phantom{--}H\phantom{--}T"

            mapping = {
                pos_to_letter_right[index]: value for index, value in enumerate(perm)
            }

            three_updated = "".join(
                [mapping[c] if c in mapping else c for c in three_template]
            )
            four_updated = "".join(
                [mapping[c] if c in mapping else c for c in four_template]
            )
            one_updated = "".join(
                [mapping[c] if c in mapping else c for c in one_template]
            )
            eight_updated = "".join(
                [mapping[c] if c in mapping else c for c in eight_template]
            )

            three_updated = update_text_right(
                Tex(three_updated, color=color), terms_right["three"]
            )
            four_updated = update_text_right(
                Tex(four_updated, color=color), terms_right["four"]
            )
            one_updated = update_text_right(
                Tex(one_updated, color=color), terms_right["one"]
            )
            eight_updated = update_text_right(
                Tex(eight_updated, color=color), terms_right["eight"]
            )

            puzzle_updated = (
                three_updated,
                four_updated,
                one_updated,
                eight_updated,
            )

            return puzzle_updated

        def update_table_right(perm):
            updated = (
                Table(
                    [letters_right, perm],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                    line_config={"stroke_width": 1.5},
                )
                .scale(0.25)
                .shift(2 * UP + 3 * RIGHT)
            )

            return updated

        def apply_permutation(
            perm_left, perm_right, speed=0.2, color_left=RED, color_right=RED
        ):
            new_table_right = update_table_right(perm_right)
            (
                three_temp,
                four_temp,
                one_temp,
                eight_temp,
            ) = update_puzzle_right(perm_right, color_right)

            new_table_left = update_table_left(perm_left)
            (
                father_temp,
                mother_temp,
                parent_temp,
            ) = update_puzzle_left(perm_left, color_left)

            self.play(
                Transform(father, father_temp),
                Transform(mother, mother_temp),
                Transform(parent, parent_temp),
                Transform(table_left, new_table_left),
                Transform(three, three_temp),
                Transform(four, four_temp),
                Transform(one, one_temp),
                Transform(eight, eight_temp),
                Transform(table_right, new_table_right),
                run_time=speed,
            )

        perms = [list(p) for p in permutations("0123456789")]

        left_indices = {42: True, 72: True}
        sampled_left = (
            sample(perms, 42)
            + [
                [
                    "4",
                    "7",
                    "0",
                    "1",
                    "2",
                    "5",
                    "9",
                    "8",
                    "6",
                    "3",
                ]
            ]
            + sample(perms, 29)
            + [
                [
                    "4",
                    "7",
                    "0",
                    "2",
                    "1",
                    "5",
                    "9",
                    "8",
                    "6",
                    "3",
                ]
            ]
            + sample(perms, 27)
        )

        right_indices = {18: True, 33: True, 57: True, 69: True, 88: True}
        sampled_right = (
            sample(perms, 18)
            + [
                [
                    "0",
                    "2",
                    "9",
                    "5",
                    "4",
                    "1",
                    "7",
                    "6",
                    "8",
                    "3",
                ]
            ]  # 19
            + sample(perms, 14)
            + [
                [
                    "0",
                    "8",
                    "6",
                    "4",
                    "3",
                    "7",
                    "1",
                    "9",
                    "2",
                    "5",
                ]
            ]  # 34
            + sample(perms, 23)
            + [
                [
                    "3",
                    "0",
                    "8",
                    "9",
                    "6",
                    "7",
                    "1",
                    "4",
                    "2",
                    "5",
                ]
            ]  # 58
            + sample(perms, 11)
            + [
                [
                    "7",
                    "2",
                    "3",
                    "6",
                    "4",
                    "0",
                    "8",
                    "5",
                    "9",
                    "1",
                ]
            ]  # 70
            + sample(perms, 18)
            + [
                [
                    "9",
                    "5",
                    "6",
                    "8",
                    "0",
                    "7",
                    "1",
                    "4",
                    "2",
                    "3",
                ]
            ]  # 89
            + sample(perms, 11)
        )

        for i in range(100):
            speed = 1 if i == 0 or i == 99 else 0.3
            color_left = GREEN if i in left_indices else RED
            color_right = GREEN if i in right_indices else RED

            apply_permutation(
                sampled_left[i],
                sampled_right[i],
                speed=speed,
                color_left=color_left,
                color_right=color_right,
            )

        self.wait()

        right_solutions = Text("22", color=GREEN, font_size=40).shift(
            2 * UP + 3 * RIGHT
        )
        left_solutions = Text("2", color=GREEN, font_size=40).shift(2 * UP + 3 * LEFT)

        self.play(
            Transform(table_left, left_solutions),
            Transform(table_right, right_solutions),
        )
        self.wait()

        self.play(FadeOut(left_puzzle, right_puzzle, table_left, table_right))


class SemiBruteForce(Scene):
    def construct(self):
        def update_text(target, term):
            if term == 1:
                target.next_to(first_ten, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        first_ten, aligned_edge=RIGHT, direction=UP
                    )
                )

            elif term == 2:
                target.next_to(second_ten, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        second_ten, aligned_edge=RIGHT, direction=UP
                    )
                )

            elif term == 3:
                target.next_to(line, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(line, aligned_edge=RIGHT, direction=UP)
                )

            else:
                target.next_to(operator, aligned_edge=RIGHT, direction=DOWN)
                target.add_updater(
                    lambda x: target.next_to(
                        operator, aligned_edge=RIGHT, direction=DOWN
                    )
                )

            return target

        line = Line(stroke_width=2).set_length(4)
        plus = Tex("+")

        operator = VGroup(line, plus).arrange(UP, aligned_edge=LEFT)

        second_ten = update_text(Tex("T\phantom{--}E\phantom{--}N"), 3)
        first_ten = update_text(Tex("T\phantom{--}E\phantom{--}N"), 2)
        forty = update_text(
            Tex("F\phantom{--}O\phantom{--}R\phantom{--}T\phantom{--}Y"), 1
        )
        sixty = update_text(
            Tex("S\phantom{---}I\phantom{::-}X\phantom{--}T\phantom{--}Y"), 4
        )

        puzzle = VGroup(forty, first_ten, second_ten, operator, sixty)
        puzzle.shift((0.75 * DOWN))

        self.play(FadeIn(puzzle))
        self.wait()

        letters = ["N", "I", "F", "S", "X", "E", "Y", "R", "T", "O"]
        base = ["0", "1", " ", " ", " ", "5", " ", " ", " ", "9"]

        letter_to_pos = {letter: idx for idx, letter in enumerate(letters)}
        pos_to_letter = {
            idx: letter for idx, letter in enumerate(["F", "S", "X", "Y", "R", "T"])
        }

        def update_puzzle(perm, color=RED):
            ten_1, ten_2, ten_3, ten_4 = ("T\phantom{--}", "5", "\phantom{--}", "0")
            forty_1, forty_2, forty_3 = (
                "F\phantom{--}",
                "9",
                "\phantom{--}R\phantom{--}T\phantom{--}Y",
            )
            sixty_1, sixty_2, sixty_3 = (
                "S\phantom{--}",
                "1",
                "\phantom{--}X\phantom{--}T\phantom{--}Y",
            )

            mapping = {pos_to_letter[index]: value for index, value in enumerate(perm)}

            ten_1_updated = "".join([mapping[c] if c in mapping else c for c in ten_1])
            ten_3_updated = "".join([mapping[c] if c in mapping else c for c in ten_3])

            forty_1_updated = "".join(
                [mapping[c] if c in mapping else c for c in forty_1]
            )
            forty_3_updated = "".join(
                [mapping[c] if c in mapping else c for c in forty_3]
            )

            sixty_1_updated = "".join(
                [mapping[c] if c in mapping else c for c in sixty_1]
            )
            sixty_3_updated = "".join(
                [mapping[c] if c in mapping else c for c in sixty_3]
            )

            first_ten_updated = (
                Tex(ten_1_updated, ten_2, ten_3_updated, ten_4, color=color)
                .set_color_by_tex("5", GREEN)
                .set_color_by_tex("0", GREEN)
            )
            second_ten_updated = (
                Tex(ten_1_updated, ten_2, ten_3_updated, ten_4, color=color)
                .set_color_by_tex("5", GREEN)
                .set_color_by_tex("0", GREEN)
            )
            forty_updated = Tex(
                forty_1_updated, forty_2, forty_3_updated, color=color
            ).set_color_by_tex("9", GREEN)
            sixty_updated = Tex(
                sixty_1_updated, sixty_2, sixty_3_updated, color=color
            ).set_color_by_tex("1", GREEN)

            second_ten_updated = update_text(second_ten_updated, 3)
            first_ten_updated = update_text(first_ten_updated, 2)
            forty_updated = update_text(forty_updated, 1)
            sixty_updated = update_text(sixty_updated, 4)

            puzzle_updated = (
                forty_updated,
                first_ten_updated,
                second_ten_updated,
                sixty_updated,
            )

            return puzzle_updated

        def update_table(perm):
            for i, v in enumerate(perm):
                letter = pos_to_letter[i]
                base[letter_to_pos[letter]] = v

            updated = (
                Table(
                    [letters, base],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                )
                .scale(0.5)
                .shift(2.25 * UP)
            )
            updated.add_highlighted_cell((2, 2), color=GREEN)
            updated.add_highlighted_cell((2, 3), color=GREEN)
            updated.add_highlighted_cell((2, 11), color=GREEN)
            updated.add_highlighted_cell((2, 7), color=GREEN)

            return updated

        def apply_permutation(perm, speed=0.1):
            new_table = update_table(perm)
            (
                forty_temp,
                first_ten_temp,
                second_ten_temp,
                sixty_temp,
            ) = update_puzzle(perm)

            self.play(
                Transform(forty, forty_temp),
                Transform(sixty, sixty_temp),
                Transform(first_ten, first_ten_temp),
                Transform(second_ten, second_ten_temp),
                Transform(table, new_table),
                run_time=speed,
            )

        self.play(
            Transform(
                first_ten,
                update_text(
                    Tex(
                        "T",
                        r"\phantom{O}5\phantom{---}0\phantom{-}",
                    ).set_color_by_tex("5", RED),
                    2,
                ),
            ),
            Transform(
                second_ten,
                update_text(
                    Tex(
                        "T",
                        r"\phantom{O}5\phantom{---}0\phantom{-}",
                    ).set_color_by_tex("5", RED),
                    3,
                ),
            ),
            Transform(
                forty,
                update_text(
                    Tex(
                        r"F\phantom{---}",
                        "9",
                        r"\phantom{--}R\phantom{--}T\phantom{--}Y",
                    ).set_color_by_tex("9", RED),
                    1,
                ),
            ),
            Transform(
                sixty,
                update_text(
                    Tex(
                        r"S\phantom{---}",
                        "1",
                        r"\phantom{:-}X\phantom{--}T\phantom{--}Y",
                    ).set_color_by_tex("1", RED),
                    4,
                ),
            ),
        )

        table = (
            Table(
                [letters, base],
                row_labels=[Text("Letters", color=GREEN), Text("Digits", color=RED)],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift(2.25 * UP)
        )
        table.add_highlighted_cell((2, 2), color=GREEN)
        table.add_highlighted_cell((2, 3), color=GREEN)
        table.add_highlighted_cell((2, 7), color=GREEN)
        table.add_highlighted_cell((2, 11), color=GREEN)

        self.play(FadeIn(table))
        self.wait()

        perms = [list(p) for p in permutations("234678")]
        sampled = sample(perms, 75)

        for index, perm in enumerate(sampled):
            speed = 1 if index < 2 else 0.1
            apply_permutation(perm, speed)

        perm_solution = ["2", "3", "4", "6", "7", "8"]
        new_table = update_table(perm_solution)
        (
            forty_temp,
            first_ten_temp,
            second_ten_temp,
            sixty_temp,
        ) = update_puzzle(perm_solution, color=GREEN)

        self.play(
            Transform(forty, forty_temp),
            Transform(sixty, sixty_temp),
            Transform(first_ten, first_ten_temp),
            Transform(second_ten, second_ten_temp),
            Transform(table, new_table),
            run_time=0.5,
        )
        self.wait()

        self.play(FadeOut(table, puzzle))


class BruteForce(Scene):
    def construct(self):
        letters = ["N", "I", "F", "S", "X", "E", "Y", "R", "T", "O"]
        perm_solution = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        blank = [" " for _ in range(10)]

        table = (
            Table(
                [letters, blank],
                row_labels=[Text("Letters", color=GREEN), Text("Digits", color=RED)],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift(2.25 * UP)
        )

        self.play(FadeIn(table))
        self.wait()

        def update_text(target, term):
            if term == 1:
                target.next_to(first_ten, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        first_ten, aligned_edge=RIGHT, direction=UP
                    )
                )

            elif term == 2:
                target.next_to(second_ten, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(
                        second_ten, aligned_edge=RIGHT, direction=UP
                    )
                )

            elif term == 3:
                target.next_to(line, aligned_edge=RIGHT, direction=UP)
                target.add_updater(
                    lambda x: target.next_to(line, aligned_edge=RIGHT, direction=UP)
                )

            else:
                target.next_to(operator, aligned_edge=RIGHT, direction=DOWN)
                target.add_updater(
                    lambda x: target.next_to(
                        operator, aligned_edge=RIGHT, direction=DOWN
                    )
                )

            return target

        line = Line(stroke_width=2).set_length(4)
        plus = Tex("+")

        operator = VGroup(line, plus).arrange(UP, aligned_edge=LEFT)

        second_ten = update_text(
            Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED), 3
        )
        first_ten = update_text(
            Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED), 2
        )
        forty = update_text(
            Tex(r"2\phantom{---}9\phantom{--}7\phantom{.O}8\phantom{---}6", color=RED),
            1,
        )
        sixty = update_text(
            Tex(r"3\phantom{---}1\phantom{:-}4\phantom{.O}8\phantom{---}6", color=RED),
            4,
        )

        pos_to_letter = {idx: letter for idx, letter in enumerate(letters)}

        def update_puzzle(perm, color=RED):
            ten_template = "T\phantom{--}E\phantom{--}N"
            forty_template = "F\phantom{--}O\phantom{--}R\phantom{--}T\phantom{--}Y"
            sixty_template = "S\phantom{--}I\phantom{--}X\phantom{--}T\phantom{--}Y"

            mapping = {pos_to_letter[index]: value for index, value in enumerate(perm)}

            ten_updated = "".join(
                [mapping[c] if c in mapping else c for c in ten_template]
            )
            forty_updated = "".join(
                [mapping[c] if c in mapping else c for c in forty_template]
            )
            sixty_updated = "".join(
                [mapping[c] if c in mapping else c for c in sixty_template]
            )

            second_ten_updated = update_text(Tex(ten_updated, color=color), 3)
            first_ten_updated = update_text(Tex(ten_updated, color=color), 2)
            forty_updated = update_text(Tex(forty_updated, color=color), 1)
            sixty_updated = update_text(Tex(sixty_updated, color=color), 4)

            puzzle_updated = (
                forty_updated,
                first_ten_updated,
                second_ten_updated,
                sixty_updated,
            )

            return puzzle_updated

        def update_table(perm):
            updated = (
                Table(
                    [letters, perm],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                )
                .scale(0.5)
                .shift(2.25 * UP)
            )

            return updated

        def apply_permutation(perm):
            new_table = update_table(perm)
            (
                forty_temp,
                first_ten_temp,
                second_ten_temp,
                sixty_temp,
            ) = update_puzzle(perm)

            self.play(
                Transform(forty, forty_temp),
                Transform(sixty, sixty_temp),
                Transform(first_ten, first_ten_temp),
                Transform(second_ten, second_ten_temp),
                Transform(table, new_table),
                run_time=0.1,
            )

        perms = [list(p) for p in permutations("0123456789")]
        sampled = sample(perms, 75)

        for index, perm in enumerate(sampled):
            if index == 0:
                (
                    forty,
                    first_ten,
                    second_ten,
                    sixty,
                ) = update_puzzle(perm)
                solution = VGroup(forty, first_ten, second_ten, operator, sixty)
                solution.shift((1 * DOWN))

                new_table = update_table(perm)

                self.play(Transform(table, new_table), FadeIn(solution))
                self.wait()

            else:
                apply_permutation(perm)

        new_table = update_table(perm_solution)
        (
            forty_temp,
            first_ten_temp,
            second_ten_temp,
            sixty_temp,
        ) = update_puzzle(perm_solution, GREEN)

        self.play(
            Transform(forty, forty_temp),
            Transform(sixty, sixty_temp),
            Transform(first_ten, first_ten_temp),
            Transform(second_ten, second_ten_temp),
            Transform(table, new_table),
            run_time=0.5,
        )

        self.wait()


class Permutations(Scene):
    def construct(self):
        def update_text(target, term, left=False):
            if term == 1:
                if left:
                    target.next_to(first_ten_fixed, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(
                            first_ten_fixed, aligned_edge=RIGHT, direction=UP
                        )
                    )
                else:
                    target.next_to(first_ten, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(
                            first_ten, aligned_edge=RIGHT, direction=UP
                        )
                    )

            elif term == 2:
                if left:
                    target.next_to(second_ten_fixed, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(
                            second_ten_fixed, aligned_edge=RIGHT, direction=UP
                        )
                    )
                else:
                    target.next_to(second_ten, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(
                            second_ten, aligned_edge=RIGHT, direction=UP
                        )
                    )

            elif term == 3:
                if left:
                    target.next_to(line_fixed, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(
                            line_fixed, aligned_edge=RIGHT, direction=UP
                        )
                    )
                else:
                    target.next_to(line, aligned_edge=RIGHT, direction=UP)
                    target.add_updater(
                        lambda x: target.next_to(line, aligned_edge=RIGHT, direction=UP)
                    )

            else:
                if left:
                    target.next_to(operator_fixed, aligned_edge=RIGHT, direction=DOWN)
                    target.add_updater(
                        lambda x: target.next_to(
                            operator_fixed, aligned_edge=RIGHT, direction=DOWN
                        )
                    )
                else:
                    target.next_to(operator, aligned_edge=RIGHT, direction=DOWN)
                    target.add_updater(
                        lambda x: target.next_to(
                            operator, aligned_edge=RIGHT, direction=DOWN
                        )
                    )

            return target

        line = Line(stroke_width=2).set_length(4)
        plus = Tex("+")

        operator = VGroup(line, plus).arrange(UP, aligned_edge=LEFT)

        second_ten = update_text(
            Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED), 3
        )
        first_ten = update_text(
            Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED), 2
        )
        forty = update_text(
            Tex(r"2\phantom{---}9\phantom{--}7\phantom{.O}8\phantom{---}6", color=RED),
            1,
        )
        sixty = update_text(
            Tex(r"3\phantom{---}1\phantom{:-}4\phantom{.O}8\phantom{---}6", color=RED),
            4,
        )

        solution = VGroup(forty, first_ten, second_ten, operator, sixty)
        solution.shift((0.75 * DOWN))

        used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            color=RED,
            t2c={
                "[0:1]": WHITE,
                "[20:]": WHITE,
            },
        ).shift(2.5 * UP)

        self.add(solution, used_digits)

        used_letters = Text(
            "{N, I, F,  S, X, E, Y,  R, T, O}",
            color=GREEN,
            font_size=DEFAULT_FONT_SIZE * 0.85,
            t2c={
                "[0:1]": WHITE,
                "[20:]": WHITE,
            },
        ).next_to(used_digits, DOWN)

        mapping = VGroup(used_letters, used_digits)

        letters = ["N", "I", "F", "S", "X", "E", "Y", "R", "T", "O"]
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        self.play(FadeIn(used_letters))
        self.play(
            Transform(
                forty,
                update_text(
                    Tex(
                        r"2\phantom{---}9\phantom{--}7\phantom{.O}8\phantom{---}6",
                        color=GREEN,
                    ),
                    1,
                ),
            ),
            Transform(
                sixty,
                update_text(
                    Tex(
                        r"3\phantom{---}1\phantom{:-}4\phantom{.O}8\phantom{---}6",
                        color=GREEN,
                    ),
                    4,
                ),
            ),
            Transform(
                first_ten,
                update_text(
                    Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=GREEN), 2
                ),
            ),
            Transform(
                second_ten,
                update_text(
                    Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=GREEN), 3
                ),
            ),
        )

        line_fixed = Line(stroke_width=2).set_length(4)
        plus_fixed = Tex("+")
        operator_fixed = VGroup(line_fixed, plus_fixed).arrange(UP, aligned_edge=LEFT)

        second_ten_fixed = update_text(Tex("T\phantom{--}E\phantom{--}N"), 3, left=True)
        first_ten_fixed = update_text(Tex("T\phantom{--}E\phantom{--}N"), 2, left=True)
        forty_fixed = update_text(
            Tex("F\phantom{--}O\phantom{--}R\phantom{--}T\phantom{--}Y"), 1, left=True
        )
        sixty_fixed = update_text(
            Tex("S\phantom{---}I\phantom{::-}X\phantom{--}T\phantom{--}Y"), 4, left=True
        )

        puzzle = VGroup(
            forty_fixed, first_ten_fixed, second_ten_fixed, operator_fixed, sixty_fixed
        )
        puzzle.shift((0.75 * DOWN) + (LEFT * 3))

        vbar = (
            Line(start=[0.0, 1.0, 0.0], end=[0.0, -1.0, 0.0], stroke_width=1)
            .set_length(2.5)
            .shift(0.5 * DOWN)
        )

        self.play(solution.animate.shift(RIGHT * 3))
        self.play(FadeIn(vbar))
        self.play(FadeIn(puzzle), run_time=1)
        self.wait()

        table = (
            Table(
                [letters, digits],
                row_labels=[Text("Letters", color=GREEN), Text("Digits", color=RED)],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift(2.25 * UP)
        )

        self.play(ReplacementTransform(mapping, table))
        self.wait()

        def update_puzzle(perm):
            ten_template = "T\phantom{--}E\phantom{--}N"
            forty_template = "F\phantom{--}O\phantom{--}R\phantom{--}T\phantom{--}Y"
            sixty_template = "S\phantom{--}I\phantom{--}X\phantom{--}T\phantom{--}Y"

            mapping = {pos_to_letter[index]: value for index, value in enumerate(perm)}

            ten_updated = "".join(
                [mapping[c] if c in mapping else c for c in ten_template]
            )
            forty_updated = "".join(
                [mapping[c] if c in mapping else c for c in forty_template]
            )
            sixty_updated = "".join(
                [mapping[c] if c in mapping else c for c in sixty_template]
            )

            second_ten_updated = update_text(Tex(ten_updated, color=RED), 3, left=False)
            first_ten_updated = update_text(Tex(ten_updated, color=RED), 2, left=False)
            forty_updated = update_text(Tex(forty_updated, color=RED), 1, left=False)
            sixty_updated = update_text(Tex(sixty_updated, color=RED), 4, left=False)

            puzzle_updated = (
                forty_updated,
                first_ten_updated,
                second_ten_updated,
                sixty_updated,
            )

            return puzzle_updated

        def update_table(perm):
            updated = (
                Table(
                    [letters, perm],
                    row_labels=[
                        Text("Letters", color=GREEN),
                        Text("Digits", color=RED),
                    ],
                    include_outer_lines=True,
                )
                .scale(0.5)
                .shift(2.25 * UP)
            )

            return updated

        def apply_permutation(perm):
            new_table = update_table(perm)
            (
                forty_temp,
                first_ten_temp,
                second_ten_temp,
                sixty_temp,
            ) = update_puzzle(perm)

            self.play(
                Transform(forty, forty_temp),
                Transform(sixty, sixty_temp),
                Transform(first_ten, first_ten_temp),
                Transform(second_ten, second_ten_temp),
                Transform(table, new_table),
                run_time=0.25,
            )

        pos_to_letter = {idx: letter for idx, letter in enumerate(letters)}

        reverse = list("9876543210")
        apply_permutation(reverse)
        self.wait(duration=3)

        perms = [
            ["1", "7", "6", "8", "3", "0", "5", "4", "2", "9"],
            ["6", "1", "0", "4", "5", "3", "7", "2", "8", "9"],
            ["7", "8", "5", "3", "0", "2", "4", "9", "6", "1"],
        ]

        for perm in perms:
            apply_permutation(perm)
            self.wait(duration=1)

        self.wait()
        self.play(FadeOut(vbar, puzzle, table, solution))
        self.wait()
