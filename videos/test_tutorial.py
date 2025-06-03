#!/usr/bin/env python3
"""
Test Script for Complete Programming Tutorial
===========================================
This script tests that the complete programming tutorial can be rendered
by creating a simple test scene first.
"""

from manimlib import *


class TestScene(Scene):
    def construct(self):
        """Simple test to verify ManimGL setup"""
        title = Text("Test: Complete Programming Tutorial", font_size=48, color=BLUE)
        subtitle = Text("From Computer Basics to Python", font_size=32, color=GREEN)

        title.to_edge(UP)
        subtitle.next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(2)

        # Test animations
        circle = Circle(radius=1, color=YELLOW, fill_opacity=0.5)
        self.play(FadeIn(circle), run_time=1)
        self.play(circle.animate.scale(1.5).set_color(RED), run_time=2)

        success_text = Text("✅ ManimGL Test Successful!", font_size=36, color=GREEN)
        success_text.next_to(circle, DOWN, buff=1)
        self.play(Write(success_text), run_time=2)

        self.wait(2)

        # Clear for actual tutorial
        self.play(FadeOut(VGroup(title, subtitle, circle, success_text)), run_time=1)


if __name__ == "__main__":
    pass
