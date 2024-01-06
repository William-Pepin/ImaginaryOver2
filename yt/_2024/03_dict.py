from manim import *
from yt.config.config import cf
from yt.helper.title_helper import TitleHelper
from yt.helper.code_helper import CodeHelper
from yt.core.dict_of_text import DictOfText
from yt.core.dict_of_mobject import DictOfMobject
from yt.helper.fade_out_helper import fade_out_all


config.background_color = "#1F2430"
config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1920
config.pixel_width = 1080

default_font = "Menlo"


class Intro(Scene):
    def construct(self):
        TitleHelper(self).show_title(["Dictionnary", "in", "Python"])


class Scene_1(Scene):
    def construct(self):
        keys = ["id", "name", "surname", "category", "logged_in"]
        datas = ["935", '"John"', '"Smith"', '"Employee"', "False"]
        datas_for_dict = ["935", 'John', 'Smith', 'Employee', "False"]
        code = \
            """
user = {"id": 935,
    "name": "John",
    "surname": "Smith",
    "category": "Employee",
    "logged_in": False}
print(user["name"])
"""
        code_helper = CodeHelper(self)
        code_layout = code_helper.generate_code_layout(code)

        code_helper.show_code_block(code_layout)
        code_helper.write_code(code_layout)

        self.wait(cf.RATE_SLOW)

        self.play(code_helper.highlight_in_code(
            code_layout, "{"), code_helper.highlight_in_code(code_layout, "}"))

        self.play(*[code_helper.highlight_in_code(code_layout, f'"{key}"')
                    for key in keys])
        self.play(*[code_helper.highlight_in_code(code_layout, data)
                  for data in datas])

        self.wait(cf.RATE_SLOW)

        code_layout.generate_target()
        code_layout.target.shift(DOWN*5.5)
        self.play(MoveToTarget(code_layout))

        dict_of_text = DictOfText(keys, datas_for_dict, 42, 42, 36)

        self.play(
            FadeIn(dict_of_text.table))

        self.play(code_helper.highlight_in_code(
            code_layout, 'print(user["name"])'))

        self.play(code_helper.highlight(dict_of_text.get_key(1)))
        self.play(code_helper.highlight(dict_of_text.get_value(1)))

        self.wait(cf.RATE_END)

        fade_out_all(self)


class Scene_2(Scene):
    def construct(self):
        code = """
shapes = [Square(), Circle(),
          Square(), Triangle(), Circle()]
freq = {}
for shape in shapes:
    freq[shape] = shapes.count(shape)
"""
        code_helper = CodeHelper(self)
        code_layout = code_helper.generate_code_layout(code)

        code_helper.show_code_block(code_layout)
        code_helper.write_code(code_layout)

        code_layout.generate_target()
        code_layout.target.shift(DOWN*4)
        self.wait(cf.RATE_SLOW)

        self.play(MoveToTarget(code_layout))

        base_shapes = VGroup(
            Square(color=cf.GREY, side_length=0.82),
            Circle(color=cf.BLUE, radius=0.4),
            Square(color=cf.GREY, side_length=0.82),
            Triangle(color=cf.PURPLE).scale(0.45),
            Circle(color=cf.BLUE, radius=0.4),
        )
        base_shapes.arrange(RIGHT).shift(UP * 4)

        brackets = VGroup(
            Text("[", font=cf.DEFAULT_FONT, font_size=64, color=cf.YELLOW).next_to(
                base_shapes, LEFT
            ),
            Text(f"]", font=cf.DEFAULT_FONT, font_size=64, color=cf.YELLOW).next_to(
                base_shapes, RIGHT
            ),
        )

        keys = VGroup(Square(color=cf.GREY, side_length=0.82),
                      Circle(color=cf.BLUE, radius=0.4), Triangle(color=cf.PURPLE).scale(0.45))
        values = VGroup(
            *[DecimalNumber(0, font_size=64, num_decimal_places=0) for _ in range(3)]
        )
        m_dict = DictOfMobject(
            keys, values, [Text(header, font_size=48, color=cf.ORANGE) for header in ("Keys", "Values")])

        self.play(FadeIn(base_shapes, brackets,
                  m_dict.get_table_without_elements(), m_dict.table.get_columns()[1]))
        self.wait(cf.RATE_SLOW)

        self._count_shape(
            base_shapes[0], m_dict.get_key(0), m_dict.get_value(0))
        self._count_shape(
            base_shapes[1], m_dict.get_key(1), m_dict.get_value(1))
        self._count_shape(
            base_shapes[2], m_dict.get_key(0), m_dict.get_value(0))
        self._count_shape(
            base_shapes[3], m_dict.get_key(2), m_dict.get_value(2))
        self._count_shape(
            base_shapes[4], m_dict.get_key(1), m_dict.get_value(1))
        self.play(FadeOut(brackets))
        self.wait(cf.RATE_END)
        fade_out_all(self)

    def _count_shape(self, shape, dict_key, dict_value):
        self.play(
            Transform(shape, dict_key),
            ChangeDecimalToValue(dict_value, dict_value.number + 1),
        )
        self.wait(cf.RATE_MEDIUM)
