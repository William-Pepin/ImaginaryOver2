from manim import *

# config.background_color = WHITE
# config.frame_width = 9
# config.frame_height = 16

config.pixel_width = 1080
config.pixel_height = 1920


class SimpleScene(Scene):
    def construct(self):
        plane = NumberPlane(x_range=(-5, 5), y_range=(-8, 8))
        t = Triangle(color=PURPLE, fill_opacity=0.5)
        self.add(t)
        self.add(plane)


class ChangeDefaults(Scene):
    def construct(self):
        Text.set_default(color=BLACK)
        t = Text("Hello World!")
        self.add(t)


class GroupingScene(Scene):
    def construct(self):
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)
