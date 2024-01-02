from manim import *
from yt.config.config import cf


config.background_color = "#1C202A"
config.frame_width = 9
config.frame_height = 16
config.pixel_height = 3840
config.pixel_width = 2160

default_font = "Menlo"


class ListComprehensionScene(Scene):
    def construct(self):
        squares = VGroup(*[Square(color=cf.GREY, side_length=0.7)
                         for _ in range(5)])
        circles = VGroup(*[Circle(color=cf.BLUE, radius=0.25)
                         for _ in range(5)])
        squares.arrange(LEFT)
        circles.arrange(LEFT)
        circles.shift(DOWN * 2)
        brackets = VGroup(
            Text("[", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                squares, LEFT
            ),
            Text(f"]", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                squares, RIGHT
            ),
        )
        brackets_2 = VGroup(
            Text("[", font=default_font, font_size=64, color=cf.YELLOW)
            .next_to(circles, LEFT)
            .scale(0.75),
            Text(f"]", font=default_font, font_size=64, color=cf.YELLOW)
            .next_to(circles, RIGHT)
            .scale(0.75),
        )
        self.play(FadeIn(squares), FadeIn(brackets))
        self.wait(0.5)
        self.play(
            squares.animate(run_time=0.75).scale(0.75).shift(UP * 2),
            brackets.animate(run_time=0.75).scale(0.75).shift(UP * 2),
        )
        self.wait(0.5)
        equal_sign = Text("=", font=default_font,
                          font_size=64, color=cf.ORANGE)
        self.play(FadeIn(equal_sign, run_time=0.5),
                  FadeIn(brackets_2, run_time=0.5))
        self.wait(0.5)
        for i in reversed(range(5)):
            self.play(Transform(squares[i], circles[i]))
        self.play(
            FadeOut(equal_sign, run_time=0.5),
            FadeOut(brackets, run_time=0.5),
            squares.animate(run_time=0.75).scale(1.25).shift(UP * 2),
            brackets_2.animate(run_time=0.75).scale(1.25).shift(UP * 2),
        )
        self.wait()
        self.play(FadeOut(squares, run_time=0.5),
                  FadeOut(brackets_2, run_time=0.5))


class ListComprehensionScene_2(Scene):
    def construct(self):
        shapes = VGroup(
            Square(color=cf.GREY, side_length=0.7),
            Circle(color=cf.BLUE, radius=0.4),
            Square(color=cf.GREY, side_length=0.7),
            Square(color=cf.GREY, side_length=0.7),
            Circle(color=cf.BLUE, radius=0.4),
        )
        shapes.arrange(RIGHT)
        brackets = VGroup(
            Text("[", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                shapes, LEFT
            ),
            Text(f"]", font=default_font, font_size=64, color=cf.YELLOW).next_to(
                shapes, RIGHT
            ),
        )
        self.play(FadeIn(brackets))
        self.wait(0.5)
        for i in range(5):
            self.play(FadeIn(shapes[i], run_time=0.75))
        self.wait()
        self.play(FadeOut(shapes, run_time=0.5),
                  FadeOut(brackets, run_time=0.5))
