from manim import *
from yt.config.config import cf
from typing import Sequence


class DictOfText():
    def __init__(self, keys: Sequence[str], values: Sequence[str], keys_size=48, values_size=48, header_size=48, v_buff=0.4, h_buff=1):

        keys = [Text(key, font=cf.DEFAULT_FONT, font_size=keys_size, color=cf.BLUE)
                for key in (keys)]
        values = [Text(value, font=cf.DEFAULT_FONT, font_size=values_size,
                       color=cf.BLUE) for value in (values)]

        headers = [Text("Keys", font_size=header_size, color=cf.ORANGE), Text(
            "Values", font_size=header_size, color=cf.ORANGE)]

        keys_values = list(zip(keys, values))

        self.table = MobjectTable(keys_values, arrange_in_grid_config={"cell_alignment": LEFT}, include_outer_lines=True, line_config={
                                  "stroke_width": 3, "color": cf.DARK_GREY}, col_labels=headers, v_buff=0.4, h_buff=1)

    def get_key(self, index):
        return self.table.get_entries_without_labels((index + 1, 1))

    def get_value(self, index):
        return self.table.get_entries_without_labels((index + 1, 2))

    def get_table_without_elements(self):
        return VGroup(self.table.get_horizontal_lines(), self.table.get_vertical_lines(), self.table.get_labels())
