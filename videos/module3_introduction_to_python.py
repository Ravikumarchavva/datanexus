"""
Module 3: Introduction to Python
===============================

This module introduces Python as a programming language, its philosophy,
ecosystem, and gets students ready to write their first Python programs.

Learning Objectives:
- Understand why Python is popular and widely used
- Learn Python's philosophy and design principles
- Understand Python's ecosystem and applications
- Set up Python development environment
- Write and run your first Python programs
- Understand the difference between REPL and scripts
- Learn basic Python syntax and conventions

Duration: ~30 minutes
"""

from manimlib import *
import numpy as np


class IntroductionToPython(Scene):
    def construct(self):
        """Main course structure"""
        # Title
        title = Title("Module 3: Introduction to Python", include_underline=False)
        title.scale(0.8)

        # Course overview
        topics = VGroup(
            Text("• Why Python?", font_size=24),
            Text("• Python Philosophy", font_size=24),
            Text("• Python Ecosystem", font_size=24),
            Text("• Development Environment", font_size=24),
            Text("• First Python Program", font_size=24),
            Text("• REPL vs Scripts", font_size=24),
            Text("• Basic Syntax Rules", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(topics))
        self.wait(2)
        self.play(FadeOut(topics))

        # Run demonstrations
        self.why_python()
        self.python_philosophy()
        self.python_ecosystem()
        self.development_environment()
        self.first_python_program()
        self.repl_vs_scripts()
        self.basic_syntax()

        # Conclusion
        self.play(FadeOut(title))
        conclusion = Text("Let's Start Coding in Python!", font_size=36, color=GREEN)
        self.play(Write(conclusion))
        self.wait(2)

    def why_python(self):
        """Explain why Python is popular and widely used"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Why Python?", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Python logo animation
        python_logo = Circle(radius=1, color=BLUE)
        python_logo.add(Text("Python", font_size=24, color=WHITE))
        python_logo.shift(UP * 1.5)

        self.play(Create(python_logo))

        # Reasons why Python is popular
        reasons = (
            VGroup(
                Text("🔤 Easy to Read and Write", font_size=20, color=GREEN),
                Text("⚡ Simple Syntax", font_size=20, color=GREEN),
                Text("🌍 Huge Community", font_size=20, color=GREEN),
                Text("📚 Rich Libraries", font_size=20, color=GREEN),
                Text("🚀 Versatile Applications", font_size=20, color=GREEN),
                Text("💼 High Demand in Jobs", font_size=20, color=GREEN),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .shift(DOWN * 0.5)
        )

        # Animate each reason
        for reason in reasons:
            self.play(Write(reason))
            self.wait(0.5)

        self.wait(2)

        # Comparison with other languages
        self.play(FadeOut(reasons), FadeOut(python_logo))

        comparison_title = Text("Python vs Other Languages", font_size=24, color=YELLOW)
        comparison_title.shift(UP * 2)

        # Code comparison
        java_code = (
            VGroup(
                Text("Java:", font_size=18, color=RED),
                Text("public class Hello {", font_size=14, color=GRAY),
                Text(
                    "  public static void main(String[] args) {",
                    font_size=14,
                    color=GRAY,
                ),
                Text(
                    '    System.out.println("Hello, World!");', font_size=14, color=GRAY
                ),
                Text("  }", font_size=14, color=GRAY),
                Text("}", font_size=14, color=GRAY),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 3 + UP * 0.5)
        )

        python_code = (
            VGroup(
                Text("Python:", font_size=18, color=GREEN),
                Text('print("Hello, World!")', font_size=14, color=WHITE),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(RIGHT * 3 + UP * 0.5)
        )

        self.play(Write(comparison_title))
        self.play(Write(java_code))
        self.wait(1)
        self.play(Write(python_code))
        self.wait(2)

        # Highlight simplicity
        simplicity_note = Text("Same result, much simpler!", font_size=20, color=GOLD)
        simplicity_note.shift(DOWN * 1.5)
        self.play(Write(simplicity_note))
        self.wait(2)

        # Applications showcase
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        apps_title = Text("What Can You Build with Python?", font_size=24, color=PURPLE)
        apps_title.shift(UP * 2)

        applications = VGroup(
            VGroup(
                Text("🌐 Web Development", font_size=18, color=BLUE),
                Text("Django, Flask, FastAPI", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("🤖 AI & Machine Learning", font_size=18, color=GREEN),
                Text("TensorFlow, PyTorch, scikit-learn", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("📊 Data Science", font_size=18, color=ORANGE),
                Text("Pandas, NumPy, Matplotlib", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("🎮 Game Development", font_size=18, color=RED),
                Text("Pygame, Panda3D", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("🖥️ Desktop Applications", font_size=18, color=YELLOW),
                Text("Tkinter, PyQt, Kivy", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("⚙️ Automation & Scripting", font_size=18, color=PURPLE),
                Text("System administration, testing", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange_in_grid(rows=3, cols=2, buff=0.5)

        self.play(Write(apps_title))

        # Animate applications one by one
        for app in applications:
            self.play(Write(app))
            self.wait(0.3)

        self.wait(3)

    def python_philosophy(self):
        """Explain Python's design philosophy"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Python Philosophy", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # The Zen of Python
        zen_title = Text("The Zen of Python", font_size=28, color=GOLD)
        zen_title.shift(UP * 2)

        # Key principles
        zen_principles = VGroup(
            Text("Beautiful is better than ugly", font_size=18),
            Text("Simple is better than complex", font_size=18),
            Text("Readability counts", font_size=18),
            Text("There should be one obvious way to do it", font_size=18),
            Text(
                "If the implementation is hard to explain, it's a bad idea",
                font_size=18,
            ),
        ).arrange(DOWN, buff=0.3)

        self.play(Write(zen_title))
        self.wait(1)

        # Animate principles with emphasis
        for i, principle in enumerate(zen_principles):
            self.play(Write(principle))
            if i < 2:  # Highlight first few principles
                self.play(principle.animate.set_color(YELLOW))
            self.wait(0.8)

        self.wait(2)

        # Show practical example
        self.play(FadeOut(zen_principles))

        example_title = Text(
            "Example: Readability in Action", font_size=24, color=GREEN
        )
        example_title.shift(UP * 1)

        # Bad code example
        bad_code = (
            VGroup(
                Text("Hard to read:", font_size=16, color=RED),
                Text("x=[i for i in range(10) if i%2==0]", font_size=14, color=GRAY),
            )
            .arrange(DOWN, buff=0.2)
            .shift(LEFT * 3)
        )

        # Good code example
        good_code = (
            VGroup(
                Text("Easy to read:", font_size=16, color=GREEN),
                Text("even_numbers = []", font_size=14, color=WHITE),
                Text("for number in range(10):", font_size=14, color=WHITE),
                Text("    if number % 2 == 0:", font_size=14, color=WHITE),
                Text("        even_numbers.append(number)", font_size=14, color=WHITE),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 2.5)
        )

        self.play(Write(example_title))
        self.play(Write(bad_code), Write(good_code))
        self.wait(3)

        # Python's motto
        motto = Text(
            '"Code should be written for humans to read"',
            font_size=20,
            color=BLUE,
            slant=ITALIC,
        )
        motto.shift(DOWN * 2)
        self.play(Write(motto))
        self.wait(2)

    def python_ecosystem(self):
        """Show Python's rich ecosystem"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Python Ecosystem", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Python at center
        python_center = Circle(radius=1, color=BLUE, fill_opacity=0.3)
        python_center.add(Text("Python", font_size=20, color=WHITE))

        # Ecosystem components
        components = [
            ("Standard Library", "Built-in modules", GREEN, UP * 2),
            ("PyPI", "Package Index", ORANGE, UP * 1.4 + RIGHT * 2),
            ("pip", "Package Manager", PURPLE, RIGHT * 2.5),
            (
                "Virtual Environments",
                "Isolated projects",
                YELLOW,
                DOWN * 1.4 + RIGHT * 2,
            ),
            ("IDEs", "Development tools", RED, DOWN * 2),
            ("Frameworks", "Web, AI, etc.", PINK, DOWN * 1.4 + LEFT * 2),
            ("Community", "Support & docs", TEAL, LEFT * 2.5),
            ("Documentation", "Official guides", GOLD, UP * 1.4 + LEFT * 2),
        ]

        ecosystem_parts = VGroup()
        arrows = VGroup()

        for name, desc, color, position in components:
            # Create component
            component = VGroup(
                Circle(radius=0.6, color=color, fill_opacity=0.2),
                Text(name, font_size=12, color=WHITE),
                Text(desc, font_size=10, color=GRAY),
            )
            component[1].move_to(component[0].get_center())
            component[2].next_to(component[0], DOWN, buff=0.1)
            component.shift(position)

            # Create arrow
            arrow = Arrow(
                python_center.get_center(),
                component[0].get_center(),
                color=WHITE,
                buff=0.1,
                stroke_width=2,
            )

            ecosystem_parts.add(component)
            arrows.add(arrow)

        # Animate the ecosystem
        self.play(Create(python_center))
        self.wait(1)

        for i, (component, arrow) in enumerate(zip(ecosystem_parts, arrows)):
            self.play(Create(arrow), Create(component))
            self.wait(0.3)

        self.wait(2)

        # Highlight package installation
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        pip_demo = VGroup(
            Text("Installing Packages is Easy!", font_size=24, color=GREEN),
            Text("pip install requests", font_size=18, color=WHITE, font="Courier"),
            Text("pip install pandas", font_size=18, color=WHITE, font="Courier"),
            Text("pip install matplotlib", font_size=18, color=WHITE, font="Courier"),
        ).arrange(DOWN, buff=0.5)

        pip_demo[0].shift(UP * 1)

        self.play(Write(pip_demo[0]))
        for cmd in pip_demo[1:]:
            self.play(Write(cmd))
            self.wait(0.5)

        self.wait(2)

    def development_environment(self):
        """Show different ways to run Python"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Development Environment", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Different ways to run Python
        ways_title = Text("Ways to Run Python", font_size=24, color=YELLOW)
        ways_title.shift(UP * 2)

        # Method 1: Command line/Terminal
        method1 = VGroup(
            Text("1. Command Line/Terminal", font_size=20, color=GREEN),
            Rectangle(width=5, height=1.5, color=DARK_GRAY, fill_opacity=0.8),
            Text("$ python", font_size=16, color=WHITE, font="Courier"),
            Text(">>> print('Hello!')", font_size=16, color=WHITE, font="Courier"),
            Text("Hello!", font_size=16, color=GREEN, font="Courier"),
        )
        method1[2:].arrange(DOWN, buff=0.1)
        method1[2:].move_to(method1[1].get_center())
        method1.arrange(DOWN, buff=0.3).shift(LEFT * 4 + UP * 0.5)

        # Method 2: Code Editor
        method2 = VGroup(
            Text("2. Code Editor (VS Code)", font_size=20, color=BLUE),
            Rectangle(width=5, height=1.5, color=DARK_BLUE, fill_opacity=0.8),
            Text("# hello.py", font_size=14, color=GRAY, font="Courier"),
            Text("print('Hello, World!')", font_size=16, color=WHITE, font="Courier"),
        )
        method2[2:].arrange(DOWN, buff=0.1)
        method2[2:].move_to(method2[1].get_center())
        method2.arrange(DOWN, buff=0.3).shift(RIGHT * 4 + UP * 0.5)

        # Method 3: Jupyter Notebook
        method3 = VGroup(
            Text("3. Jupyter Notebook", font_size=20, color=ORANGE),
            Rectangle(width=5, height=1.5, color=DARK_GRAY, fill_opacity=0.8),
            Text(
                "In [1]: print('Interactive!')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("Interactive!", font_size=14, color=GREEN, font="Courier"),
        )
        method3[2:].arrange(DOWN, buff=0.1)
        method3[2:].move_to(method3[1].get_center())
        method3.arrange(DOWN, buff=0.3).shift(DOWN * 1.5)

        self.play(Write(ways_title))
        self.play(Write(method1))
        self.wait(1)
        self.play(Write(method2))
        self.wait(1)
        self.play(Write(method3))
        self.wait(2)

        # Installation note
        install_note = Text(
            "💡 First install Python from python.org", font_size=18, color=GOLD
        )
        install_note.shift(DOWN * 3)
        self.play(Write(install_note))
        self.wait(2)

    def first_python_program(self):
        """Create and explain the first Python program"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Your First Python Program", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Hello World tradition
        tradition_text = Text(
            "Programming Tradition: Hello, World!", font_size=24, color=YELLOW
        )
        tradition_text.shift(UP * 2)

        # The program
        program_bg = Rectangle(
            width=8, height=3, color=DARK_GRAY, fill_opacity=0.8, stroke_color=WHITE
        )
        program_bg.shift(UP * 0.3)

        program_code = VGroup(
            Text(
                "# My first Python program", font_size=16, color=GREEN, font="Courier"
            ),
            Text("print('Hello, World!')", font_size=18, color=WHITE, font="Courier"),
        ).arrange(DOWN, buff=0.3)
        program_code.move_to(program_bg.get_center())

        self.play(Write(tradition_text))
        self.play(Create(program_bg))
        self.play(Write(program_code))
        self.wait(2)

        # Explanation of each part
        explanations = (
            VGroup(
                Text("# - This is a comment (ignored by Python)", font_size=16),
                Text("print() - A function that displays text", font_size=16),
                Text("'Hello, World!' - A string (text data)", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .shift(DOWN * 2)
        )

        for explanation in explanations:
            self.play(Write(explanation))
            self.wait(0.8)

        # Running the program
        self.play(FadeOut(explanations))

        run_title = Text("Running the Program:", font_size=20, color=GREEN)
        run_title.shift(DOWN * 1.5)

        output_bg = Rectangle(
            width=6, height=1, color=BLACK, fill_opacity=0.8, stroke_color=GREEN
        )
        output_bg.shift(DOWN * 2.5)

        output_text = Text("Hello, World!", font_size=18, color=GREEN, font="Courier")
        output_text.move_to(output_bg.get_center())

        self.play(Write(run_title))
        self.play(Create(output_bg))
        self.play(Write(output_text))
        self.wait(2)

        # Celebration
        celebration = Text(
            "🎉 Congratulations! You're a programmer now! 🎉", font_size=20, color=GOLD
        )
        celebration.shift(DOWN * 3.5)
        self.play(Write(celebration))
        self.wait(3)

    def repl_vs_scripts(self):
        """Explain the difference between REPL and scripts"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("REPL vs Scripts", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # REPL explanation
        repl_title = Text("REPL (Interactive Mode)", font_size=24, color=GREEN)
        repl_title.shift(UP * 2 + LEFT * 4)

        repl_full = Text("Read-Eval-Print-Loop", font_size=16, color=GRAY)
        repl_full.next_to(repl_title, DOWN, buff=0.2)

        repl_demo = VGroup(
            Rectangle(width=4, height=2.5, color=DARK_GRAY, fill_opacity=0.8),
            Text(">>> 2 + 3", font_size=14, color=WHITE, font="Courier"),
            Text("5", font_size=14, color=GREEN, font="Courier"),
            Text(">>> name = 'Alice'", font_size=14, color=WHITE, font="Courier"),
            Text(">>> print(name)", font_size=14, color=WHITE, font="Courier"),
            Text("Alice", font_size=14, color=GREEN, font="Courier"),
        )
        repl_demo[1:].arrange(DOWN, buff=0.1)
        repl_demo[1:].move_to(repl_demo[0].get_center())
        repl_demo.next_to(repl_full, DOWN, buff=0.3)

        # Script explanation
        script_title = Text("Scripts (File Mode)", font_size=24, color=ORANGE)
        script_title.shift(UP * 2 + RIGHT * 4)

        script_desc = Text("Save code in .py file", font_size=16, color=GRAY)
        script_desc.next_to(script_title, DOWN, buff=0.2)

        script_demo = VGroup(
            Rectangle(width=4, height=2.5, color=DARK_BLUE, fill_opacity=0.8),
            Text("# calculator.py", font_size=12, color=GRAY, font="Courier"),
            Text("num1 = 10", font_size=14, color=WHITE, font="Courier"),
            Text("num2 = 5", font_size=14, color=WHITE, font="Courier"),
            Text("result = num1 + num2", font_size=14, color=WHITE, font="Courier"),
            Text("print(result)", font_size=14, color=WHITE, font="Courier"),
        )
        script_demo[1:].arrange(DOWN, buff=0.1)
        script_demo[1:].move_to(script_demo[0].get_center())
        script_demo.next_to(script_desc, DOWN, buff=0.3)

        # Animate both
        self.play(Write(repl_title), Write(repl_full))
        self.play(Create(repl_demo))
        self.wait(1)

        self.play(Write(script_title), Write(script_desc))
        self.play(Create(script_demo))
        self.wait(2)

        # When to use each
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        usage_title = Text("When to Use Each?", font_size=24, color=PURPLE)
        usage_title.shift(UP * 2)

        usage_comparison = VGroup(
            VGroup(
                Text("REPL - Good for:", font_size=20, color=GREEN),
                Text("• Quick calculations", font_size=16),
                Text("• Testing small code snippets", font_size=16),
                Text("• Learning and experimenting", font_size=16),
                Text("• Debugging", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(LEFT * 3),
            VGroup(
                Text("Scripts - Good for:", font_size=20, color=ORANGE),
                Text("• Complete programs", font_size=16),
                Text("• Reusable code", font_size=16),
                Text("• Complex logic", font_size=16),
                Text("• Sharing with others", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(RIGHT * 3),
        )

        self.play(Write(usage_title))
        self.play(Write(usage_comparison))
        self.wait(3)

    def basic_syntax(self):
        """Introduce basic Python syntax rules"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Basic Python Syntax", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Syntax rules
        rules_title = Text("Important Syntax Rules", font_size=24, color=YELLOW)
        rules_title.shift(UP * 2)

        # Rule 1: Indentation
        rule1 = (
            VGroup(
                Text("1. Indentation Matters!", font_size=20, color=GREEN),
                VGroup(
                    Text("if 5 > 3:", font_size=16, color=WHITE, font="Courier"),
                    Text(
                        "    print('True')", font_size=16, color=WHITE, font="Courier"
                    ),
                    Text(
                        "print('Always runs')",
                        font_size=16,
                        color=WHITE,
                        font="Courier",
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            )
            .arrange(DOWN, buff=0.3)
            .shift(LEFT * 4 + UP * 0.5)
        )

        # Rule 2: Case sensitive
        rule2 = (
            VGroup(
                Text("2. Case Sensitive", font_size=20, color=ORANGE),
                VGroup(
                    Text(
                        "Name ≠ name ≠ NAME", font_size=16, color=WHITE, font="Courier"
                    ),
                    Text(
                        "print() ≠ Print()", font_size=16, color=WHITE, font="Courier"
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            )
            .arrange(DOWN, buff=0.3)
            .shift(RIGHT * 4 + UP * 0.5)
        )

        # Rule 3: Comments
        rule3 = (
            VGroup(
                Text("3. Comments with #", font_size=20, color=PURPLE),
                VGroup(
                    Text(
                        "# This is a comment", font_size=16, color=GREEN, font="Courier"
                    ),
                    Text(
                        "print('Hello')  # Comment here too",
                        font_size=16,
                        color=WHITE,
                        font="Courier",
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            )
            .arrange(DOWN, buff=0.3)
            .shift(LEFT * 4 + DOWN * 1.2)
        )

        # Rule 4: Line continuation
        rule4 = (
            VGroup(
                Text("4. Line Continuation", font_size=20, color=RED),
                VGroup(
                    Text(
                        "long_calculation = 1 + 2 + \\",
                        font_size=14,
                        color=WHITE,
                        font="Courier",
                    ),
                    Text(
                        "                  3 + 4",
                        font_size=14,
                        color=WHITE,
                        font="Courier",
                    ),
                ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            )
            .arrange(DOWN, buff=0.3)
            .shift(RIGHT * 4 + DOWN * 1.2)
        )

        self.play(Write(rules_title))

        # Animate rules one by one
        rules = [rule1, rule2, rule3, rule4]
        for rule in rules:
            self.play(Write(rule))
            self.wait(1.5)

        # Common mistakes
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        mistakes_title = Text("Common Beginner Mistakes", font_size=24, color=RED)
        mistakes_title.shift(UP * 2.5)

        mistakes = VGroup(
            VGroup(
                Text("❌ Wrong:", font_size=16, color=RED),
                Text("Print('hello')", font_size=14, color=GRAY, font="Courier"),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("✅ Correct:", font_size=16, color=GREEN),
                Text("print('hello')", font_size=14, color=WHITE, font="Courier"),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("❌ Wrong:", font_size=16, color=RED),
                Text("if True:", font_size=14, color=GRAY, font="Courier"),
                Text("print('indented')", font_size=14, color=GRAY, font="Courier"),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("✅ Correct:", font_size=16, color=GREEN),
                Text("if True:", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "    print('indented')", font_size=14, color=WHITE, font="Courier"
                ),
            ).arrange(DOWN, buff=0.1),
        ).arrange_in_grid(rows=2, cols=2, buff=1)

        self.play(Write(mistakes_title))

        for mistake in mistakes:
            self.play(Write(mistake))
            self.wait(1)

        self.wait(2)

        # Encouragement
        encouragement = Text(
            "💪 Don't worry - everyone makes these mistakes at first!",
            font_size=18,
            color=GOLD,
        )
        encouragement.shift(DOWN * 3)
        self.play(Write(encouragement))
        self.wait(3)


if __name__ == "__main__":
    from manimlib import config

    config.media_width = "854px"
    config.media_height = "480px"
    config.frame_rate = 30

    scene = IntroductionToPython()
    scene.render()
