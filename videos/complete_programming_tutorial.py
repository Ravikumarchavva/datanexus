from manimlib import *
import numpy as np


class CompleteProgrammingTutorial(Scene):
    def construct(self):
        """Main construction method for the complete tutorial"""
        # Set up the scene
        self.camera.background_color = "#0f0f23"

        # Title sequence
        self.intro_sequence()

        # Part 1: Computer Fundamentals
        self.computer_fundamentals()

        # Part 2: Binary and Data Representation
        self.binary_and_data()

        # Part 3: Programming as Communication
        self.programming_communication()

        # Part 4: Python Introduction
        self.python_introduction()

        # Part 5: Variables and Memory
        self.variables_and_memory()

        # Part 6: Data Types Deep Dive
        self.data_types_exploration()

        # Part 7: Input and Type Casting
        self.input_and_casting()

        # Part 8: Functions as Tools
        self.functions_as_tools()

        # Part 9: Control Flow
        self.control_flow()

        # Part 10: Loops and Iteration
        self.loops_and_iteration()

        # Conclusion
        self.conclusion()

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
        for _ in range(50):
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
            run_time=3,
        )

        # Clear for main content
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(particles), run_time=1.5)

    def computer_fundamentals(self):
        """Part 1: How computers work at the fundamental level"""
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
        off_state = Circle(radius=0.8, color="#808080", fill_opacity=0.3)  # Gray as hex

        on_label = Text("ON (Electricity flows)", font_size=20, color=WHITE)
        off_label = Text("OFF (No electricity)", font_size=20, color=WHITE)

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

        # Transition to binary
        binary_intro = Text(
            "These ON/OFF states become 1s and 0s\n(Binary Numbers)",
            font_size=32,
            color=BLUE,
        ).move_to(ORIGIN)

        self.play(
            Transform(explanation, binary_intro),
            Transform(
                on_label, Text("1", font_size=60, color=YELLOW).move_to(LEFT * 3)
            ),
            Transform(
                off_label, Text("0", font_size=60, color="#808080").move_to(RIGHT * 3)
            ),
        )
        self.wait(2)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title, explanation, on_state, off_state, on_label, off_label
                )
            )
        )

    def binary_and_data(self):
        """Part 2: Binary representation and how computers store data"""
        # Section title
        section_title = Text(
            "Binary: The Language of Computers", font_size=48, color=BLUE
        )
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Binary explanation with cricket analogy (following user's style)
        analogy = Text(
            "Think of binary like cricket scoring:\nEither you score a run (1) or you don't (0)",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(analogy))
        self.wait(2)

        # Show binary number formation
        binary_demo = Text("Let's count in binary:", font_size=32, color=GREEN)
        binary_demo.next_to(analogy, DOWN, buff=1)
        self.play(Write(binary_demo))

        # Animated binary counting
        numbers = VGroup()
        for i in range(8):
            decimal = Text(str(i), font_size=40, color=WHITE)
            binary = Text(format(i, "03b"), font_size=40, color=YELLOW)
            equals = Text("=", font_size=40, color=WHITE)

            row = VGroup(decimal, equals, binary).arrange(RIGHT, buff=0.3)
            numbers.add(row)

        numbers.arrange(DOWN, buff=0.3)
        numbers.next_to(binary_demo, DOWN, buff=0.5)

        # Animate counting
        for i, number_row in enumerate(numbers):
            self.play(Write(number_row), run_time=0.8)
            if i < 3:  # Pause on first few
                self.wait(0.5)

        self.wait(2)

        # Show how computers store different data
        storage_title = Text(
            "How Computers Store Different Types of Data", font_size=36, color=ORANGE
        )
        storage_title.to_edge(UP)

        self.play(
            Transform(section_title, storage_title),
            FadeOut(analogy),
            FadeOut(binary_demo),
            FadeOut(numbers),
        )

        # Data examples
        examples = VGroup(
            Text("Number 60 → 111100 (binary)", font_size=28, color=WHITE),
            Text("Letter 'A' → 01000001 (ASCII)", font_size=28, color=WHITE),
            Text(
                "Color Red → 11111111 00000000 00000000 (RGB)",
                font_size=28,
                color=WHITE,
            ),
        ).arrange(DOWN, buff=0.5)

        examples.move_to(ORIGIN)

        for example in examples:
            self.play(Write(example), run_time=1.5)
            self.wait(1)

        self.wait(2)

        # Memory visualization
        memory_title = Text(
            "Computer Memory: Like Numbered Boxes", font_size=32, color=PURPLE
        )
        memory_title.next_to(examples, DOWN, buff=1)

        self.play(Write(memory_title))

        # Create memory boxes
        memory_boxes = VGroup()
        for i in range(8):
            box = Rectangle(width=0.8, height=0.6, color=WHITE)
            address = Text(str(i), font_size=16, color="#808080").move_to(
                box.get_top() + UP * 0.2
            )
            content = Text("", font_size=20, color=YELLOW)
            memory_boxes.add(VGroup(box, address, content))

        memory_boxes.arrange(RIGHT, buff=0.1)
        memory_boxes.next_to(memory_title, DOWN, buff=0.5)

        self.play(FadeIn(memory_boxes))

        # Simulate storing data
        data_to_store = ["60", "5.2", "'A'", "True"]
        for i, data in enumerate(data_to_store):
            if i < len(memory_boxes):
                content_text = Text(data, font_size=16, color=YELLOW)
                content_text.move_to(memory_boxes[i][0].get_center())
                # Remove the old empty content and add new content
                memory_boxes[i].remove(memory_boxes[i][2])
                memory_boxes[i].add(content_text)
                self.play(Write(content_text), run_time=0.8)
                self.wait(0.5)

        self.wait(2)

        # Clear for next section
        self.play(FadeOut(VGroup(section_title, examples, memory_title, memory_boxes)))

    def programming_communication(self):
        """Part 3: Programming as communication with computers"""
        # Section title
        section_title = Text(
            "Programming: Talking to Computers", font_size=48, color=GREEN
        )
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Communication analogy
        human_computer = VGroup(
            Text("👤 Human", font_size=40, color=BLUE),
            Text("💻 Computer", font_size=40, color=GREEN),
        ).arrange(RIGHT, buff=4)

        human_computer.move_to(ORIGIN + UP)
        self.play(Write(human_computer))

        # Problem explanation
        problem_text = Text(
            "Problem: Humans think in words and concepts\nComputers only understand 1s and 0s",
            font_size=28,
            color=WHITE,
        ).next_to(human_computer, DOWN, buff=1)

        self.play(Write(problem_text))
        self.wait(2)

        # Solution: Programming languages
        solution_text = Text(
            "Solution: Programming Languages", font_size=36, color=YELLOW
        )
        solution_text.next_to(problem_text, DOWN, buff=1)
        self.play(Write(solution_text))

        # Show translation process
        translation_demo = VGroup(
            Text("Human Idea:", font_size=24, color=BLUE),
            Text('"Calculate cricket run rate"', font_size=20, color=WHITE),
            Text("↓", font_size=30, color=YELLOW),
            Text("Python Code:", font_size=24, color=GREEN),
            Text(
                "run_rate = runs / overs", font_size=20, color=ORANGE, font="monospace"
            ),
            Text("↓", font_size=30, color=YELLOW),
            Text("Computer Instructions:", font_size=24, color=PURPLE),
            Text(
                "10110101 11001010 01110011...",
                font_size=18,
                color="#808080",
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.3)

        translation_demo.next_to(solution_text, DOWN, buff=0.5)

        for item in translation_demo:
            self.play(Write(item), run_time=0.8)
            if "↓" not in item.text:
                self.wait(0.5)

        self.wait(3)

        # Clear for Python introduction
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    human_computer,
                    problem_text,
                    solution_text,
                    translation_demo,
                )
            )
        )

    def python_introduction(self):
        """Part 4: Why Python and what makes it special"""
        # Python logo-style animation
        python_title = Text("Why Python?", font_size=56, color="#3776ab")  # Python blue
        self.play(Write(python_title))
        self.wait(1)
        self.play(python_title.animate.to_edge(UP))

        # Python benefits with animations
        benefits = [
            ("🐍 Easy to Read", "Python looks almost like English"),
            ("🚀 Beginner Friendly", "Great for learning programming"),
            ("💪 Powerful", "Used by Google, Instagram, Netflix"),
            ("📚 Rich Libraries", "Tools for everything: web, AI, data science"),
        ]

        benefit_group = VGroup()
        for emoji_title, description in benefits:
            title_text = Text(emoji_title, font_size=32, color=GREEN)
            desc_text = Text(description, font_size=24, color=WHITE)
            benefit_item = VGroup(title_text, desc_text).arrange(DOWN, buff=0.2)
            benefit_group.add(benefit_item)

        benefit_group.arrange(DOWN, buff=0.8)
        benefit_group.move_to(ORIGIN)

        for benefit in benefit_group:
            self.play(FadeIn(benefit, shift=LEFT), run_time=1.5)
            self.wait(1)

        self.wait(2)

        # Show first Python code
        first_code_title = Text("Your First Python Program", font_size=36, color=YELLOW)
        first_code_title.next_to(benefit_group, DOWN, buff=1)

        self.play(Write(first_code_title))

        # Code example
        code_background = Rectangle(
            width=10,
            height=2,
            fill_color="#1e1e1e",
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=2,
        )

        code_text = Text(
            'print("Hello, World!")',
            font_size=28,
            color="#4ec9b0",  # Python string color
            font="monospace",
        )

        code_group = VGroup(code_background, code_text)
        code_group.next_to(first_code_title, DOWN, buff=0.5)

        self.play(FadeIn(code_background))
        self.play(Write(code_text, run_time=2))

        # Show output
        output_text = Text("Output: Hello, World!", font_size=24, color=GREEN)
        output_text.next_to(code_group, DOWN, buff=0.5)
        self.play(Write(output_text))

        self.wait(3)

        # Clear for variables section
        self.play(
            FadeOut(
                VGroup(
                    python_title,
                    benefit_group,
                    first_code_title,
                    code_group,
                    output_text,
                )
            )
        )

    def variables_and_memory(self):
        """Part 5: Variables as containers in computer memory"""
        # Section title
        section_title = Text(
            "Variables: Containers in Memory", font_size=48, color=ORANGE
        )
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Cricket analogy (following user's style)
        analogy_text = Text(
            "Think of variables like scoreboard labels:\nruns = 60, overs = 5.2",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(analogy_text))
        self.wait(2)

        # Memory representation
        memory_title = Text(
            "How This Looks in Computer Memory:", font_size=28, color=BLUE
        )
        memory_title.next_to(analogy_text, DOWN, buff=1)
        self.play(Write(memory_title))

        # Create variable boxes
        var_runs = self.create_variable_box("runs", "60", LEFT * 3)
        var_overs = self.create_variable_box("overs", "5.2", RIGHT * 3)

        self.play(FadeIn(var_runs), FadeIn(var_overs))
        self.wait(2)

        # Show Python code
        code_demo = VGroup(
            Text("Python Code:", font_size=24, color=GREEN),
            Text("runs = 60", font_size=20, color=YELLOW, font="monospace"),
            Text("overs = 5.2", font_size=20, color=YELLOW, font="monospace"),
            Text(
                "run_rate = runs / overs", font_size=20, color=YELLOW, font="monospace"
            ),
        ).arrange(DOWN, buff=0.3)

        code_demo.next_to(memory_title, DOWN, buff=1)

        for line in code_demo:
            self.play(Write(line), run_time=1)
            self.wait(0.5)

        # Calculate and show result
        var_run_rate = self.create_variable_box("run_rate", "11.54", ORIGIN + DOWN * 2)
        self.play(FadeIn(var_run_rate))

        # Connect with arrows
        arrow1 = Arrow(
            var_runs.get_right(), var_run_rate.get_left() + UP * 0.3, color=YELLOW
        )
        arrow2 = Arrow(
            var_overs.get_left(), var_run_rate.get_right() + UP * 0.3, color=YELLOW
        )

        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(2)

        # Type checking demonstration
        type_demo = Text(
            "Python automatically detects data types:", font_size=28, color=PURPLE
        )
        type_demo.to_edge(DOWN)
        self.play(Write(type_demo))

        # Show type checking
        type_annotations = VGroup(
            Text("int", font_size=16, color=RED).next_to(var_runs, UP),
            Text("float", font_size=16, color=RED).next_to(var_overs, UP),
            Text("float", font_size=16, color=RED).next_to(var_run_rate, UP),
        )

        self.play(Write(type_annotations))
        self.wait(3)

        # Clear for next section
        all_objects = VGroup(
            section_title,
            analogy_text,
            memory_title,
            var_runs,
            var_overs,
            var_run_rate,
            code_demo,
            arrow1,
            arrow2,
            type_demo,
            type_annotations,
        )
        self.play(FadeOut(all_objects))

    def create_variable_box(self, name, value, position):
        """Helper method to create a variable representation box"""
        box = Rectangle(width=2, height=1.2, color=WHITE, fill_opacity=0.1)
        name_text = Text(name, font_size=20, color=BLUE)
        value_text = Text(value, font_size=24, color=YELLOW)

        name_text.move_to(box.get_top() + DOWN * 0.3)
        value_text.move_to(box.get_center())

        var_group = VGroup(box, name_text, value_text)
        var_group.move_to(position)
        return var_group

    def data_types_exploration(self):
        """Part 6: Deep dive into Python data types"""
        # Section title
        section_title = Text("Python Data Types", font_size=48, color=PURPLE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Introduction
        intro_text = Text(
            "Python has several built-in data types\nfor different kinds of information:",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(intro_text))
        self.wait(1)

        # Data types with examples
        data_types = [
            ("Numbers", "int, float", "60, 5.2", BLUE),
            ("Text", "str", "'Rohit Sharma'", GREEN),
            ("True/False", "bool", "True, False", RED),
            ("Collections", "list, dict", "[1,2,3], {'runs': 60}", YELLOW),
        ]

        type_boxes = VGroup()
        for i, (category, type_name, example, color) in enumerate(data_types):
            # Create box for each data type
            box = Rectangle(width=6, height=1.5, color=color, fill_opacity=0.2)

            category_text = Text(category, font_size=24, color=color, weight=BOLD)
            type_text = Text(type_name, font_size=20, color=WHITE)
            example_text = Text(
                example, font_size=18, color="#808080", font="monospace"
            )

            content = VGroup(category_text, type_text, example_text).arrange(
                DOWN, buff=0.1
            )
            content.move_to(box.get_center())

            type_box = VGroup(box, content)
            type_boxes.add(type_box)

        # Arrange in 2x2 grid
        type_boxes[:2].arrange(RIGHT, buff=1)
        type_boxes[2:].arrange(RIGHT, buff=1)
        type_boxes[2:].next_to(type_boxes[:2], DOWN, buff=0.8)

        type_boxes.next_to(intro_text, DOWN, buff=1)

        # Animate each type
        for type_box in type_boxes:
            self.play(FadeIn(type_box, shift=UP), run_time=1.5)
            self.wait(0.8)

        self.wait(2)

        # Practical example with cricket data
        practical_title = Text(
            "Practical Example: Cricket Player Data", font_size=32, color=ORANGE
        )
        practical_title.to_edge(DOWN, buff=2)
        self.play(Write(practical_title))

        # Code example
        code_lines = [
            "player_name = 'Rohit Sharma'  # string",
            "runs_scored = 60             # integer",
            "strike_rate = 85.7          # float",
            "is_captain = True           # boolean",
        ]

        code_group = VGroup()
        for line in code_lines:
            code_text = Text(line, font_size=18, color=YELLOW, font="monospace")
            code_group.add(code_text)

        code_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        code_group.next_to(practical_title, UP, buff=0.5)

        for line in code_group:
            self.play(Write(line), run_time=1.2)
            self.wait(0.5)

        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title, intro_text, type_boxes, practical_title, code_group
                )
            )
        )

    def input_and_casting(self):
        """Part 7: Getting input and converting between types"""
        # Section title
        section_title = Text(
            "Getting Input & Type Conversion", font_size=44, color=TEAL
        )
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Input explanation
        input_explanation = Text(
            "Programs need to interact with users\nGetting input is like asking questions",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(input_explanation))
        self.wait(2)

        # Input demonstration
        input_demo = VGroup(
            Text("Python Code:", font_size=24, color=GREEN),
            Text(
                'num = input("Enter a number: ")',
                font_size=20,
                color=YELLOW,
                font="monospace",
            ),
            Text("print(type(num))", font_size=20, color=YELLOW, font="monospace"),
        ).arrange(DOWN, buff=0.3)

        input_demo.next_to(input_explanation, DOWN, buff=1)

        for line in input_demo:
            self.play(Write(line), run_time=1)
            self.wait(0.5)

        # Show the problem
        problem_box = Rectangle(width=8, height=2, color=RED, fill_opacity=0.2)
        problem_text = VGroup(
            Text(
                "Problem: input() always returns a string!",
                font_size=24,
                color=RED,
                weight=BOLD,
            ),
            Text(
                'Even if user types "123", Python stores it as "123"',
                font_size=20,
                color=WHITE,
            ),
            Text("not as the number 123", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        problem_group = VGroup(problem_box, problem_text)
        problem_text.move_to(problem_box.get_center())
        problem_group.next_to(input_demo, DOWN, buff=1)

        self.play(FadeIn(problem_box))
        self.play(Write(problem_text))
        self.wait(2)

        # Solution: Type casting
        solution_title = Text("Solution: Type Casting", font_size=32, color=GREEN)
        solution_title.next_to(problem_group, DOWN, buff=1)
        self.play(Write(solution_title))

        # Type casting examples
        casting_examples = VGroup(
            Text(
                'num_str = "123"      # string',
                font_size=18,
                color=WHITE,
                font="monospace",
            ),
            Text(
                'num_int = int("123") # convert to integer',
                font_size=18,
                color=YELLOW,
                font="monospace",
            ),
            Text(
                'num_float = float("123") # convert to float',
                font_size=18,
                color=YELLOW,
                font="monospace",
            ),
            Text(
                "back_to_str = str(123)   # convert back to string",
                font_size=18,
                color=YELLOW,
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        casting_examples.next_to(solution_title, DOWN, buff=0.5)

        for example in casting_examples:
            self.play(Write(example), run_time=1.2)
            self.wait(0.5)

        # Practical example
        practical = Text(
            "Practical: Calculate ticket fare from user input",
            font_size=24,
            color=ORANGE,
        )
        practical.to_edge(DOWN, buff=1.5)
        self.play(Write(practical))

        self.wait(3)

        # Clear for next section
        all_objects = VGroup(
            section_title,
            input_explanation,
            input_demo,
            problem_group,
            solution_title,
            casting_examples,
            practical,
        )
        self.play(FadeOut(all_objects))

    def functions_as_tools(self):
        """Part 8: Functions as reusable tools"""
        # Section title
        section_title = Text("Functions: Reusable Tools", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Real-world analogy
        analogy_text = Text(
            "Functions are like tools in a toolkit\nYou define them once, use them many times",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(analogy_text))
        self.wait(2)

        # Function anatomy
        anatomy_title = Text("Anatomy of a Function", font_size=32, color=GREEN)
        anatomy_title.next_to(analogy_text, DOWN, buff=1)
        self.play(Write(anatomy_title))

        # Function example with annotations
        function_code = '''def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"'''

        code_lines = function_code.split("\n")
        code_group = VGroup()

        for line in code_lines:
            code_text = Text(line, font_size=18, color=YELLOW, font="monospace")
            code_group.add(code_text)

        code_group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        code_group.next_to(anatomy_title, DOWN, buff=0.5)

        # Annotations
        annotations = [
            ("def - defines function", code_group[0], RIGHT),
            ("name - parameter", code_group[0], RIGHT),
            ("docstring - description", code_group[1], RIGHT),
            ("return - gives back result", code_group[2], RIGHT),
        ]

        for line in code_group:
            self.play(Write(line), run_time=1)
            self.wait(0.3)

        # Add annotations
        for i, (annotation, target, direction) in enumerate(annotations):
            if i < len(annotations):
                arrow = Arrow(
                    target.get_right(),
                    target.get_right() + RIGHT * 2,
                    color=RED,
                    buff=0.1,
                )
                annotation_text = Text(annotation, font_size=16, color=RED)
                annotation_text.next_to(arrow, RIGHT)

                self.play(GrowArrow(arrow), Write(annotation_text))
                self.wait(0.5)

        self.wait(2)

        # Cricket function example (user's style)
        cricket_title = Text(
            "Cricket Example: Calculate Strike Rate", font_size=28, color=ORANGE
        )
        cricket_title.to_edge(DOWN, buff=2.5)
        self.play(Write(cricket_title))

        cricket_function = VGroup(
            Text(
                "def calculate_strike_rate(runs, balls):",
                font_size=16,
                color=YELLOW,
                font="monospace",
            ),
            Text(
                "    return (runs / balls) * 100",
                font_size=16,
                color=YELLOW,
                font="monospace",
            ),
            Text("", font_size=16),
            Text("# Usage:", font_size=16, color=GREEN, font="monospace"),
            Text(
                "strike_rate = calculate_strike_rate(60, 40)",
                font_size=16,
                color=WHITE,
                font="monospace",
            ),
            Text(
                "print(f'Strike rate: {strike_rate}%')",
                font_size=16,
                color=WHITE,
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        cricket_function.next_to(cricket_title, UP, buff=0.3)

        for line in cricket_function:
            if line.text:  # Skip empty lines
                self.play(Write(line), run_time=1)
                self.wait(0.3)

        self.wait(3)

        # Clear for next section
        self.clear()

    def control_flow(self):
        """Part 9: Making decisions with if/else"""
        # Section title
        section_title = Text("Making Decisions: Control Flow", font_size=48, color=RED)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Decision making analogy
        decision_text = Text(
            "Programs need to make decisions\nJust like humans do every day",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(decision_text))
        self.wait(2)

        # Flowchart demonstration
        flowchart_title = Text("Decision Flowchart:", font_size=24, color=GREEN)
        flowchart_title.next_to(decision_text, DOWN, buff=1)
        self.play(Write(flowchart_title))

        # Create flowchart elements
        question_box = Rectangle(width=3, height=1, color=YELLOW)
        question_text = Text("Age >= 18?", font_size=18, color=BLACK)
        question = VGroup(question_box, question_text)

        yes_box = Rectangle(width=2.5, height=0.8, color=GREEN)
        yes_text = Text("Can get license", font_size=14, color=BLACK)
        yes_result = VGroup(yes_box, yes_text)

        no_box = Rectangle(width=2.5, height=0.8, color=RED)
        no_text = Text("Cannot get license", font_size=14, color=BLACK)
        no_result = VGroup(no_box, no_text)

        # Position elements
        question.next_to(flowchart_title, DOWN, buff=1)
        yes_result.next_to(question, DOWN + LEFT, buff=1)
        no_result.next_to(question, DOWN + RIGHT, buff=1)

        # Draw flowchart
        self.play(FadeIn(question))

        # Arrows
        yes_arrow = Arrow(question.get_bottom(), yes_result.get_top(), color=GREEN)
        no_arrow = Arrow(question.get_bottom(), no_result.get_top(), color=RED)

        yes_label = Text("Yes", font_size=16, color=GREEN)
        no_label = Text("No", font_size=16, color=RED)

        yes_label.next_to(yes_arrow, LEFT)
        no_label.next_to(no_arrow, RIGHT)

        self.play(
            GrowArrow(yes_arrow), Write(yes_label), GrowArrow(no_arrow), Write(no_label)
        )
        self.play(FadeIn(yes_result), FadeIn(no_result))
        self.wait(2)

        # Python if/else code
        code_title = Text("Python Code:", font_size=24, color=PURPLE)
        code_title.to_edge(DOWN, buff=2.5)
        self.play(Write(code_title))

        if_code = VGroup(
            Text("age = 20", font_size=18, color=YELLOW, font="monospace"),
            Text("if age >= 18:", font_size=18, color=YELLOW, font="monospace"),
            Text(
                "    print('Can get license')",
                font_size=18,
                color=WHITE,
                font="monospace",
            ),
            Text("else:", font_size=18, color=YELLOW, font="monospace"),
            Text(
                "    print('Cannot get license')",
                font_size=18,
                color=WHITE,
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        if_code.next_to(code_title, UP, buff=0.3)

        for line in if_code:
            self.play(Write(line), run_time=1)
            self.wait(0.3)

        self.wait(3)

        # Clear for next section
        self.clear()

    def loops_and_iteration(self):
        """Part 10: Repeating actions with loops"""
        # Section title
        section_title = Text("Loops: Repeating Actions", font_size=48, color=ORANGE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Loop concept
        loop_concept = Text(
            "Sometimes you need to repeat the same action\nLoops help you avoid writing repetitive code",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(loop_concept))
        self.wait(2)

        # Manual repetition vs loop
        manual_title = Text("Without Loops (Repetitive):", font_size=24, color=RED)
        manual_title.next_to(loop_concept, DOWN, buff=1)
        self.play(Write(manual_title))

        manual_code = VGroup(
            Text(
                "print('Iteration 0')", font_size=16, color="#808080", font="monospace"
            ),
            Text(
                "print('Iteration 1')", font_size=16, color="#808080", font="monospace"
            ),
            Text(
                "print('Iteration 2')", font_size=16, color="#808080", font="monospace"
            ),
            Text("# ... imagine 100 lines!", font_size=16, color=RED, font="monospace"),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)

        manual_code.next_to(manual_title, DOWN, buff=0.3)

        for line in manual_code:
            self.play(Write(line), run_time=0.8)

        # With loops
        loop_title = Text("With Loops (Elegant):", font_size=24, color=GREEN)
        loop_title.next_to(manual_code, DOWN, buff=1)
        self.play(Write(loop_title))

        loop_code = VGroup(
            Text("for i in range(3):", font_size=18, color=YELLOW, font="monospace"),
            Text(
                "    print(f'Iteration {i}')",
                font_size=18,
                color=WHITE,
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        loop_code.next_to(loop_title, DOWN, buff=0.3)

        for line in loop_code:
            self.play(Write(line), run_time=1)
            self.wait(0.5)

        # Animated loop execution
        execution_title = Text("Loop Execution:", font_size=20, color=BLUE)
        execution_title.next_to(loop_code, DOWN, buff=1)
        self.play(Write(execution_title))

        # Show loop iterations
        for i in range(3):
            iteration_text = Text(f"i = {i} → Iteration {i}", font_size=16, color=GREEN)
            iteration_text.next_to(execution_title, DOWN, buff=0.3 + i * 0.4)
            self.play(Write(iteration_text), run_time=1)
            self.wait(0.5)

        # Cricket example (user's style)
        cricket_example = Text(
            "Cricket Example: Calculate total runs", font_size=20, color=ORANGE
        )
        cricket_example.to_edge(DOWN, buff=1.5)
        self.play(Write(cricket_example))

        cricket_loop = VGroup(
            Text(
                "runs_per_over = [6, 12, 8, 15, 4]",
                font_size=16,
                color=YELLOW,
                font="monospace",
            ),
            Text("total_runs = 0", font_size=16, color=YELLOW, font="monospace"),
            Text(
                "for runs in runs_per_over:",
                font_size=16,
                color=YELLOW,
                font="monospace",
            ),
            Text("    total_runs += runs", font_size=16, color=WHITE, font="monospace"),
            Text(
                "print(f'Total: {total_runs} runs')",
                font_size=16,
                color=WHITE,
                font="monospace",
            ),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        cricket_loop.next_to(cricket_example, UP, buff=0.3)

        for line in cricket_loop:
            self.play(Write(line), run_time=1)
            self.wait(0.3)

        self.wait(3)

        # Clear for conclusion
        self.clear()

    def conclusion(self):
        """Conclusion - bringing it all together"""
        # Title
        conclusion_title = Text(
            "You've Learned Programming!", font_size=56, color=YELLOW
        )
        self.play(Write(conclusion_title))
        self.wait(1)
        self.play(conclusion_title.animate.to_edge(UP))

        # Journey recap
        journey_text = Text(
            "Your Journey: From Computer Basics to Python Programming",
            font_size=32,
            color=WHITE,
        ).next_to(conclusion_title, DOWN, buff=1)

        self.play(Write(journey_text))
        self.wait(1)

        # Key concepts learned
        concepts = [
            "✓ How computers work (binary, memory)",
            "✓ Programming as communication",
            "✓ Python syntax and data types",
            "✓ Variables and functions",
            "✓ Control flow and loops",
        ]

        concept_group = VGroup()
        for concept in concepts:
            concept_text = Text(concept, font_size=24, color=GREEN)
            concept_group.add(concept_text)

        concept_group.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        concept_group.next_to(journey_text, DOWN, buff=1)

        for concept in concept_group:
            self.play(Write(concept), run_time=1)
            self.wait(0.5)

        # Next steps
        next_steps_title = Text("Next Steps:", font_size=32, color=BLUE)
        next_steps_title.next_to(concept_group, DOWN, buff=1)
        self.play(Write(next_steps_title))

        next_steps = [
            "🚀 Practice with more Python projects",
            "📚 Explore libraries like pandas, matplotlib",
            "🌐 Build web applications with Flask/Django",
            "🤖 Dive into AI and machine learning",
        ]

        steps_group = VGroup()
        for step in next_steps:
            step_text = Text(step, font_size=20, color=WHITE)
            steps_group.add(step_text)

        steps_group.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        steps_group.next_to(next_steps_title, DOWN, buff=0.5)

        for step in steps_group:
            self.play(Write(step), run_time=1)
            self.wait(0.3)

        # Final message
        final_message = Text(
            "Keep coding, keep learning! 🐍", font_size=36, color=YELLOW
        ).to_edge(DOWN, buff=1)

        self.play(Write(final_message))

        # Celebration particles
        particles = VGroup()
        for _ in range(30):
            particle = Dot(radius=0.03, color=random_bright_color())
            particle.move_to([np.random.uniform(-7, 7), np.random.uniform(-4, 4), 0])
            particles.add(particle)

        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.1), run_time=2)

        # Final celebration animation
        self.play(
            LaggedStartMap(
                lambda p: p.animate.shift(
                    [np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0]
                ).set_color(random_bright_color()),
                particles,
                lag_ratio=0.05,
            ),
            run_time=4,
        )

        self.wait(3)

        # Fade out everything
        all_objects = VGroup(
            conclusion_title,
            journey_text,
            concept_group,
            next_steps_title,
            steps_group,
            final_message,
            particles,
        )
        self.play(FadeOut(all_objects, run_time=3))

        self.wait(2)


# This is the main scene that contains the complete tutorial
if __name__ == "__main__":
    # This allows the file to be run directly
    pass
