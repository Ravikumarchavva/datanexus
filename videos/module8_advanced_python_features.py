"""
Module 8: Advanced Python Features
=================================

This module covers advanced Python concepts and features that help write
more efficient, elegant, and Pythonic code.

Learning Objectives:
- Master list comprehensions and generator expressions
- Understand decorators and their applications
- Learn about iterators and generators
- Work with context managers
- Understand lambda functions and functional programming
- Master advanced data structures (collections)
- Learn about metaclasses and descriptors
- Practice advanced OOP patterns

Duration: ~45 minutes
"""

from manimlib import *
import numpy as np


class AdvancedPythonFeatures(Scene):
    def construct(self):
        """Main course structure"""
        # Title
        title = Title("Module 8: Advanced Python Features", include_underline=False)
        title.scale(0.8)

        # Course overview
        topics = VGroup(
            Text("• List Comprehensions", font_size=24),
            Text("• Generators & Iterators", font_size=24),
            Text("• Decorators", font_size=24),
            Text("• Context Managers", font_size=24),
            Text("• Lambda & Functional Programming", font_size=24),
            Text("• Advanced Collections", font_size=24),
            Text("• Regular Expressions", font_size=24),
            Text("• Advanced OOP Patterns", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(topics))
        self.wait(2)
        self.play(FadeOut(topics))

        # Run demonstrations
        self.list_comprehensions()
        self.generators_iterators()
        self.decorators()
        self.context_managers()
        self.lambda_functional()
        self.advanced_collections()
        self.regular_expressions()
        self.advanced_oop_patterns()

        # Conclusion
        self.play(FadeOut(title))
        conclusion = Text(
            "Advanced Python Mastery Achieved!", font_size=36, color=GREEN
        )
        self.play(Write(conclusion))
        self.wait(2)

    def list_comprehensions(self):
        """Demonstrate list comprehensions and their power"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("List Comprehensions", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Traditional approach vs comprehension
        traditional_title = Text("Traditional Approach", font_size=20, color=RED)
        traditional_title.shift(UP * 2.5 + LEFT * 4)

        traditional_code = VGroup(
            Text(
                "numbers = [1, 2, 3, 4, 5]", font_size=14, color=WHITE, font="Courier"
            ),
            Text("squares = []", font_size=14, color=WHITE, font="Courier"),
            Text("for num in numbers:", font_size=14, color=WHITE, font="Courier"),
            Text(
                "    squares.append(num ** 2)",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("print(squares)", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        traditional_code.next_to(traditional_title, DOWN, buff=0.3)

        comprehension_title = Text("List Comprehension", font_size=20, color=GREEN)
        comprehension_title.shift(UP * 2.5 + RIGHT * 4)

        comprehension_code = VGroup(
            Text(
                "numbers = [1, 2, 3, 4, 5]", font_size=14, color=WHITE, font="Courier"
            ),
            Text(
                "squares = [num**2 for num in numbers]",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
            Text("print(squares)", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        comprehension_code.next_to(comprehension_title, DOWN, buff=0.3)

        # Result
        result = Text(
            "# Output: [1, 4, 9, 16, 25]", font_size=16, color=YELLOW, font="Courier"
        )
        result.shift(DOWN * 0.5)

        self.play(Write(traditional_title), Write(traditional_code))
        self.wait(1)
        self.play(Write(comprehension_title), Write(comprehension_code))
        self.wait(1)
        self.play(Write(result))
        self.wait(2)

        # Anatomy of list comprehension
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        anatomy_title = Text(
            "Anatomy of List Comprehension", font_size=24, color=YELLOW
        )
        anatomy_title.shift(UP * 2)

        # Visual breakdown
        comprehension_visual = Text(
            "[expression for item in iterable if condition]",
            font_size=18,
            color=WHITE,
            font="Courier",
        )
        comprehension_visual.shift(UP * 1)

        # Color-coded parts
        expression_box = Rectangle(width=2, height=0.6, color=GREEN, fill_opacity=0.2)
        expression_box.move_to(comprehension_visual.get_left() + RIGHT * 1.2)
        expression_label = Text("Expression", font_size=14, color=GREEN)
        expression_label.next_to(expression_box, UP, buff=0.2)

        iterator_box = Rectangle(width=3, height=0.6, color=BLUE, fill_opacity=0.2)
        iterator_box.move_to(comprehension_visual.get_center() + RIGHT * 0.8)
        iterator_label = Text("Iterator", font_size=14, color=BLUE)
        iterator_label.next_to(iterator_box, UP, buff=0.2)

        condition_box = Rectangle(width=2.5, height=0.6, color=ORANGE, fill_opacity=0.2)
        condition_box.move_to(comprehension_visual.get_right() + LEFT * 1.5)
        condition_label = Text("Condition (optional)", font_size=14, color=ORANGE)
        condition_label.next_to(condition_box, UP, buff=0.2)

        self.play(Write(anatomy_title))
        self.play(Write(comprehension_visual))
        self.play(
            Create(expression_box),
            Write(expression_label),
            Create(iterator_box),
            Write(iterator_label),
            Create(condition_box),
            Write(condition_label),
        )
        self.wait(3)

        # Examples with conditions
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        examples_title = Text("Examples with Conditions", font_size=24, color=PURPLE)
        examples_title.shift(UP * 2.5)

        examples = VGroup(
            VGroup(
                Text("# Even numbers only", font_size=14, color=GREEN, font="Courier"),
                Text(
                    "evens = [x for x in range(10) if x % 2 == 0]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("# [0, 2, 4, 6, 8]", font_size=12, color=YELLOW, font="Courier"),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("# String processing", font_size=14, color=GREEN, font="Courier"),
                Text(
                    "words = ['hello', 'world', 'python']",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "caps = [word.upper() for word in words if len(word) > 4]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# ['HELLO', 'WORLD', 'PYTHON']",
                    font_size=12,
                    color=YELLOW,
                    font="Courier",
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text(
                    "# Nested comprehension", font_size=14, color=GREEN, font="Courier"
                ),
                Text(
                    "matrix = [[1,2,3], [4,5,6], [7,8,9]]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "flat = [num for row in matrix for num in row]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# [1, 2, 3, 4, 5, 6, 7, 8, 9]",
                    font_size=12,
                    color=YELLOW,
                    font="Courier",
                ),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(examples_title))

        for example in examples:
            self.play(Write(example))
            self.wait(1.5)

        self.wait(2)

    def generators_iterators(self):
        """Explain generators and iterators"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Generators & Iterators", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Memory comparison
        memory_title = Text("Memory Efficiency", font_size=24, color=YELLOW)
        memory_title.shift(UP * 2.5)

        # List vs Generator memory usage
        list_memory = VGroup(
            Text("List (stores all in memory)", font_size=18, color=RED),
            Rectangle(width=6, height=1, color=RED, fill_opacity=0.3),
            Text(
                "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
        )
        list_memory[2].move_to(list_memory[1].get_center())
        list_memory.arrange(DOWN, buff=0.2).shift(LEFT * 4 + UP * 1)

        generator_memory = VGroup(
            Text("Generator (creates on demand)", font_size=18, color=GREEN),
            Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.3),
            Text("next →", font_size=14, color=WHITE, font="Courier"),
        )
        generator_memory[2].move_to(generator_memory[1].get_center())
        generator_memory.arrange(DOWN, buff=0.2).shift(RIGHT * 4 + UP * 1)

        self.play(Write(memory_title))
        self.play(Write(list_memory))
        self.play(Write(generator_memory))
        self.wait(2)

        # Generator syntax
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        syntax_title = Text("Generator Syntax", font_size=24, color=GREEN)
        syntax_title.shift(UP * 2.5)

        # Generator expression vs function
        gen_expression = (
            VGroup(
                Text("Generator Expression:", font_size=18, color=GREEN),
                Text(
                    "squares = (x**2 for x in range(10))",
                    font_size=16,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# Similar to list comprehension but with ()",
                    font_size=14,
                    color=GRAY,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(LEFT * 4 + UP * 1)
        )

        gen_function = (
            VGroup(
                Text("Generator Function:", font_size=18, color=BLUE),
                Text(
                    "def count_up_to(max):", font_size=16, color=WHITE, font="Courier"
                ),
                Text("    count = 1", font_size=16, color=WHITE, font="Courier"),
                Text(
                    "    while count <= max:", font_size=16, color=WHITE, font="Courier"
                ),
                Text("        yield count", font_size=16, color=YELLOW, font="Courier"),
                Text("        count += 1", font_size=16, color=WHITE, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 3 + UP * 0.5)
        )

        self.play(Write(syntax_title))
        self.play(Write(gen_expression))
        self.play(Write(gen_function))
        self.wait(2)

        # Using generators
        usage_title = Text("Using Generators", font_size=20, color=ORANGE)
        usage_title.shift(DOWN * 1)

        usage_code = VGroup(
            Text("# Creating generator", font_size=14, color=GREEN, font="Courier"),
            Text("gen = count_up_to(3)", font_size=14, color=WHITE, font="Courier"),
            Text("", font_size=2),
            Text(
                "# Getting values one by one", font_size=14, color=GREEN, font="Courier"
            ),
            Text("print(next(gen))  # 1", font_size=14, color=WHITE, font="Courier"),
            Text("print(next(gen))  # 2", font_size=14, color=WHITE, font="Courier"),
            Text("print(next(gen))  # 3", font_size=14, color=WHITE, font="Courier"),
            Text("", font_size=2),
            Text("# Or use in loop", font_size=14, color=GREEN, font="Courier"),
            Text(
                "for num in count_up_to(5):", font_size=14, color=WHITE, font="Courier"
            ),
            Text("    print(num)", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        usage_code.next_to(usage_title, DOWN, buff=0.3)

        self.play(Write(usage_title), Write(usage_code))
        self.wait(3)

    def decorators(self):
        """Explain decorators and their use cases"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Decorators", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # What are decorators?
        concept_title = Text("What are Decorators?", font_size=24, color=YELLOW)
        concept_title.shift(UP * 2.5)

        # Visual metaphor
        original_func = Rectangle(width=2.5, height=1.5, color=BLUE)
        original_func.add(Text("Original\nFunction", font_size=14))
        original_func.shift(LEFT * 4)

        decorator_wrapper = Rectangle(
            width=4, height=2.5, color=GREEN, fill_opacity=0.2
        )
        decorator_wrapper.add(Text("Decorator", font_size=16, color=GREEN))
        decorator_wrapper.move_to(original_func.get_center())

        enhanced_func = Rectangle(width=2.5, height=1.5, color=PURPLE)
        enhanced_func.add(Text("Enhanced\nFunction", font_size=14))
        enhanced_func.shift(RIGHT * 4)

        arrow1 = Arrow(LEFT * 2, LEFT * 0.5, color=ORANGE, buff=0.1)
        arrow2 = Arrow(RIGHT * 0.5, RIGHT * 2, color=ORANGE, buff=0.1)

        decorator_label = Text("Adds extra functionality", font_size=16, color=GREEN)
        decorator_label.next_to(decorator_wrapper, UP, buff=0.3)

        self.play(Write(concept_title))
        self.play(Create(original_func))
        self.play(Create(decorator_wrapper), Write(decorator_label))
        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(enhanced_func))
        self.wait(2)

        # Simple decorator example
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        example_title = Text("Simple Decorator Example", font_size=24, color=GREEN)
        example_title.shift(UP * 2.5)

        decorator_code = (
            VGroup(
                Text("# Define decorator", font_size=14, color=GREEN, font="Courier"),
                Text(
                    "def timing_decorator(func):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "    def wrapper(*args, **kwargs):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("        import time", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "        start = time.time()",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        result = func(*args, **kwargs)",
                    font_size=14,
                    color=YELLOW,
                    font="Courier",
                ),
                Text(
                    "        end = time.time()",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        print(f'Execution time: {end-start:.4f}s')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        return result", font_size=14, color=WHITE, font="Courier"
                ),
                Text("    return wrapper", font_size=14, color=WHITE, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(UP * 0.5)
        )

        usage_code = (
            VGroup(
                Text(
                    "# Using the decorator", font_size=14, color=GREEN, font="Courier"
                ),
                Text("@timing_decorator", font_size=14, color=BLUE, font="Courier"),
                Text("def slow_function():", font_size=14, color=WHITE, font="Courier"),
                Text("    import time", font_size=14, color=WHITE, font="Courier"),
                Text("    time.sleep(1)", font_size=14, color=WHITE, font="Courier"),
                Text("    return 'Done!'", font_size=14, color=WHITE, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(DOWN * 2)
        )

        self.play(Write(example_title))
        self.play(Write(decorator_code))
        self.wait(2)
        self.play(Write(usage_code))
        self.wait(2)

        # Common decorators
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        common_title = Text("Common Built-in Decorators", font_size=24, color=PURPLE)
        common_title.shift(UP * 2.5)

        common_decorators = VGroup(
            VGroup(
                Text("@property", font_size=16, color=BLUE, font="Courier"),
                Text("Convert method to attribute", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("@staticmethod", font_size=16, color=GREEN, font="Courier"),
                Text("Method doesn't need self/cls", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("@classmethod", font_size=16, color=ORANGE, font="Courier"),
                Text("Method gets class as first argument", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("@functools.wraps", font_size=16, color=RED, font="Courier"),
                Text("Preserve function metadata", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        self.play(Write(common_title))

        for decorator in common_decorators:
            self.play(Write(decorator))
            self.wait(0.8)

        self.wait(2)

    def context_managers(self):
        """Explain context managers beyond file handling"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Context Managers", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Context manager concept
        concept_title = Text("Context Manager Concept", font_size=24, color=YELLOW)
        concept_title.shift(UP * 2.5)

        # Flow diagram
        setup_block = Rectangle(width=2, height=1, color=GREEN)
        setup_block.add(Text("Setup", font_size=14))
        setup_block.shift(LEFT * 4 + UP * 1)

        work_block = Rectangle(width=2, height=1, color=BLUE)
        work_block.add(Text("Do Work", font_size=14))
        work_block.shift(UP * 1)

        cleanup_block = Rectangle(width=2, height=1, color=RED)
        cleanup_block.add(Text("Cleanup", font_size=14))
        cleanup_block.shift(RIGHT * 4 + UP * 1)

        # Arrows
        setup_arrow = Arrow(setup_block.get_right(), work_block.get_left(), buff=0.1)
        cleanup_arrow = Arrow(
            work_block.get_right(), cleanup_block.get_left(), buff=0.1
        )

        # Labels
        enter_label = Text("__enter__", font_size=12, color=GREEN, font="Courier")
        enter_label.next_to(setup_arrow, UP)

        exit_label = Text("__exit__", font_size=12, color=RED, font="Courier")
        exit_label.next_to(cleanup_arrow, UP)

        self.play(Write(concept_title))
        self.play(
            Create(setup_block),
            Create(work_block),
            Create(cleanup_block),
            Create(setup_arrow),
            Create(cleanup_arrow),
            Write(enter_label),
            Write(exit_label),
        )
        self.wait(2)

        # Custom context manager
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        custom_title = Text(
            "Creating Custom Context Manager", font_size=24, color=GREEN
        )
        custom_title.shift(UP * 2.5)

        # Class-based context manager
        class_cm = (
            VGroup(
                Text(
                    "# Class-based context manager",
                    font_size=14,
                    color=GREEN,
                    font="Courier",
                ),
                Text(
                    "class DatabaseConnection:",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "    def __enter__(self):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        print('Connecting to database...')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("        return self", font_size=14, color=WHITE, font="Courier"),
                Text("    ", font_size=2),
                Text(
                    "    def __exit__(self, exc_type, exc_val, exc_tb):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        print('Closing database connection...')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("        return False", font_size=14, color=WHITE, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 3)
        )

        # Function-based context manager
        func_cm = (
            VGroup(
                Text(
                    "# Function-based with contextlib",
                    font_size=14,
                    color=GREEN,
                    font="Courier",
                ),
                Text(
                    "from contextlib import contextmanager",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text("", font_size=2),
                Text("@contextmanager", font_size=14, color=BLUE, font="Courier"),
                Text(
                    "def database_connection():",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "    print('Connecting...')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("    try:", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "        yield 'connection'",
                    font_size=14,
                    color=YELLOW,
                    font="Courier",
                ),
                Text("    finally:", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "        print('Closing...')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 3.5)
        )

        self.play(Write(custom_title))
        self.play(Write(class_cm))
        self.wait(1)
        self.play(Write(func_cm))
        self.wait(2)

        # Usage example
        usage_title = Text("Using Context Managers", font_size=20, color=ORANGE)
        usage_title.shift(DOWN * 1.5)

        usage_code = VGroup(
            Text(
                "# Using the context manager", font_size=14, color=GREEN, font="Courier"
            ),
            Text(
                "with DatabaseConnection():", font_size=14, color=WHITE, font="Courier"
            ),
            Text(
                "    print('Doing database work...')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "# Cleanup happens automatically!",
                font_size=14,
                color=BLUE,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        usage_code.next_to(usage_title, DOWN, buff=0.3)

        self.play(Write(usage_title), Write(usage_code))
        self.wait(3)

    def lambda_functional(self):
        """Demonstrate lambda functions and functional programming"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text(
            "Lambda & Functional Programming", font_size=32, color=BLUE
        )
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Lambda basics
        lambda_title = Text("Lambda Functions", font_size=24, color=YELLOW)
        lambda_title.shift(UP * 2.5)

        # Regular function vs lambda
        regular_func = (
            VGroup(
                Text("Regular Function:", font_size=18, color=GREEN),
                Text("def square(x):", font_size=14, color=WHITE, font="Courier"),
                Text("    return x ** 2", font_size=14, color=WHITE, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 4 + UP * 1)
        )

        lambda_func = (
            VGroup(
                Text("Lambda Function:", font_size=18, color=ORANGE),
                Text(
                    "square = lambda x: x ** 2",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 3 + UP * 1)
        )

        self.play(Write(lambda_title))
        self.play(Write(regular_func))
        self.play(Write(lambda_func))
        self.wait(2)

        # Functional programming tools
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        fp_title = Text("Functional Programming Tools", font_size=24, color=PURPLE)
        fp_title.shift(UP * 2.5)

        # Map example
        map_example = (
            VGroup(
                Text("map() - Apply function to all items", font_size=16, color=GREEN),
                Text(
                    "numbers = [1, 2, 3, 4, 5]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "squares = list(map(lambda x: x**2, numbers))",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("# [1, 4, 9, 16, 25]", font_size=12, color=YELLOW, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(UP * 1.2)
        )

        # Filter example
        filter_example = (
            VGroup(
                Text(
                    "filter() - Filter items based on condition",
                    font_size=16,
                    color=BLUE,
                ),
                Text(
                    "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "evens = list(filter(lambda x: x % 2 == 0, numbers))",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("# [2, 4, 6, 8, 10]", font_size=12, color=YELLOW, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(DOWN * 0.2)
        )

        # Reduce example
        reduce_example = (
            VGroup(
                Text("reduce() - Reduce to single value", font_size=16, color=RED),
                Text(
                    "from functools import reduce",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text(
                    "numbers = [1, 2, 3, 4, 5]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "product = reduce(lambda x, y: x * y, numbers)",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# 120 (1 * 2 * 3 * 4 * 5)",
                    font_size=12,
                    color=YELLOW,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(DOWN * 1.8)
        )

        self.play(Write(fp_title))
        self.play(Write(map_example))
        self.wait(1)
        self.play(Write(filter_example))
        self.wait(1)
        self.play(Write(reduce_example))
        self.wait(3)

    def advanced_collections(self):
        """Show advanced collection types from collections module"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Advanced Collections", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Collections overview
        collections_title = Text("collections Module", font_size=24, color=YELLOW)
        collections_title.shift(UP * 2.5)

        # Counter example
        counter_example = (
            VGroup(
                Text("Counter - Count occurrences", font_size=16, color=GREEN),
                Text(
                    "from collections import Counter",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text("text = 'hello world'", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "counts = Counter(text)", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "print(counts.most_common(3))",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# [('l', 3), ('o', 2), ('h', 1)]",
                    font_size=12,
                    color=YELLOW,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 4 + UP * 0.8)
        )

        # defaultdict example
        defaultdict_example = (
            VGroup(
                Text("defaultdict - Default values", font_size=16, color=ORANGE),
                Text(
                    "from collections import defaultdict",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text(
                    "dd = defaultdict(list)", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "dd['fruits'].append('apple')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "dd['fruits'].append('banana')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("# No KeyError!", font_size=12, color=GREEN, font="Courier"),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 4 + UP * 0.8)
        )

        # deque example
        deque_example = (
            VGroup(
                Text("deque - Double-ended queue", font_size=16, color=PURPLE),
                Text(
                    "from collections import deque",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text("d = deque([1, 2, 3])", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "d.appendleft(0)  # [0, 1, 2, 3]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "d.append(4)      # [0, 1, 2, 3, 4]",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "# Fast operations at both ends",
                    font_size=12,
                    color=GREEN,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 4 + DOWN * 1.5)
        )

        # namedtuple example
        namedtuple_example = (
            VGroup(
                Text("namedtuple - Named tuple", font_size=16, color=RED),
                Text(
                    "from collections import namedtuple",
                    font_size=14,
                    color=BLUE,
                    font="Courier",
                ),
                Text(
                    "Point = namedtuple('Point', ['x', 'y'])",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("p = Point(1, 2)", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "print(p.x, p.y)  # 1 2", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "# Immutable and memory efficient",
                    font_size=12,
                    color=GREEN,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 4 + DOWN * 1.5)
        )

        self.play(Write(collections_title))
        self.play(Write(counter_example))
        self.wait(1)
        self.play(Write(defaultdict_example))
        self.wait(1)
        self.play(Write(deque_example))
        self.wait(1)
        self.play(Write(namedtuple_example))
        self.wait(3)

    def regular_expressions(self):
        """Introduce regular expressions"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Regular Expressions", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # What are regex?
        regex_title = Text("What are Regular Expressions?", font_size=24, color=YELLOW)
        regex_title.shift(UP * 2.5)

        regex_desc = Text(
            "Pattern matching for text processing", font_size=18, color=WHITE
        )
        regex_desc.next_to(regex_title, DOWN, buff=0.3)

        # Common patterns
        patterns_title = Text("Common Patterns", font_size=20, color=GREEN)
        patterns_title.shift(UP * 1)

        patterns = VGroup(
            VGroup(
                Text("\\d", font_size=16, color=BLUE, font="Courier"),
                Text("Any digit (0-9)", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("\\w", font_size=16, color=BLUE, font="Courier"),
                Text("Any word character", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("\\s", font_size=16, color=BLUE, font="Courier"),
                Text("Any whitespace", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text(".", font_size=16, color=BLUE, font="Courier"),
                Text("Any character", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("*", font_size=16, color=BLUE, font="Courier"),
                Text("Zero or more", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("+", font_size=16, color=BLUE, font="Courier"),
                Text("One or more", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
        ).arrange_in_grid(rows=3, cols=2, buff=0.8)
        patterns.next_to(patterns_title, DOWN, buff=0.3)

        self.play(Write(regex_title), Write(regex_desc))
        self.play(Write(patterns_title))

        for pattern in patterns:
            self.play(Write(pattern))
            self.wait(0.3)

        self.wait(2)

        # Practical example
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        example_title = Text(
            "Practical Example: Email Validation", font_size=24, color=ORANGE
        )
        example_title.shift(UP * 2.5)

        email_regex = VGroup(
            Text("import re", font_size=14, color=BLUE, font="Courier"),
            Text("", font_size=2),
            Text("# Email pattern", font_size=14, color=GREEN, font="Courier"),
            Text(
                "pattern = r'\\w+@\\w+\\.\\w+'",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("", font_size=2),
            Text("# Test emails", font_size=14, color=GREEN, font="Courier"),
            Text(
                "emails = ['user@email.com', 'invalid.email', 'test@site.org']",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("", font_size=2),
            Text("for email in emails:", font_size=14, color=WHITE, font="Courier"),
            Text(
                "    if re.match(pattern, email):",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "        print(f'{email} is valid')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("    else:", font_size=14, color=WHITE, font="Courier"),
            Text(
                "        print(f'{email} is invalid')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(example_title))
        self.play(Write(email_regex))
        self.wait(3)

    def advanced_oop_patterns(self):
        """Show advanced OOP patterns and concepts"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Advanced OOP Patterns", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Design patterns overview
        patterns_title = Text("Common Design Patterns", font_size=24, color=YELLOW)
        patterns_title.shift(UP * 2.5)

        # Singleton pattern
        singleton_example = (
            VGroup(
                Text("Singleton Pattern", font_size=18, color=GREEN),
                Text("class Singleton:", font_size=14, color=WHITE, font="Courier"),
                Text("    _instance = None", font_size=14, color=WHITE, font="Courier"),
                Text("    ", font_size=2),
                Text(
                    "    def __new__(cls):", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "        if cls._instance is None:",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "            cls._instance = super().__new__(cls)",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        return cls._instance",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(LEFT * 4 + UP * 0.5)
        )

        # Factory pattern
        factory_example = (
            VGroup(
                Text("Factory Pattern", font_size=18, color=ORANGE),
                Text("class AnimalFactory:", font_size=14, color=WHITE, font="Courier"),
                Text("    @staticmethod", font_size=14, color=BLUE, font="Courier"),
                Text(
                    "    def create_animal(animal_type):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        if animal_type == 'dog':",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "            return Dog()",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        elif animal_type == 'cat':",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "            return Cat()",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(RIGHT * 4 + UP * 0.5)
        )

        # Property decorators
        property_example = (
            VGroup(
                Text("Property Decorators", font_size=18, color=PURPLE),
                Text("class Circle:", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "    def __init__(self, radius):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        self._radius = radius",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("    ", font_size=2),
                Text("    @property", font_size=14, color=BLUE, font="Courier"),
                Text("    def area(self):", font_size=14, color=WHITE, font="Courier"),
                Text(
                    "        return 3.14159 * self._radius ** 2",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("    ", font_size=2),
                Text("    @property", font_size=14, color=BLUE, font="Courier"),
                Text(
                    "    def radius(self):", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "        return self._radius",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text("    ", font_size=2),
                Text("    @radius.setter", font_size=14, color=BLUE, font="Courier"),
                Text(
                    "    def radius(self, value):",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        if value < 0:", font_size=14, color=WHITE, font="Courier"
                ),
                Text(
                    "            raise ValueError('Radius must be positive')",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
                Text(
                    "        self._radius = value",
                    font_size=14,
                    color=WHITE,
                    font="Courier",
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            .shift(DOWN * 2)
        )

        self.play(Write(patterns_title))
        self.play(Write(singleton_example))
        self.wait(1)
        self.play(Write(factory_example))
        self.wait(1)
        self.play(Write(property_example))
        self.wait(3)

        # Best practices summary
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        best_practices = VGroup(
            Text("Advanced Python Best Practices", font_size=24, color=GOLD),
            Text(
                "✅ Use list comprehensions for simple transformations",
                font_size=16,
                color=GREEN,
            ),
            Text("✅ Prefer generators for large datasets", font_size=16, color=GREEN),
            Text("✅ Use decorators to separate concerns", font_size=16, color=GREEN),
            Text(
                "✅ Implement context managers for resource management",
                font_size=16,
                color=GREEN,
            ),
            Text("✅ Leverage functional programming tools", font_size=16, color=GREEN),
            Text("✅ Choose appropriate data structures", font_size=16, color=GREEN),
            Text("✅ Apply design patterns judiciously", font_size=16, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(best_practices))
        self.wait(4)


if __name__ == "__main__":
    from manimlib import config

    config.media_width = "854px"
    config.media_height = "480px"
    config.frame_rate = 30

    scene = AdvancedPythonFeatures()
    scene.render()
