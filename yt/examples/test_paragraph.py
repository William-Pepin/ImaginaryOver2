from manim import *
from yt.config.config import cf
import numpy as np


class TestScene(Scene):
    def construct(self):
        paragraph = Paragraph("test : ok", "banane : bana")
        paragraph[1][6:7].align_to(paragraph[0][4:5])
        self.add(paragraph)
        self.play(Indicate(paragraph[0][4:5]))
