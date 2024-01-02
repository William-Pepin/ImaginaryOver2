# faire un wrapper avec un abstract class pour une default scene avec des fadeouts et un titre
from manim import *
from typing import Iterable
import config as cf


class DefaultScene(Scene):
    _title = ("Default","Scene","Title")

    def construct(self):
        self.title(self._title)
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()
'''
        self.write_code(self.generate_code_layout(code))

    def title(self, text:Iterable[str]):
        title = Paragraph(*text, font_size="48", alignment="center")
        self.play(FadeIn(title, run_time=cf.RATE_MEDIUM, rate_func=rate_functions.ease_in_cubic))
        self.wait(2)
        self.play(FadeOut(title, run_time=cf.RATE_MEDIUM, rate_func=rate_functions.ease_out_cubic))

    def generate_code_layout(self, raw_code: str) -> Code:
        code_layout = rendered_code = Code(code=raw_code, tab_width=2, line_spacing=0.8, background="rectangle", background_stroke_width=0,
                            language="Python", font="Menlo", style="lightbulb")
        rendered_code.background_mobject.color = cf.LINE_BACKBROUND
        rendered_code.line_numbers.color = cf.GREY
        return code_layout

    def write_code(self, code_layout:Code) -> None:
        self.play(FadeIn(code_layout.background_mobject, code_layout.line_numbers, run_time=cf.RATE_MEDIUM))
        for line in code_layout.code:
            self.play(AddTextLetterByLetter(line, time_per_char=0.08333, rate_func=rate_functions.ease_in_out_sine))

       
       
        
        
        
        


    
        

        


        


