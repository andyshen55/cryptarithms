from manim import *


class CreateCircle(Scene):
    def construct(self):
        # default constructor color arg sets line color
        circle = Circle(color=PINK)

        circle = Circle()
        circle.set_fill(MAROON, opacity=0.7)

        self.play(Create(circle))


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_color(WHITE)

        square = Square()
        square.rotate(PI / 4)
        square.set_fill(PURPLE, opacity=0.25)

        # self.play(Create(square))
        # self.play(Transform(square, circle))
        # self.play(FadeOut(square))

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(color=PINK, opacity=0.5)

        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        square2 = Square()
        square2.set_fill(GREEN, opacity=0.5)

        # buff of 1 corresponds to screen edge for UP, DOWN
        square2.next_to(circle, direction=LEFT, buff=1)
        square.next_to(circle, direction=RIGHT, buff=1)

        self.play(Create(circle), Create(square), Create(square2))


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        # Transform changes first arg into second arg, without updating alias
        # Replacement transform changes first into second arg, to continue use second alias

        self.play(Create(circle))
        self.play(circle.animate.set_fill(color=PINK, opacity=0.5))
        self.play(ReplacementTransform(circle, square))
        self.play(square.animate.rotate(PI / 4))
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.shift(RIGHT, UP))
        self.play(square.animate.shift(RIGHT, DOWN))
        self.play(square.animate.shift(LEFT, DOWN))
        self.play(square.animate.shift(LEFT, UP))
        self.play(square.animate.shift(RIGHT))
        self.play(FadeOut(square))


class DifferentRotations(Scene):
    def construct(self):
        # shift of 6 corresponds to left and right edges
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(6 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(6 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )

        # Waits for longest duration animation in preceding play
        self.wait()
