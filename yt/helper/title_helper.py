from manim import *
from yt.config.config import cf
from typing import Iterable


class TitleHelper():
    def __init__(self, scene: Scene):
        self._scene = scene

    def show_title(self, text: Iterable[str]):
        title = Paragraph(*text, font_size="48",
                          alignment="center", line_spacing=1)
        self._scene.play(FadeIn(title, run_time=cf.RATE_MEDIUM,
                                rate_func=rate_functions.ease_in_cubic))
        self._scene.wait(2)
        self._scene.play(FadeOut(title, run_time=cf.RATE_MEDIUM,
                                 rate_func=rate_functions.ease_out_cubic))
