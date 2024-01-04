from manim import *
from yt.config.config import cf
from typing import Sequence


class DictOfMobject():
    def __init__(self, keys: Sequence[Mobject], values: Sequence[Mobject], headers: Sequence[Mobject], keys_size=48, values_size=48, header_size=48, v_buff=0.4, h_buff=1):
        keys_values = list(zip(keys, values))

        self.table = MobjectTable(keys_values, arrange_in_grid_config={"cell_alignment": LEFT}, include_outer_lines=True, line_config={
                                  "stroke_width": 3, "color": cf.DARK_GREY}, col_labels=headers, v_buff=0.4, h_buff=1)

    def get_key(self, index):
        return self.table.get_entries_without_labels((index + 1, 1))

    def get_value(self, index):
        return self.table.get_entries_without_labels((index + 1, 2))

    def get_table_without_elements(self):
        return VGroup(self.table.get_horizontal_lines(), self.table.get_vertical_lines(), self.table.get_labels())
