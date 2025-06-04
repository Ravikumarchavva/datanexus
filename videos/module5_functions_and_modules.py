from manimlib import *
import numpy as np
import random


class Module5FunctionsAndModules(Scene):
    def construct(self):
        """Module 5: Functions & Modules (45 min)"""
        self.camera.background_color = "#0f0f23"

        # Module introduction
        self.module_intro()

        # Functions
        self.function_basics()
        self.function_parameters()
        self.return_values()
        self.scope_and_lifetime()
        self.built_in_vs_user_defined()

        # Modules and packages
        self.modules_introduction()
        self.import_statements()
        self.creating_modules()
        self.packages_overview()

        # Module conclusion
        self.module_conclusion()

    def module_intro(self):
        """Introduction to Module 5"""
        title = Text("Module 5", font_size=64, color=BLUE)
        subtitle = Text("Functions & Modules", font_size=48, color=GREEN)
        description = Text("Organize • Reuse • Structure", font_size=32, color=YELLOW)

        title.to_edge(UP, buff=1)
        subtitle.next_to(title, DOWN, buff=0.5)
        description.next_to(subtitle, DOWN, buff=0.8)

        # Create function visualization
        function_box = RoundedRectangle(
            width=4, height=2, corner_radius=0.2, color=BLUE, stroke_width=3
        )
        function_title = Text("Function", font_size=24, color=WHITE)
        function_title.move_to(function_box.get_top() + DOWN * 0.3)

        # Input arrow
        input_arrow = Arrow(LEFT * 2, LEFT * 0.2, color=GREEN, stroke_width=4)
        input_label = Text("Input", font_size=18, color=GREEN)
        input_label.next_to(input_arrow, UP, buff=0.2)

        # Output arrow
        output_arrow = Arrow(RIGHT * 0.2, RIGHT * 2, color=RED, stroke_width=4)
        output_label = Text("Output", font_size=18, color=RED)
        output_label.next_to(output_arrow, UP, buff=0.2)

        # Process text
        process_text = Text("Process", font_size=20, color=YELLOW)
        process_text.move_to(function_box)

        function_diagram = VGroup(
            function_box,
            function_title,
            input_arrow,
            input_label,
            output_arrow,
            output_label,
            process_text,
        )
        function_diagram.next_to(description, DOWN, buff=1.5)

        # Animate introduction
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(Write(description), run_time=1.5)

        # Build function diagram
        self.play(Create(function_box), Write(function_title))
        self.play(Write(process_text))
        self.play(Create(input_arrow), Write(input_label))
        self.play(Create(output_arrow), Write(output_label))

        # Animate data flow
        data_point = Dot(color=GREEN, radius=0.1)
        data_point.move_to(input_arrow.get_start())

        self.play(FadeIn(data_point))
        self.play(data_point.animate.move_to(function_box.get_center()), run_time=1.5)
        self.play(data_point.animate.set_color(RED), run_time=0.5)
        self.play(data_point.animate.move_to(output_arrow.get_end()), run_time=1.5)
        self.play(FadeOut(data_point))

        self.wait(2)
        self.play(FadeOut(VGroup(title, subtitle, description, function_diagram)))

    def function_basics(self):
        """Basic function concepts"""
        title = Text("What are Functions?", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Function definition
        definition = Text(
            "A function is a reusable block of code that performs a specific task",
            font_size=24,
            color=WHITE,
        )
        definition.next_to(title, DOWN, buff=0.8)

        # Benefits of functions
        benefits_title = Text("Why Use Functions?", font_size=32, color=GREEN)
        benefits_title.next_to(definition, DOWN, buff=1)

        benefits = [
            "🔄 Reusability - Write once, use many times",
            "📦 Organization - Keep code clean and structured",
            "🐛 Debugging - Easier to find and fix problems",
            "🧪 Testing - Test individual pieces separately",
            "👥 Collaboration - Team members can work on different functions",
        ]

        benefit_objects = VGroup()
        for benefit in benefits:
            benefit_text = Text(benefit, font_size=20, color=WHITE)
            benefit_objects.add(benefit_text)

        benefit_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        benefit_objects.next_to(benefits_title, DOWN, buff=0.5)

        self.play(Write(definition))
        self.play(Write(benefits_title))
        self.play(LaggedStartMap(FadeIn, benefit_objects, lag_ratio=0.3))

        # Simple function example
        example_title = Text("Simple Function Example", font_size=28, color=YELLOW)
        example_title.next_to(benefit_objects, DOWN, buff=1)

        # Code editor mockup
        editor = Rectangle(
            width=8, height=2.5, color=BLACK, fill_opacity=0.9, stroke_color=GRAY
        )
        editor.next_to(example_title, DOWN, buff=0.5)

        code_lines = [
            "def greet(name):",
            "    return f'Hello, {name}!'",
            "",
            "message = greet('Alice')",
            "print(message)  # Output: Hello, Alice!",
        ]

        code_objects = VGroup()
        for i, line in enumerate(code_lines):
            if line.startswith("def"):
                line_text = Text(line, font_size=18, color=YELLOW)
            elif "return" in line:
                line_text = Text(line, font_size=18, color=GREEN)
            elif line.strip().startswith("#"):
                line_text = Text(line, font_size=16, color=BLUE)
            else:
                line_text = Text(line, font_size=18, color=WHITE)

            line_text.move_to(editor.get_top() + DOWN * (0.3 + i * 0.35))
            line_text.align_to(editor.get_left() + RIGHT * 0.3, LEFT)
            code_objects.add(line_text)

        self.play(Write(example_title))
        self.play(Create(editor))
        self.play(LaggedStartMap(Write, code_objects, lag_ratio=0.4))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    definition,
                    benefits_title,
                    benefit_objects,
                    example_title,
                    editor,
                    code_objects,
                )
            )
        )

    def function_parameters(self):
        """Function parameters and arguments"""
        title = Text("Function Parameters", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Parameter types overview
        param_types = [
            ("Positional", "def greet(name, age):", "greet('Alice', 25)"),
            ("Keyword", "def greet(name, age=18):", "greet(name='Bob', age=30)"),
            ("Default", "def greet(name='User'):", "greet()  # Uses default"),
            ("*args", "def sum_all(*numbers):", "sum_all(1, 2, 3, 4)"),
            ("**kwargs", "def info(**data):", "info(name='Alice', age=25)"),
        ]

        # Create comparison table
        for i, (param_type, definition, usage) in enumerate(param_types):
            # Type label
            type_label = Text(param_type, font_size=24, color=YELLOW)
            type_label.move_to(LEFT * 5 + UP * (1.5 - i * 0.8))

            # Definition
            def_text = Text(definition, font_size=18, color=GREEN)
            def_text.next_to(type_label, RIGHT, buff=1)

            # Usage example
            usage_text = Text(usage, font_size=18, color=WHITE)
            usage_text.next_to(def_text, RIGHT, buff=1)

            # Animate each row
            self.play(Write(type_label), run_time=0.8)
            self.play(Write(def_text), run_time=1)
            self.play(Write(usage_text), run_time=1)
            self.wait(0.5)

        # Detailed example
        detail_title = Text("Detailed Example", font_size=32, color=RED)
        detail_title.move_to(DOWN * 2)

        # Advanced function example
        editor = Rectangle(
            width=10, height=3, color=BLACK, fill_opacity=0.9, stroke_color=GRAY
        )
        editor.next_to(detail_title, DOWN, buff=0.5)

        advanced_code = [
            "def create_profile(name, age, *hobbies, **details):",
            "    profile = f'{name}, {age} years old'",
            "    if hobbies:",
            "        profile += f', hobbies: {', '.join(hobbies)}'",
            "    for key, value in details.items():",
            "        profile += f', {key}: {value}'",
            "    return profile",
        ]

        code_objects = VGroup()
        for i, line in enumerate(advanced_code):
            if line.startswith("def"):
                line_text = Text(line, font_size=16, color=YELLOW)
            elif "return" in line:
                line_text = Text(line, font_size=16, color=GREEN)
            elif line.strip().startswith("for") or line.strip().startswith("if"):
                line_text = Text(line, font_size=16, color=BLUE)
            else:
                line_text = Text(line, font_size=16, color=WHITE)

            line_text.move_to(editor.get_top() + DOWN * (0.3 + i * 0.3))
            line_text.align_to(editor.get_left() + RIGHT * 0.2, LEFT)
            code_objects.add(line_text)

        self.play(Write(detail_title))
        self.play(Create(editor))
        self.play(LaggedStartMap(Write, code_objects, lag_ratio=0.3))

        # Show usage example
        usage_example = Text(
            "create_profile('Alice', 25, 'reading', 'coding', city='NYC', job='Developer')",
            font_size=16,
            color=YELLOW,
        )
        usage_example.next_to(editor, DOWN, buff=0.3)

        result = Text(
            "→ 'Alice, 25 years old, hobbies: reading, coding, city: NYC, job: Developer'",
            font_size=14,
            color=GREEN,
        )
        result.next_to(usage_example, DOWN, buff=0.2)

        self.play(Write(usage_example))
        self.play(Write(result))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(title, detail_title, editor, code_objects, usage_example, result)
            )
        )

    def return_values(self):
        """Function return values"""
        title = Text("Return Values", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Return concepts
        concepts = [
            ("Single Value", "return 42", "Returns one value"),
            ("Multiple Values", "return x, y, z", "Returns tuple of values"),
            ("No Return", "print('Hello')", "Returns None implicitly"),
            (
                "Conditional Return",
                "return x if x > 0 else 0",
                "Different values based on condition",
            ),
        ]

        for i, (concept, example, description) in enumerate(concepts):
            concept_title = Text(concept, font_size=24, color=YELLOW)
            example_code = Text(example, font_size=20, color=GREEN)
            desc_text = Text(description, font_size=18, color=WHITE)

            concept_title.move_to(UP * (1.5 - i * 1))
            example_code.next_to(concept_title, RIGHT, buff=1)
            desc_text.next_to(example_code, RIGHT, buff=1)

            self.play(Write(concept_title), run_time=0.8)
            self.play(Write(example_code), run_time=0.8)
            self.play(Write(desc_text), run_time=0.8)
            self.wait(0.5)

        # Interactive example
        interactive_title = Text("Interactive Example", font_size=28, color=RED)
        interactive_title.move_to(DOWN * 2.5)

        # Calculator function
        calc_editor = Rectangle(
            width=8, height=2, color=BLACK, fill_opacity=0.9, stroke_color=GRAY
        )
        calc_editor.next_to(interactive_title, DOWN, buff=0.5)

        calc_code = [
            "def calculate(a, b, operation):",
            "    if operation == 'add':",
            "        return a + b",
            "    elif operation == 'multiply':",
            "        return a * b",
            "    else:",
            "        return 'Unknown operation'",
        ]

        calc_objects = VGroup()
        for i, line in enumerate(calc_code):
            if line.startswith("def"):
                line_text = Text(line, font_size=16, color=YELLOW)
            elif "return" in line:
                line_text = Text(line, font_size=16, color=GREEN)
            elif line.strip().startswith(("if", "elif", "else")):
                line_text = Text(line, font_size=16, color=BLUE)
            else:
                line_text = Text(line, font_size=16, color=WHITE)

            line_text.move_to(calc_editor.get_top() + DOWN * (0.2 + i * 0.22))
            line_text.align_to(calc_editor.get_left() + RIGHT * 0.2, LEFT)
            calc_objects.add(line_text)

        self.play(Write(interactive_title))
        self.play(Create(calc_editor))
        self.play(LaggedStartMap(Write, calc_objects, lag_ratio=0.3))

        # Test the function
        test_cases = [
            ("calculate(5, 3, 'add')", "8"),
            ("calculate(4, 7, 'multiply')", "28"),
            ("calculate(2, 6, 'divide')", "'Unknown operation'"),
        ]

        for test_input, expected in test_cases:
            test_text = Text(test_input, font_size=16, color=WHITE)
            result_text = Text(f"→ {expected}", font_size=16, color=GREEN)

            test_text.next_to(calc_editor, DOWN, buff=0.5)
            result_text.next_to(test_text, RIGHT, buff=0.5)

            self.play(Write(test_text), run_time=1)
            self.play(Write(result_text), run_time=0.8)
            self.wait(0.8)
            self.play(FadeOut(VGroup(test_text, result_text)), run_time=0.3)

        self.wait(2)
        self.play(FadeOut(VGroup(title, interactive_title, calc_editor, calc_objects)))

    def scope_and_lifetime(self):
        """Variable scope and lifetime"""
        title = Text("Scope & Variable Lifetime", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Scope visualization
        global_box = Rectangle(width=10, height=6, color=BLUE, stroke_width=2)
        global_label = Text("Global Scope", font_size=20, color=BLUE)
        global_label.move_to(global_box.get_top() + DOWN * 0.3)

        function_box = Rectangle(width=6, height=3, color=GREEN, stroke_width=2)
        function_box.move_to(global_box.get_center() + DOWN * 0.5)
        function_label = Text("Function Scope (Local)", font_size=16, color=GREEN)
        function_label.move_to(function_box.get_top() + DOWN * 0.2)

        self.play(Create(global_box), Write(global_label))
        self.play(Create(function_box), Write(function_label))

        # Code example with scope
        scope_code = [
            "global_var = 'I am global'  # Global scope",
            "",
            "def my_function():",
            "    local_var = 'I am local'  # Function scope",
            "    print(global_var)  # Can access global",
            "    print(local_var)   # Can access local",
            "    return local_var",
            "",
            "print(global_var)  # ✓ Works",
            "print(local_var)   # ✗ Error! Not accessible",
        ]

        code_objects = VGroup()
        for i, line in enumerate(scope_code):
            if "global" in line and not line.strip().startswith("#"):
                line_text = Text(line, font_size=14, color=BLUE)
            elif "local" in line and not line.strip().startswith("#"):
                line_text = Text(line, font_size=14, color=GREEN)
            elif line.strip().startswith("#"):
                line_text = Text(line, font_size=12, color=YELLOW)
            elif line.startswith("def"):
                line_text = Text(line, font_size=14, color=YELLOW)
            elif "✗" in line:
                line_text = Text(line, font_size=14, color=RED)
            elif "✓" in line:
                line_text = Text(line, font_size=14, color=GREEN)
            else:
                line_text = Text(line, font_size=14, color=WHITE)

            # Position based on scope
            if i < 2 or i >= 7:  # Global scope lines
                line_text.move_to(
                    global_box.get_left() + RIGHT * 0.5 + UP * (2.5 - i * 0.3)
                )
            else:  # Function scope lines
                line_text.move_to(
                    function_box.get_left() + RIGHT * 0.3 + UP * (1.5 - (i - 2) * 0.3)
                )

            line_text.align_to(global_box.get_left() + RIGHT * 0.3, LEFT)
            code_objects.add(line_text)

        self.play(LaggedStartMap(Write, code_objects, lag_ratio=0.2))

        # Highlight scope access
        access_note = Text(
            "Functions can read global variables but need 'global' keyword to modify them",
            font_size=16,
            color=YELLOW,
        )
        access_note.next_to(global_box, DOWN, buff=0.5)
        self.play(Write(access_note))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    global_box,
                    global_label,
                    function_box,
                    function_label,
                    code_objects,
                    access_note,
                )
            )
        )

    def built_in_vs_user_defined(self):
        """Built-in vs user-defined functions"""
        title = Text("Built-in vs User-Defined Functions", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Split screen comparison
        divider = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=2)

        # Built-in functions
        builtin_title = Text("Built-in Functions", font_size=32, color=GREEN)
        builtin_title.move_to(LEFT * 3.5 + UP * 2)

        builtin_desc = Text(
            "Ready to use, provided by Python", font_size=18, color=WHITE
        )
        builtin_desc.next_to(builtin_title, DOWN, buff=0.3)

        builtin_examples = [
            ("len()", "Get length of sequence"),
            ("print()", "Display output"),
            ("input()", "Get user input"),
            ("max()", "Find maximum value"),
            ("min()", "Find minimum value"),
            ("sum()", "Add all numbers"),
            ("type()", "Get data type"),
            ("range()", "Generate number sequence"),
        ]

        builtin_objects = VGroup()
        for func, desc in builtin_examples:
            func_text = Text(func, font_size=16, color=YELLOW)
            desc_text = Text(desc, font_size=14, color=WHITE)

            func_group = VGroup(func_text, desc_text)
            func_group.arrange(RIGHT, buff=0.5)
            builtin_objects.add(func_group)

        builtin_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        builtin_objects.next_to(builtin_desc, DOWN, buff=0.5)

        # User-defined functions
        userdef_title = Text("User-Defined Functions", font_size=32, color=BLUE)
        userdef_title.move_to(RIGHT * 3.5 + UP * 2)

        userdef_desc = Text(
            "Created by you for specific needs", font_size=18, color=WHITE
        )
        userdef_desc.next_to(userdef_title, DOWN, buff=0.3)

        userdef_example = Rectangle(
            width=5, height=3, color=BLACK, fill_opacity=0.9, stroke_color=GRAY
        )
        userdef_example.next_to(userdef_desc, DOWN, buff=0.5)

        userdef_code = [
            "def calculate_area(length, width):",
            '    """Calculate rectangle area"""',
            "    return length * width",
            "",
            "def greet_user(name, time='day'):",
            '    """Greet user with time"""',
            "    return f'Good {time}, {name}!'",
            "",
            "# Usage:",
            "area = calculate_area(5, 3)",
            "greeting = greet_user('Alice', 'morning')",
        ]

        userdef_objects = VGroup()
        for i, line in enumerate(userdef_code):
            if line.startswith("def"):
                line_text = Text(line, font_size=12, color=YELLOW)
            elif line.strip().startswith('"""') or line.strip().endswith('"""'):
                line_text = Text(line, font_size=10, color=GREEN)
            elif line.strip().startswith("#"):
                line_text = Text(line, font_size=10, color=BLUE)
            elif "return" in line:
                line_text = Text(line, font_size=12, color=GREEN)
            else:
                line_text = Text(line, font_size=12, color=WHITE)

            line_text.move_to(userdef_example.get_top() + DOWN * (0.2 + i * 0.22))
            line_text.align_to(userdef_example.get_left() + RIGHT * 0.1, LEFT)
            userdef_objects.add(line_text)

        # Animate everything
        self.play(Create(divider))
        self.play(Write(builtin_title), Write(userdef_title))
        self.play(Write(builtin_desc), Write(userdef_desc))
        self.play(LaggedStartMap(FadeIn, builtin_objects, lag_ratio=0.1))
        self.play(Create(userdef_example))
        self.play(LaggedStartMap(Write, userdef_objects, lag_ratio=0.2))

        # Key differences
        differences_title = Text("Key Differences", font_size=24, color=RED)
        differences_title.move_to(DOWN * 2.8)

        differences = VGroup(
            Text(
                "Built-in: Immediate use, optimized, limited to Python's design",
                font_size=16,
                color=GREEN,
            ),
            Text(
                "User-defined: Custom logic, specific to your problem, unlimited possibilities",
                font_size=16,
                color=BLUE,
            ),
        )
        differences.arrange(DOWN, buff=0.2)
        differences.next_to(differences_title, DOWN, buff=0.3)

        self.play(Write(differences_title))
        self.play(LaggedStartMap(Write, differences, lag_ratio=0.5))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    divider,
                    builtin_title,
                    userdef_title,
                    builtin_desc,
                    userdef_desc,
                    builtin_objects,
                    userdef_example,
                    userdef_objects,
                    differences_title,
                    differences,
                )
            )
        )

    def modules_introduction(self):
        """Introduction to modules"""
        title = Text("Python Modules", font_size=48, color=BLUE)
        subtitle = Text("Organize code into reusable files", font_size=24, color=GREEN)

        title.to_edge(UP, buff=0.5)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), Write(subtitle))

        # Module concept visualization
        # Main file
        main_file = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.2)
        main_title = Text("main.py", font_size=18, color=WHITE)
        main_title.move_to(main_file.get_top() + DOWN * 0.3)
        main_content = VGroup(
            Text("import math_utils", font_size=12, color=YELLOW),
            Text("import string_utils", font_size=12, color=YELLOW),
            Text("", font_size=12, color=WHITE),
            Text("result = math_utils.add(5, 3)", font_size=11, color=WHITE),
            Text("clean = string_utils.clean('text')", font_size=11, color=WHITE),
        )
        main_content.arrange(DOWN, buff=0.1)
        main_content.move_to(main_file.get_center() + DOWN * 0.2)
        main_group = VGroup(main_file, main_title, main_content)

        # Math utils module
        math_file = Rectangle(width=2.5, height=2, color=GREEN, fill_opacity=0.2)
        math_title = Text("math_utils.py", font_size=16, color=WHITE)
        math_title.move_to(math_file.get_top() + DOWN * 0.3)
        math_content = VGroup(
            Text("def add(a, b):", font_size=11, color=YELLOW),
            Text("    return a + b", font_size=11, color=WHITE),
            Text("", font_size=11, color=WHITE),
            Text("def multiply(a, b):", font_size=11, color=YELLOW),
            Text("    return a * b", font_size=11, color=WHITE),
        )
        math_content.arrange(DOWN, buff=0.1)
        math_content.move_to(math_file.get_center() + DOWN * 0.1)
        math_group = VGroup(math_file, math_title, math_content)

        # String utils module
        string_file = Rectangle(width=2.5, height=2, color=RED, fill_opacity=0.2)
        string_title = Text("string_utils.py", font_size=16, color=WHITE)
        string_title.move_to(string_file.get_top() + DOWN * 0.3)
        string_content = VGroup(
            Text("def clean(text):", font_size=11, color=YELLOW),
            Text("    return text.strip()", font_size=11, color=WHITE),
            Text("", font_size=11, color=WHITE),
            Text("def uppercase(text):", font_size=11, color=YELLOW),
            Text("    return text.upper()", font_size=11, color=WHITE),
        )
        string_content.arrange(DOWN, buff=0.1)
        string_content.move_to(string_file.get_center() + DOWN * 0.1)
        string_group = VGroup(string_file, string_title, string_content)

        # Arrange modules
        main_group.move_to(LEFT * 3.5 + DOWN * 0.5)
        math_group.move_to(RIGHT * 1.5 + UP * 1)
        string_group.move_to(RIGHT * 1.5 + DOWN * 2)

        # Connection arrows
        arrow1 = Arrow(main_group.get_right(), math_group.get_left(), color=GREEN)
        arrow2 = Arrow(main_group.get_right(), string_group.get_left(), color=RED)

        # Animate module creation
        self.play(FadeIn(main_group))
        self.play(FadeIn(math_group), Create(arrow1))
        self.play(FadeIn(string_group), Create(arrow2))

        # Benefits of modules
        benefits_title = Text("Benefits of Modules", font_size=28, color=YELLOW)
        benefits_title.move_to(DOWN * 3.5)

        benefits = VGroup(
            Text("• Code Reusability", font_size=16, color=WHITE),
            Text("• Better Organization", font_size=16, color=WHITE),
            Text("• Easier Maintenance", font_size=16, color=WHITE),
            Text("• Team Collaboration", font_size=16, color=WHITE),
        )
        benefits.arrange(RIGHT, buff=1)
        benefits.next_to(benefits_title, DOWN, buff=0.3)

        self.play(Write(benefits_title))
        self.play(LaggedStartMap(FadeIn, benefits, lag_ratio=0.3))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    subtitle,
                    main_group,
                    math_group,
                    string_group,
                    arrow1,
                    arrow2,
                    benefits_title,
                    benefits,
                )
            )
        )

    def import_statements(self):
        """Different ways to import modules"""
        title = Text("Import Statements", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Import methods
        import_methods = [
            ("import math", "Import entire module", "math.sqrt(16)"),
            ("import math as m", "Import with alias", "m.sqrt(16)"),
            ("from math import sqrt", "Import specific function", "sqrt(16)"),
            (
                "from math import sqrt, cos",
                "Import multiple functions",
                "sqrt(16), cos(0)",
            ),
            (
                "from math import *",
                "Import everything (not recommended)",
                "sqrt(16), cos(0)",
            ),
        ]

        for i, (syntax, description, usage) in enumerate(import_methods):
            # Method number
            number = Text(f"{i + 1}.", font_size=24, color=YELLOW)
            number.move_to(LEFT * 5 + UP * (2 - i * 0.8))

            # Import syntax
            syntax_text = Text(syntax, font_size=20, color=GREEN)
            syntax_text.next_to(number, RIGHT, buff=0.3)

            # Description
            desc_text = Text(description, font_size=16, color=WHITE)
            desc_text.next_to(syntax_text, RIGHT, buff=0.8)

            # Usage example
            usage_text = Text(usage, font_size=16, color=BLUE)
            usage_text.next_to(desc_text, DOWN, buff=0.1)
            usage_text.align_to(desc_text, LEFT)

            # Animate each import method
            self.play(Write(number), run_time=0.5)
            self.play(Write(syntax_text), run_time=0.8)
            self.play(Write(desc_text), run_time=0.8)
            self.play(Write(usage_text), run_time=0.8)
            self.wait(0.5)

        # Common modules showcase
        common_title = Text("Popular Python Modules", font_size=28, color=RED)
        common_title.move_to(DOWN * 2.5)

        modules = [
            ("math", "Mathematical functions"),
            ("random", "Random number generation"),
            ("datetime", "Date and time handling"),
            ("os", "Operating system interface"),
            ("json", "JSON data handling"),
            ("requests", "HTTP requests (external)"),
        ]

        module_objects = VGroup()
        for module, desc in modules:
            module_text = Text(module, font_size=16, color=YELLOW)
            desc_text = Text(f"- {desc}", font_size=14, color=WHITE)

            module_group = VGroup(module_text, desc_text)
            module_group.arrange(RIGHT, buff=0.3)
            module_objects.add(module_group)

        module_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        module_objects.next_to(common_title, DOWN, buff=0.5)

        self.play(Write(common_title))
        self.play(LaggedStartMap(FadeIn, module_objects, lag_ratio=0.2))

        # Import best practices
        practices_title = Text("Import Best Practices", font_size=24, color=GREEN)
        practices_title.next_to(module_objects, DOWN, buff=0.8)

        practices = VGroup(
            Text("✓ Import at the top of the file", font_size=14, color=GREEN),
            Text("✓ Use specific imports when possible", font_size=14, color=GREEN),
            Text("✗ Avoid 'from module import *'", font_size=14, color=RED),
            Text(
                "✓ Group imports: standard library, third-party, local",
                font_size=14,
                color=GREEN,
            ),
        )
        practices.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        practices.next_to(practices_title, DOWN, buff=0.3)

        self.play(Write(practices_title))
        self.play(LaggedStartMap(FadeIn, practices, lag_ratio=0.3))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(title, common_title, module_objects, practices_title, practices)
            )
        )

    def creating_modules(self):
        """How to create your own modules"""
        title = Text("Creating Your Own Modules", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Step-by-step module creation
        steps_title = Text("Step-by-Step Module Creation", font_size=32, color=GREEN)
        steps_title.move_to(UP * 1.5)

        # Step 1: Create file
        step1_title = Text("Step 1: Create a .py file", font_size=24, color=YELLOW)
        step1_title.move_to(LEFT * 4.5 + UP * 0.5)

        # calculator.py file
        calc_file = Rectangle(
            width=4, height=3, color=BLACK, fill_opacity=0.9, stroke_color=GREEN
        )
        calc_file.next_to(step1_title, DOWN, buff=0.3)

        calc_filename = Text("calculator.py", font_size=16, color=GREEN)
        calc_filename.next_to(calc_file, UP, buff=0.1)

        calc_content = [
            '"""Simple calculator module"""',
            "",
            "def add(a, b):",
            "    return a + b",
            "",
            "def subtract(a, b):",
            "    return a - b",
            "",
            "def multiply(a, b):",
            "    return a * b",
            "",
            "PI = 3.14159",
        ]

        calc_objects = VGroup()
        for i, line in enumerate(calc_content):
            if line.startswith('"""') or line.endswith('"""'):
                line_text = Text(line, font_size=12, color=GREEN)
            elif line.startswith("def"):
                line_text = Text(line, font_size=12, color=YELLOW)
            elif "return" in line:
                line_text = Text(line, font_size=12, color=BLUE)
            elif line.isupper():
                line_text = Text(line, font_size=12, color=RED)
            else:
                line_text = Text(line, font_size=12, color=WHITE)

            line_text.move_to(calc_file.get_top() + DOWN * (0.2 + i * 0.2))
            line_text.align_to(calc_file.get_left() + RIGHT * 0.1, LEFT)
            calc_objects.add(line_text)

        # Step 2: Import and use
        step2_title = Text("Step 2: Import and use", font_size=24, color=YELLOW)
        step2_title.move_to(RIGHT * 4.5 + UP * 0.5)

        # main.py file
        main_file = Rectangle(
            width=4, height=3, color=BLACK, fill_opacity=0.9, stroke_color=BLUE
        )
        main_file.next_to(step2_title, DOWN, buff=0.3)

        main_filename = Text("main.py", font_size=16, color=BLUE)
        main_filename.next_to(main_file, UP, buff=0.1)

        main_content = [
            "import calculator",
            "",
            "# Use functions from module",
            "result1 = calculator.add(5, 3)",
            "result2 = calculator.multiply(4, 7)",
            "",
            "print(f'5 + 3 = {result1}')",
            "print(f'4 × 7 = {result2}')",
            "",
            "# Use module variable",
            "print(f'PI = {calculator.PI}')",
        ]

        main_objects = VGroup()
        for i, line in enumerate(main_content):
            if line.startswith("import"):
                line_text = Text(line, font_size=12, color=YELLOW)
            elif line.strip().startswith("#"):
                line_text = Text(line, font_size=10, color=GREEN)
            elif "calculator." in line:
                line_text = Text(line, font_size=11, color=BLUE)
            else:
                line_text = Text(line, font_size=12, color=WHITE)

            line_text.move_to(main_file.get_top() + DOWN * (0.2 + i * 0.2))
            line_text.align_to(main_file.get_left() + RIGHT * 0.1, LEFT)
            main_objects.add(line_text)

        self.play(Write(steps_title))

        # Animate step 1
        self.play(Write(step1_title))
        self.play(Create(calc_file), Write(calc_filename))
        self.play(LaggedStartMap(Write, calc_objects, lag_ratio=0.1))

        # Animate step 2
        self.play(Write(step2_title))
        self.play(Create(main_file), Write(main_filename))
        self.play(LaggedStartMap(Write, main_objects, lag_ratio=0.1))

        # Show output
        output_title = Text("Output:", font_size=20, color=GREEN)
        output_title.move_to(DOWN * 1.8)

        output_lines = ["5 + 3 = 8", "4 × 7 = 28", "PI = 3.14159"]

        output_objects = VGroup()
        for line in output_lines:
            output_text = Text(line, font_size=16, color=WHITE)
            output_objects.add(output_text)

        output_objects.arrange(DOWN, buff=0.2)
        output_objects.next_to(output_title, DOWN, buff=0.3)

        self.play(Write(output_title))
        self.play(LaggedStartMap(Write, output_objects, lag_ratio=0.3))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    steps_title,
                    step1_title,
                    step2_title,
                    calc_file,
                    calc_filename,
                    calc_objects,
                    main_file,
                    main_filename,
                    main_objects,
                    output_title,
                    output_objects,
                )
            )
        )

    def packages_overview(self):
        """Introduction to Python packages"""
        title = Text("Python Packages", font_size=48, color=BLUE)
        subtitle = Text(
            "Collections of modules in directories", font_size=24, color=GREEN
        )

        title.to_edge(UP, buff=0.5)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), Write(subtitle))

        # Package structure visualization
        structure_title = Text("Package Structure", font_size=28, color=YELLOW)
        structure_title.move_to(UP * 1)

        # Create file tree visualization
        tree_structure = [
            ("mypackage/", 0, BLUE),
            ("├── __init__.py", 1, GREEN),
            ("├── math_ops/", 1, BLUE),
            ("│   ├── __init__.py", 2, GREEN),
            ("│   ├── basic.py", 2, WHITE),
            ("│   └── advanced.py", 2, WHITE),
            ("├── string_ops/", 1, BLUE),
            ("│   ├── __init__.py", 2, GREEN),
            ("│   └── utils.py", 2, WHITE),
            ("└── main.py", 1, WHITE),
        ]

        tree_objects = VGroup()
        for i, (item, indent_level, color) in enumerate(tree_structure):
            item_text = Text(item, font_size=16, color=color)
            item_text.move_to(LEFT * (4 - indent_level * 0.5) + UP * (0.5 - i * 0.3))
            tree_objects.add(item_text)

        self.play(Write(structure_title))
        self.play(LaggedStartMap(Write, tree_objects, lag_ratio=0.2))

        # Explain __init__.py
        init_explanation = Text(
            "__init__.py makes directories into packages", font_size=18, color=YELLOW
        )
        init_explanation.next_to(tree_objects, DOWN, buff=0.8)

        self.play(Write(init_explanation))

        # Package import examples
        import_title = Text("Importing from Packages", font_size=24, color=RED)
        import_title.next_to(init_explanation, DOWN, buff=0.8)

        import_examples = [
            "import mypackage.math_ops.basic",
            "from mypackage.math_ops import basic",
            "from mypackage.string_ops.utils import clean_text",
        ]

        import_objects = VGroup()
        for example in import_examples:
            example_text = Text(example, font_size=16, color=GREEN)
            import_objects.add(example_text)

        import_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        import_objects.next_to(import_title, DOWN, buff=0.3)

        self.play(Write(import_title))
        self.play(LaggedStartMap(Write, import_objects, lag_ratio=0.4))

        # Popular packages
        popular_title = Text("Popular Third-Party Packages", font_size=24, color=BLUE)
        popular_title.next_to(import_objects, DOWN, buff=0.8)

        packages = [
            ("numpy", "Numerical computing"),
            ("pandas", "Data analysis"),
            ("requests", "HTTP requests"),
            ("matplotlib", "Data visualization"),
            ("django", "Web framework"),
            ("flask", "Micro web framework"),
        ]

        package_objects = VGroup()
        for package, desc in packages:
            package_text = Text(f"{package}: {desc}", font_size=14, color=WHITE)
            package_objects.add(package_text)

        package_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        package_objects.next_to(popular_title, DOWN, buff=0.3)

        self.play(Write(popular_title))
        self.play(LaggedStartMap(FadeIn, package_objects, lag_ratio=0.2))

        # pip installation note
        pip_note = Text(
            "Install packages with: pip install package_name",
            font_size=16,
            color=YELLOW,
        )
        pip_note.next_to(package_objects, DOWN, buff=0.5)

        self.play(Write(pip_note))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    subtitle,
                    structure_title,
                    tree_objects,
                    init_explanation,
                    import_title,
                    import_objects,
                    popular_title,
                    package_objects,
                    pip_note,
                )
            )
        )

    def module_conclusion(self):
        """Conclusion for Module 5"""
        title = Text("Module 5 Complete!", font_size=56, color=GREEN)
        title.move_to(UP * 1.5)

        # Summary of what was learned
        summary = VGroup(
            Text("✓ Master function definition and usage", font_size=24, color=WHITE),
            Text(
                "✓ Understand parameters, arguments, and return values",
                font_size=24,
                color=WHITE,
            ),
            Text("✓ Learn variable scope and lifetime", font_size=24, color=WHITE),
            Text(
                "✓ Distinguish built-in vs user-defined functions",
                font_size=24,
                color=WHITE,
            ),
            Text(
                "✓ Organize code with modules and packages", font_size=24, color=WHITE
            ),
            Text(
                "✓ Master import statements and best practices",
                font_size=24,
                color=WHITE,
            ),
        )
        summary.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        summary.next_to(title, DOWN, buff=0.8)

        # Next module preview
        next_module = Text(
            "Next: Object-Oriented Programming", font_size=32, color=YELLOW
        )
        next_module.next_to(summary, DOWN, buff=1)

        # Create function and module celebration
        celebration_elements = VGroup()

        # Function boxes
        for i in range(8):
            func_box = RoundedRectangle(
                width=1.5,
                height=0.8,
                corner_radius=0.1,
                color=random.choice([BLUE, GREEN, YELLOW, RED]),
                fill_opacity=0.3,
            )
            func_text = Text(f"def func{i + 1}()", font_size=12, color=WHITE)
            func_text.move_to(func_box)

            func_group = VGroup(func_box, func_text)
            func_group.move_to(
                np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-2, 2) * UP
            )
            celebration_elements.add(func_group)

        # Module files
        for i in range(5):
            module_icon = Rectangle(
                width=1,
                height=1.2,
                color=random.choice([BLUE, GREEN, YELLOW]),
                fill_opacity=0.5,
            )
            module_text = Text(f"mod{i + 1}.py", font_size=10, color=WHITE)
            module_text.move_to(module_icon)

            module_group = VGroup(module_icon, module_text)
            module_group.move_to(
                np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-2, 2) * UP
            )
            celebration_elements.add(module_group)

        # Animate conclusion
        self.play(Write(title), run_time=2)
        self.play(LaggedStartMap(FadeIn, summary, lag_ratio=0.2), run_time=3)
        self.play(Write(next_module), run_time=2)

        # Add celebration elements
        self.play(
            LaggedStartMap(FadeIn, celebration_elements, lag_ratio=0.1), run_time=2
        )

        # Make elements float and organize
        self.play(
            *[
                element.animate.shift(UP * np.random.uniform(0.5, 1.5)).rotate(
                    np.random.uniform(-PI / 4, PI / 4)
                )
                for element in celebration_elements
            ],
            run_time=3,
        )

        self.wait(2)


# Main execution
if __name__ == "__main__":
    # This allows the file to be run directly
    pass
