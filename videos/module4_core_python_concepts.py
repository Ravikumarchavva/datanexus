from manimlib import *
import numpy as np
import random


class Module4CorePythonConcepts(Scene):
    def construct(self):
        """Module 4: Core Python Concepts (60 min)"""
        self.camera.background_color = "#0f0f23"

        # Module introduction
        self.module_intro()

        # Data types and structures
        self.data_types_overview()
        self.numbers_demonstration()
        self.strings_demonstration()
        self.booleans_demonstration()
        self.collections_overview()
        self.lists_demonstration()
        self.dictionaries_demonstration()
        self.tuples_and_sets()

        # Control flow and loops
        self.control_flow_intro()
        self.conditional_statements()
        self.loops_demonstration()
        self.list_comprehensions()

        # Module conclusion
        self.module_conclusion()

    def module_intro(self):
        """Introduction to Module 4"""
        title = Text("Module 4", font_size=64, color=BLUE)
        subtitle = Text("Core Python Concepts", font_size=48, color=GREEN)
        description = Text(
            "Data Types • Control Flow • Collections", font_size=32, color=YELLOW
        )

        title.to_edge(UP, buff=1)
        subtitle.next_to(title, DOWN, buff=0.5)
        description.next_to(subtitle, DOWN, buff=0.8)

        # Create animated Python data structures
        data_icons = VGroup()

        # Number icon
        number_icon = Circle(radius=0.5, color=BLUE, fill_opacity=0.3)
        number_text = Text("42", font_size=24, color=WHITE)
        number_text.move_to(number_icon)
        number_group = VGroup(number_icon, number_text)

        # String icon
        string_icon = RoundedRectangle(
            width=1.5, height=0.8, corner_radius=0.1, color=GREEN, fill_opacity=0.3
        )
        string_text = Text('"Hello"', font_size=20, color=WHITE)
        string_text.move_to(string_icon)
        string_group = VGroup(string_icon, string_text)

        # List icon
        list_icon = Rectangle(width=2, height=0.8, color=YELLOW, fill_opacity=0.3)
        list_text = Text("[1, 2, 3]", font_size=20, color=WHITE)
        list_text.move_to(list_icon)
        list_group = VGroup(list_icon, list_text)

        # Dictionary icon
        dict_icon = RoundedRectangle(
            width=2, height=1, corner_radius=0.1, color=RED, fill_opacity=0.3
        )
        dict_text = Text('{"key": "value"}', font_size=16, color=WHITE)
        dict_text.move_to(dict_icon)
        dict_group = VGroup(dict_icon, dict_text)

        data_icons.add(number_group, string_group, list_group, dict_group)
        data_icons.arrange(RIGHT, buff=1)
        data_icons.next_to(description, DOWN, buff=1.5)

        # Animate introduction
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(Write(description), run_time=1.5)

        # Animate data structure icons
        self.play(LaggedStartMap(FadeIn, data_icons, lag_ratio=0.3), run_time=2)

        # Rotate and scale animations
        self.play(*[icon.animate.scale(1.2) for icon in data_icons], run_time=1)
        self.play(*[icon.animate.scale(1 / 1.2) for icon in data_icons], run_time=1)

        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle, description, data_icons)))

    def data_types_overview(self):
        """Overview of Python data types"""
        title = Text("Python Data Types", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        # Create data type hierarchy
        basic_types = Text("Basic Types", font_size=36, color=GREEN)
        basic_types.move_to(LEFT * 4 + UP * 1.5)

        collections = Text("Collections", font_size=36, color=YELLOW)
        collections.move_to(RIGHT * 4 + UP * 1.5)

        # Basic types list
        basic_list = VGroup(
            Text("int - Whole numbers", font_size=24, color=WHITE),
            Text("float - Decimal numbers", font_size=24, color=WHITE),
            Text("str - Text strings", font_size=24, color=WHITE),
            Text("bool - True/False", font_size=24, color=WHITE),
        )
        basic_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        basic_list.next_to(basic_types, DOWN, buff=0.5)

        # Collections list
        collections_list = VGroup(
            Text("list - Ordered, mutable", font_size=24, color=WHITE),
            Text("tuple - Ordered, immutable", font_size=24, color=WHITE),
            Text("dict - Key-value pairs", font_size=24, color=WHITE),
            Text("set - Unique elements", font_size=24, color=WHITE),
        )
        collections_list.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        collections_list.next_to(collections, DOWN, buff=0.5)

        # Draw connecting lines
        divider = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=1)

        self.play(Write(title))
        self.play(Create(divider))
        self.play(Write(basic_types), Write(collections))
        self.play(LaggedStartMap(FadeIn, basic_list, lag_ratio=0.2))
        self.play(LaggedStartMap(FadeIn, collections_list, lag_ratio=0.2))

        # Highlight mutable vs immutable
        mutable_note = Text("Mutable = Can be changed", font_size=20, color=GREEN)
        immutable_note = Text("Immutable = Cannot be changed", font_size=20, color=RED)

        mutable_note.move_to(DOWN * 2.5)
        immutable_note.next_to(mutable_note, DOWN, buff=0.3)

        self.play(Write(mutable_note), Write(immutable_note))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    basic_types,
                    collections,
                    basic_list,
                    collections_list,
                    divider,
                    mutable_note,
                    immutable_note,
                )
            )
        )

    def numbers_demonstration(self):
        """Demonstrate numbers (int, float, complex)"""
        title = Text("Numbers in Python", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Integer demonstration
        int_title = Text("Integers (int)", font_size=32, color=GREEN)
        int_title.move_to(LEFT * 4 + UP * 1.5)

        int_examples = VGroup(
            Text("age = 25", font_size=24, color=YELLOW),
            Text("count = -10", font_size=24, color=YELLOW),
            Text("big_num = 1_000_000", font_size=24, color=YELLOW),
        )
        int_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        int_examples.next_to(int_title, DOWN, buff=0.5)

        # Float demonstration
        float_title = Text("Floats (float)", font_size=32, color=YELLOW)
        float_title.move_to(RIGHT * 4 + UP * 1.5)

        float_examples = VGroup(
            Text("price = 19.99", font_size=24, color=YELLOW),
            Text("pi = 3.14159", font_size=24, color=YELLOW),
            Text("scientific = 1.5e-4", font_size=24, color=YELLOW),
        )
        float_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        float_examples.next_to(float_title, DOWN, buff=0.5)

        # Animate number types
        self.play(Write(int_title))
        self.play(LaggedStartMap(Write, int_examples, lag_ratio=0.5))
        self.play(Write(float_title))
        self.play(LaggedStartMap(Write, float_examples, lag_ratio=0.5))

        # Mathematical operations demonstration
        math_title = Text("Mathematical Operations", font_size=28, color=RED)
        math_title.move_to(DOWN * 0.5)

        operations = [
            ("Addition: 5 + 3", "8"),
            ("Subtraction: 10 - 4", "6"),
            ("Multiplication: 6 * 7", "42"),
            ("Division: 15 / 4", "3.75"),
            ("Floor Division: 15 // 4", "3"),
            ("Modulo: 15 % 4", "3"),
            ("Exponentiation: 2 ** 3", "8"),
        ]

        self.play(Write(math_title))

        # Animate each operation
        for operation, result in operations:
            op_text = Text(operation, font_size=20, color=WHITE)
            result_text = Text(f"= {result}", font_size=20, color=GREEN)

            op_text.next_to(math_title, DOWN, buff=0.5)
            result_text.next_to(op_text, RIGHT, buff=0.5)

            self.play(Write(op_text), run_time=0.8)
            self.play(Write(result_text), run_time=0.5)
            self.wait(0.3)
            self.play(FadeOut(VGroup(op_text, result_text)), run_time=0.3)

        self.wait(2)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    int_title,
                    float_title,
                    int_examples,
                    float_examples,
                    math_title,
                )
            )
        )

    def strings_demonstration(self):
        """Demonstrate strings and string operations"""
        title = Text("Strings in Python", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # String creation examples
        creation_title = Text("Creating Strings", font_size=32, color=GREEN)
        creation_title.move_to(UP * 1.5)

        string_examples = VGroup(
            Text('name = "Alice"', font_size=24, color=YELLOW),
            Text("message = 'Hello World'", font_size=24, color=YELLOW),
            Text('multiline = """This is a', font_size=24, color=YELLOW),
            Text('multiline string"""', font_size=24, color=YELLOW),
        )
        string_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        string_examples.next_to(creation_title, DOWN, buff=0.5)

        self.play(Write(creation_title))
        self.play(LaggedStartMap(Write, string_examples, lag_ratio=0.3))

        self.wait(1)
        self.play(FadeOut(VGroup(creation_title, string_examples)))

        # String operations
        ops_title = Text("String Operations", font_size=32, color=YELLOW)
        ops_title.move_to(UP * 1)

        # Interactive string operations
        operations = [
            ('text = "Python"', ""),
            ("len(text)", "6"),
            ("text.upper()", '"PYTHON"'),
            ("text.lower()", '"python"'),
            ("text[0]", '"P"'),
            ("text[-1]", '"n"'),
            ("text[1:4]", '"yth"'),
            ('"Hello " + "World"', '"Hello World"'),
            ("f'I love {text}'", '"I love Python"'),
        ]

        self.play(Write(ops_title))

        for operation, result in operations:
            op_text = Text(operation, font_size=22, color=WHITE)
            if result:
                result_text = Text(f"→ {result}", font_size=22, color=GREEN)

            op_text.next_to(ops_title, DOWN, buff=0.8)

            if result:
                result_text.next_to(op_text, RIGHT, buff=1)
                self.play(Write(op_text), run_time=0.8)
                self.play(Write(result_text), run_time=0.5)
                self.wait(0.5)
                self.play(FadeOut(VGroup(op_text, result_text)), run_time=0.3)
            else:
                self.play(Write(op_text), run_time=0.8)
                self.wait(0.8)
                self.play(FadeOut(op_text), run_time=0.3)

        # String methods showcase
        methods_title = Text("Common String Methods", font_size=28, color=RED)
        methods_title.move_to(DOWN * 0.5)

        methods = [
            ".strip() - Remove whitespace",
            ".split() - Split into list",
            ".replace(old, new) - Replace text",
            ".startswith() - Check beginning",
            ".isdigit() - Check if numeric",
        ]

        self.play(Write(methods_title))

        methods_objects = VGroup()
        for method in methods:
            method_text = Text(method, font_size=20, color=WHITE)
            methods_objects.add(method_text)

        methods_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        methods_objects.next_to(methods_title, DOWN, buff=0.5)

        self.play(LaggedStartMap(FadeIn, methods_objects, lag_ratio=0.2))

        self.wait(3)
        self.play(FadeOut(VGroup(title, ops_title, methods_title, methods_objects)))

    def booleans_demonstration(self):
        """Demonstrate booleans and logical operations"""
        title = Text("Booleans in Python", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Boolean values
        bool_title = Text("Boolean Values", font_size=32, color=GREEN)
        bool_title.move_to(UP * 1.5)

        bool_examples = VGroup(
            Text("is_student = True", font_size=24, color=YELLOW),
            Text("is_teacher = False", font_size=24, color=YELLOW),
            Text("# Only two values: True or False", font_size=20, color=GREEN),
        )
        bool_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        bool_examples.next_to(bool_title, DOWN, buff=0.5)

        self.play(Write(bool_title))
        self.play(LaggedStartMap(Write, bool_examples, lag_ratio=0.4))

        # Comparison operations
        comp_title = Text("Comparison Operations", font_size=28, color=YELLOW)
        comp_title.move_to(DOWN * 0.2)

        comparisons = [
            ("5 > 3", "True"),
            ("10 == 10", "True"),
            ("7 != 8", "True"),
            ("4 < 2", "False"),
            ("6 >= 6", "True"),
            ("'apple' == 'apple'", "True"),
        ]

        self.play(Write(comp_title))

        for comparison, result in comparisons:
            comp_text = Text(comparison, font_size=20, color=WHITE)
            result_text = Text(
                f"→ {result}", font_size=20, color=GREEN if result == "True" else RED
            )

            comp_text.next_to(comp_title, DOWN, buff=0.8)
            result_text.next_to(comp_text, RIGHT, buff=1)

            self.play(Write(comp_text), run_time=0.6)
            self.play(Write(result_text), run_time=0.4)
            self.wait(0.4)
            self.play(FadeOut(VGroup(comp_text, result_text)), run_time=0.3)

        # Logical operations
        logical_title = Text("Logical Operations", font_size=28, color=RED)
        logical_title.move_to(DOWN * 1.8)

        logical_ops = [
            ("True and False", "False"),
            ("True or False", "True"),
            ("not True", "False"),
            ("not False", "True"),
        ]

        self.play(Write(logical_title))

        for operation, result in logical_ops:
            op_text = Text(operation, font_size=20, color=WHITE)
            result_text = Text(
                f"→ {result}", font_size=20, color=GREEN if result == "True" else RED
            )

            op_text.next_to(logical_title, DOWN, buff=0.5)
            result_text.next_to(op_text, RIGHT, buff=1)

            self.play(Write(op_text), run_time=0.6)
            self.play(Write(result_text), run_time=0.4)
            self.wait(0.4)
            self.play(FadeOut(VGroup(op_text, result_text)), run_time=0.3)

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, bool_title, bool_examples, comp_title, logical_title))
        )

    def collections_overview(self):
        """Overview of Python collections"""
        title = Text("Python Collections", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create visual comparison table
        headers = VGroup(
            Text("Type", font_size=24, color=YELLOW),
            Text("Ordered", font_size=24, color=YELLOW),
            Text("Mutable", font_size=24, color=YELLOW),
            Text("Duplicates", font_size=24, color=YELLOW),
            Text("Syntax", font_size=24, color=YELLOW),
        )
        headers.arrange(RIGHT, buff=1.2)
        headers.move_to(UP * 1.5)

        # Data for each collection type
        collections_data = [
            ("list", "✓", "✓", "✓", "[1, 2, 3]"),
            ("tuple", "✓", "✗", "✓", "(1, 2, 3)"),
            ("dict", "✓*", "✓", "✗", "{'a': 1}"),
            ("set", "✗", "✓", "✗", "{1, 2, 3}"),
        ]

        # Create table rows
        rows = VGroup()
        for data in collections_data:
            row = VGroup()
            for item in data:
                if item in ["✓", "✗"]:
                    cell = Text(item, font_size=20, color=GREEN if item == "✓" else RED)
                elif item.startswith(("list", "tuple", "dict", "set")):
                    cell = Text(item, font_size=20, color=BLUE)
                else:
                    cell = Text(item, font_size=18, color=WHITE)
                row.add(cell)
            row.arrange(RIGHT, buff=1.2)
            rows.add(row)

        rows.arrange(DOWN, buff=0.4)
        rows.next_to(headers, DOWN, buff=0.8)

        # Draw table lines
        table_lines = VGroup()
        # Horizontal lines
        for i in range(len(collections_data) + 1):
            y_pos = headers.get_bottom()[1] - i * 0.8
            line = Line(
                LEFT * 4 + UP * (y_pos - headers.get_bottom()[1]),
                RIGHT * 4 + UP * (y_pos - headers.get_bottom()[1]),
                color=GRAY,
                stroke_width=1,
            )
            table_lines.add(line)

        self.play(Write(headers))
        self.play(Create(table_lines))
        self.play(LaggedStartMap(FadeIn, rows, lag_ratio=0.3))

        # Add note about dict ordering
        note = Text(
            "* dict preserves insertion order (Python 3.7+)", font_size=16, color=GREEN
        )
        note.next_to(rows, DOWN, buff=0.8)
        self.play(Write(note))

        self.wait(3)
        self.play(FadeOut(VGroup(title, headers, rows, table_lines, note)))

    def lists_demonstration(self):
        """Comprehensive list demonstration"""
        title = Text("Lists - Ordered & Mutable", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create visual list representation
        list_container = Rectangle(width=8, height=1.5, color=GREEN, stroke_width=2)
        list_container.move_to(UP * 1.5)

        # List elements
        elements = ["'apple'", "'banana'", "'cherry'", "'date'"]
        element_objects = VGroup()

        for i, element in enumerate(elements):
            # Element box
            element_box = Rectangle(
                width=1.8, height=1.2, color=YELLOW, fill_opacity=0.2
            )
            element_text = Text(element, font_size=18, color=WHITE)
            element_text.move_to(element_box)

            # Index label
            index_label = Text(str(i), font_size=16, color=RED)
            index_label.next_to(element_box, UP, buff=0.1)

            element_group = VGroup(element_box, element_text, index_label)
            element_objects.add(element_group)

        element_objects.arrange(RIGHT, buff=0.1)
        element_objects.move_to(list_container)

        # List variable
        list_var = Text(
            "fruits = ['apple', 'banana', 'cherry', 'date']", font_size=20, color=YELLOW
        )
        list_var.next_to(list_container, UP, buff=0.5)

        self.play(Write(list_var))
        self.play(Create(list_container))
        self.play(LaggedStartMap(FadeIn, element_objects, lag_ratio=0.2))

        # Demonstrate indexing
        indexing_title = Text("List Indexing", font_size=28, color=GREEN)
        indexing_title.move_to(DOWN * 0.5)

        indexing_examples = [
            ("fruits[0]", "'apple'"),
            ("fruits[1]", "'banana'"),
            ("fruits[-1]", "'date'"),
            ("fruits[-2]", "'cherry'"),
        ]

        self.play(Write(indexing_title))

        for index_expr, result in indexing_examples:
            # Highlight the corresponding element
            if "[0]" in index_expr:
                target_element = element_objects[0]
            elif "[1]" in index_expr:
                target_element = element_objects[1]
            elif "[-1]" in index_expr:
                target_element = element_objects[-1]
            elif "[-2]" in index_expr:
                target_element = element_objects[-2]

            index_text = Text(index_expr, font_size=20, color=WHITE)
            result_text = Text(f"→ {result}", font_size=20, color=GREEN)

            index_text.next_to(indexing_title, DOWN, buff=0.8)
            result_text.next_to(index_text, RIGHT, buff=1)

            self.play(target_element.animate.set_color(RED), run_time=0.5)
            self.play(Write(index_text), run_time=0.6)
            self.play(Write(result_text), run_time=0.4)
            self.wait(0.5)
            self.play(target_element.animate.set_color(YELLOW), run_time=0.3)
            self.play(FadeOut(VGroup(index_text, result_text)), run_time=0.3)

        # List methods demonstration
        self.play(FadeOut(indexing_title))

        methods_title = Text("List Methods", font_size=28, color=RED)
        methods_title.move_to(DOWN * 0.5)

        self.play(Write(methods_title))

        methods = [
            (".append('grape')", "Add to end"),
            (".insert(1, 'kiwi')", "Insert at position"),
            (".remove('banana')", "Remove first occurrence"),
            (".pop()", "Remove and return last"),
            (".sort()", "Sort in place"),
            (".reverse()", "Reverse in place"),
        ]

        for method, description in methods:
            method_text = Text(method, font_size=18, color=YELLOW)
            desc_text = Text(f"# {description}", font_size=16, color=GREEN)

            method_text.next_to(methods_title, DOWN, buff=0.8)
            desc_text.next_to(method_text, RIGHT, buff=0.5)

            self.play(Write(method_text), run_time=0.8)
            self.play(Write(desc_text), run_time=0.5)
            self.wait(0.5)
            self.play(FadeOut(VGroup(method_text, desc_text)), run_time=0.3)

        self.wait(2)
        self.play(
            FadeOut(
                VGroup(title, list_var, list_container, element_objects, methods_title)
            )
        )

    def dictionaries_demonstration(self):
        """Comprehensive dictionary demonstration"""
        title = Text("Dictionaries - Key-Value Pairs", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create visual dictionary representation
        dict_title = Text(
            "student = {'name': 'Alice', 'age': 20, 'grade': 'A'}",
            font_size=20,
            color=YELLOW,
        )
        dict_title.move_to(UP * 1.5)

        # Dictionary visualization
        dict_container = RoundedRectangle(
            width=10, height=2, corner_radius=0.2, color=BLUE, stroke_width=2
        )
        dict_container.next_to(dict_title, DOWN, buff=0.5)

        # Key-value pairs
        pairs = [("'name'", "'Alice'"), ("'age'", "20"), ("'grade'", "'A'")]

        pair_objects = VGroup()
        for key, value in pairs:
            # Key box
            key_box = Rectangle(width=1.5, height=0.8, color=GREEN, fill_opacity=0.3)
            key_text = Text(key, font_size=16, color=WHITE)
            key_text.move_to(key_box)

            # Arrow
            arrow = Arrow(ORIGIN, RIGHT * 0.8, color=WHITE, stroke_width=2)
            arrow.next_to(key_box, RIGHT, buff=0.1)

            # Value box
            value_box = Rectangle(width=1.5, height=0.8, color=RED, fill_opacity=0.3)
            value_text = Text(value, font_size=16, color=WHITE)
            value_text.move_to(value_box)
            value_box.next_to(arrow, RIGHT, buff=0.1)

            pair_group = VGroup(key_box, key_text, arrow, value_box, value_text)
            pair_objects.add(pair_group)

        pair_objects.arrange(RIGHT, buff=0.5)
        pair_objects.move_to(dict_container)

        self.play(Write(dict_title))
        self.play(Create(dict_container))
        self.play(LaggedStartMap(FadeIn, pair_objects, lag_ratio=0.3))

        # Dictionary operations
        ops_title = Text("Dictionary Operations", font_size=28, color=GREEN)
        ops_title.move_to(DOWN * 0.8)

        operations = [
            ("student['name']", "'Alice'"),
            ("student['age'] = 21", "Update value"),
            ("student['school'] = 'MIT'", "Add new key"),
            ("del student['grade']", "Remove key"),
            ("'name' in student", "True"),
            ("student.keys()", "dict_keys(['name', 'age', 'school'])"),
            ("student.values()", "dict_values(['Alice', 21, 'MIT'])"),
        ]

        self.play(Write(ops_title))

        for operation, result in operations:
            op_text = Text(operation, font_size=18, color=WHITE)
            if "Update" in result or "Add" in result or "Remove" in result:
                result_text = Text(f"# {result}", font_size=16, color=GREEN)
            else:
                result_text = Text(f"→ {result}", font_size=16, color=YELLOW)

            op_text.next_to(ops_title, DOWN, buff=0.8)
            result_text.next_to(op_text, RIGHT, buff=0.5)

            self.play(Write(op_text), run_time=0.8)
            self.play(Write(result_text), run_time=0.5)
            self.wait(0.6)
            self.play(FadeOut(VGroup(op_text, result_text)), run_time=0.3)

        # Dictionary methods
        methods_note = Text(
            "Common methods: .get(), .update(), .pop(), .items()",
            font_size=20,
            color=RED,
        )
        methods_note.next_to(ops_title, DOWN, buff=1.5)

        self.play(Write(methods_note))

        self.wait(2)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    dict_title,
                    dict_container,
                    pair_objects,
                    ops_title,
                    methods_note,
                )
            )
        )

    def tuples_and_sets(self):
        """Demonstrate tuples and sets"""
        title = Text("Tuples & Sets", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Split screen for tuples and sets
        divider = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=1)

        # Tuples section
        tuple_title = Text("Tuples (Immutable)", font_size=32, color=GREEN)
        tuple_title.move_to(LEFT * 3.5 + UP * 2)

        tuple_examples = VGroup(
            Text("coordinates = (3, 4)", font_size=20, color=YELLOW),
            Text("rgb = (255, 128, 0)", font_size=20, color=YELLOW),
            Text("# Cannot be changed!", font_size=18, color=GREEN),
        )
        tuple_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        tuple_examples.next_to(tuple_title, DOWN, buff=0.5)

        tuple_use_cases = VGroup(
            Text("✓ Store coordinates", font_size=18, color=WHITE),
            Text("✓ Return multiple values", font_size=18, color=WHITE),
            Text("✓ Dictionary keys", font_size=18, color=WHITE),
            Text("✓ Unpacking: x, y = coordinates", font_size=18, color=WHITE),
        )
        tuple_use_cases.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        tuple_use_cases.next_to(tuple_examples, DOWN, buff=0.8)

        # Sets section
        set_title = Text("Sets (Unique Elements)", font_size=32, color=YELLOW)
        set_title.move_to(RIGHT * 3.5 + UP * 2)

        set_examples = VGroup(
            Text("fruits = {'apple', 'banana'}", font_size=20, color=YELLOW),
            Text("numbers = {1, 2, 3, 2, 1}", font_size=20, color=YELLOW),
            Text("# Result: {1, 2, 3}", font_size=18, color=GREEN),
        )
        set_examples.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        set_examples.next_to(set_title, DOWN, buff=0.5)

        set_operations = VGroup(
            Text("• .add() - Add element", font_size=18, color=WHITE),
            Text("• .remove() - Remove element", font_size=18, color=WHITE),
            Text("• union() - Combine sets", font_size=18, color=WHITE),
            Text("• intersection() - Common elements", font_size=18, color=WHITE),
        )
        set_operations.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        set_operations.next_to(set_examples, DOWN, buff=0.8)

        # Animate everything
        self.play(Create(divider))
        self.play(Write(tuple_title), Write(set_title))
        self.play(LaggedStartMap(Write, tuple_examples, lag_ratio=0.3))
        self.play(LaggedStartMap(Write, set_examples, lag_ratio=0.3))
        self.play(LaggedStartMap(FadeIn, tuple_use_cases, lag_ratio=0.2))
        self.play(LaggedStartMap(FadeIn, set_operations, lag_ratio=0.2))

        # Set operations visualization
        set_demo_title = Text("Set Operations Demo", font_size=24, color=RED)
        set_demo_title.move_to(DOWN * 2)

        self.play(Write(set_demo_title))

        # Create visual sets
        set_a = Circle(radius=0.8, color=BLUE, fill_opacity=0.3)
        set_b = Circle(radius=0.8, color=RED, fill_opacity=0.3)
        set_a.move_to(LEFT * 1.5 + DOWN * 3)
        set_b.move_to(RIGHT * 1.5 + DOWN * 3)

        # Overlap for intersection
        set_b.shift(LEFT * 0.5)

        label_a = Text("A = {1, 2, 3}", font_size=16, color=WHITE)
        label_b = Text("B = {3, 4, 5}", font_size=16, color=WHITE)
        label_a.next_to(set_a, DOWN, buff=0.3)
        label_b.next_to(set_b, DOWN, buff=0.3)

        self.play(Create(set_a), Create(set_b))
        self.play(Write(label_a), Write(label_b))

        # Highlight intersection
        intersection = Intersection(set_a, set_b, color=GREEN, fill_opacity=0.5)
        self.play(Create(intersection))

        intersection_label = Text("Intersection: {3}", font_size=16, color=GREEN)
        intersection_label.move_to(DOWN * 4.5)
        self.play(Write(intersection_label))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    divider,
                    tuple_title,
                    set_title,
                    tuple_examples,
                    set_examples,
                    tuple_use_cases,
                    set_operations,
                    set_demo_title,
                    set_a,
                    set_b,
                    label_a,
                    label_b,
                    intersection,
                    intersection_label,
                )
            )
        )

    def control_flow_intro(self):
        """Introduction to control flow"""
        title = Text("Control Flow", font_size=48, color=BLUE)
        subtitle = Text(
            "Making Decisions & Repeating Actions", font_size=32, color=GREEN
        )

        title.to_edge(UP, buff=0.8)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Create flowchart visualization
        flowchart = VGroup()

        # Start
        start = Circle(radius=0.5, color=GREEN, fill_opacity=0.3)
        start_text = Text("Start", font_size=16, color=WHITE)
        start_text.move_to(start)
        start_group = VGroup(start, start_text)

        # Decision diamond
        decision = Polygon(
            UP * 0.6,
            RIGHT * 0.8,
            DOWN * 0.6,
            LEFT * 0.8,
            color=YELLOW,
            fill_opacity=0.3,
        )
        decision_text = Text("Condition?", font_size=14, color=WHITE)
        decision_text.move_to(decision)
        decision_group = VGroup(decision, decision_text)

        # Yes path
        yes_box = Rectangle(width=1.5, height=0.8, color=BLUE, fill_opacity=0.3)
        yes_text = Text("Action A", font_size=14, color=WHITE)
        yes_text.move_to(yes_box)
        yes_group = VGroup(yes_box, yes_text)

        # No path
        no_box = Rectangle(width=1.5, height=0.8, color=RED, fill_opacity=0.3)
        no_text = Text("Action B", font_size=14, color=WHITE)
        no_text.move_to(no_box)
        no_group = VGroup(no_box, no_text)

        # End
        end = Circle(radius=0.5, color=RED, fill_opacity=0.3)
        end_text = Text("End", font_size=16, color=WHITE)
        end_text.move_to(end)
        end_group = VGroup(end, end_text)

        # Arrange flowchart
        start_group.move_to(UP * 1)
        decision_group.next_to(start_group, DOWN, buff=1)
        yes_group.move_to(LEFT * 2 + DOWN * 1)
        no_group.move_to(RIGHT * 2 + DOWN * 1)
        end_group.move_to(DOWN * 2.5)

        flowchart.add(start_group, decision_group, yes_group, no_group, end_group)

        # Arrows
        arrows = VGroup(
            Arrow(start_group.get_bottom(), decision_group.get_top(), color=WHITE),
            Arrow(decision_group.get_left(), yes_group.get_top(), color=WHITE),
            Arrow(decision_group.get_right(), no_group.get_top(), color=WHITE),
            Arrow(yes_group.get_bottom(), end_group.get_left(), color=WHITE),
            Arrow(no_group.get_bottom(), end_group.get_right(), color=WHITE),
        )

        # Labels
        yes_label = Text("Yes", font_size=12, color=GREEN)
        no_label = Text("No", font_size=12, color=RED)
        yes_label.move_to(LEFT * 1 + UP * 0.3)
        no_label.move_to(RIGHT * 1 + UP * 0.3)

        self.play(Write(title), Write(subtitle))
        self.play(LaggedStartMap(FadeIn, flowchart, lag_ratio=0.3))
        self.play(LaggedStartMap(Create, arrows, lag_ratio=0.2))
        self.play(Write(yes_label), Write(no_label))

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, subtitle, flowchart, arrows, yes_label, no_label))
        )

    def conditional_statements(self):
        """Demonstrate if/elif/else statements"""
        title = Text("Conditional Statements", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create code editor mockup
        editor = Rectangle(
            width=10, height=6, color=BLACK, fill_opacity=0.9, stroke_color=GRAY
        )
        editor.move_to(DOWN * 0.5)

        # Code example
        code_lines = [
            "age = 18",
            "",
            "if age >= 18:",
            "    print('You can vote!')",
            "elif age >= 16:",
            "    print('You can drive!')",
            "else:",
            "    print('You are too young!')",
        ]

        code_objects = VGroup()
        for i, line in enumerate(code_lines):
            if (
                line.startswith("if")
                or line.startswith("elif")
                or line.startswith("else")
            ):
                line_text = Text(line, font_size=20, color=YELLOW)
            elif line.strip().startswith("print"):
                line_text = Text(line, font_size=20, color=GREEN)
            elif line.strip() == "":
                line_text = Text(line, font_size=20, color=WHITE)
            else:
                line_text = Text(line, font_size=20, color=WHITE)

            line_text.move_to(editor.get_top() + DOWN * (0.5 + i * 0.4))
            line_text.align_to(editor.get_left() + RIGHT * 0.5, LEFT)
            code_objects.add(line_text)

        self.play(Create(editor))

        # Type code line by line
        for line_obj in code_objects:
            self.play(Write(line_obj), run_time=0.8)

        # Show execution flow
        flow_title = Text("Execution Flow", font_size=24, color=YELLOW)
        flow_title.next_to(editor, RIGHT, buff=1)
        flow_title.align_to(editor.get_top(), UP)

        flow_steps = [
            "1. Check: age >= 18?",
            "2. 18 >= 18 → True",
            "3. Execute first block",
            "4. Skip elif and else",
            "5. Output: 'You can vote!'",
        ]

        flow_objects = VGroup()
        for step in flow_steps:
            step_text = Text(step, font_size=16, color=WHITE)
            flow_objects.add(step_text)

        flow_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        flow_objects.next_to(flow_title, DOWN, buff=0.5)

        self.play(Write(flow_title))
        self.play(LaggedStartMap(Write, flow_objects, lag_ratio=0.4))

        # Highlight the executed path
        executed_lines = [code_objects[0], code_objects[2], code_objects[3]]
        for line in executed_lines:
            self.play(line.animate.set_color(GREEN), run_time=0.5)
            self.wait(0.3)

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, editor, code_objects, flow_title, flow_objects))
        )

    def loops_demonstration(self):
        """Demonstrate for and while loops"""
        title = Text("Loops in Python", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # For loop demonstration
        for_title = Text("For Loops", font_size=32, color=GREEN)
        for_title.move_to(LEFT * 4 + UP * 1.5)

        # Create visual representation of list iteration
        items = ["apple", "banana", "cherry"]
        item_boxes = VGroup()

        for i, item in enumerate(items):
            box = Rectangle(width=1.5, height=0.8, color=YELLOW, stroke_width=2)
            text = Text(item, font_size=16, color=WHITE)
            text.move_to(box)
            item_group = VGroup(box, text)
            item_boxes.add(item_group)

        item_boxes.arrange(RIGHT, buff=0.2)
        item_boxes.next_to(for_title, DOWN, buff=0.5)

        # For loop code
        for_code = VGroup(
            Text("fruits = ['apple', 'banana', 'cherry']", font_size=16, color=WHITE),
            Text("for fruit in fruits:", font_size=16, color=YELLOW),
            Text("    print(f'I like {fruit}')", font_size=16, color=GREEN),
        )
        for_code.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        for_code.next_to(item_boxes, DOWN, buff=0.5)

        self.play(Write(for_title))
        self.play(LaggedStartMap(FadeIn, item_boxes, lag_ratio=0.3))
        self.play(LaggedStartMap(Write, for_code, lag_ratio=0.4))

        # Animate loop execution
        pointer = Arrow(UP * 0.5, DOWN * 0.2, color=RED)

        for i, box in enumerate(item_boxes):
            pointer.next_to(box, UP, buff=0.1)
            self.play(FadeIn(pointer), box.animate.set_color(RED), run_time=0.5)

            # Show output
            output = Text(f"I like {items[i]}", font_size=16, color=GREEN)
            output.next_to(for_code, DOWN, buff=0.5)
            self.play(Write(output), run_time=0.8)
            self.wait(0.5)
            self.play(FadeOut(output), box.animate.set_color(YELLOW), run_time=0.3)

        self.play(FadeOut(pointer))

        # While loop demonstration
        while_title = Text("While Loops", font_size=32, color=BLUE)
        while_title.move_to(RIGHT * 4 + UP * 1.5)

        while_code = VGroup(
            Text("count = 0", font_size=16, color=WHITE),
            Text("while count < 3:", font_size=16, color=YELLOW),
            Text("    print(f'Count: {count}')", font_size=16, color=GREEN),
            Text("    count += 1", font_size=16, color=WHITE),
        )
        while_code.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        while_code.next_to(while_title, DOWN, buff=0.5)

        # Counter visualization
        counter_display = VGroup()
        for i in range(4):
            counter_box = Circle(radius=0.3, color=BLUE if i < 3 else RED)
            counter_text = Text(str(i), font_size=16, color=WHITE)
            counter_text.move_to(counter_box)
            counter_group = VGroup(counter_box, counter_text)
            counter_display.add(counter_group)

        counter_display.arrange(RIGHT, buff=0.3)
        counter_display.next_to(while_code, DOWN, buff=0.5)

        self.play(Write(while_title))
        self.play(LaggedStartMap(Write, while_code, lag_ratio=0.4))

        # Animate while loop execution
        for i in range(3):
            # Highlight current counter
            self.play(counter_display[i].animate.set_color(GREEN), run_time=0.5)

            # Show condition check
            condition = Text(f"{i} < 3? True", font_size=16, color=GREEN)
            condition.next_to(counter_display, DOWN, buff=0.3)
            self.play(Write(condition), run_time=0.5)

            # Show output
            output = Text(f"Count: {i}", font_size=16, color=YELLOW)
            output.next_to(condition, DOWN, buff=0.2)
            self.play(Write(output), run_time=0.5)

            self.wait(0.5)
            self.play(FadeOut(VGroup(condition, output)), run_time=0.3)

        # Show final condition
        final_condition = Text("3 < 3? False - Loop ends", font_size=16, color=RED)
        final_condition.next_to(counter_display, DOWN, buff=0.3)
        self.play(counter_display[3].animate.set_color(RED), run_time=0.5)
        self.play(Write(final_condition), run_time=1)

        self.wait(2)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    for_title,
                    while_title,
                    item_boxes,
                    for_code,
                    while_code,
                    counter_display,
                    final_condition,
                )
            )
        )

    def list_comprehensions(self):
        """Demonstrate list comprehensions"""
        title = Text("List Comprehensions", font_size=48, color=BLUE)
        subtitle = Text("Elegant way to create lists", font_size=24, color=GREEN)

        title.to_edge(UP, buff=0.5)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), Write(subtitle))

        # Traditional vs comprehension comparison
        comparison_title = Text(
            "Traditional Loop vs List Comprehension", font_size=28, color=YELLOW
        )
        comparison_title.move_to(UP * 1.5)

        # Traditional way
        traditional_title = Text("Traditional Way", font_size=24, color=RED)
        traditional_title.move_to(LEFT * 3 + UP * 0.5)

        traditional_code = VGroup(
            Text("squares = []", font_size=18, color=WHITE),
            Text("for x in range(5):", font_size=18, color=YELLOW),
            Text("    squares.append(x ** 2)", font_size=18, color=GREEN),
            Text("# Result: [0, 1, 4, 9, 16]", font_size=16, color=BLUE),
        )
        traditional_code.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        traditional_code.next_to(traditional_title, DOWN, buff=0.3)

        # List comprehension way
        comprehension_title = Text("List Comprehension", font_size=24, color=GREEN)
        comprehension_title.move_to(RIGHT * 3 + UP * 0.5)

        comprehension_code = VGroup(
            Text("squares = [x**2 for x in range(5)]", font_size=18, color=YELLOW),
            Text("# Same result in one line!", font_size=16, color=GREEN),
            Text("# Result: [0, 1, 4, 9, 16]", font_size=16, color=BLUE),
        )
        comprehension_code.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        comprehension_code.next_to(comprehension_title, DOWN, buff=0.3)

        self.play(Write(comparison_title))
        self.play(Write(traditional_title), Write(comprehension_title))
        self.play(LaggedStartMap(Write, traditional_code, lag_ratio=0.4))
        self.play(LaggedStartMap(Write, comprehension_code, lag_ratio=0.4))

        # Highlight the efficiency
        efficiency_note = Text(
            "✓ More concise  ✓ Often faster  ✓ More Pythonic", font_size=20, color=GREEN
        )
        efficiency_note.next_to(comprehension_code, DOWN, buff=0.5)
        self.play(Write(efficiency_note))

        self.wait(2)
        self.play(
            FadeOut(
                VGroup(
                    comparison_title,
                    traditional_title,
                    comprehension_title,
                    traditional_code,
                    comprehension_code,
                    efficiency_note,
                )
            )
        )

        # More comprehension examples
        examples_title = Text(
            "More List Comprehension Examples", font_size=32, color=BLUE
        )
        examples_title.move_to(UP * 1.5)

        examples = [
            ("Even numbers", "[x for x in range(10) if x % 2 == 0]", "[0, 2, 4, 6, 8]"),
            ("Word lengths", "[len(word) for word in ['hello', 'world']]", "[5, 5]"),
            (
                "Nested lists",
                "[[x*y for x in range(3)] for y in range(3)]",
                "[[0,0,0], [0,1,2], [0,2,4]]",
            ),
        ]

        self.play(Write(examples_title))

        for desc, code, result in examples:
            desc_text = Text(desc, font_size=20, color=YELLOW)
            code_text = Text(code, font_size=18, color=WHITE)
            result_text = Text(f"→ {result}", font_size=16, color=GREEN)

            desc_text.next_to(examples_title, DOWN, buff=1)
            code_text.next_to(desc_text, DOWN, buff=0.3)
            result_text.next_to(code_text, DOWN, buff=0.2)

            self.play(Write(desc_text), run_time=0.8)
            self.play(Write(code_text), run_time=1)
            self.play(Write(result_text), run_time=0.8)
            self.wait(1)
            self.play(FadeOut(VGroup(desc_text, code_text, result_text)), run_time=0.5)

        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle, examples_title)))

    def module_conclusion(self):
        """Conclusion for Module 4"""
        title = Text("Module 4 Complete!", font_size=56, color=GREEN)
        title.move_to(UP * 1.5)

        # Summary of what was learned
        summary = VGroup(
            Text(
                "✓ Master Python data types (int, float, str, bool)",
                font_size=24,
                color=WHITE,
            ),
            Text(
                "✓ Work with collections (list, dict, tuple, set)",
                font_size=24,
                color=WHITE,
            ),
            Text(
                "✓ Use conditional statements (if/elif/else)", font_size=24, color=WHITE
            ),
            Text(
                "✓ Create loops (for/while) for repetition", font_size=24, color=WHITE
            ),
            Text("✓ Write elegant list comprehensions", font_size=24, color=WHITE),
        )
        summary.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=0.8)

        # Next module preview
        next_module = Text("Next: Functions & Modules", font_size=32, color=YELLOW)
        next_module.next_to(summary, DOWN, buff=1)

        # Create data structure celebration
        celebration_icons = VGroup()

        # Create floating data type icons
        for i in range(15):
            icon_type = random.choice(["number", "string", "list", "dict"])

            if icon_type == "number":
                icon = Circle(radius=0.2, color=BLUE, fill_opacity=0.8)
                text = Text(str(random.randint(1, 99)), font_size=12, color=WHITE)
            elif icon_type == "string":
                icon = RoundedRectangle(
                    width=0.8,
                    height=0.4,
                    corner_radius=0.05,
                    color=GREEN,
                    fill_opacity=0.8,
                )
                text = Text('"abc"', font_size=10, color=WHITE)
            elif icon_type == "list":
                icon = Rectangle(width=0.6, height=0.4, color=YELLOW, fill_opacity=0.8)
                text = Text("[]", font_size=12, color=WHITE)
            else:  # dict
                icon = RoundedRectangle(
                    width=0.6,
                    height=0.5,
                    corner_radius=0.05,
                    color=RED,
                    fill_opacity=0.8,
                )
                text = Text("{}", font_size=12, color=WHITE)

            text.move_to(icon)
            icon_group = VGroup(icon, text)
            icon_group.move_to(
                np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-3, 3) * UP
            )
            celebration_icons.add(icon_group)

        # Animate conclusion
        self.play(Write(title), run_time=2)
        self.play(LaggedStartMap(FadeIn, summary, lag_ratio=0.2), run_time=3)
        self.play(Write(next_module), run_time=2)

        # Add celebration icons
        self.play(LaggedStartMap(FadeIn, celebration_icons, lag_ratio=0.1), run_time=2)

        # Make icons float and rotate
        self.play(
            *[
                icon.animate.shift(UP * np.random.uniform(0.5, 2)).rotate(
                    np.random.uniform(-PI, PI)
                )
                for icon in celebration_icons
            ],
            run_time=3,
        )

        self.wait(2)


# Main execution
if __name__ == "__main__":
    # This allows the file to be run directly
    pass
