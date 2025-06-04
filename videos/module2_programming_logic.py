"""
Module 2: Programming Logic & Problem Solving
============================================

This module introduces fundamental programming concepts, problem-solving techniques,
and logical thinking patterns that form the foundation of programming.

Learning Objectives:
- Understand what programming really is
- Learn algorithmic thinking and problem decomposition
- Master flowcharts and pseudocode
- Understand basic programming constructs
- Practice logical reasoning and pattern recognition
- Learn debugging and testing concepts

Duration: ~30 minutes
"""

from manimlib import *
import numpy as np


class ProgrammingLogicCourse(Scene):
    def construct(self):
        """Main course structure"""
        # Title
        title = Title(
            "Module 2: Programming Logic & Problem Solving", include_underline=False
        )
        title.scale(0.8)

        # Course overview
        topics = VGroup(
            Text("• What is Programming?", font_size=24),
            Text("• Algorithmic Thinking", font_size=24),
            Text("• Problem Decomposition", font_size=24),
            Text("• Flowcharts & Pseudocode", font_size=24),
            Text("• Logic Patterns", font_size=24),
            Text("• Debugging & Testing", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(topics))
        self.wait(2)
        self.play(FadeOut(topics))

        # Run demonstrations
        self.what_is_programming()
        self.algorithmic_thinking()
        self.problem_decomposition()
        self.flowcharts_and_pseudocode()
        self.logic_patterns()
        self.debugging_concepts()

        # Conclusion
        self.play(FadeOut(title))
        conclusion = Text("Ready for Python Programming!", font_size=36, color=GREEN)
        self.play(Write(conclusion))
        self.wait(2)

    def what_is_programming(self):
        """Demonstrate what programming really is"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("What is Programming?", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Programming definition animation
        human = Circle(radius=0.5, color=YELLOW).shift(LEFT * 4)
        human_label = Text("Human", font_size=20).next_to(human, DOWN)

        computer = Rectangle(width=2, height=1.5, color=BLUE).shift(RIGHT * 4)
        computer_label = Text("Computer", font_size=20).next_to(computer, DOWN)

        # Problem to solution arrow
        problem = Text("PROBLEM", font_size=16, color=RED).shift(LEFT * 4 + UP * 2)
        solution = Text("SOLUTION", font_size=16, color=GREEN).shift(RIGHT * 4 + UP * 2)

        self.play(
            Create(human),
            Write(human_label),
            Create(computer),
            Write(computer_label),
            Write(problem),
            Write(solution),
        )

        # Programming bridge
        bridge = Arrow(LEFT * 2, RIGHT * 2, color=ORANGE, buff=0.5)
        bridge_label = Text("PROGRAMMING", font_size=20, color=ORANGE)
        bridge_label.next_to(bridge, UP)

        self.play(Create(bridge), Write(bridge_label))
        self.wait(1)

        # Key concepts
        concepts = (
            VGroup(
                Text("Programming is:", font_size=24, color=WHITE),
                Text("• Giving step-by-step instructions", font_size=20),
                Text("• Breaking down complex problems", font_size=20),
                Text("• Creating logical sequences", font_size=20),
                Text("• Automating repetitive tasks", font_size=20),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .shift(DOWN * 1.5)
        )

        self.play(Write(concepts))
        self.wait(3)

        # Real world analogy
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        analogy_title = Text("Like Following a Recipe", font_size=28, color=YELLOW)
        analogy_title.shift(UP * 2)

        recipe_steps = VGroup(
            Text("1. Gather ingredients", font_size=20),
            Text("2. Preheat oven to 350°F", font_size=20),
            Text("3. Mix flour and sugar", font_size=20),
            Text("4. Add eggs and milk", font_size=20),
            Text("5. Bake for 30 minutes", font_size=20),
            Text("6. Cool and serve", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        programming_steps = VGroup(
            Text("1. Define the problem", font_size=20, color=BLUE),
            Text("2. Plan the solution", font_size=20, color=BLUE),
            Text("3. Write the code", font_size=20, color=BLUE),
            Text("4. Test the program", font_size=20, color=BLUE),
            Text("5. Debug if needed", font_size=20, color=BLUE),
            Text("6. Deploy solution", font_size=20, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        recipe_group = (
            VGroup(Text("Recipe Steps", font_size=24, color=GREEN), recipe_steps)
            .arrange(DOWN, buff=0.5)
            .shift(LEFT * 3)
        )

        programming_group = (
            VGroup(
                Text("Programming Steps", font_size=24, color=BLUE), programming_steps
            )
            .arrange(DOWN, buff=0.5)
            .shift(RIGHT * 3)
        )

        self.play(Write(analogy_title))
        self.play(Write(recipe_group), Write(programming_group))
        self.wait(4)

    def algorithmic_thinking(self):
        """Demonstrate algorithmic thinking process"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Algorithmic Thinking", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Example: Finding the largest number
        problem_text = Text(
            "Problem: Find the largest number in a list", font_size=24, color=YELLOW
        )
        problem_text.shift(UP * 2)

        numbers = [3, 7, 2, 9, 1, 5, 8]
        number_boxes = (
            VGroup(
                *[
                    Square(side_length=0.8).add(Text(str(num), font_size=20))
                    for num in numbers
                ]
            )
            .arrange(RIGHT, buff=0.1)
            .shift(UP * 0.5)
        )

        self.play(Write(problem_text))
        self.play(Create(number_boxes))

        # Algorithm visualization
        algorithm_steps = (
            VGroup(
                Text("Algorithm:", font_size=24, color=GREEN),
                Text("1. Start with first number as 'largest'", font_size=18),
                Text("2. Compare with next number", font_size=18),
                Text("3. If next > largest, update largest", font_size=18),
                Text("4. Repeat until end of list", font_size=18),
                Text("5. Return largest", font_size=18),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(DOWN * 1.5)
        )

        self.play(Write(algorithm_steps))
        self.wait(2)

        # Animate the algorithm execution
        largest_indicator = Text("Largest: ", font_size=20, color=RED)
        largest_value = Text("3", font_size=20, color=RED)
        largest_display = VGroup(largest_indicator, largest_value).arrange(RIGHT)
        largest_display.shift(DOWN * 3)

        self.play(Write(largest_display))

        # Highlight current comparison
        pointer = Triangle(color=RED, fill_opacity=1).scale(0.3)
        pointer.next_to(number_boxes[0], UP)
        self.play(Create(pointer))

        # Step through algorithm
        for i in range(1, len(numbers)):
            # Move pointer
            self.play(pointer.animate.next_to(number_boxes[i], UP))

            # Highlight comparison
            self.play(
                number_boxes[i].animate.set_color(YELLOW),
                number_boxes[i - 1].animate.set_color(WHITE)
                if i > 1
                else Animation(Group()),
            )

            # Update largest if needed
            current_largest = int(largest_value.text)
            if numbers[i] > current_largest:
                new_largest = Text(str(numbers[i]), font_size=20, color=RED)
                self.play(Transform(largest_value, new_largest))

            self.wait(0.5)

        # Final result
        result = Text(
            f"Result: {max(numbers)} is the largest!", font_size=24, color=GREEN
        )
        result.shift(DOWN * 3.8)
        self.play(Write(result))
        self.wait(3)

    def problem_decomposition(self):
        """Show how to break down complex problems"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Problem Decomposition", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Complex problem example
        main_problem = Rectangle(width=8, height=1.5, color=RED)
        main_problem.add(Text("Build a Calculator App", font_size=24, color=WHITE))
        main_problem.shift(UP * 2)

        self.play(Create(main_problem))
        self.wait(1)

        # Break down into sub-problems
        sub_problems = VGroup(
            Rectangle(width=3, height=1).add(Text("User Interface", font_size=16)),
            Rectangle(width=3, height=1).add(Text("Basic Operations", font_size=16)),
            Rectangle(width=3, height=1).add(Text("Input Validation", font_size=16)),
            Rectangle(width=3, height=1).add(Text("Error Handling", font_size=16)),
        )

        # Arrange in 2x2 grid
        sub_problems[:2].arrange(RIGHT, buff=0.5).shift(UP * 0.5)
        sub_problems[2:].arrange(RIGHT, buff=0.5).shift(DOWN * 0.5)
        sub_problems.set_color(YELLOW)

        # Arrows from main to sub-problems
        arrows = VGroup(
            *[
                Arrow(
                    main_problem.get_bottom(), sub_prob.get_top(), color=WHITE, buff=0.1
                )
                for sub_prob in sub_problems
            ]
        )

        self.play(Create(arrows), Create(sub_problems))
        self.wait(2)

        # Further decomposition of "Basic Operations"
        self.play(sub_problems[1].animate.set_color(GREEN))

        basic_ops = (
            VGroup(
                Rectangle(width=2, height=0.8).add(Text("Addition", font_size=14)),
                Rectangle(width=2, height=0.8).add(Text("Subtraction", font_size=14)),
                Rectangle(width=2, height=0.8).add(
                    Text("Multiplication", font_size=14)
                ),
                Rectangle(width=2, height=0.8).add(Text("Division", font_size=14)),
            )
            .arrange(DOWN, buff=0.2)
            .shift(DOWN * 2.5 + RIGHT * 3)
        )
        basic_ops.set_color(BLUE)

        detailed_arrow = Arrow(
            sub_problems[1].get_bottom(), basic_ops.get_top(), color=GREEN, buff=0.1
        )

        self.play(Create(detailed_arrow), Create(basic_ops))
        self.wait(2)

        # Benefits text
        benefits = (
            VGroup(
                Text("Benefits of Decomposition:", font_size=20, color=WHITE),
                Text("• Makes complex problems manageable", font_size=16),
                Text("• Easier to test individual parts", font_size=16),
                Text("• Can work on parts in parallel", font_size=16),
                Text("• Easier to debug and maintain", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(LEFT * 4 + DOWN * 2)
        )

        self.play(Write(benefits))
        self.wait(3)

    def flowcharts_and_pseudocode(self):
        """Demonstrate flowcharts and pseudocode"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Flowcharts & Pseudocode", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Problem: Check if number is even or odd
        problem = Text(
            "Problem: Check if a number is even or odd", font_size=20, color=YELLOW
        )
        problem.shift(UP * 2.5)
        self.play(Write(problem))

        # Create flowchart
        # Start
        start = Ellipse(width=2, height=1, color=GREEN)
        start.add(Text("START", font_size=16))
        start.shift(UP * 1.5 + LEFT * 4)

        # Input
        input_box = Parallelogram(color=BLUE)
        input_box.add(Text("Input: number", font_size=14))
        input_box.next_to(start, DOWN, buff=0.5)

        # Decision
        decision = RegularPolygon(n=4, color=ORANGE).rotate(PI / 4).scale(0.8)
        decision.add(Text("number % 2\n== 0?", font_size=12))
        decision.next_to(input_box, DOWN, buff=0.5)

        # Even output
        even_output = Rectangle(width=2, height=0.8, color=GREEN)
        even_output.add(Text("Print: Even", font_size=14))
        even_output.next_to(decision, LEFT, buff=1)

        # Odd output
        odd_output = Rectangle(width=2, height=0.8, color=RED)
        odd_output.add(Text("Print: Odd", font_size=14))
        odd_output.next_to(decision, RIGHT, buff=1)

        # End
        end = Ellipse(width=1.5, height=0.8, color=GREEN)
        end.add(Text("END", font_size=14))
        end.next_to(decision, DOWN, buff=1.5)

        # Arrows
        arrows = VGroup(
            Arrow(start.get_bottom(), input_box.get_top(), buff=0.1),
            Arrow(input_box.get_bottom(), decision.get_top(), buff=0.1),
            Arrow(decision.get_left(), even_output.get_right(), buff=0.1),
            Arrow(decision.get_right(), odd_output.get_left(), buff=0.1),
            Arrow(even_output.get_bottom(), end.get_top() + LEFT * 0.5, buff=0.1),
            Arrow(odd_output.get_bottom(), end.get_top() + RIGHT * 0.5, buff=0.1),
        )

        # Labels for decision paths
        yes_label = Text("YES", font_size=12, color=GREEN)
        yes_label.next_to(arrows[2], UP)
        no_label = Text("NO", font_size=12, color=RED)
        no_label.next_to(arrows[3], UP)

        flowchart = VGroup(
            start,
            input_box,
            decision,
            even_output,
            odd_output,
            end,
            arrows,
            yes_label,
            no_label,
        )

        self.play(Create(flowchart))
        self.wait(2)

        # Show pseudocode
        pseudocode_title = Text("Pseudocode:", font_size=20, color=GREEN)
        pseudocode_title.shift(RIGHT * 4 + UP * 1.5)

        pseudocode = VGroup(
            Text("BEGIN", font_size=14),
            Text("  INPUT number", font_size=14),
            Text("  IF number MOD 2 = 0 THEN", font_size=14),
            Text("    PRINT 'Even'", font_size=14),
            Text("  ELSE", font_size=14),
            Text("    PRINT 'Odd'", font_size=14),
            Text("  END IF", font_size=14),
            Text("END", font_size=14),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        pseudocode.next_to(pseudocode_title, DOWN, buff=0.3)

        # Background for pseudocode
        pseudo_bg = Rectangle(width=3.5, height=2.5, color=DARK_GRAY, fill_opacity=0.2)
        pseudo_bg.move_to(pseudocode.get_center())

        self.play(Write(pseudocode_title), Create(pseudo_bg), Write(pseudocode))
        self.wait(3)

    def logic_patterns(self):
        """Demonstrate common programming logic patterns"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Common Logic Patterns", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Pattern 1: Sequence
        seq_title = Text("1. Sequence (Step by Step)", font_size=20, color=GREEN)
        seq_title.shift(UP * 2 + LEFT * 4)

        seq_steps = (
            VGroup(
                Text("Step 1", font_size=16),
                Text("Step 2", font_size=16),
                Text("Step 3", font_size=16),
            )
            .arrange(DOWN, buff=0.3)
            .next_to(seq_title, DOWN)
        )

        seq_arrows = VGroup(
            *[
                Arrow(
                    seq_steps[i].get_bottom(),
                    seq_steps[i + 1].get_top(),
                    buff=0.1,
                    stroke_width=2,
                )
                for i in range(len(seq_steps) - 1)
            ]
        )

        self.play(Write(seq_title), Write(seq_steps), Create(seq_arrows))
        self.wait(1)

        # Pattern 2: Selection
        sel_title = Text("2. Selection (If-Then-Else)", font_size=20, color=ORANGE)
        sel_title.shift(UP * 2)

        condition = RegularPolygon(n=4, color=ORANGE).rotate(PI / 4).scale(0.6)
        condition.add(Text("Condition?", font_size=12))
        condition.next_to(sel_title, DOWN, buff=0.5)

        true_path = Rectangle(width=1.5, height=0.6, color=GREEN)
        true_path.add(Text("True Path", font_size=12))
        true_path.next_to(condition, LEFT, buff=0.8)

        false_path = Rectangle(width=1.5, height=0.6, color=RED)
        false_path.add(Text("False Path", font_size=12))
        false_path.next_to(condition, RIGHT, buff=0.8)

        sel_arrows = VGroup(
            Arrow(condition.get_left(), true_path.get_right(), buff=0.1),
            Arrow(condition.get_right(), false_path.get_left(), buff=0.1),
        )

        self.play(
            Write(sel_title),
            Create(condition),
            Create(true_path),
            Create(false_path),
            Create(sel_arrows),
        )
        self.wait(1)

        # Pattern 3: Iteration
        iter_title = Text("3. Iteration (Loops)", font_size=20, color=PURPLE)
        iter_title.shift(UP * 2 + RIGHT * 4)

        loop_condition = RegularPolygon(n=4, color=PURPLE).rotate(PI / 4).scale(0.6)
        loop_condition.add(Text("Continue?", font_size=12))
        loop_condition.next_to(iter_title, DOWN, buff=0.5)

        loop_body = Rectangle(width=1.5, height=0.6, color=BLUE)
        loop_body.add(Text("Loop Body", font_size=12))
        loop_body.next_to(loop_condition, DOWN, buff=0.8)

        loop_arrows = VGroup(
            Arrow(loop_condition.get_bottom(), loop_body.get_top(), buff=0.1),
            Arrow(
                loop_body.get_left(),
                loop_condition.get_left() + DOWN * 0.5,
                buff=0.1,
                path_arc=-PI / 2,
            ),
        )

        self.play(
            Write(iter_title),
            Create(loop_condition),
            Create(loop_body),
            Create(loop_arrows),
        )
        self.wait(2)

        # Show combination example
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        combo_title = Text(
            "Combining Patterns: Password Validator", font_size=24, color=YELLOW
        )
        combo_title.shift(UP * 2)

        combo_logic = VGroup(
            Text("1. INPUT password (Sequence)", font_size=16),
            Text("2. WHILE attempts < 3 (Iteration)", font_size=16),
            Text("3.   IF password valid (Selection)", font_size=16),
            Text("4.     THEN grant access", font_size=16),
            Text("5.     ELSE increment attempts", font_size=16),
            Text("6. END WHILE", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(combo_title), Write(combo_logic))
        self.wait(3)

    def debugging_concepts(self):
        """Introduce debugging and testing concepts"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Debugging & Testing Mindset", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Bug visualization
        bug_title = Text("What are Bugs?", font_size=24, color=RED)
        bug_title.shift(UP * 2)

        # Code with bug
        buggy_code = (
            VGroup(
                Text("ALGORITHM: Add two numbers", font_size=16, color=WHITE),
                Text("1. INPUT first_number", font_size=14),
                Text("2. INPUT second_number", font_size=14),
                Text("3. result = first_number + second_number", font_size=14),
                Text("4. PRINT result", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(LEFT * 3)
        )

        # Expected vs Actual
        expected = (
            VGroup(
                Text("Expected: 5 + 3 = 8", font_size=16, color=GREEN),
                Text("Actual: 5 + 3 = 53", font_size=16, color=RED),
            )
            .arrange(DOWN, buff=0.3)
            .shift(RIGHT * 3)
        )

        self.play(Write(bug_title))
        self.play(Write(buggy_code), Write(expected))
        self.wait(2)

        # Bug explanation
        bug_explanation = Text(
            "Bug: Numbers treated as text, not numbers!", font_size=18, color=ORANGE
        )
        bug_explanation.shift(DOWN * 1)
        self.play(Write(bug_explanation))
        self.wait(2)

        # Debugging steps
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        debug_title = Text("Debugging Process", font_size=24, color=GREEN)
        debug_title.shift(UP * 2)

        debug_steps = VGroup(
            Text("1. 🔍 Identify the Problem", font_size=18),
            Text("   - What should happen?", font_size=14, color=GRAY),
            Text("   - What actually happens?", font_size=14, color=GRAY),
            Text("2. 🎯 Locate the Bug", font_size=18),
            Text("   - Check inputs and outputs", font_size=14, color=GRAY),
            Text("   - Trace through step by step", font_size=14, color=GRAY),
            Text("3. 🔧 Fix the Bug", font_size=18),
            Text("   - Make minimal changes", font_size=14, color=GRAY),
            Text("   - Fix root cause, not symptoms", font_size=14, color=GRAY),
            Text("4. ✅ Test the Fix", font_size=18),
            Text("   - Try original failing case", font_size=14, color=GRAY),
            Text("   - Try other test cases", font_size=14, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(debug_title), Write(debug_steps))
        self.wait(4)

        # Testing mindset
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        test_title = Text("Testing Mindset", font_size=24, color=PURPLE)
        test_title.shift(UP * 2)

        test_examples = VGroup(
            Text("Think like a detective:", font_size=20, color=WHITE),
            Text("• Test normal cases: 5 + 3", font_size=16),
            Text("• Test edge cases: 0 + 0, -5 + 3", font_size=16),
            Text("• Test invalid inputs: 'hello' + 3", font_size=16),
            Text("• Test extreme values: 999999 + 1", font_size=16),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(test_title), Write(test_examples))
        self.wait(3)

        # Final wisdom
        wisdom = Text(
            "💡 Good programmers expect bugs and plan for them!",
            font_size=20,
            color=GOLD,
        )
        wisdom.shift(DOWN * 2)
        self.play(Write(wisdom))
        self.wait(3)


if __name__ == "__main__":
    from manimlib import config

    config.media_width = "854px"
    config.media_height = "480px"
    config.frame_rate = 30

    scene = ProgrammingLogicCourse()
    scene.render()
