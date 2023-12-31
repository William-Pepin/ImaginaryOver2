from manim import *


class cf:

    ###  Constant ###
    # Colors
    DEFAULT_FONT = "Menlo"
    WHITE = "#FFFFFF"
    GREY = "#CCCAC2"
    YELLOW = "#FFD173"
    ORANGE = "#E19A5A"
    PURPLE = "#BF62BC"
    BLUE = "#69BCE6"
    DARK_GREY = "#939392"
    GREEN = "#DDFE90"
    BACKGROUND = "#1C202A"
    LINE_BACKBROUND = "#1B1F28"

    # Speed
    RATE_VERY_SLOW = 2
    RATE_SLOW = 1
    RATE_MEDIUM = 0.5
    RATE_FAST = 0.25
    RATE_END = 3


# Viewport
config.background_color = cf.BACKGROUND
config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1920
config.pixel_width = 1080


# Stylization
Text.set_default(font=cf.DEFAULT_FONT, color=cf.GREY)
