from manim import *
from math import sin


class FirstExample(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)

        green_square.next_to(blue_circle, RIGHT)

        self.add(blue_circle, green_square)


class SecondExample(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: sin(x), color=RED)
        area = ax.get_area(curve, x_range=(-3, 0))
        self.play(Create(ax), Create(curve), run_time=3)
        self.play(FadeIn(area))
        self.wait(2)


class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        self.play(DrawBorderThenFill(green_square))
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(ReplacementTransform(green_square, blue_circle))
        self.play(Indicate(blue_circle))
        self.wait()
        self.play(FadeOut(blue_circle))


class PositioningScene(Scene):
    def construct(self):
        plane = NumberPlane()
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)
        self.add(plane, red_dot, green_dot)

        # shift
        s = Square(color=ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)

        # move_to
        c = Circle(color=PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c)


class Grouping(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)

        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)

        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP, buff=0.5)

        self.add(circles)

        stars = VGroup(
            *[Star(color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)]
        )
        stars.arrange_in_grid(4, 5, buff=0.2)

        self.add(stars)
