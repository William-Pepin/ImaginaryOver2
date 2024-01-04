from manim import *
from yt.config.config import cf
from yt.helper.title_helper import TitleHelper


config.background_color = "#1F2430"
config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1920
config.pixel_width = 1080

default_font = "Menlo"


class Intro(Scene):
    def construct(self):
        TitleHelper(self).show_title(["Dictionnary", "in", "Python"])


class Scene_1(Scene):
    def construct(self):
        keys_strings = ["id", "name", "surname", "category", "logged_in"]
        data_strings = ["935", "John", "Smith", "Employee", "False"]

        keys = VGroup(
            *[
                Text(text, font=default_font, font_size=48, color=cf.BLUE)
                for text in keys_strings
            ]
        )

        data = VGroup(
            *[
                Text(text, font=default_font, font_size=24, color=cf.BLUE)
                for text in data_strings
            ]
        )

        data.arrange(RIGHT)
        names.arrange(LEFT)

        identificators.shift(UP * 6)
        names.shift(UP * 4)

        brackets = VGroup(
            Text("[", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                identificators, LEFT
            ),
            Text(f"]", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                identificators, RIGHT
            ),
        )

        brackets_2 = VGroup(
            Text(
                "[",
                font=default_font,
                font_size=64,
                color=cf.YELLOW,
            ).next_to(names, LEFT),
            Text(
                f"]",
                font=default_font,
                font_size=64,
                color=cf.YELLOW,
            ).next_to(names, RIGHT),
        )
        self.play(
            FadeIn(identificators), FadeIn(
                brackets), FadeIn(names), FadeIn(brackets_2)
        )
        self.wait(0.5)

        identificators_end = VGroup(
            *[
                Text(
                    text, font=default_font, font_size=64, color=cf.BLUE, line_spacing=4
                )
                for text in reversed(raw_identificators)
            ]
        )

        names_end = VGroup(
            *[
                Text(
                    text,
                    font=default_font,
                    font_size=64,
                    color=cf.BLUE,
                    line_spacing=4,
                )
                for text in reversed(raw_names)
            ]
        )

        double_dots = VGroup(
            *[
                Text(
                    ":",
                    font=default_font,
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

        for i in reversed(range(1, 5)):
            self.play(
                Transform(identificators[i], identificators_end[4 - i]),
                Transform(names[i], names_end[4 - i]),
                FadeIn(double_dots[4 - i], run_time=1.5),
            )
        self.play(
            FadeOut(brackets, brackets_2),
            Transform(identificators[0], identificators_end[4]),
            Transform(names[0], names_end[4]),
            FadeIn(double_dots[4], run_time=1.2),
        )
        self.wait()
        self.play(
            FadeOut(identificators, run_time=0.5),
            FadeOut(double_dots, run_time=0.5),
            FadeOut(names, run_time=0.5),
        )


class Scene_2(Scene):
    def construct(self):
        base_shapes = VGroup(
            Square(color=cf.GREY, side_length=0.82),
            Circle(color=cf.BLUE, radius=0.4),
            Square(color=cf.GREY, side_length=0.82),
            Triangle(color=cf.PURPLE).scale(0.45),
            Circle(color=cf.BLUE, radius=0.4),
        )
        base_shapes.arrange(RIGHT).shift(UP * 4)

        brackets = VGroup(
            Text("[", font=cf.DEFAULT_FONT, font_size=64, color=cf.YELLOW).next_to(
                base_shapes, LEFT
            ),
            Text(f"]", font=cf.DEFAULT_FONT, font_size=64, color=cf.YELLOW).next_to(
                base_shapes, RIGHT
            ),
        )

        self.play(FadeIn(base_shapes, brackets))
        self.wait(0.5)

        shape_end = (
            VGroup(
                Square(color=cf.GREY, side_length=0.82),
                Circle(color=cf.BLUE, radius=0.4),
                Triangle(color=cf.PURPLE).scale(0.45),
            )
            .arrange(DOWN)
            .shift(LEFT * 0.5)
        )

        double_dots = VGroup(
            *[
                Text(":", font=cf.DEFAULT_FONT, font_size=64, color=cf.ORANGE)
                for _ in range(3)
            ]
        )

        count_state = VGroup(
            *[DecimalNumber(1, font_size=64, num_decimal_places=0) for _ in range(3)]
        )

        self.play(
            Transform(base_shapes[0], shape_end[0]),
            FadeIn(double_dots[0].next_to(shape_end[0])),
            FadeIn(count_state[0].next_to(double_dots[0], RIGHT * 2.5)),
        )
        self.play(
            Transform(base_shapes[1], shape_end[1]),
            FadeIn(double_dots[1].next_to(shape_end[1])),
            FadeIn(count_state[1].next_to(double_dots[1], RIGHT * 2.5)),
        )
        self.play(
            Transform(base_shapes[2], shape_end[0]),
            ChangeDecimalToValue(count_state[0], 2),
        )

        self.play(
            Transform(base_shapes[3], shape_end[2]),
            FadeIn(double_dots[2].next_to(shape_end[2])),
            FadeIn(count_state[2].next_to(double_dots[2], RIGHT * 2.5)),
        )

        self.play(
            Transform(base_shapes[4], shape_end[1]),
            ChangeDecimalToValue(count_state[1], 2),
            FadeOut(brackets),
        )

        self.wait()
        self.play(FadeOut(count_state, double_dots, base_shapes))
