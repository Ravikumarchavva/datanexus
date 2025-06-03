from manimlib import *
import numpy as np


class PythonIntroTitle(Scene):
    def construct(self):
        # Main title with gradient effect
        title = Text("Python Programming", font_size=72, font="Arial Black")
        title.set_color_by_gradient(BLUE, PURPLE)

        subtitle = Text("From Zero to Hero", font_size=48)
        subtitle.set_color(YELLOW)
        subtitle.next_to(title, DOWN, buff=0.8)

        # Python logo animation (simplified)
        python_circle1 = Circle(radius=0.5, color=BLUE, fill_opacity=0.8).shift(
            LEFT * 0.3
        )
        python_circle2 = Circle(radius=0.5, color=YELLOW, fill_opacity=0.8).shift(
            RIGHT * 0.3
        )
        python_logo = VGroup(python_circle1, python_circle2).scale(0.8)
        python_logo.next_to(subtitle, DOWN, buff=1.0)

        # Decorative elements
        particles = VGroup()
        for i in range(20):
            particle = Circle(
                radius=0.05, color=random_bright_color(), fill_opacity=0.7
            )
            particle.move_to([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
            particles.add(particle)

        # Animations
        self.play(
            Write(title, run_time=2), ShowIncreasingSubsets(particles, run_time=3)
        )
        self.play(Write(subtitle, run_time=1.5))
        self.play(
            DrawBorderThenFill(python_circle1),
            DrawBorderThenFill(python_circle2),
            run_time=2,
        )

        # Floating animation for particles
        self.play(
            *[
                particle.animate.shift(
                    UP * np.random.uniform(-0.5, 0.5)
                    + RIGHT * np.random.uniform(-0.5, 0.5)
                )
                for particle in particles
            ],
            run_time=2,
        )

        self.wait(2)

        # Fade out for next scene
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(python_logo),
            FadeOut(particles),
            run_time=1.5,
        )


class WhatIsPython(Scene):
    def construct(self):
        # Section title
        title = Text("What is Python?", font_size=56)
        title.set_color(BLUE)
        title.to_edge(UP)

        self.play(Write(title, run_time=1.5))

        # Python characteristics with icons
        characteristics = VGroup()

        # Simple and Readable
        simple_icon = Circle(radius=0.3, color=GREEN, fill_opacity=0.8)
        simple_text = Text("Simple & Readable", font_size=32)
        simple_text.next_to(simple_icon, RIGHT, buff=0.3)
        simple_group = VGroup(simple_icon, simple_text)

        # Powerful
        powerful_icon = Circle(radius=0.3, color=RED, fill_opacity=0.8)
        powerful_text = Text("Powerful & Versatile", font_size=32)
        powerful_text.next_to(powerful_icon, RIGHT, buff=0.3)
        powerful_group = VGroup(powerful_icon, powerful_text)

        # Open Source
        open_icon = Circle(radius=0.3, color=YELLOW, fill_opacity=0.8)
        open_text = Text("Free & Open Source", font_size=32)
        open_text.next_to(open_icon, RIGHT, buff=0.3)
        open_group = VGroup(open_icon, open_text)

        # Large Community
        community_icon = Circle(radius=0.3, color=PURPLE, fill_opacity=0.8)
        community_text = Text("Huge Community", font_size=32)
        community_text.next_to(community_icon, RIGHT, buff=0.3)
        community_group = VGroup(community_icon, community_text)

        characteristics.add(simple_group, powerful_group, open_group, community_group)
        characteristics.arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        characteristics.next_to(title, DOWN, buff=1.5)
        characteristics.shift(LEFT * 1)

        # Animate each characteristic
        for i, char in enumerate(characteristics):
            self.play(DrawBorderThenFill(char[0]), Write(char[1]), run_time=1.2)
            self.wait(0.5)

        # Add some examples on the right
        examples_title = Text("Used For:", font_size=36, color=ORANGE)
        examples_title.to_edge(RIGHT).shift(UP * 2 + LEFT * 2)

        examples = VGroup(
            Text("• Web Development", font_size=24),
            Text("• Data Science", font_size=24),
            Text("• Artificial Intelligence", font_size=24),
            Text("• Automation", font_size=24),
            Text("• Game Development", font_size=24),
            Text("• Scientific Computing", font_size=24),
        )
        examples.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        examples.next_to(examples_title, DOWN, buff=0.5)

        self.play(Write(examples_title))
        self.play(ShowIncreasingSubsets(examples, run_time=3))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class PythonBasics(Scene):
    def construct(self):
        title = Text("Python Basics", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create a code editor-like background
        code_bg = Rectangle(
            width=12,
            height=6,
            fill_color=BLACK,
            fill_opacity=0.9,
            stroke_color=GREY,
            stroke_width=2,
        )
        code_bg.shift(DOWN * 0.5)

        self.play(DrawBorderThenFill(code_bg))

        # Line numbers
        line_numbers = VGroup()
        for i in range(1, 8):
            num = Text(str(i), font_size=20, color=GREY)
            num.move_to(code_bg.get_left() + RIGHT * 0.5 + UP * (3 - i * 0.8))
            line_numbers.add(num)

        self.play(ShowIncreasingSubsets(line_numbers))

        # Code examples with syntax highlighting
        code_lines = [
            "# This is a comment",
            'print("Hello, World!")',
            "",
            'name = "Alice"',
            "age = 25",
            "height = 5.6",
            "is_student = True",
        ]

        code_objects = VGroup()
        for i, line in enumerate(code_lines):
            if line.strip():
                if line.startswith("#"):
                    # Comment
                    code_text = Text(line, font_size=24, color=GREEN)
                elif "print" in line:
                    # Print statement
                    code_text = Text(line, font_size=24, color=YELLOW)
                elif "=" in line:
                    # Variable assignment
                    parts = line.split("=")
                    var_name = Text(parts[0].strip(), font_size=24, color=BLUE)
                    equals = Text(" = ", font_size=24, color=WHITE)
                    value = Text(parts[1].strip(), font_size=24, color=ORANGE)
                    code_text = VGroup(var_name, equals, value).arrange(RIGHT, buff=0)
                else:
                    code_text = Text(line, font_size=24, color=WHITE)
            else:
                code_text = Text(line, font_size=24, color=WHITE)

            code_text.move_to(code_bg.get_left() + RIGHT * 2 + UP * (2.5 - i * 0.7))
            code_objects.add(code_text)

        # Type each line with typewriter effect
        for i, code_obj in enumerate(code_objects):
            if code_lines[i].strip():  # Skip empty lines
                self.play(Write(code_obj, run_time=1.5))
                self.wait(0.5)

        self.wait(2)

        # Show output
        output_box = Rectangle(
            width=6,
            height=2,
            fill_color=DARK_GREY,
            fill_opacity=0.8,
            stroke_color=GREEN,
            stroke_width=2,
        )
        output_box.to_edge(RIGHT).shift(DOWN * 2)

        output_title = Text("Output:", font_size=24, color=GREEN)
        output_title.next_to(output_box, UP, buff=0.2)

        output_text = Text("Hello, World!", font_size=24, color=GREEN)
        output_text.move_to(output_box.get_center())

        self.play(DrawBorderThenFill(output_box), Write(output_title))
        self.play(Write(output_text, run_time=1))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class VariablesAndDataTypes(Scene):
    def construct(self):
        title = Text("Variables & Data Types", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Create visual representation of variables as boxes
        subtitle = Text(
            "Think of variables as labeled boxes that store data",
            font_size=32,
            color=GREY,
        )
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle))

        # Create variable boxes
        var_boxes = VGroup()

        # String variable
        str_box = Rectangle(width=3, height=1.5, color=BLUE, fill_opacity=0.3)
        str_label = Text("name", font_size=24, color=BLUE).move_to(
            str_box.get_top() + UP * 0.3
        )
        str_value = Text('"Alice"', font_size=20, color=WHITE).move_to(
            str_box.get_center()
        )
        str_type = Text("str", font_size=16, color=BLUE).move_to(
            str_box.get_bottom() + DOWN * 0.3
        )
        str_group = VGroup(str_box, str_label, str_value, str_type)

        # Integer variable
        int_box = Rectangle(width=3, height=1.5, color=GREEN, fill_opacity=0.3)
        int_label = Text("age", font_size=24, color=GREEN).move_to(
            int_box.get_top() + UP * 0.3
        )
        int_value = Text("25", font_size=20, color=WHITE).move_to(int_box.get_center())
        int_type = Text("int", font_size=16, color=GREEN).move_to(
            int_box.get_bottom() + DOWN * 0.3
        )
        int_group = VGroup(int_box, int_label, int_value, int_type)

        # Float variable
        float_box = Rectangle(width=3, height=1.5, color=YELLOW, fill_opacity=0.3)
        float_label = Text("height", font_size=24, color=YELLOW).move_to(
            float_box.get_top() + UP * 0.3
        )
        float_value = Text("5.6", font_size=20, color=WHITE).move_to(
            float_box.get_center()
        )
        float_type = Text("float", font_size=16, color=YELLOW).move_to(
            float_box.get_bottom() + DOWN * 0.3
        )
        float_group = VGroup(float_box, float_label, float_value, float_type)

        # Boolean variable
        bool_box = Rectangle(width=3, height=1.5, color=RED, fill_opacity=0.3)
        bool_label = Text("is_student", font_size=20, color=RED).move_to(
            bool_box.get_top() + UP * 0.3
        )
        bool_value = Text("True", font_size=20, color=WHITE).move_to(
            bool_box.get_center()
        )
        bool_type = Text("bool", font_size=16, color=RED).move_to(
            bool_box.get_bottom() + DOWN * 0.3
        )
        bool_group = VGroup(bool_box, bool_label, bool_value, bool_type)

        var_boxes.add(str_group, int_group, float_group, bool_group)
        var_boxes.arrange(RIGHT, buff=0.8)
        var_boxes.shift(DOWN * 1)

        # Animate creation of each variable
        for var_group in var_boxes:
            self.play(
                DrawBorderThenFill(var_group[0]),  # box
                Write(var_group[1]),  # label
                run_time=1,
            )
            self.play(
                Write(var_group[2]),  # value
                Write(var_group[3]),  # type
                run_time=1,
            )
            self.wait(0.5)

        # Show assignment arrows
        assignment_text = Text('name = "Alice"', font_size=28, color=WHITE)
        assignment_text.shift(UP * 3)

        arrow = Arrow(
            start=assignment_text.get_bottom(),
            end=str_group.get_top(),
            color=BLUE,
            stroke_width=6,
        )

        self.play(Write(assignment_text))
        self.play(ShowCreation(arrow))
        self.wait(2)

        # Demonstrate type checking
        type_demo_text = Text(
            "Python automatically determines data types!", font_size=32, color=ORANGE
        )
        type_demo_text.to_edge(DOWN)

        self.play(Write(type_demo_text))
        self.wait(3)

        self.play(FadeOut(Group(*self.mobjects)))


class BasicOperations(Scene):
    def construct(self):
        title = Text("Basic Operations", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        # Arithmetic Operations
        arith_title = Text("Arithmetic Operations", font_size=40, color=YELLOW)
        arith_title.shift(UP * 2 + LEFT * 4)
        self.play(Write(arith_title))

        # Create operation examples
        operations = [
            ("5 + 3", "8", "Addition"),
            ("10 - 4", "6", "Subtraction"),
            ("6 * 7", "42", "Multiplication"),
            ("15 / 3", "5.0", "Division"),
            ("17 // 5", "3", "Floor Division"),
            ("17 % 5", "2", "Modulus"),
            ("2 ** 3", "8", "Exponentiation"),
        ]

        op_group = VGroup()
        for i, (expr, result, name) in enumerate(operations):
            # Expression
            expression = Text(expr, font_size=24, color=WHITE)
            equals = Text(" = ", font_size=24, color=GREY)
            answer = Text(result, font_size=24, color=GREEN)
            operation = VGroup(expression, equals, answer).arrange(RIGHT)

            # Operation name
            op_name = Text(name, font_size=18, color=ORANGE)
            op_name.next_to(operation, RIGHT, buff=0.5)

            full_op = VGroup(operation, op_name)
            op_group.add(full_op)

        op_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        op_group.next_to(arith_title, DOWN, buff=0.5)
        op_group.shift(LEFT * 2)

        # Animate each operation
        for op in op_group:
            self.play(Write(op[0]), run_time=1)  # expression and result
            self.play(Write(op[1]), run_time=0.5)  # operation name
            self.wait(0.3)

        # String Operations
        str_title = Text("String Operations", font_size=40, color=PURPLE)
        str_title.to_edge(RIGHT).shift(UP * 2 + LEFT * 2)
        self.play(Write(str_title))

        # String examples
        str_examples = [
            ('"Hello" + " World"', '"Hello World"'),
            ('"Python" * 3', '"PythonPythonPython"'),
            ('len("Hello")', "5"),
            ('"HELLO".lower()', '"hello"'),
            ('"hello".upper()', '"HELLO"'),
        ]

        str_group = VGroup()
        for expr, result in str_examples:
            expression = Text(expr, font_size=20, color=WHITE)
            equals = Text(" → ", font_size=20, color=GREY)
            answer = Text(result, font_size=20, color=PURPLE)
            str_op = VGroup(expression, equals, answer).arrange(RIGHT)
            str_group.add(str_op)

        str_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        str_group.next_to(str_title, DOWN, buff=0.5)

        for str_op in str_group:
            self.play(Write(str_op), run_time=1)
            self.wait(0.3)

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class ListsAndCollections(Scene):
    def construct(self):
        title = Text("Lists & Collections", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text(
            "Store multiple items in a single variable", font_size=32, color=GREY
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Visual representation of a list
        list_title = Text(
            "fruits = ['apple', 'banana', 'orange']", font_size=32, color=WHITE
        )
        list_title.shift(UP * 1.5)
        self.play(Write(list_title))

        # Create visual list with boxes
        boxes = VGroup()
        items = ["apple", "banana", "orange"]
        colors = [RED, YELLOW, ORANGE]

        for i, (item, color) in enumerate(zip(items, colors)):
            # Box for each item
            box = Rectangle(width=2.5, height=1, color=color, fill_opacity=0.3)

            # Index number
            index = Text(f"[{i}]", font_size=20, color=GREY)
            index.next_to(box, UP, buff=0.1)

            # Item value
            value = Text(f'"{item}"', font_size=24, color=WHITE)
            value.move_to(box.get_center())

            item_group = VGroup(box, index, value)
            boxes.add(item_group)

        boxes.arrange(RIGHT, buff=0.3)
        boxes.shift(DOWN * 0.5)

        # Animate list creation
        for i, box_group in enumerate(boxes):
            self.play(
                DrawBorderThenFill(box_group[0]),  # box
                Write(box_group[1]),  # index
                Write(box_group[2]),  # value
                run_time=1,
            )
            self.wait(0.3)

        # Show indexing
        index_arrow = Arrow(
            start=UP * 2.5,
            end=boxes[1][1].get_top() + UP * 0.2,
            color=YELLOW,
            stroke_width=6,
        )
        index_text = Text("fruits[1] returns 'banana'", font_size=28, color=YELLOW)
        index_text.next_to(index_arrow, UP, buff=0.2)

        self.play(ShowCreation(index_arrow))
        self.play(Write(index_text))
        self.wait(2)

        # List operations
        self.play(FadeOut(index_arrow), FadeOut(index_text))

        operations_title = Text("Common List Operations:", font_size=36, color=GREEN)
        operations_title.shift(DOWN * 2.5)
        self.play(Write(operations_title))

        operations = [
            "fruits.append('grape')  # Add item",
            "fruits.remove('banana')  # Remove item",
            "len(fruits)  # Get length",
            "fruits[0]  # Access first item",
        ]

        op_texts = VGroup()
        for op in operations:
            op_text = Text(op, font_size=24, color=WHITE)
            op_texts.add(op_text)

        op_texts.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        op_texts.next_to(operations_title, DOWN, buff=0.5)

        self.play(ShowIncreasingSubsets(op_texts, run_time=3))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class ConditionalStatements(Scene):
    def construct(self):
        title = Text("Conditional Statements", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Making Decisions in Code", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Create a flowchart-style visualization
        # Decision diamond
        decision = Polygon(
            [0, 1.2, 0],
            [1.5, 0, 0],
            [0, -1.2, 0],
            [-1.5, 0, 0],
            color=YELLOW,
            fill_opacity=0.3,
        )
        decision_text = Text("age >= 18?", font_size=24, color=WHITE)
        decision_text.move_to(decision.get_center())

        # True path
        true_box = Rectangle(width=3, height=1, color=GREEN, fill_opacity=0.3)
        true_box.shift(RIGHT * 4 + DOWN * 1)
        true_text = Text("Can vote", font_size=24, color=WHITE)
        true_text.move_to(true_box.get_center())

        # False path
        false_box = Rectangle(width=3, height=1, color=RED, fill_opacity=0.3)
        false_box.shift(LEFT * 4 + DOWN * 1)
        false_text = Text("Cannot vote", font_size=24, color=WHITE)
        false_text.move_to(false_box.get_center())

        # Arrows
        true_arrow = Arrow(
            start=decision.get_right(),
            end=true_box.get_left(),
            color=GREEN,
            stroke_width=4,
        )
        false_arrow = Arrow(
            start=decision.get_left(),
            end=false_box.get_right(),
            color=RED,
            stroke_width=4,
        )

        # Labels for arrows
        true_label = Text("True", font_size=20, color=GREEN)
        true_label.next_to(true_arrow, UP, buff=0.1)
        false_label = Text("False", font_size=20, color=RED)
        false_label.next_to(false_arrow, UP, buff=0.1)

        # Animate flowchart
        self.play(DrawBorderThenFill(decision))
        self.play(Write(decision_text))
        self.wait(1)

        self.play(ShowCreation(true_arrow), ShowCreation(false_arrow), run_time=1.5)
        self.play(Write(true_label), Write(false_label), run_time=1)

        self.play(
            DrawBorderThenFill(true_box), DrawBorderThenFill(false_box), run_time=1.5
        )
        self.play(Write(true_text), Write(false_text), run_time=1)

        # Show code equivalent
        code_bg = Rectangle(
            width=8,
            height=3,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREY,
            stroke_width=2,
        )
        code_bg.to_edge(DOWN)

        code_text = Text(
            "age = 20\n"
            "if age >= 18:\n"
            "    print('Can vote')\n"
            "else:\n"
            "    print('Cannot vote')",
            font_size=24,
            color=WHITE,
        )
        code_text.move_to(code_bg.get_center())

        self.play(DrawBorderThenFill(code_bg))
        self.play(Write(code_text, run_time=2))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class LoopsAndIteration(Scene):
    def construct(self):
        title = Text("Loops & Iteration", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Repeating Actions Efficiently", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # For loop visualization
        for_title = Text(
            "For Loop: Iterate over a sequence", font_size=32, color=YELLOW
        )
        for_title.shift(UP * 1.5 + LEFT * 3)
        self.play(Write(for_title))

        # Create visual representation of for loop
        numbers = [1, 2, 3, 4, 5]
        squares = []

        # Input sequence
        input_title = Text("Numbers:", font_size=24, color=WHITE)
        input_title.shift(LEFT * 5 + UP * 0.5)
        self.play(Write(input_title))

        input_boxes = VGroup()
        for i, num in enumerate(numbers):
            box = Rectangle(width=0.8, height=0.8, color=BLUE, fill_opacity=0.3)
            num_text = Text(str(num), font_size=20, color=WHITE)
            num_text.move_to(box.get_center())
            box_group = VGroup(box, num_text)
            input_boxes.add(box_group)

        input_boxes.arrange(RIGHT, buff=0.2)
        input_boxes.next_to(input_title, DOWN, buff=0.3)

        self.play(ShowIncreasingSubsets(input_boxes, run_time=2))

        # Process arrow
        process_arrow = Arrow(
            start=input_boxes.get_right() + RIGHT * 0.5,
            end=input_boxes.get_right() + RIGHT * 2,
            color=YELLOW,
            stroke_width=4,
        )
        process_text = Text("× 2", font_size=24, color=YELLOW)
        process_text.next_to(process_arrow, UP, buff=0.1)

        self.play(ShowCreation(process_arrow))
        self.play(Write(process_text))

        # Output sequence
        output_title = Text("Doubled:", font_size=24, color=WHITE)
        output_title.shift(RIGHT * 2 + UP * 0.5)
        self.play(Write(output_title))

        output_boxes = VGroup()
        for i, num in enumerate(numbers):
            box = Rectangle(width=0.8, height=0.8, color=GREEN, fill_opacity=0.3)
            doubled = num * 2
            num_text = Text(str(doubled), font_size=20, color=WHITE)
            num_text.move_to(box.get_center())
            box_group = VGroup(box, num_text)
            output_boxes.add(box_group)

        output_boxes.arrange(RIGHT, buff=0.2)
        output_boxes.next_to(output_title, DOWN, buff=0.3)

        # Animate the processing
        for i in range(len(numbers)):
            # Highlight current input
            self.play(
                input_boxes[i][0].animate.set_stroke(YELLOW, width=4), run_time=0.5
            )

            # Show output
            self.play(
                DrawBorderThenFill(output_boxes[i][0]),
                Write(output_boxes[i][1]),
                run_time=0.8,
            )

            # Unhighlight input
            self.play(input_boxes[i][0].animate.set_stroke(BLUE, width=1), run_time=0.3)

        # Show code
        code_bg = Rectangle(
            width=8,
            height=2.5,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREY,
            stroke_width=2,
        )
        code_bg.to_edge(DOWN)

        code_text = Text(
            "numbers = [1, 2, 3, 4, 5]\n"
            "for num in numbers:\n"
            "    doubled = num * 2\n"
            "    print(doubled)",
            font_size=24,
            color=WHITE,
        )
        code_text.move_to(code_bg.get_center())

        self.play(DrawBorderThenFill(code_bg))
        self.play(Write(code_text, run_time=2))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class FunctionsIntro(Scene):
    def construct(self):
        title = Text("Functions", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Reusable Blocks of Code", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Function machine concept
        machine_title = Text(
            "Think of functions as machines:", font_size=32, color=YELLOW
        )
        machine_title.shift(UP * 1.5)
        self.play(Write(machine_title))

        # Create function machine
        machine = Rectangle(
            width=4, height=3, color=PURPLE, fill_opacity=0.3, stroke_width=3
        )
        machine.shift(DOWN * 0.5)

        function_name = Text("calculate_area", font_size=28, color=WHITE)
        function_name.move_to(machine.get_center())

        # Input
        input_arrow = Arrow(
            start=machine.get_left() + LEFT * 2,
            end=machine.get_left(),
            color=GREEN,
            stroke_width=6,
        )
        input_text = Text("Input:\nradius = 5", font_size=24, color=GREEN)
        input_text.next_to(input_arrow, LEFT, buff=0.3)

        # Output
        output_arrow = Arrow(
            start=machine.get_right(),
            end=machine.get_right() + RIGHT * 2,
            color=ORANGE,
            stroke_width=6,
        )
        output_text = Text("Output:\narea = 78.54", font_size=24, color=ORANGE)
        output_text.next_to(output_arrow, RIGHT, buff=0.3)

        # Animate function machine
        self.play(DrawBorderThenFill(machine))
        self.play(Write(function_name))

        self.play(ShowCreation(input_arrow))
        self.play(Write(input_text))

        # Show processing
        processing_text = Text("Processing...", font_size=20, color=YELLOW)
        processing_text.next_to(function_name, DOWN, buff=0.2)
        self.play(Write(processing_text, run_time=1))
        self.play(FadeOut(processing_text))

        self.play(ShowCreation(output_arrow))
        self.play(Write(output_text))

        # Show actual function code
        code_bg = Rectangle(
            width=10,
            height=3.5,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREY,
            stroke_width=2,
        )
        code_bg.to_edge(DOWN)

        code_text = Text(
            "def calculate_area(radius):\n"
            "    area = 3.14159 * radius * radius\n"
            "    return area\n"
            "\n"
            "result = calculate_area(5)\n"
            "print(result)  # Output: 78.54",
            font_size=22,
            color=WHITE,
        )
        code_text.move_to(code_bg.get_center())

        self.play(DrawBorderThenFill(code_bg))
        self.play(Write(code_text, run_time=3))

        # Highlight function benefits
        benefits_title = Text("Benefits of Functions:", font_size=24, color=ORANGE)
        benefits_title.to_edge(RIGHT).shift(UP * 2)

        benefits = VGroup(
            Text("• Reusable", font_size=20, color=WHITE),
            Text("• Organized", font_size=20, color=WHITE),
            Text("• Easier to test", font_size=20, color=WHITE),
            Text("• Reduces errors", font_size=20, color=WHITE),
        )
        benefits.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        benefits.next_to(benefits_title, DOWN, buff=0.3)

        self.play(Write(benefits_title))
        self.play(ShowIncreasingSubsets(benefits, run_time=2))

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class RealWorldExample(Scene):
    def construct(self):
        title = Text("Real-World Example", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("Building a Simple Calculator", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle))

        # Calculator visual
        calc_bg = Rectangle(
            width=6,
            height=8,
            color=DARK_GREY,
            fill_opacity=0.8,
            stroke_color=WHITE,
            stroke_width=3,
        )
        calc_bg.shift(LEFT * 3)

        # Display screen
        screen = Rectangle(
            width=5,
            height=1.5,
            color=BLACK,
            fill_opacity=1,
            stroke_color=GREEN,
            stroke_width=2,
        )
        screen.move_to(calc_bg.get_top() + DOWN * 1.5)

        display_text = Text("0", font_size=36, color=GREEN)
        display_text.move_to(screen.get_center())

        # Create calculator
        self.play(DrawBorderThenFill(calc_bg))
        self.play(DrawBorderThenFill(screen))
        self.play(Write(display_text))

        # Calculator buttons (simplified)
        buttons = VGroup()
        button_layout = [
            ["7", "8", "9", "+"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "*"],
            ["0", ".", "=", "/"],
        ]

        for row_idx, row in enumerate(button_layout):
            for col_idx, btn_text in enumerate(row):
                btn = Rectangle(width=0.8, height=0.6, color=GREY, fill_opacity=0.5)
                btn_label = Text(btn_text, font_size=20, color=WHITE)
                btn_label.move_to(btn.get_center())

                btn_group = VGroup(btn, btn_label)
                x_pos = calc_bg.get_left()[0] + 1 + col_idx * 1
                y_pos = screen.get_bottom()[1] - 1 - row_idx * 0.8
                btn_group.move_to([x_pos, y_pos, 0])

                buttons.add(btn_group)

        self.play(ShowIncreasingSubsets(buttons, run_time=2))

        # Show code implementation
        code_bg = Rectangle(
            width=8,
            height=7,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_color=GREY,
            stroke_width=2,
        )
        code_bg.shift(RIGHT * 3)

        code_text = Text(
            "# Simple Calculator\n"
            "\n"
            "def add(x, y):\n"
            "    return x + y\n"
            "\n"
            "def subtract(x, y):\n"
            "    return x - y\n"
            "\n"
            "def multiply(x, y):\n"
            "    return x * y\n"
            "\n"
            "def divide(x, y):\n"
            "    if y != 0:\n"
            "        return x / y\n"
            "    else:\n"
            "        return 'Error'\n"
            "\n"
            "# Usage\n"
            "result = add(10, 5)\n"
            "print(result)  # 15",
            font_size=18,
            color=WHITE,
            line_spacing=0.8,
        )
        code_text.move_to(code_bg.get_center())

        self.play(DrawBorderThenFill(code_bg))
        self.play(Write(code_text, run_time=4))

        # Demonstrate calculation
        demo_text = Text("Demo: 10 + 5", font_size=24, color=YELLOW)
        demo_text.next_to(calc_bg, DOWN, buff=0.5)
        self.play(Write(demo_text))

        # Update display
        self.play(
            Transform(
                display_text,
                Text("15", font_size=36, color=GREEN).move_to(screen.get_center()),
            )
        )

        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)))


class NextSteps(Scene):
    def construct(self):
        title = Text("Your Python Journey Continues!", font_size=56, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text("What to learn next:", font_size=36, color=GREY)
        subtitle.next_to(title, DOWN, buff=0.5)
        self.play(Write(subtitle))

        # Learning path with connected nodes
        topics = [
            ("Object-Oriented Programming", YELLOW),
            ("File Handling", GREEN),
            ("Error Handling", RED),
            ("Libraries & Modules", PURPLE),
            ("Web Development", ORANGE),
            ("Data Science", BLUE),
            ("Machine Learning", PINK),
        ]

        # Create learning path
        nodes = VGroup()
        connections = VGroup()

        for i, (topic, color) in enumerate(topics):
            # Create node
            circle = Circle(radius=0.8, color=color, fill_opacity=0.3)
            text = Text(topic, font_size=16, color=WHITE)
            text.move_to(circle.get_center())
            node = VGroup(circle, text)

            # Position nodes in a path
            if i < 4:
                x_pos = -4 + i * 2.5
                y_pos = 1
            else:
                x_pos = -4 + (i - 4) * 2.5
                y_pos = -1.5

            node.move_to([x_pos, y_pos, 0])
            nodes.add(node)

            # Create connections
            if i > 0:
                if i == 4:  # Connect to next row
                    start_node = nodes[i - 1]
                    connection = Arrow(
                        start=start_node.get_bottom(),
                        end=node.get_top(),
                        color=GREY,
                        stroke_width=2,
                    )
                else:
                    start_node = nodes[i - 1]
                    connection = Arrow(
                        start=start_node.get_right(),
                        end=node.get_left(),
                        color=GREY,
                        stroke_width=2,
                    )
                connections.add(connection)

        # Animate learning path
        self.play(ShowIncreasingSubsets(nodes, run_time=4))
        self.play(ShowIncreasingSubsets(connections, run_time=2))

        # Tips for learning
        tips_title = Text("Learning Tips:", font_size=32, color=ORANGE)
        tips_title.to_edge(DOWN).shift(UP * 2)

        tips = VGroup(
            Text("• Practice coding every day", font_size=24, color=WHITE),
            Text("• Build real projects", font_size=24, color=WHITE),
            Text("• Join Python communities", font_size=24, color=WHITE),
            Text("• Read other people's code", font_size=24, color=WHITE),
        )
        tips.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        tips.next_to(tips_title, DOWN, buff=0.3)

        self.play(Write(tips_title))
        self.play(ShowIncreasingSubsets(tips, run_time=2))

        # Final message
        final_message = Text("Happy Coding! 🐍", font_size=48, color=YELLOW)
        final_message.to_edge(DOWN)
        self.play(Write(final_message, run_time=2))

        # Celebration particles
        particles = VGroup()
        for i in range(30):
            particle = Circle(
                radius=0.05, color=random_bright_color(), fill_opacity=0.8
            )
            particle.move_to([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
            particles.add(particle)

        self.play(ShowIncreasingSubsets(particles, run_time=2))
        self.play(
            *[
                particle.animate.shift(
                    UP * np.random.uniform(0.5, 2) + RIGHT * np.random.uniform(-1, 1)
                )
                for particle in particles
            ],
            run_time=3,
        )

        self.wait(3)
