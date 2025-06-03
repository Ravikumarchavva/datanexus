#!/usr/bin/env python3
"""
Quick Demo: Complete Programming Tutorial Preview
===============================================
A quick preview of the complete programming tutorial to test rendering.
This renders just the introduction sequence to verify everything works.
"""

from manimlib import *
import numpy as np


class TutorialPreview(Scene):
    def construct(self):
        """Preview of the complete tutorial - just intro and first section"""
        # Set up the scene
        self.camera.background_color = "#0f0f23"  # Dark blue background like notebooks

        # Title sequence
        self.intro_sequence()

        # Quick preview of computer fundamentals
        self.computer_fundamentals_preview()

    def intro_sequence(self):
        """Introduction sequence - From Bits to Python"""
        # Title animation with particles
        title = Text("From Computer Basics", font_size=60, color=BLUE)
        subtitle = Text("to Python Programming", font_size=50, color=GREEN)

        # Position titles
        title.to_edge(UP, buff=1)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Create particle system
        particles = VGroup()
        for _ in range(30):  # Reduced for faster rendering
            particle = Dot(radius=0.02, color=random_bright_color())
            particle.move_to([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
            particles.add(particle)

        # Animate intro
        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.1), run_time=2)
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)

        # Floating particles
        self.play(
            LaggedStartMap(
                lambda p: p.animate.shift(
                    [np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5), 0]
                ),
                particles,
                lag_ratio=0.05,
            ),
            run_time=2,
        )

        # Clear for main content
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(particles), run_time=1.5)

    def computer_fundamentals_preview(self):
        """Quick preview of computer fundamentals section"""
        # Section title
        section_title = Text("Understanding Computers", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Everything is electricity
        explanation = Text(
            "At their core, computers are electrical devices\nthat can only understand two states:",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(explanation))
        self.wait(2)

        # Show electrical states
        on_state = Circle(radius=0.8, color=YELLOW, fill_opacity=0.8)
        off_state = Circle(radius=0.8, color=GRAY, fill_opacity=0.3)

        on_label = Text("ON (1)", font_size=20, color=WHITE)
        off_label = Text("OFF (0)", font_size=20, color=WHITE)

        # Position the states
        on_state.move_to(LEFT * 3)
        off_state.move_to(RIGHT * 3)
        on_label.next_to(on_state, DOWN)
        off_label.next_to(off_state, DOWN)

        self.play(
            FadeIn(on_state), FadeIn(off_state), Write(on_label), Write(off_label)
        )
        self.wait(2)

        # Animate electrical flow
        for _ in range(3):
            self.play(
                on_state.animate.set_fill(opacity=1),
                off_state.animate.set_fill(opacity=0.1),
                run_time=0.5,
            )
            self.play(
                on_state.animate.set_fill(opacity=0.1),
                off_state.animate.set_fill(opacity=1),
                run_time=0.5,
            )

        # Success message
        success_text = Text(
            "✅ Preview Complete!\nFull tutorial ready to render.",
            font_size=32,
            color=GREEN,
        ).move_to(ORIGIN)

        self.play(
            FadeOut(
                VGroup(
                    section_title, explanation, on_state, off_state, on_label, off_label
                )
            ),
            Write(success_text),
            run_time=2,
        )
        self.wait(3)


if __name__ == "__main__":
    pass
