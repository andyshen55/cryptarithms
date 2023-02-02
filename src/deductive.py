from manim import *


class Takeaways(Scene):
    def construct(self):
        first = Text(
            "1. Computers are our problem solving friends!", color=GREEN, font_size=36
        )
        second = Text(
            "2. They can help us only as much as we allow them to.",
            color=BLUE,
            font_size=36,
        )

        words = VGroup(first, second).arrange(DOWN, aligned_edge=LEFT).center()
        self.play(Write(words[0]), run_time=1.5)
        self.wait()

        self.play(Write(words[1]), run_time=1.5)
        self.wait()

        self.play(FadeOut(words))


class BetterFactorial(Scene):
    def construct(self):
        letters = ["N", "I", "F", "S", "X", "E", "Y", "R", "T", "O"]

        letters_dict = {l: Text(l, font_size=40) for l in letters}
        header = (
            VGroup(
                letters_dict["N"],
                letters_dict["I"],
                letters_dict["F"],
                letters_dict["S"],
                letters_dict["X"],
                letters_dict["E"],
                letters_dict["Y"],
                letters_dict["R"],
                letters_dict["T"],
                letters_dict["O"],
            )
            .arrange(RIGHT, buff=0.75)
            .shift(UP * 3)
        )

        self.play(FadeIn(header))

        n_ = (
            Text("1", font_size=40, color=GREEN)
            .next_to(header[0], DOWN)
            .shift(DOWN * 2.5)
        )
        i_ = (
            Text("1", font_size=40, color=GREEN)
            .next_to(header[1], DOWN)
            .shift(DOWN * 2.5)
        )
        e_ = (
            Text("1", font_size=40, color=GREEN)
            .next_to(header[5], DOWN)
            .shift(DOWN * 2.5)
        )
        o_ = (
            Text("1", font_size=40, color=GREEN)
            .next_to(header[9], DOWN)
            .shift(DOWN * 2.5)
        )

        self.play(FadeIn(n_, i_, e_, o_))
        self.wait()

        f_ = (
            Text("6", font_size=40, color=BLUE)
            .next_to(header[2], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(f_))

        s_ = (
            Text("5", font_size=40, color=BLUE)
            .next_to(header[3], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(s_), run_time=0.8)

        x_ = (
            Text("4", font_size=40, color=BLUE)
            .next_to(header[4], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(x_), run_time=0.6)

        y_ = (
            Text("3", font_size=40, color=BLUE)
            .next_to(header[6], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(y_), run_time=0.4)

        r_ = (
            Text("2", font_size=40, color=BLUE)
            .next_to(header[7], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(r_), run_time=0.3)

        t_ = (
            Text("1", font_size=40, color=BLUE)
            .next_to(header[8], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(FadeIn(t_), run_time=0.2)
        self.wait()

        operators = VGroup(
            Text("*", font_size=40).next_to(n_, RIGHT),
            Text("*", font_size=40).next_to(i_, RIGHT),
            Text("*", font_size=40).next_to(f_, RIGHT),
            Text("*", font_size=40).next_to(s_, RIGHT),
            Text("*", font_size=40).next_to(e_, RIGHT),
            Text("*", font_size=40).next_to(x_, RIGHT),
            Text("*", font_size=40).next_to(y_, RIGHT),
            Text("*", font_size=40).next_to(r_, RIGHT),
            Text("*", font_size=40).next_to(t_, RIGHT),
        )
        self.play(FadeIn(operators))
        self.wait()

        numbers = VGroup(n_, i_, f_, s_, e_, x_, y_, t_, r_, o_, operators)
        complexity = Text("6!", color=BLUE, font_size=50)
        prev_complexity = Text("10!", color=RED, font_size=50).shift(2.5 * RIGHT)

        self.play(ReplacementTransform(numbers, complexity))
        self.wait()

        self.play(complexity.animate.shift(2.5 * LEFT))
        self.play(FadeIn(prev_complexity))

        self.wait()

        line = Line(stroke_width=1.5).set_length(1)
        self.play(
            complexity.animate.shift(2.5 * RIGHT + 0.5 * UP),
            prev_complexity.animate.shift(2.5 * LEFT + 0.5 * DOWN),
            FadeIn(line),
        )
        self.wait()

        fraction = VGroup(line, complexity, prev_complexity)
        expanded = MathTex(r"\frac{720}{3628800}", font_size=60)
        simplified = MathTex(r"\approx \ 0.0198\%", font_size=60).shift(1.5 * RIGHT)

        self.play(Transform(fraction, expanded))
        self.wait()

        self.play(fraction.animate.shift(1.5 * LEFT))
        self.play(Write(simplified))
        self.wait()

        self.play(FadeOut(fraction, simplified, header))


class Factorial(Scene):
    def construct(self):
        line = Line(stroke_width=2).set_length(4)
        plus = Tex("+")
        operator = VGroup(line, plus).arrange(UP, aligned_edge=LEFT)

        second_ten = Tex(
            r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=GREEN
        ).next_to(line, aligned_edge=RIGHT, direction=UP)
        first_ten = Tex(
            r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=GREEN
        ).next_to(second_ten, aligned_edge=RIGHT, direction=UP)
        forty = Tex(
            r"2\phantom{---}9\phantom{--}7\phantom{.O}8\phantom{---}6", color=GREEN
        ).next_to(first_ten, aligned_edge=RIGHT, direction=UP)
        sixty = Tex(
            r"3\phantom{---}1\phantom{:-}4\phantom{.O}8\phantom{---}6", color=GREEN
        ).next_to(operator, aligned_edge=RIGHT, direction=DOWN)

        solution = VGroup(forty, first_ten, second_ten, operator, sixty)
        solution.shift((1 * DOWN))

        letters = ["N", "I", "F", "S", "X", "E", "Y", "R", "T", "O"]

        perm_solution = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        table = (
            Table(
                [letters, perm_solution],
                row_labels=[Text("Letters", color=GREEN), Text("Digits", color=RED)],
                include_outer_lines=True,
            )
            .scale(0.5)
            .shift(2.25 * UP)
        )

        self.add(table, solution)
        self.wait()

        self.play(FadeOut(table, solution))

        letters_dict = {l: Text(l, font_size=40) for l in letters}
        header = (
            VGroup(
                letters_dict["N"],
                letters_dict["I"],
                letters_dict["F"],
                letters_dict["S"],
                letters_dict["X"],
                letters_dict["E"],
                letters_dict["Y"],
                letters_dict["R"],
                letters_dict["T"],
                letters_dict["O"],
            )
            .arrange(RIGHT, buff=0.75)
            .shift(UP * 3)
        )

        self.play(FadeIn(header))

        n_digits = (
            VGroup(
                Text("0", font_size=30, color=GREEN),
                Text("1", font_size=30, color=RED),
                Text("2", font_size=30, color=RED),
                Text("3", font_size=30, color=RED),
                Text("4", font_size=30, color=RED),
                Text("5", font_size=30, color=RED),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[0], DOWN * 2)
        )
        self.play(Write(n_digits))

        i_digits = (
            VGroup(
                Text("1", font_size=30, color=GREEN),
                Text("2", font_size=30, color=RED),
                Text("3", font_size=30, color=RED),
                Text("4", font_size=30, color=RED),
                Text("5", font_size=30, color=RED),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[1], DOWN * 2)
        )
        self.play(Write(i_digits))

        f_digits = (
            VGroup(
                Text("2", font_size=30, color=GREEN),
                Text("3", font_size=30, color=RED),
                Text("4", font_size=30, color=RED),
                Text("5", font_size=30, color=RED),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[2], DOWN * 2)
        )
        self.play(Write(f_digits))

        s_digits = (
            VGroup(
                Text("3", font_size=30, color=GREEN),
                Text("4", font_size=30, color=RED),
                Text("5", font_size=30, color=RED),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[3], DOWN * 2)
        )
        self.play(Write(s_digits), run_time=0.8)

        x_digits = (
            VGroup(
                Text("4", font_size=30, color=GREEN),
                Text("5", font_size=30, color=RED),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[4], DOWN * 2)
        )
        self.play(Write(x_digits), run_time=0.7)

        e_digits = (
            VGroup(
                Text("5", font_size=30, color=GREEN),
                Text("6", font_size=30, color=RED),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[5], DOWN * 2)
        )
        self.play(Write(e_digits), run_time=0.6)

        y_digits = (
            VGroup(
                Text("6", font_size=30, color=GREEN),
                Text("7", font_size=30, color=RED),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[6], DOWN * 2)
        )
        self.play(Write(y_digits), run_time=0.5)

        r_digits = (
            VGroup(
                Text("7", font_size=30, color=GREEN),
                Text("8", font_size=30, color=RED),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[7], DOWN * 2)
        )
        self.play(Write(r_digits), run_time=0.4)

        t_digits = (
            VGroup(
                Text("8", font_size=30, color=GREEN),
                Text("9", font_size=30, color=RED),
            )
            .arrange(DOWN)
            .next_to(header[8], DOWN * 2)
        )
        self.play(Write(t_digits), run_time=0.3)

        o_digits = (
            VGroup(
                Text("9", font_size=30, color=GREEN),
            )
            .arrange(DOWN)
            .next_to(header[9], DOWN * 2)
        )
        self.play(Write(o_digits), run_time=0.2)
        self.wait()

        n_10 = (
            Text("10", font_size=40, color=BLUE)
            .next_to(header[0], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(n_digits, n_10))

        i_9 = (
            Text("9", font_size=40, color=BLUE)
            .next_to(header[1], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(i_digits, i_9))

        f_8 = (
            Text("8", font_size=40, color=BLUE)
            .next_to(header[2], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(f_digits, f_8))

        s_7 = (
            Text("7", font_size=40, color=BLUE)
            .next_to(header[3], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(s_digits, s_7), run_time=0.8)

        x_6 = (
            Text("6", font_size=40, color=BLUE)
            .next_to(header[4], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(x_digits, x_6), run_time=0.7)

        e_5 = (
            Text("5", font_size=40, color=BLUE)
            .next_to(header[5], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(e_digits, e_5), run_time=0.6)

        y_4 = (
            Text("4", font_size=40, color=BLUE)
            .next_to(header[6], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(y_digits, y_4), run_time=0.5)

        r_3 = (
            Text("3", font_size=40, color=BLUE)
            .next_to(header[7], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(r_digits, r_3), run_time=0.4)

        t_2 = (
            Text("2", font_size=40, color=BLUE)
            .next_to(header[8], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(t_digits, t_2), run_time=0.3)

        o_1 = (
            Text("1", font_size=40, color=BLUE)
            .next_to(header[9], DOWN)
            .shift(DOWN * 2.5)
        )
        self.play(ReplacementTransform(o_digits, o_1), run_time=0.2)

        operators = VGroup(
            Text("*", font_size=40).next_to(n_10, RIGHT),
            Text("*", font_size=40).next_to(i_9, RIGHT),
            Text("*", font_size=40).next_to(f_8, RIGHT),
            Text("*", font_size=40).next_to(s_7, RIGHT),
            Text("*", font_size=40).next_to(x_6, RIGHT),
            Text("*", font_size=40).next_to(e_5, RIGHT),
            Text("*", font_size=40).next_to(y_4, RIGHT),
            Text("*", font_size=40).next_to(r_3, RIGHT),
            Text("*", font_size=40).next_to(t_2, RIGHT),
        )
        self.play(FadeIn(operators))
        self.wait()

        numbers = VGroup(n_10, i_9, f_8, s_7, x_6, e_5, y_4, r_3, t_2, o_1, operators)
        complexity = Text("10!", color=BLUE, font_size=50)

        self.play(ReplacementTransform(numbers, complexity))
        self.wait()

        self.play(FadeOut(complexity, header))


class ColumnSolve(Scene):
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

        self.play(puzzle.animate.shift(3 * LEFT), run_time=1.5)

        # First deductive step, on column 1
        column_rectangle = (
            Rectangle(height=3.33, width=0.66)
            .shift((0.6 * UP) + (1.85 * RIGHT) + (0.75 * DOWN) + (3 * LEFT))
            .set_color(YELLOW)
        )
        first_eq = MathTex(r"Y + 2N \equiv Y \ (\textrm{mod}\ 10)", font_size=42)
        first_eq.shift((3 * RIGHT) + (0.5 * UP))

        self.play(Create(column_rectangle))
        self.play(Write(first_eq), run_time=1)
        self.wait(2)

        first_implies = MathTex(
            r"\implies \ N = 5 \ \textrm{or} \ N = 0", font_size=42
        ).next_to(first_eq, DOWN)

        self.play(Write(first_implies), run_time=1)
        self.play(column_rectangle.animate.shift(0.725 * LEFT))

        # Second step, on column 2
        second_eq = MathTex(
            r"T + 2E + (1) \equiv T \ (\textrm{mod}\ 10)", font_size=42
        ).next_to(first_implies, DOWN)

        self.play(Write(second_eq), run_time=1)
        self.wait(2)

        second_implies = MathTex(r"\implies \ N = 0, \ E = 5", font_size=42).next_to(
            second_eq, DOWN
        )

        self.play(Write(second_implies), run_time=1)
        self.play(FadeOut(column_rectangle))

        # Fill in N, E entries
        temp_first_ten = Tex(
            "T",
            r"\phantom{O}5\phantom{---}0\phantom{-}",
        ).set_color_by_tex("5", RED)

        temp_second_ten = Tex(
            "T",
            r"\phantom{O}5\phantom{---}0\phantom{-}",
        ).set_color_by_tex("5", RED)

        self.play(
            Transform(first_ten, update_text(temp_first_ten, 2)),
            Transform(second_ten, update_text(temp_second_ten, 3)),
        )
        self.wait()

        used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}", t2c={"[1:2]": RED, "[11:12]": RED}
        ).shift(2.5 * UP)
        self.play(FadeIn(used_digits))

        # Third step, on column 5
        column_rectangle.shift(2.9 * 0.725 * LEFT)
        self.play(
            Create(column_rectangle),
            FadeOut(first_eq, first_implies, second_eq, second_implies),
        )

        first_eq = MathTex(r"F + c_4 = S", font_size=42)
        first_eq.shift((3 * RIGHT) + (0.5 * UP))

        self.play(Write(first_eq), run_time=1)
        self.wait(2)

        first_implies = MathTex(r"\implies \ c_4 = 1", font_size=42).next_to(
            first_eq, DOWN
        )

        carry_c4 = (
            Tex("1", font_size=42).next_to(column_rectangle, UP).shift(0.725 * DOWN)
        )

        self.play(Write(first_implies), FadeIn(carry_c4), run_time=1)

        temp_first_eq = MathTex(r"F + 1 = S", font_size=42)
        temp_first_eq.shift((3 * RIGHT) + (0.5 * UP))

        self.play(Transform(first_eq, temp_first_eq), FadeOut(first_implies))

        # Fourth step, on column 4
        self.play(column_rectangle.animate.shift(0.725 * RIGHT))
        second_eq = MathTex(r"O + c_3 = I + 10", font_size=42).next_to(first_eq, DOWN)

        self.play(Write(second_eq), run_time=1)
        self.wait(2)

        second_implies = MathTex(r"\implies \ c_3 = 2", font_size=42).next_to(
            second_eq, DOWN
        )

        carry_c3 = (
            Tex("2", font_size=42).next_to(column_rectangle, UP).shift(0.725 * DOWN)
        )

        self.play(Write(second_implies), FadeIn(carry_c3), run_time=1)

        third_implies = MathTex(
            r"\implies \ O = 8 \ \textrm{or} \ O = 9", font_size=42
        ).next_to(second_implies, DOWN)
        self.play(Write(third_implies), run_time=1)
        self.wait(2)

        fourth_implies = MathTex(r"\implies \ O = 9, \ I = 1", font_size=42).next_to(
            first_eq, DOWN
        )

        third_eq = MathTex(r"F + 1 = S", font_size=42)
        third_eq.shift((3 * RIGHT) + (0.5 * UP))

        self.play(
            Transform(third_implies, fourth_implies),
            FadeOut(second_eq, second_implies),
        )

        # Fill in O, I entries
        self.play(FadeOut(column_rectangle))

        temp_forty = Tex(
            r"F\phantom{---}", "9", r"\phantom{--}R\phantom{--}T\phantom{--}Y"
        ).set_color_by_tex("9", RED)

        temp_sixty = Tex(
            r"S\phantom{---}", "1", r"\phantom{:-}X\phantom{--}T\phantom{--}Y"
        ).set_color_by_tex("1", RED)

        self.play(
            Transform(forty, update_text(temp_forty, 1)),
            Transform(sixty, update_text(temp_sixty, 4)),
        )
        self.wait()

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={"[1:2]": RED, "[11:12]": RED, "[3:4]": RED, "[19:20]": RED},
        ).shift(2.5 * UP)
        self.play(Transform(used_digits, temp_used_digits))

        # Fifth step, column 3
        column_rectangle.shift(0.725 * RIGHT)
        self.play(Create(column_rectangle), FadeOut(third_implies))

        second_eq = MathTex(r"R + 2T + 1 = 20 + X", font_size=42).next_to(
            first_eq, DOWN
        )

        carry_c2 = (
            Tex("1", font_size=42).next_to(column_rectangle, UP).shift(0.725 * DOWN)
        )

        self.play(Write(second_eq), FadeIn(carry_c2), run_time=1)
        self.wait(2)

        second_implies = MathTex(r"\implies \ T \geq 6", font_size=42).next_to(
            second_eq, DOWN
        )

        self.play(Write(second_implies, run_time=1))
        self.wait(2)

        temp_second = MathTex(
            r"\implies \ T = 7 \ \textrm{or} \ T = 8", font_size=42
        ).next_to(second_eq, DOWN)

        self.play(Transform(second_implies, temp_second))
        self.wait()

        # Case 7
        case_7 = (
            Tex("Case: T = 7", color=BLUE)
            .next_to(first_eq, UP)
            .shift((LEFT) + (0.125 * UP))
        )
        self.play(Write(case_7), run_time=1)

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
                "[15:16]": BLUE,
            },
        ).shift(2.5 * UP)
        self.play(Transform(used_digits, temp_used_digits), FadeOut(second_implies))

        temp_second = MathTex(r"R + 15 = 20 + X", font_size=42).next_to(first_eq, DOWN)
        self.play(Transform(second_eq, temp_second))
        self.wait(2)

        temp_second = MathTex(r"\implies \ R = 8, \ X = 3", font_size=42).next_to(
            second_eq, DOWN
        )
        self.play(Write(temp_second), run_time=1)

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
                "[15:16]": BLUE,
                "[7:8]": BLUE,
                "[17:18]": BLUE,
            },
        ).shift(2.5 * UP)
        self.play(Transform(used_digits, temp_used_digits))
        self.wait()

        box = SurroundingRectangle(first_eq)
        self.play(Create(box))
        self.wait(2)

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
            },
        ).shift(2.5 * UP)
        self.play(
            Transform(used_digits, temp_used_digits),
            Transform(
                second_eq,
                MathTex(r"R + 2T + 1 = 20 + X", font_size=42).next_to(first_eq, DOWN),
            ),
            FadeOut(temp_second),
        )
        self.wait()

        # Case 8
        case_8 = (
            Tex("Case: T = 8", color=BLUE)
            .next_to(first_eq, UP)
            .shift((LEFT) + (0.125 * UP))
        )
        self.play(FadeOut(box), ReplacementTransform(case_7, case_8), run_time=1)

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
                "[17:18]": BLUE,
            },
        ).shift(2.5 * UP)
        self.play(Transform(used_digits, temp_used_digits))

        temp_second = MathTex(r"R + 17 = 20 + X", font_size=42).next_to(first_eq, DOWN)
        self.play(Transform(second_eq, temp_second))
        self.wait(2)

        temp_second = MathTex(r"\implies \ R = 7, \ X = 4", font_size=42).next_to(
            second_eq, DOWN
        )
        self.play(Write(temp_second), run_time=1)

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
                "[15:16]": BLUE,
                "[9:10]": BLUE,
                "[17:18]": BLUE,
            },
        ).shift(2.5 * UP)
        self.play(Transform(used_digits, temp_used_digits))
        self.wait()

        # Final assignments
        temp_forty = Tex(
            r"F\phantom{---}", r"9\phantom{--}7\phantom{.O}8\phantom{--}", "Y"
        ).set_color_by_tex("9", RED)

        temp_first_ten = Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED)
        temp_second_ten = Tex(r"8\phantom{.--}5\phantom{---}0\phantom{-}", color=RED)

        temp_sixty = Tex(
            r"S\phantom{---}", r"1\phantom{:-}4\phantom{.O}8\phantom{--}", "Y"
        ).set_color_by_tex("1", RED)

        self.play(
            Transform(forty, update_text(temp_forty, 1)),
            Transform(first_ten, update_text(temp_first_ten, 2)),
            Transform(second_ten, update_text(temp_second_ten, 3)),
            Transform(sixty, update_text(temp_sixty, 4)),
        )
        self.wait()

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            t2c={
                "[1:2]": RED,
                "[11:12]": RED,
                "[3:4]": RED,
                "[19:20]": RED,
                "[15:16]": RED,
                "[9:10]": RED,
                "[17:18]": RED,
            },
        ).shift(2.5 * UP)

        self.play(
            Transform(used_digits, temp_used_digits),
            FadeOut(case_8, second_eq, temp_second, column_rectangle),
        )
        self.wait(2)

        first_implies = MathTex(r"\implies \ F = 2, \ S = 3", font_size=42).next_to(
            first_eq, DOWN
        )
        second_implies = MathTex(r"\implies \ Y = 6", font_size=42).next_to(
            first_implies, DOWN
        )

        self.play(Write(first_implies), run_time=1)
        self.play(Write(second_implies), run_time=1)

        temp_forty = Tex(
            r"2\phantom{---}9\phantom{--}7\phantom{.O}8\phantom{---}6", color=RED
        )
        temp_sixty = Tex(
            r"3\phantom{---}1\phantom{:-}4\phantom{.O}8\phantom{---}6", color=RED
        )

        self.play(
            Transform(forty, update_text(temp_forty, 1)),
            Transform(sixty, update_text(temp_sixty, 4)),
        )
        self.wait()

        temp_used_digits = Text(
            "{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
            color=RED,
            t2c={
                "[0:1]": WHITE,
                "[20:]": WHITE,
            },
        ).shift(2.5 * UP)
        self.play(
            Transform(used_digits, temp_used_digits),
            FadeOut(
                carry_c2, carry_c3, carry_c4, first_eq, first_implies, second_implies
            ),
        )

        # Cleanup
        self.play(puzzle.animate.shift(3 * RIGHT), run_time=1.5)

        self.wait()
