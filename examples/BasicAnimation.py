from manim import *

import config


class BasicAnimation(Scene):
    def construct(self):
        polys = VGroup(
            *[
                RegularPolygon(
                    5,
                    radius=1,
                    fill_opacity=0.5,
                    color=Color(hue=j / 5, saturation=1, luminance=0.5),
                )
                for j in range(5)
            ]
        ).arrange(RIGHT)
        self.play(DrawBorderThenFill(polys), run_time=2)
        self.play(
            Rotate(polys[0], PI, rate_func=lambda t: t),
            Rotate(polys[1], PI, rate_func=smooth),
            Rotate(polys[2], PI, rate_func=lambda t: np.sin(t * PI)),
            Rotate(polys[3], PI, rate_func=there_and_back),
            Rotate(polys[4], PI, rate_func=lambda t: 1 - abs(1 - 2 * t)),
            run_time=2,
        )
        self.wait()


class LaggingGroup(Scene):
    def construct(self):
        squares = (
            VGroup(
                *[
                    Square(
                        fill_opacity=0.5,
                        color=Color(hue=j / 20, saturation=1, luminance=0.5),
                    )
                    for j in range(20)
                ]
            )
            .arrange_in_grid(4, 5)
            .scale(0.75)
        )
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio=0.15))


class AnimateSyntax(Scene):
    def construct(self):
        s = Square()
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate(run_time=2).scale(3))
        self.play(s.animate.scale(1 / 2).shift(2 * LEFT))


class AnimateSyntax_2(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s, c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s, c).animate.arrange(RIGHT, buff=1))
        self.play(c.animate(rate_func=linear).shift(RIGHT).scale(2))


class AnimateProblem(Scene):
    def construct(self):
        left_square = Square()
        right_square = Square()
        VGroup(left_square, right_square).arrange(RIGHT, buff=1)
        self.add(left_square, right_square)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, PI), run_time=2
        )  # left.square.animate will take the point and send it where it needs to, without knowing what to do
        self.wait()


class AnimationMechanism(Scene):
    def construct(self):
        c = Circle()

        c.generate_target()
        c.target.set_fill(color=GREEN, opacity=0.5)
        c.target.shift(2 * RIGHT + UP).scale(0.5)
        self.add(c)
        self.wait()
        self.play(MoveToTarget(c))

        s = Square()
        s.save_state()
        self.play(FadeIn(s))
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2 * LEFT).scale(3))
        self.play(s.animate.shift(5 * DOWN).rotate(PI / 4))
        self.wait()
        self.play(Restore(s), run_time=2)
        self.wait()
