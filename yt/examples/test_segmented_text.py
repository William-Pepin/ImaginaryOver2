from manim import *
from yt.config.config import cf


class TestScene(Scene):
    def construct(self):
        raw_identificators = ["1F", "2C", "3B", "4D", "5G"]
        raw_names = ["Steve", "Stephen", "Sarah", "Bob", "Alice"]
        identificators_end = VGroup(

            *[
                Text(
                    text, font=cf.DEFAULT_FONT, font_size=64, color=cf.BLUE, line_spacing=4,
                )
                for text in (raw_identificators)
            ]
        )

        names_end = VGroup(
            *[
                Text(
                    text,
                    font=cf.DEFAULT_FONT,
                    font_size=64,
                    color=cf.BLUE,
                    line_spacing=4,
                )
                for text in (raw_names)
            ]
        )

        double_dots = VGroup(
            *[
                Text(
                    ":",
                    font=cf.DEFAULT_FONT,
                    font_size=64,
                    color=cf.ORANGE,
                    line_spacing=4,
                )
                for _ in range(5)
            ]
        )

        identificators_end.arrange_in_grid(5, 1).shift(LEFT * 2.5)
        double_dots.arrange_in_grid(5, 1, buff=0.462).align_to(
            identificators_end
        ).shift(LEFT * 1.5)
        names_end.arrange_in_grid(5, 1, col_alignments="l").shift(RIGHT * 1.5).align_to(
            identificators_end, DOWN
        )
        self.add(identificators_end, double_dots, names_end)
