from manim import *
from yt.config.config import cf
from typing import Sequence


class ListOfText(VGroup):
    def __init__(self, elements: Sequence[str], font_size, color, bracket_size):
        self.elements = VGroup(
            *[
                Text(element, font_size=font_size, color=color)
                for element in elements
            ]).arrange(RIGHT)
        self.brackets = VGroup(
            Text("[", font=cf.DEFAULT_FONT, font_size=bracket_size, color=cf.YELLOW).next_to(
                self.elements, LEFT
            ), Text(f"]", font=cf.DEFAULT_FONT, font_size=bracket_size, color=cf.YELLOW).next_to(
                self.elements, RIGHT))
        super().__init__(self.elements, self.brackets)
