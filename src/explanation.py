from manim import *
import os


class Introduction(Scene):
    def construct(self):
        path = os.path.join(os.getcwd(), "media", "images", "raw", "snippet_black.png")
        code_snippet = ImageMobject(path).scale(0.6).to_edge(LEFT)

        self.add(code_snippet)

        highlight = (
            Rectangle(height=2.2, width=6.7)
            .set_stroke(width=1.5)
            .move_to(code_snippet, aligned_edge=LEFT)
            .shift(0.05 * DOWN, 0.3 * RIGHT)
        )
        self.add(highlight)
