"""
Module 7: File Handling & Error Management
=========================================

This module covers file operations, error handling, and debugging techniques
in Python, essential skills for building robust applications.

Learning Objectives:
- Master file reading and writing operations
- Understand different file modes and contexts
- Learn exception handling with try/except
- Practice debugging techniques and tools
- Handle common file and runtime errors
- Implement logging for better error tracking
- Work with different file formats (text, CSV, JSON)

Duration: ~45 minutes
"""

from manimlib import *
import numpy as np


class FileHandlingErrorManagement(Scene):
    def construct(self):
        """Main course structure"""
        # Title
        title = Title(
            "Module 7: File Handling & Error Management", include_underline=False
        )
        title.scale(0.8)

        # Course overview
        topics = VGroup(
            Text("• File Operations", font_size=24),
            Text("• Reading & Writing Files", font_size=24),
            Text("• File Modes & Context Managers", font_size=24),
            Text("• Exception Handling", font_size=24),
            Text("• Try/Except/Finally", font_size=24),
            Text("• Debugging Techniques", font_size=24),
            Text("• Working with CSV & JSON", font_size=24),
            Text("• Logging & Error Tracking", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        self.play(Write(topics))
        self.wait(2)
        self.play(FadeOut(topics))

        # Run demonstrations
        self.file_operations_basics()
        self.reading_writing_files()
        self.file_modes_context_managers()
        self.exception_handling()
        self.try_except_finally()
        self.debugging_techniques()
        self.working_with_formats()
        self.logging_error_tracking()

        # Conclusion
        self.play(FadeOut(title))
        conclusion = Text(
            "Master of Files and Error Handling!", font_size=36, color=GREEN
        )
        self.play(Write(conclusion))
        self.wait(2)

    def file_operations_basics(self):
        """Introduce file operations concepts"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("File Operations Basics", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # File system visualization
        computer = Rectangle(width=3, height=2, color=BLUE)
        computer.add(Text("Computer", font_size=16))
        computer.shift(LEFT * 4)

        file_system = VGroup(
            Rectangle(width=4, height=3, color=GREEN, fill_opacity=0.1),
            Text("File System", font_size=16, color=GREEN),
            VGroup(
                Text("📁 Documents/", font_size=14),
                Text("  📄 data.txt", font_size=12),
                Text("  📄 report.csv", font_size=12),
                Text("📁 Projects/", font_size=14),
                Text("  📄 code.py", font_size=12),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        )
        file_system[2].move_to(file_system[0].get_center())
        file_system[1].next_to(file_system[0], UP, buff=0.1)
        file_system.shift(RIGHT * 2)

        # Program interaction
        program = Rectangle(width=2.5, height=1.5, color=ORANGE)
        program.add(Text("Python\nProgram", font_size=14))
        program.shift(LEFT * 4 + DOWN * 2)

        # Arrows showing interaction
        read_arrow = Arrow(
            file_system.get_left(),
            program.get_right() + UP * 0.3,
            color=GREEN,
            buff=0.1,
        )
        read_label = Text("Read", font_size=12, color=GREEN)
        read_label.next_to(read_arrow, UP)

        write_arrow = Arrow(
            program.get_right() + DOWN * 0.3,
            file_system.get_left() + DOWN * 0.5,
            color=RED,
            buff=0.1,
        )
        write_label = Text("Write", font_size=12, color=RED)
        write_label.next_to(write_arrow, DOWN)

        self.play(Create(computer), Create(file_system), Create(program))
        self.wait(1)
        self.play(Create(read_arrow), Write(read_label))
        self.play(Create(write_arrow), Write(write_label))
        self.wait(2)

        # Why work with files?
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        why_files = VGroup(
            Text("Why Work with Files?", font_size=24, color=YELLOW),
            Text("• Store data permanently", font_size=18),
            Text("• Share data between programs", font_size=18),
            Text("• Process large datasets", font_size=18),
            Text("• Create reports and logs", font_size=18),
            Text("• Configure applications", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(why_files))
        self.wait(3)

    def reading_writing_files(self):
        """Demonstrate basic file reading and writing"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Reading & Writing Files", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Writing to a file
        write_title = Text("Writing to a File", font_size=24, color=GREEN)
        write_title.shift(UP * 2.5 + LEFT * 4)

        write_code = VGroup(
            Text("# Open file for writing", font_size=14, color=GREEN, font="Courier"),
            Text(
                "file = open('data.txt', 'w')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "file.write('Hello, World!')", font_size=14, color=WHITE, font="Courier"
            ),
            Text(
                "file.write('\\nPython is awesome!')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("file.close()", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        write_code.next_to(write_title, DOWN, buff=0.3)

        # File representation
        file_visual = VGroup(
            Rectangle(width=3, height=2, color=YELLOW, fill_opacity=0.2),
            Text("data.txt", font_size=16, color=YELLOW),
            VGroup(
                Text("Hello, World!", font_size=12, color=WHITE),
                Text("Python is awesome!", font_size=12, color=WHITE),
            ).arrange(DOWN, buff=0.1),
        )
        file_visual[2].move_to(file_visual[0].get_center())
        file_visual[1].next_to(file_visual[0], UP, buff=0.1)
        file_visual.shift(UP * 1 + RIGHT * 4)

        self.play(Write(write_title))
        self.play(Write(write_code))
        self.wait(1)
        self.play(Create(file_visual))
        self.wait(2)

        # Reading from a file
        read_title = Text("Reading from a File", font_size=24, color=ORANGE)
        read_title.shift(DOWN * 0.5 + LEFT * 4)

        read_code = VGroup(
            Text("# Open file for reading", font_size=14, color=GREEN, font="Courier"),
            Text(
                "file = open('data.txt', 'r')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("content = file.read()", font_size=14, color=WHITE, font="Courier"),
            Text("print(content)", font_size=14, color=WHITE, font="Courier"),
            Text("file.close()", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        read_code.next_to(read_title, DOWN, buff=0.3)

        # Output
        output_visual = VGroup(
            Rectangle(width=3, height=1.5, color=BLACK, fill_opacity=0.8),
            Text("Hello, World!", font_size=12, color=GREEN, font="Courier"),
            Text("Python is awesome!", font_size=12, color=GREEN, font="Courier"),
        )
        output_visual[1:].arrange(DOWN, buff=0.1)
        output_visual[1:].move_to(output_visual[0].get_center())
        output_visual.shift(DOWN * 1.5 + RIGHT * 4)

        self.play(Write(read_title))
        self.play(Write(read_code))
        self.wait(1)
        self.play(Create(output_visual))
        self.wait(3)

    def file_modes_context_managers(self):
        """Explain file modes and context managers"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("File Modes & Context Managers", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # File modes
        modes_title = Text("File Modes", font_size=24, color=YELLOW)
        modes_title.shift(UP * 2.5)

        modes_table = VGroup(
            VGroup(
                Text("Mode", font_size=16, color=WHITE),
                Text("Description", font_size=16, color=WHITE),
                Text("Example", font_size=16, color=WHITE),
            ).arrange(RIGHT, buff=1.5),
            VGroup(
                Text("'r'", font_size=16, color=GREEN, font="Courier"),
                Text("Read only", font_size=16),
                Text("Reading data", font_size=16, color=GRAY),
            ).arrange(RIGHT, buff=1.5),
            VGroup(
                Text("'w'", font_size=16, color=RED, font="Courier"),
                Text("Write (overwrites)", font_size=16),
                Text("Creating new file", font_size=16, color=GRAY),
            ).arrange(RIGHT, buff=1.5),
            VGroup(
                Text("'a'", font_size=16, color=ORANGE, font="Courier"),
                Text("Append", font_size=16),
                Text("Adding to log", font_size=16, color=GRAY),
            ).arrange(RIGHT, buff=1.5),
            VGroup(
                Text("'r+'", font_size=16, color=PURPLE, font="Courier"),
                Text("Read and write", font_size=16),
                Text("Updating file", font_size=16, color=GRAY),
            ).arrange(RIGHT, buff=1.5),
        ).arrange(DOWN, buff=0.3)

        # Underline header
        header_line = Line(
            modes_table[0].get_left() + DOWN * 0.1,
            modes_table[0].get_right() + DOWN * 0.1,
            color=WHITE,
        )

        self.play(Write(modes_title))
        self.play(Write(modes_table[0]), Create(header_line))

        for row in modes_table[1:]:
            self.play(Write(row))
            self.wait(0.5)

        self.wait(2)

        # Context managers
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        context_title = Text(
            "Context Managers (with statement)", font_size=24, color=GREEN
        )
        context_title.shift(UP * 2.5)

        # Problem with manual file handling
        problem_title = Text(
            "❌ Problem with manual handling:", font_size=20, color=RED
        )
        problem_title.shift(UP * 1.5 + LEFT * 4)

        problem_code = VGroup(
            Text(
                "file = open('data.txt', 'r')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("data = file.read()", font_size=14, color=WHITE, font="Courier"),
            Text(
                "# What if error occurs here?", font_size=14, color=RED, font="Courier"
            ),
            Text(
                "file.close()  # Might not execute!",
                font_size=14,
                color=RED,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        problem_code.next_to(problem_title, DOWN, buff=0.3)

        # Solution with context manager
        solution_title = Text(
            "✅ Solution with context manager:", font_size=20, color=GREEN
        )
        solution_title.shift(UP * 1.5 + RIGHT * 4)

        solution_code = VGroup(
            Text(
                "with open('data.txt', 'r') as file:",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("    data = file.read()", font_size=14, color=WHITE, font="Courier"),
            Text("    # Process data", font_size=14, color=GREEN, font="Courier"),
            Text(
                "# File automatically closed!",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        solution_code.next_to(solution_title, DOWN, buff=0.3)

        self.play(Write(context_title))
        self.play(Write(problem_title), Write(problem_code))
        self.wait(1)
        self.play(Write(solution_title), Write(solution_code))
        self.wait(2)

        # Benefits
        benefits = (
            VGroup(
                Text("Benefits of 'with' statement:", font_size=20, color=BLUE),
                Text("• Automatically closes files", font_size=16),
                Text("• Works even if errors occur", font_size=16),
                Text("• Cleaner, more readable code", font_size=16),
                Text("• Prevents resource leaks", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .shift(DOWN * 2)
        )

        self.play(Write(benefits))
        self.wait(3)

    def exception_handling(self):
        """Introduce exception handling concepts"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Exception Handling", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # What are exceptions?
        exceptions_title = Text("What are Exceptions?", font_size=24, color=YELLOW)
        exceptions_title.shift(UP * 2.5)

        # Normal vs exceptional flow
        normal_flow = (
            VGroup(
                Text("Normal Flow:", font_size=20, color=GREEN),
                VGroup(
                    Rectangle(width=2, height=0.8, color=BLUE).add(
                        Text("Step 1", font_size=14)
                    ),
                    Rectangle(width=2, height=0.8, color=BLUE).add(
                        Text("Step 2", font_size=14)
                    ),
                    Rectangle(width=2, height=0.8, color=BLUE).add(
                        Text("Step 3", font_size=14)
                    ),
                    Rectangle(width=2, height=0.8, color=GREEN).add(
                        Text("Success", font_size=14)
                    ),
                ).arrange(DOWN, buff=0.2),
            )
            .arrange(DOWN, buff=0.3)
            .shift(LEFT * 4)
        )

        # Add arrows for normal flow
        normal_arrows = VGroup(
            *[
                Arrow(
                    normal_flow[1][i].get_bottom(),
                    normal_flow[1][i + 1].get_top(),
                    buff=0.1,
                )
                for i in range(3)
            ]
        )

        exceptional_flow = (
            VGroup(
                Text("Exceptional Flow:", font_size=20, color=RED),
                VGroup(
                    Rectangle(width=2, height=0.8, color=BLUE).add(
                        Text("Step 1", font_size=14)
                    ),
                    Rectangle(width=2, height=0.8, color=RED).add(
                        Text("ERROR!", font_size=14)
                    ),
                    Rectangle(width=2, height=0.8, color=GRAY).add(
                        Text("Skipped", font_size=12)
                    ),
                    Rectangle(width=2, height=0.8, color=ORANGE).add(
                        Text("Handle", font_size=14)
                    ),
                ).arrange(DOWN, buff=0.2),
            )
            .arrange(DOWN, buff=0.3)
            .shift(RIGHT * 4)
        )

        # Add arrows for exceptional flow
        except_arrows = VGroup(
            Arrow(
                exceptional_flow[1][0].get_bottom(),
                exceptional_flow[1][1].get_top(),
                buff=0.1,
            ),
            Arrow(
                exceptional_flow[1][1].get_right(),
                exceptional_flow[1][3].get_left(),
                color=ORANGE,
                buff=0.1,
                path_arc=PI / 3,
            ),
        )

        self.play(Write(exceptions_title))
        self.play(Write(normal_flow), Create(normal_arrows))
        self.wait(1)
        self.play(Write(exceptional_flow), Create(except_arrows))
        self.wait(2)

        # Common exceptions
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        common_title = Text("Common Python Exceptions", font_size=24, color=ORANGE)
        common_title.shift(UP * 2.5)

        exceptions_list = VGroup(
            VGroup(
                Text("FileNotFoundError", font_size=16, color=RED, font="Courier"),
                Text("File doesn't exist", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("ValueError", font_size=16, color=RED, font="Courier"),
                Text("Wrong value type", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("TypeError", font_size=16, color=RED, font="Courier"),
                Text("Wrong data type", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("ZeroDivisionError", font_size=16, color=RED, font="Courier"),
                Text("Division by zero", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("IndexError", font_size=16, color=RED, font="Courier"),
                Text("List index out of range", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("KeyError", font_size=16, color=RED, font="Courier"),
                Text("Dictionary key not found", font_size=14, color=GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange_in_grid(rows=3, cols=2, buff=0.8)

        self.play(Write(common_title))

        for exception in exceptions_list:
            self.play(Write(exception))
            self.wait(0.5)

        self.wait(2)

    def try_except_finally(self):
        """Demonstrate try/except/finally blocks"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Try/Except/Finally", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Basic try/except structure
        structure_title = Text("Basic Structure", font_size=24, color=YELLOW)
        structure_title.shift(UP * 2.5)

        basic_structure = VGroup(
            Text("try:", font_size=18, color=GREEN, font="Courier"),
            Text(
                "    # Code that might fail", font_size=16, color=WHITE, font="Courier"
            ),
            Text("except ExceptionType:", font_size=18, color=RED, font="Courier"),
            Text("    # Handle the error", font_size=16, color=WHITE, font="Courier"),
            Text("finally:", font_size=18, color=BLUE, font="Courier"),
            Text("    # Always runs", font_size=16, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(structure_title))
        self.play(Write(basic_structure))
        self.wait(2)

        # Practical example
        self.play(FadeOut(basic_structure))

        example_title = Text(
            "Practical Example: File Reading", font_size=20, color=GREEN
        )
        example_title.shift(UP * 1.5)

        example_code = VGroup(
            Text("try:", font_size=16, color=GREEN, font="Courier"),
            Text(
                "    with open('data.txt', 'r') as file:",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "        content = file.read()",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("        print(content)", font_size=14, color=WHITE, font="Courier"),
            Text("except FileNotFoundError:", font_size=16, color=RED, font="Courier"),
            Text(
                "    print('File not found!')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("except PermissionError:", font_size=16, color=ORANGE, font="Courier"),
            Text(
                "    print('No permission to read file!')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("finally:", font_size=16, color=BLUE, font="Courier"),
            Text(
                "    print('File operation completed.')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(example_title))
        self.play(Write(example_code))
        self.wait(3)

        # Flow diagram
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        flow_title = Text("Exception Handling Flow", font_size=24, color=PURPLE)
        flow_title.shift(UP * 2.5)

        # Create flow diagram
        try_block = Rectangle(width=2.5, height=1, color=GREEN)
        try_block.add(Text("try block", font_size=14))
        try_block.shift(UP * 1.5)

        decision = RegularPolygon(n=4, color=ORANGE).rotate(PI / 4).scale(0.8)
        decision.add(Text("Exception\noccurred?", font_size=10))
        decision.next_to(try_block, DOWN, buff=0.5)

        except_block = Rectangle(width=2.5, height=1, color=RED)
        except_block.add(Text("except block", font_size=14))
        except_block.next_to(decision, LEFT, buff=1)

        success_block = Rectangle(width=2.5, height=1, color=BLUE)
        success_block.add(Text("continue", font_size=14))
        success_block.next_to(decision, RIGHT, buff=1)

        finally_block = Rectangle(width=2.5, height=1, color=PURPLE)
        finally_block.add(Text("finally block", font_size=14))
        finally_block.next_to(decision, DOWN, buff=1.5)

        # Arrows
        flow_arrows = VGroup(
            Arrow(try_block.get_bottom(), decision.get_top(), buff=0.1),
            Arrow(decision.get_left(), except_block.get_right(), buff=0.1),
            Arrow(decision.get_right(), success_block.get_left(), buff=0.1),
            Arrow(
                except_block.get_bottom(),
                finally_block.get_top() + LEFT * 0.5,
                buff=0.1,
            ),
            Arrow(
                success_block.get_bottom(),
                finally_block.get_top() + RIGHT * 0.5,
                buff=0.1,
            ),
        )

        # Labels
        yes_label = Text("YES", font_size=12, color=RED).next_to(flow_arrows[1], UP)
        no_label = Text("NO", font_size=12, color=GREEN).next_to(flow_arrows[2], UP)

        flow_diagram = VGroup(
            try_block,
            decision,
            except_block,
            success_block,
            finally_block,
            flow_arrows,
            yes_label,
            no_label,
        )

        self.play(Write(flow_title))
        self.play(Create(flow_diagram))
        self.wait(3)

    def debugging_techniques(self):
        """Show debugging techniques and tools"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Debugging Techniques", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Debugging strategies
        strategies_title = Text("Debugging Strategies", font_size=24, color=YELLOW)
        strategies_title.shift(UP * 2.5)

        strategies = VGroup(
            Text("1. 🖨️ Print Debugging", font_size=20, color=GREEN),
            Text("2. 🐛 Use Debugger", font_size=20, color=ORANGE),
            Text("3. 📝 Read Error Messages", font_size=20, color=RED),
            Text("4. 🔍 Rubber Duck Debugging", font_size=20, color=BLUE),
            Text("5. ✂️ Divide and Conquer", font_size=20, color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(strategies_title))

        for strategy in strategies:
            self.play(Write(strategy))
            self.wait(0.5)

        self.wait(1)

        # Print debugging example
        self.play(FadeOut(strategies))

        print_debug_title = Text("Print Debugging Example", font_size=20, color=GREEN)
        print_debug_title.shift(UP * 1.5)

        debug_code = VGroup(
            Text(
                "def calculate_average(numbers):",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "    print(f'Input: {numbers}')  # Debug",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
            Text("    total = sum(numbers)", font_size=14, color=WHITE, font="Courier"),
            Text(
                "    print(f'Total: {total}')  # Debug",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
            Text("    count = len(numbers)", font_size=14, color=WHITE, font="Courier"),
            Text(
                "    print(f'Count: {count}')  # Debug",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
            Text(
                "    average = total / count", font_size=14, color=WHITE, font="Courier"
            ),
            Text(
                "    print(f'Average: {average}')  # Debug",
                font_size=14,
                color=GREEN,
                font="Courier",
            ),
            Text("    return average", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(print_debug_title))
        self.play(Write(debug_code))
        self.wait(3)

        # Error message anatomy
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        error_title = Text("Understanding Error Messages", font_size=24, color=RED)
        error_title.shift(UP * 2.5)

        error_example = VGroup(
            Rectangle(width=10, height=3, color=RED, fill_opacity=0.1),
            Text(
                "Traceback (most recent call last):",
                font_size=12,
                color=RED,
                font="Courier",
            ),
            Text(
                "  File 'main.py', line 5, in <module>",
                font_size=12,
                color=WHITE,
                font="Courier",
            ),
            Text("    result = 10 / 0", font_size=12, color=WHITE, font="Courier"),
            Text(
                "ZeroDivisionError: division by zero",
                font_size=12,
                color=RED,
                font="Courier",
            ),
        )
        error_example[1:].arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        error_example[1:].move_to(error_example[0].get_center())

        # Annotations
        annotations = VGroup(
            Text("← Error type", font_size=12, color=YELLOW).next_to(
                error_example[4], RIGHT
            ),
            Text("← Line that caused error", font_size=12, color=YELLOW).next_to(
                error_example[3], RIGHT
            ),
            Text("← File and line number", font_size=12, color=YELLOW).next_to(
                error_example[2], RIGHT
            ),
        )

        self.play(Write(error_title))
        self.play(Create(error_example))
        self.play(Write(annotations))
        self.wait(3)

    def working_with_formats(self):
        """Show working with different file formats"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Working with CSV & JSON", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # CSV example
        csv_title = Text("CSV (Comma Separated Values)", font_size=24, color=GREEN)
        csv_title.shift(UP * 2.5 + LEFT * 4)

        csv_data = VGroup(
            Text("data.csv:", font_size=16, color=GREEN),
            Rectangle(width=3, height=2, color=GREEN, fill_opacity=0.1),
            VGroup(
                Text("name,age,city", font_size=12, color=WHITE, font="Courier"),
                Text("Alice,25,NYC", font_size=12, color=WHITE, font="Courier"),
                Text("Bob,30,LA", font_size=12, color=WHITE, font="Courier"),
                Text("Carol,28,Chicago", font_size=12, color=WHITE, font="Courier"),
            ).arrange(DOWN, buff=0.1),
        )
        csv_data[2].move_to(csv_data[1].get_center())
        csv_data.arrange(DOWN, buff=0.2)
        csv_data.next_to(csv_title, DOWN, buff=0.3)

        csv_code = VGroup(
            Text("import csv", font_size=14, color=BLUE, font="Courier"),
            Text("", font_size=2),
            Text(
                "with open('data.csv', 'r') as file:",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "    reader = csv.reader(file)",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("    for row in reader:", font_size=14, color=WHITE, font="Courier"),
            Text("        print(row)", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        csv_code.next_to(csv_data, DOWN, buff=0.5)

        # JSON example
        json_title = Text(
            "JSON (JavaScript Object Notation)", font_size=24, color=ORANGE
        )
        json_title.shift(UP * 2.5 + RIGHT * 4)

        json_data = VGroup(
            Text("data.json:", font_size=16, color=ORANGE),
            Rectangle(width=3, height=2, color=ORANGE, fill_opacity=0.1),
            VGroup(
                Text("{", font_size=12, color=WHITE, font="Courier"),
                Text('  "name": "Alice",', font_size=12, color=WHITE, font="Courier"),
                Text('  "age": 25,', font_size=12, color=WHITE, font="Courier"),
                Text('  "city": "NYC"', font_size=12, color=WHITE, font="Courier"),
                Text("}", font_size=12, color=WHITE, font="Courier"),
            ).arrange(DOWN, buff=0.1),
        )
        json_data[2].move_to(json_data[1].get_center())
        json_data.arrange(DOWN, buff=0.2)
        json_data.next_to(json_title, DOWN, buff=0.3)

        json_code = VGroup(
            Text("import json", font_size=14, color=BLUE, font="Courier"),
            Text("", font_size=2),
            Text(
                "with open('data.json', 'r') as file:",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "    data = json.load(file)", font_size=14, color=WHITE, font="Courier"
            ),
            Text("    print(data['name'])", font_size=14, color=WHITE, font="Courier"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        json_code.next_to(json_data, DOWN, buff=0.5)

        # Animate both examples
        self.play(Write(csv_title), Write(csv_data))
        self.play(Write(csv_code))
        self.wait(1)

        self.play(Write(json_title), Write(json_data))
        self.play(Write(json_code))
        self.wait(3)

    def logging_error_tracking(self):
        """Introduce logging for error tracking"""
        self.play(FadeOut(*self.mobjects))

        # Section title
        section_title = Text("Logging & Error Tracking", font_size=32, color=BLUE)
        section_title.to_edge(UP)
        self.play(Write(section_title))

        # Why logging?
        why_logging = (
            VGroup(
                Text("Why Use Logging?", font_size=24, color=YELLOW),
                Text("• Track program execution", font_size=18),
                Text("• Record errors and warnings", font_size=18),
                Text("• Debug issues in production", font_size=18),
                Text("• Monitor application health", font_size=18),
                Text("• Better than print statements", font_size=18),
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .shift(UP * 1)
        )

        self.play(Write(why_logging))
        self.wait(2)

        # Logging levels
        self.play(FadeOut(why_logging))

        levels_title = Text("Logging Levels", font_size=24, color=GREEN)
        levels_title.shift(UP * 2.5)

        levels = VGroup(
            VGroup(
                Text("DEBUG", font_size=16, color=BLUE, font="Courier"),
                Text("Detailed information", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("INFO", font_size=16, color=GREEN, font="Courier"),
                Text("General information", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("WARNING", font_size=16, color=YELLOW, font="Courier"),
                Text("Something unexpected", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("ERROR", font_size=16, color=RED, font="Courier"),
                Text("Serious problem", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("CRITICAL", font_size=16, color=DARK_RED, font="Courier"),
                Text("Very serious error", font_size=14, color=GRAY),
            ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(levels_title))

        for level in levels:
            self.play(Write(level))
            self.wait(0.3)

        self.wait(1)

        # Logging example
        self.play(FadeOut(levels))

        example_title = Text("Logging Example", font_size=20, color=PURPLE)
        example_title.shift(UP * 1.5)

        logging_code = VGroup(
            Text("import logging", font_size=14, color=BLUE, font="Courier"),
            Text("", font_size=2),
            Text("# Configure logging", font_size=14, color=GREEN, font="Courier"),
            Text("logging.basicConfig(", font_size=14, color=WHITE, font="Courier"),
            Text("    level=logging.INFO,", font_size=14, color=WHITE, font="Courier"),
            Text(
                "    format='%(asctime)s - %(levelname)s - %(message)s',",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text("    filename='app.log'", font_size=14, color=WHITE, font="Courier"),
            Text(")", font_size=14, color=WHITE, font="Courier"),
            Text("", font_size=2),
            Text("# Use logging", font_size=14, color=GREEN, font="Courier"),
            Text(
                "logging.info('Application started')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "logging.warning('This is a warning')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
            Text(
                "logging.error('An error occurred')",
                font_size=14,
                color=WHITE,
                font="Courier",
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(example_title))
        self.play(Write(logging_code))
        self.wait(3)

        # Best practices
        self.play(FadeOut(*self.mobjects[1:]))  # Keep title

        best_practices = VGroup(
            Text("File Handling Best Practices", font_size=24, color=GOLD),
            Text("✅ Always use 'with' statements", font_size=18, color=GREEN),
            Text("✅ Handle exceptions appropriately", font_size=18, color=GREEN),
            Text("✅ Use meaningful error messages", font_size=18, color=GREEN),
            Text("✅ Log important events", font_size=18, color=GREEN),
            Text("✅ Validate file paths and permissions", font_size=18, color=GREEN),
            Text(
                "✅ Close files explicitly if not using 'with'",
                font_size=18,
                color=GREEN,
            ),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(best_practices))
        self.wait(4)


if __name__ == "__main__":
    from manimlib import config

    config.media_width = "854px"
    config.media_height = "480px"
    config.frame_rate = 30

    scene = FileHandlingErrorManagement()
    scene.render()
