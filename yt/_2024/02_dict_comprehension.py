from manim import *
from yt.config.config import cf
from yt.helper.code_helper import CodeHelper
from yt.helper.title_helper import TitleHelper
from yt.helper.fade_out_helper import fade_out_all
from yt.core.list_of_text import ListOfText
from yt.core.dict_of_text import DictOfText


class Intro(Scene):
    _title = ("Dictionnary", "comprehension", "in Python")

    def construct(self):
        TitleHelper(self).show_title(self._title)


class Scene_1(Scene):

    def construct(self):
        code = \
            r"""
ids = ["1F", "2C", "3B", "4D", "5G"]
names = ["Steve", "Steven", 
        "Sarah", "Bob", "Alice"]

id_to_name = {id: name for id, name
        in zip(ids, names)}
print(id_to_name["2C"])
"""
        code_helper = CodeHelper(self)
        code_layout = code_helper.generate_code_layout(code)

        code_helper.show_code_block(code_layout)
        code_helper.write_code(code_layout)

        self.wait(cf.RATE_SLOW)

        self.play(code_helper.highlight(
            code_layout.code[4][0:36]), code_helper.highlight(code_layout.code[5][0:39]))
        self.play(code_helper.highlight(
            code_layout.code[0][0:3]), code_helper.highlight(code_layout.code[1][0:5]))
        self.play(code_helper.highlight(code_layout.code[4][14:23]))
        self.play(code_helper.highlight(code_layout.code[4][23:26]))
        self.play(code_helper.highlight(code_layout.code[5][1:4]))

        code_layout.generate_target()
        code_layout.target.shift(DOWN*5.5)
        self.play(MoveToTarget(code_layout))

        keys = ["1F", "2C", "3B", "4D", "5G"]
        values = ["Steve", "Steven", "Sarah", "Bob", "Alice"]

        dict_of_text = DictOfText(keys, values, 64, 64)
        m_keys = ListOfText(keys, 48, cf.BLUE, 64).shift(UP*6)
        m_values = ListOfText(values, 24, cf.BLUE, 64).shift(UP*5)

        self.play(
            FadeIn(dict_of_text.get_table_without_elements(), m_keys, m_values))

        for i in (range(0, 5)):
            self.play(
                Transform(m_keys.elements[i], dict_of_text.get_key(i)),
                Transform(m_values.elements[i], dict_of_text.get_value(i)),
            )
            self.wait(cf.RATE_MEDIUM)
#
        dict_name = "id_to_name ="
        dict_text = Text(
            dict_name, t2c={"=": cf.ORANGE}, font_size=48).shift(UP*4).align_on_border(LEFT)
#
        self.play(
            FadeOut(m_keys.brackets, m_values.brackets),
            FadeIn(dict_text))
        self.wait(cf.RATE_SLOW)
#
        self.play(code_helper.highlight(code_layout.code[6][0:23]))
        self.wait(cf.RATE_SLOW)
#
        self.play(code_helper.highlight(m_keys.elements[1][0:3]))
        self.play(code_helper.highlight(m_values.elements[1][0:6]))

        self.wait(cf.RATE_END)
        fade_out_all(self)
