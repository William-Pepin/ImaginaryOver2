from manim import *
from yt.config.config import cf


class CodeHelper():
    def __init__(self, scene: Scene):
        self._scene = scene

    def generate_code_layout(self, raw_code: str, font_size=24) -> Code:
        code_layout = Code(code=raw_code, tab_width=2, line_spacing=0.8, font_size=font_size, background="rectangle", background_stroke_width=0,
                           language="Python", font="Menlo", style="lightbulb").align_on_border(LEFT)
        code_layout.background_mobject.color = cf.LINE_BACKBROUND
        code_layout.line_numbers.color = cf.DARK_GREY
        return code_layout

    def show_code_block(self, code_layout: Code) -> None:
        self._scene.play(FadeIn(code_layout.background_mobject,
                                code_layout.line_numbers, run_time=cf.RATE_MEDIUM))

    def write_line(self, code_line) -> None:
        self._scene.play(AddTextLetterByLetter(code_line, time_per_char=0.07))

    def write_code(self, code_layout: Code) -> None:
        for line in code_layout.code:
            self._scene.play(AddTextLetterByLetter(line, time_per_char=0.07))

    def highlight(self, text: Text) -> Indicate:
        return Indicate(text, run_time=cf.RATE_VERY_SLOW,
                        rate_func=rate_functions.there_and_back_with_pause)
