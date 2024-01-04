
from manim import *
from yt.config.config import cf


def fade_out_all(scene: Scene):
    scene.play(*[FadeOut(mob, run_time=cf.RATE_MEDIUM,
                         rate_func=rate_functions.ease_out_cubic)for mob in scene.mobjects])
