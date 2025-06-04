from manimlib import *
import numpy as np


class Module1TableOfContents(Scene):
    def construct(self):
        """Module 1: Course Overview & Table of Contents (15 min)"""
        # Set up the scene
        self.camera.background_color = "#0f0f23"

        # Course introduction
        self.course_intro()

        # Table of contents overview
        self.show_table_of_contents()

        # Learning objectives
        self.learning_objectives()

        # Course prerequisites and setup
        self.prerequisites_and_setup()

        # Module conclusion
        self.module_conclusion()

    def course_intro(self):
        """Welcome to the Python Programming Course"""
        # Create main title with gradient effect
        main_title = Text("Python Programming", font_size=80, color=BLUE)
        subtitle = Text("From Zero to Hero", font_size=60, color=GREEN)
        tagline = Text("Master Python in 6 Hours", font_size=40, color=YELLOW)

        # Position elements
        main_title.to_edge(UP, buff=1)
        subtitle.next_to(main_title, DOWN, buff=0.5)
        tagline.next_to(subtitle, DOWN, buff=1)

        # Create Python logo-inspired animation
        python_colors = [BLUE, YELLOW]
        python_rings = VGroup()
        for i, color in enumerate(python_colors):
            ring = Circle(radius=1.5 + i * 0.3, color=color)
            ring.set_stroke(width=8)
            ring.shift(RIGHT * i * 0.5)
            python_rings.add(ring)

        python_rings.next_to(tagline, DOWN, buff=1.5)

        # Animate introduction
        self.play(Write(main_title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(Write(tagline), run_time=1.5)

        # Animate Python rings
        self.play(
            LaggedStartMap(Create, python_rings, lag_ratio=0.3),
            run_time=2,
        )

        # Rotate rings
        self.play(
            Rotate(python_rings[0], PI / 2),
            Rotate(python_rings[1], -PI / 2),
            run_time=2,
        )

        # Welcome message
        welcome_msg = Text(
            "Welcome to your journey from beginner to Python expert!",
            font_size=36,
            color=WHITE,
        ).next_to(python_rings, DOWN, buff=1)

        self.play(Write(welcome_msg), run_time=2)
        self.wait(2)

        # Clear scene
        self.play(
            FadeOut(VGroup(main_title, subtitle, tagline, python_rings, welcome_msg))
        )

    def show_table_of_contents(self):
        """Display the complete course table of contents"""
        # Title
        toc_title = Text("Course Contents", font_size=64, color=BLUE)
        toc_title.to_edge(UP, buff=0.5)

        # Course modules with duration
        modules = [
            ("Module 1", "Course Introduction & Overview", "15 min"),
            ("Module 2", "Computer Fundamentals", "30 min"),
            ("Module 3", "Introduction to Python", "30 min"),
            ("Module 4", "Core Python Concepts", "60 min"),
            ("Module 5", "Functions & Modules", "45 min"),
            ("Module 6", "Object-Oriented Programming", "45 min"),
            ("Module 7", "Error Handling & Exceptions", "30 min"),
            ("Module 8", "File I/O & Context Managers", "30 min"),
            ("Module 9", "Advanced Topics", "60 min"),
            ("Module 10", "Putting It All Together", "30 min"),
            ("Module 11", "Next Steps & Resources", "15 min"),
        ]

        self.play(Write(toc_title))

        # Create module list
        module_list = VGroup()
        colors = [
            BLUE,
            GREEN,
            YELLOW,
            RED,
            PURPLE,
            PINK,
            ORANGE,
            TEAL,
            MAROON,
            GRAY,
            WHITE,
        ]

        for i, (mod_num, mod_name, duration) in enumerate(modules):
            color = colors[i % len(colors)]

            # Module number
            num_text = Text(mod_num, font_size=32, color=color, weight=BOLD)

            # Module name
            name_text = Text(mod_name, font_size=28, color=WHITE)

            # Duration
            dur_text = Text(f"({duration})", font_size=24, color=GRAY)

            # Arrange horizontally
            module_row = VGroup(num_text, name_text, dur_text)
            module_row.arrange(RIGHT, buff=0.5)
            module_row.set_width(12)

            # Left align the module name
            name_text.shift(LEFT * 2)
            dur_text.to_edge(RIGHT, buff=1)

            module_list.add(module_row)

        # Arrange modules vertically
        module_list.arrange(DOWN, buff=0.4)
        module_list.next_to(toc_title, DOWN, buff=1)
        module_list.scale(0.85)

        # Animate each module appearing
        for i, module_row in enumerate(module_list):
            self.play(FadeIn(module_row), run_time=0.3)

        # Total duration
        total_text = Text(
            "Total Duration: ~6 Hours", font_size=36, color=YELLOW, weight=BOLD
        )
        total_text.next_to(module_list, DOWN, buff=1)

        self.play(Write(total_text), run_time=1)
        self.wait(3)

        # Clear scene
        self.play(FadeOut(VGroup(toc_title, module_list, total_text)))

    def learning_objectives(self):
        """Show what students will learn"""
        # Title
        objectives_title = Text("What You'll Learn", font_size=64, color=GREEN)
        objectives_title.to_edge(UP, buff=0.5)

        # Learning objectives
        objectives = [
            "🖥️  How computers work at the fundamental level",
            "🐍  Python syntax, data types, and control structures",
            "🔧  Functions, modules, and code organization",
            "🏗️  Object-oriented programming concepts",
            "🐛  Error handling and debugging techniques",
            "📁  File operations and data management",
            "🚀  Advanced Python features and best practices",
            "🛠️  Building real-world projects",
            "📚  Resources for continued learning",
        ]

        self.play(Write(objectives_title))

        # Create objective list
        obj_list = VGroup()
        for obj in objectives:
            obj_text = Text(obj, font_size=32, color=WHITE)
            obj_list.add(obj_text)

        obj_list.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        obj_list.next_to(objectives_title, DOWN, buff=1)
        obj_list.shift(LEFT * 2)

        # Animate objectives
        for obj_text in obj_list:
            self.play(Write(obj_text), run_time=0.8)

        # Success message
        success_msg = Text(
            "By the end, you'll be confident writing Python code!",
            font_size=36,
            color=YELLOW,
        )
        success_msg.next_to(obj_list, DOWN, buff=1.5)

        self.play(Write(success_msg), run_time=2)
        self.wait(3)

        # Clear scene
        self.play(FadeOut(VGroup(objectives_title, obj_list, success_msg)))

    def prerequisites_and_setup(self):
        """Show prerequisites and setup requirements"""
        # Title
        setup_title = Text("Prerequisites & Setup", font_size=64, color=PURPLE)
        setup_title.to_edge(UP, buff=0.5)

        self.play(Write(setup_title))

        # Prerequisites section
        prereq_header = Text("Prerequisites:", font_size=40, color=YELLOW)
        prereq_header.next_to(setup_title, DOWN, buff=1)
        prereq_header.to_edge(LEFT, buff=1)

        prereq_list = [
            "✅ Basic computer literacy",
            "✅ Curiosity and willingness to learn",
            "✅ No prior programming experience needed!",
        ]

        prereq_items = VGroup()
        for item in prereq_list:
            text = Text(item, font_size=32, color=WHITE)
            prereq_items.add(text)

        prereq_items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        prereq_items.next_to(prereq_header, DOWN, buff=0.5)
        prereq_items.shift(RIGHT * 0.5)

        self.play(Write(prereq_header))
        for item in prereq_items:
            self.play(Write(item), run_time=0.6)

        # Setup section
        setup_header = Text("What You'll Need:", font_size=40, color=YELLOW)
        setup_header.next_to(prereq_items, DOWN, buff=1.5)
        setup_header.to_edge(LEFT, buff=1)

        setup_list = [
            "🖥️  A computer (Windows, Mac, or Linux)",
            "🐍  Python 3.8+ (we'll show you how to install)",
            "📝  A text editor or IDE (VS Code recommended)",
            "🌐  Internet connection for downloading packages",
        ]

        setup_items = VGroup()
        for item in setup_list:
            text = Text(item, font_size=32, color=WHITE)
            setup_items.add(text)

        setup_items.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        setup_items.next_to(setup_header, DOWN, buff=0.5)
        setup_items.shift(RIGHT * 0.5)

        self.play(Write(setup_header))
        for item in setup_items:
            self.play(Write(item), run_time=0.6)

        # Ready message
        ready_msg = Text(
            "Don't worry - we'll guide you through the setup process!",
            font_size=36,
            color=GREEN,
        )
        ready_msg.next_to(setup_items, DOWN, buff=1.5)

        self.play(Write(ready_msg), run_time=2)
        self.wait(3)

        # Clear scene
        self.play(
            FadeOut(
                VGroup(
                    setup_title,
                    prereq_header,
                    prereq_items,
                    setup_header,
                    setup_items,
                    ready_msg,
                )
            )
        )

    def module_conclusion(self):
        """Conclude Module 1"""
        # Title
        conclusion_title = Text("Ready to Begin?", font_size=72, color=BLUE)

        # Message
        conclusion_msg = Text(
            "Let's start with understanding how computers work!",
            font_size=40,
            color=WHITE,
        ).next_to(conclusion_title, DOWN, buff=1)

        # Next module preview
        next_module = Text(
            "Next: Module 2 - Computer Fundamentals", font_size=36, color=GREEN
        )
        next_module.next_to(conclusion_msg, DOWN, buff=1.5)

        # Animate conclusion
        self.play(Write(conclusion_title), run_time=2)
        self.play(Write(conclusion_msg), run_time=1.5)
        self.play(Write(next_module), run_time=1.5)

        # Create excitement particles
        particles = VGroup()
        for _ in range(30):
            particle = Circle(radius=0.05, color=random_bright_color())
            particle.move_to(
                [
                    np.random.uniform(-7, 7),
                    np.random.uniform(-3, 3),
                    0,
                ]
            )
            particles.add(particle)

        self.play(
            LaggedStartMap(FadeIn, particles, lag_ratio=0.05),
            run_time=2,
        )

        # Animate particles
        self.play(
            LaggedStartMap(
                lambda p: p.animate.shift(
                    [
                        np.random.uniform(-2, 2),
                        np.random.uniform(-2, 2),
                        0,
                    ]
                ).scale(np.random.uniform(0.5, 2)),
                particles,
                lag_ratio=0.02,
            ),
            run_time=3,
        )

        self.wait(2)


class Module2ComputerFundamentals(Scene):
    def construct(self):
        """Module 2: Computer Fundamentals & Data Representation (30 min)"""
        # Set up the scene
        self.camera.background_color = "#0f0f23"

        # Module introduction
        self.module_intro()

        # 2.1: What is a computer?
        self.what_is_computer()

        # 2.2: Hardware vs Software
        self.hardware_vs_software()

        # 2.3: Electricity and transistors
        self.electricity_and_transistors()

        # 2.4: ON/OFF states to bits
        self.on_off_to_bits()

        # 2.5: Bits to bytes and memory
        self.bits_to_bytes()

        # 2.6: Binary number system
        self.binary_numbers()

        # 2.7: Data encoding (ASCII, RGB, etc.)
        self.data_encoding()

        # 2.8: Why programming languages are needed
        self.why_programming_languages()

        # Module conclusion
        self.module_conclusion()

    def module_intro(self):
        """Introduction to Module 2"""
        # Title with animated particles
        main_title = Text("Module 2", font_size=72, color=BLUE)
        subtitle = Text("Computer Fundamentals", font_size=56, color=GREEN)
        description = Text(
            "Understanding how computers work at the deepest level",
            font_size=32,
            color=WHITE,
        )

        # Position elements
        main_title.to_edge(UP, buff=1)
        subtitle.next_to(main_title, DOWN, buff=0.5)
        description.next_to(subtitle, DOWN, buff=1)

        # Create flowing data particles
        particles = VGroup()
        for _ in range(60):
            # Mix of 1s and 0s as particles
            char = np.random.choice(["1", "0"])
            particle = Text(char, font_size=20, color=random_bright_color())
            particle.move_to([np.random.uniform(-8, 8), np.random.uniform(-4, 4), 0])
            particles.add(particle)

        # Animate introduction
        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.05), run_time=2)

        self.play(Write(main_title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(Write(description), run_time=1.5)

        # Floating binary animation
        self.play(
            LaggedStartMap(
                lambda p: p.animate.shift(
                    [np.random.uniform(-0.3, 0.3), np.random.uniform(-0.3, 0.3), 0]
                ).set_color(random_bright_color()),
                particles,
                lag_ratio=0.02,
            ),
            run_time=3,
        )

        self.wait(2)

        # Clear for next section
        self.play(FadeOut(VGroup(main_title, subtitle, description, particles)))

    def what_is_computer(self):
        """2.1: What is a computer?"""
        # Section title
        section_title = Text("What is a Computer?", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Definition
        definition = Text(
            "A computer is a machine that can store, retrieve,\nand process data according to instructions.",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(definition))
        self.wait(2)

        # Show different types of computers
        computer_types = VGroup(
            Text("💻 Laptop", font_size=28, color=BLUE),
            Text("📱 Smartphone", font_size=28, color=GREEN),
            Text("🖥️ Desktop", font_size=28, color=YELLOW),
            Text("⌚ Smartwatch", font_size=28, color=PURPLE),
            Text("🚗 Car Computer", font_size=28, color=RED),
            Text("🤖 Robot", font_size=28, color=PINK),
        ).arrange_in_grid(n_rows=2, n_cols=3, buff=1)

        computer_types.next_to(definition, DOWN, buff=1.5)

        # Animate computer types appearing
        for computer in computer_types:
            self.play(FadeIn(computer, shift=UP), run_time=0.8)
            self.wait(0.3)

        # Key insight
        insight = Text(
            "All computers, no matter the size, work the same way at their core!",
            font_size=28,
            color=YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=1)

        self.play(Write(insight))
        self.wait(3)

        # Clear for next section
        self.play(FadeOut(VGroup(section_title, definition, computer_types, insight)))

    def hardware_vs_software(self):
        """2.2: Hardware vs Software distinction"""
        # Section title
        section_title = Text("Hardware vs Software", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Create two columns
        hardware_title = Text("Hardware", font_size=40, color=RED)
        software_title = Text("Software", font_size=40, color=GREEN)

        hardware_title.move_to(LEFT * 3 + UP * 2)
        software_title.move_to(RIGHT * 3 + UP * 2)

        self.play(Write(hardware_title), Write(software_title))

        # Hardware examples
        hardware_items = VGroup(
            Text("🔌 Physical components", font_size=20, color=WHITE),
            Text("💾 CPU (Processor)", font_size=20, color=WHITE),
            Text("🧠 Memory (RAM)", font_size=20, color=WHITE),
            Text("💽 Storage (Hard drive)", font_size=20, color=WHITE),
            Text("📺 Screen", font_size=20, color=WHITE),
            Text("⌨️ Keyboard", font_size=20, color=WHITE),
            Text("🔧 You can touch it!", font_size=20, color=RED, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        hardware_items.next_to(hardware_title, DOWN, buff=0.5)

        # Software examples
        software_items = VGroup(
            Text("💻 Instructions & Programs", font_size=20, color=WHITE),
            Text("🐍 Python", font_size=20, color=WHITE),
            Text("🌐 Web Browser", font_size=20, color=WHITE),
            Text("🎮 Games", font_size=20, color=WHITE),
            Text("📱 Apps", font_size=20, color=WHITE),
            Text("🖼️ Operating System", font_size=20, color=WHITE),
            Text("👻 You can't touch it!", font_size=20, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)

        software_items.next_to(software_title, DOWN, buff=0.5)

        # Animate items appearing
        for hw, sw in zip(hardware_items, software_items):
            self.play(FadeIn(hw, shift=RIGHT), FadeIn(sw, shift=LEFT), run_time=0.8)
            self.wait(0.2)

        # Connection explanation
        connection = Text(
            "Hardware and Software work together:\nSoftware tells Hardware what to do!",
            font_size=28,
            color=YELLOW,
        ).to_edge(DOWN, buff=1)

        self.play(Write(connection))

        # Animated connection
        arrow = Arrow(
            software_title.get_bottom() + DOWN * 0.5,
            hardware_title.get_bottom() + DOWN * 0.5,
            color=YELLOW,
            stroke_width=6,
        )

        self.play(GrowArrow(arrow))
        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    hardware_title,
                    software_title,
                    hardware_items,
                    software_items,
                    connection,
                    arrow,
                )
            )
        )

    def electricity_and_transistors(self):
        """2.3: Electricity, transistors, and the foundation of computing"""
        # Section title
        section_title = Text("The Foundation: Electricity", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Electricity explanation
        explanation = Text(
            "Computers are fundamentally electrical devices\n"
            "Everything inside runs on electricity!",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(explanation))
        self.wait(2)

        # Show transistor concept
        transistor_title = Text("Meet the Transistor", font_size=36, color=BLUE)
        transistor_title.next_to(explanation, DOWN, buff=1)
        self.play(Write(transistor_title))

        # Visual transistor representation
        transistor_box = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.3)
        transistor_box.next_to(transistor_title, DOWN, buff=0.5)

        # Input/output labels
        input_label = Text("Input", font_size=20, color=WHITE)
        output_label = Text("Output", font_size=20, color=WHITE)

        input_label.next_to(transistor_box, LEFT, buff=0.5)
        output_label.next_to(transistor_box, RIGHT, buff=0.5)

        # Control label
        control_label = Text("Control", font_size=20, color=YELLOW)
        control_label.next_to(transistor_box, UP, buff=0.3)

        transistor_group = VGroup(
            transistor_box, input_label, output_label, control_label
        )

        self.play(FadeIn(transistor_group))

        # Show transistor states
        state_explanation = Text(
            "A transistor can be in two states:", font_size=24, color=WHITE
        ).next_to(transistor_group, DOWN, buff=1)

        self.play(Write(state_explanation))

        # State demonstrations
        on_state = Text("ON: Electricity flows through ⚡", font_size=22, color=GREEN)
        off_state = Text("OFF: No electricity flows ⭕", font_size=22, color=RED)

        on_state.next_to(state_explanation, DOWN, buff=0.3)
        off_state.next_to(on_state, DOWN, buff=0.3)

        # Animate states
        self.play(Write(on_state))
        self.play(transistor_box.animate.set_fill(GREEN, opacity=0.7))
        self.wait(1)

        self.play(Write(off_state))
        self.play(transistor_box.animate.set_fill(RED, opacity=0.7))
        self.wait(1)

        # Multiple transistors
        scale_text = Text(
            "Modern processors have BILLIONS of these tiny switches!",
            font_size=28,
            color=YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=1)

        self.play(Write(scale_text))

        # Show grid of mini transistors
        mini_transistors = VGroup()
        for i in range(8):
            for j in range(8):
                mini_trans = Rectangle(
                    width=0.2,
                    height=0.2,
                    color=np.random.choice([GREEN, RED]),
                    fill_opacity=0.8,
                )
                mini_trans.move_to([-2 + i * 0.3, -1 + j * 0.3, 0])
                mini_transistors.add(mini_trans)

        self.play(LaggedStartMap(FadeIn, mini_transistors, lag_ratio=0.02))

        # Animate random switching
        for _ in range(3):
            self.play(
                LaggedStartMap(
                    lambda t: t.animate.set_color(np.random.choice([GREEN, RED])),
                    mini_transistors,
                    lag_ratio=0.01,
                ),
                run_time=1,
            )
            self.wait(0.5)

        self.wait(2)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    explanation,
                    transistor_title,
                    transistor_group,
                    state_explanation,
                    on_state,
                    off_state,
                    scale_text,
                    mini_transistors,
                )
            )
        )

    def on_off_to_bits(self):
        """2.4: From ON/OFF states to bits"""
        # Section title
        section_title = Text("From Switches to Numbers", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Connection explanation
        connection_text = Text(
            "How do we turn ON/OFF switches into useful information?",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(connection_text))
        self.wait(2)

        # Show the mapping
        mapping_title = Text(
            "Simple Solution: Use Numbers!", font_size=36, color=YELLOW
        )
        mapping_title.next_to(connection_text, DOWN, buff=1)
        self.play(Write(mapping_title))

        # Visual mapping
        switch_on = Circle(radius=0.8, color=GREEN, fill_opacity=0.8)
        switch_off = Circle(radius=0.8, color=RED, fill_opacity=0.8)

        switch_on.move_to(LEFT * 4 + UP * 0.5)
        switch_off.move_to(LEFT * 4 + DOWN * 1.5)

        # Labels
        on_label = Text("Switch ON", font_size=24, color=WHITE)
        off_label = Text("Switch OFF", font_size=24, color=WHITE)

        on_label.next_to(switch_on, LEFT, buff=0.5)
        off_label.next_to(switch_off, LEFT, buff=0.5)

        # Arrows
        arrow_on = Arrow(switch_on.get_right(), RIGHT * 1.5 + UP * 0.5, color=WHITE)
        arrow_off = Arrow(switch_off.get_right(), RIGHT * 1.5 + DOWN * 1.5, color=WHITE)

        # Numbers
        number_1 = Text("1", font_size=60, color=GREEN, weight=BOLD)
        number_0 = Text("0", font_size=60, color=RED, weight=BOLD)

        number_1.move_to(RIGHT * 2.5 + UP * 0.5)
        number_0.move_to(RIGHT * 2.5 + DOWN * 1.5)

        # Animate the mapping
        mapping_group = VGroup(
            switch_on,
            switch_off,
            on_label,
            off_label,
            arrow_on,
            arrow_off,
            number_1,
            number_0,
        )

        self.play(FadeIn(switch_on), Write(on_label))
        self.play(GrowArrow(arrow_on), Write(number_1))
        self.wait(1)

        self.play(FadeIn(switch_off), Write(off_label))
        self.play(GrowArrow(arrow_off), Write(number_0))
        self.wait(1)

        # Binary introduction
        binary_intro = Text(
            "This is called BINARY - a number system using only 1s and 0s!",
            font_size=28,
            color=YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=1)

        self.play(Write(binary_intro))

        # Each digit is a "bit"
        bit_explanation = Text(
            "Each 1 or 0 is called a 'bit' (binary digit)", font_size=24, color=WHITE
        ).next_to(binary_intro, UP, buff=0.5)

        self.play(Write(bit_explanation))
        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    connection_text,
                    mapping_title,
                    mapping_group,
                    binary_intro,
                    bit_explanation,
                )
            )
        )

    def bits_to_bytes(self):
        """2.5: How bits form bytes and words"""
        # Section title
        section_title = Text("Bits → Bytes → Memory", font_size=48, color=PURPLE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Single bit demonstration
        bit_title = Text(
            "Single Bit (can store very little)", font_size=32, color=WHITE
        )
        bit_title.next_to(section_title, DOWN, buff=1)
        self.play(Write(bit_title))

        single_bit = Text("1", font_size=48, color=GREEN)
        single_bit.next_to(bit_title, DOWN, buff=0.5)
        self.play(Write(single_bit))

        bit_values = Text("Can only represent: 0 or 1", font_size=24, color="#808080")
        bit_values.next_to(single_bit, DOWN, buff=0.3)
        self.play(Write(bit_values))

        # Multiple bits
        multi_bit_title = Text(
            "Multiple Bits (more possibilities!)", font_size=32, color=WHITE
        )
        multi_bit_title.next_to(bit_values, DOWN, buff=1)
        self.play(Write(multi_bit_title))

        # Show 2 bits
        two_bits = VGroup(
            Text("2 bits:", font_size=24, color=BLUE),
            Text("00", font_size=36, color=YELLOW, font="monospace"),
            Text("01", font_size=36, color=YELLOW, font="monospace"),
            Text("10", font_size=36, color=YELLOW, font="monospace"),
            Text("11", font_size=36, color=YELLOW, font="monospace"),
            Text("(4 possibilities)", font_size=20, color="#808080"),
        ).arrange(RIGHT, buff=0.3)

        two_bits.next_to(multi_bit_title, DOWN, buff=0.5)

        for item in two_bits:
            self.play(Write(item), run_time=0.8)
            if item.text in ["00", "01", "10", "11"]:
                self.wait(0.3)

        # Show 8 bits = 1 byte
        byte_title = Text("8 Bits = 1 Byte", font_size=36, color=ORANGE, weight=BOLD)
        byte_title.next_to(two_bits, DOWN, buff=1)
        self.play(Write(byte_title))

        # Visual byte representation
        byte_boxes = VGroup()
        byte_values = "10110101"

        for i, bit in enumerate(byte_values):
            box = Rectangle(width=0.6, height=0.6, color=WHITE)
            bit_text = Text(
                bit, font_size=20, color=YELLOW if bit == "1" else "#808080"
            )
            bit_text.move_to(box.get_center())

            bit_group = VGroup(box, bit_text)
            byte_boxes.add(bit_group)

        byte_boxes.arrange(RIGHT, buff=0.1)
        byte_boxes.next_to(byte_title, DOWN, buff=0.5)

        self.play(LaggedStartMap(FadeIn, byte_boxes, lag_ratio=0.1))

        # Show byte capabilities
        byte_capability = Text(
            "1 byte can represent 256 different values (0-255)",
            font_size=24,
            color=GREEN,
        ).next_to(byte_boxes, DOWN, buff=0.5)

        self.play(Write(byte_capability))

        # Memory visualization
        memory_title = Text(
            "Computer Memory = Millions of Bytes", font_size=28, color=BLUE
        )
        memory_title.next_to(byte_capability, DOWN, buff=1)
        self.play(Write(memory_title))

        # Show memory grid
        memory_grid = VGroup()
        for i in range(8):
            for j in range(16):
                addr_box = Rectangle(
                    width=0.3, height=0.2, color=WHITE, fill_opacity=0.1
                )
                addr_box.move_to([-2.4 + j * 0.3, 1 - i * 0.25, 0])
                memory_grid.add(addr_box)

        memory_grid.to_edge(DOWN, buff=1)
        self.play(LaggedStartMap(FadeIn, memory_grid, lag_ratio=0.01), run_time=2)

        # Show addressing
        address_text = Text(
            "Each byte has a unique address (like house numbers)",
            font_size=20,
            color=YELLOW,
        ).next_to(memory_grid, UP, buff=0.2)

        self.play(Write(address_text))
        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    bit_title,
                    single_bit,
                    bit_values,
                    multi_bit_title,
                    two_bits,
                    byte_title,
                    byte_boxes,
                    byte_capability,
                    memory_title,
                    memory_grid,
                    address_text,
                )
            )
        )

    def binary_numbers(self):
        """2.6: Understanding the binary number system"""
        # Section title
        section_title = Text("Binary Number System", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Decimal vs Binary comparison
        comparison_title = Text("Decimal vs Binary", font_size=36, color=WHITE)
        comparison_title.next_to(section_title, DOWN, buff=1)
        self.play(Write(comparison_title))

        # Decimal explanation
        decimal_title = Text("Decimal (Base 10)", font_size=28, color=GREEN)
        decimal_title.move_to(LEFT * 3 + UP * 1)
        self.play(Write(decimal_title))

        decimal_digits = Text(
            "Uses digits: 0,1,2,3,4,5,6,7,8,9", font_size=20, color=WHITE
        )
        decimal_digits.next_to(decimal_title, DOWN, buff=0.3)
        self.play(Write(decimal_digits))

        # Binary explanation
        binary_title = Text("Binary (Base 2)", font_size=28, color=ORANGE)
        binary_title.move_to(RIGHT * 3 + UP * 1)
        self.play(Write(binary_title))

        binary_digits = Text("Uses digits: 0,1", font_size=20, color=WHITE)
        binary_digits.next_to(binary_title, DOWN, buff=0.3)
        self.play(Write(binary_digits))

        # Counting demonstration
        counting_title = Text(
            "Let's count in both systems:", font_size=24, color=YELLOW
        )
        counting_title.next_to(comparison_title, DOWN, buff=2)
        self.play(Write(counting_title))

        # Create counting table
        table_headers = VGroup(
            Text("Decimal", font_size=24, color=GREEN, weight=BOLD),
            Text("Binary", font_size=24, color=ORANGE, weight=BOLD),
        ).arrange(RIGHT, buff=3)

        table_headers.next_to(counting_title, DOWN, buff=0.5)
        self.play(Write(table_headers))

        # Animated counting
        counting_pairs = [
            ("0", "0"),
            ("1", "1"),
            ("2", "10"),
            ("3", "11"),
            ("4", "100"),
            ("5", "101"),
            ("6", "110"),
            ("7", "111"),
            ("8", "1000"),
        ]

        table_rows = VGroup()

        for i, (decimal, binary) in enumerate(counting_pairs):
            decimal_text = Text(decimal, font_size=20, color=GREEN, font="monospace")
            binary_text = Text(binary, font_size=20, color=ORANGE, font="monospace")

            row = VGroup(decimal_text, binary_text).arrange(RIGHT, buff=3.3)
            table_rows.add(row)

        table_rows.arrange(DOWN, buff=0.2)
        table_rows.next_to(table_headers, DOWN, buff=0.3)

        # Animate each row
        for i, row in enumerate(table_rows):
            self.play(Write(row), run_time=0.8)
            if i < 4:  # Pause on first few
                self.wait(0.5)
            else:
                self.wait(0.2)

        # Binary place values explanation
        place_value_title = Text("Binary Place Values", font_size=28, color=PURPLE)
        place_value_title.to_edge(DOWN, buff=2)
        self.play(Write(place_value_title))

        # Show place value breakdown for 1101 (13 in decimal)
        binary_example = "1101"
        place_values = [8, 4, 2, 1]  # 2^3, 2^2, 2^1, 2^0

        place_group = VGroup()
        calculation = []

        for i, (bit, value) in enumerate(zip(binary_example, place_values)):
            # Bit display
            bit_text = Text(bit, font_size=32, color=YELLOW, font="monospace")

            # Place value
            place_text = Text(f"×{value}", font_size=20, color=WHITE)
            place_text.next_to(bit_text, DOWN, buff=0.1)

            # Result
            result = int(bit) * value
            result_text = Text(f"={result}", font_size=16, color=GREEN)
            result_text.next_to(place_text, DOWN, buff=0.1)

            bit_group = VGroup(bit_text, place_text, result_text)
            place_group.add(bit_group)

            if bit == "1":
                calculation.append(result)

        place_group.arrange(RIGHT, buff=0.5)
        place_group.next_to(place_value_title, UP, buff=0.5)

        self.play(LaggedStartMap(FadeIn, place_group, lag_ratio=0.3))

        # Show final calculation
        final_calc = Text(
            f"= {' + '.join(map(str, calculation))} = {sum(calculation)}",
            font_size=24,
            color=GREEN,
        )
        final_calc.next_to(place_group, DOWN, buff=0.3)
        self.play(Write(final_calc))

        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    comparison_title,
                    decimal_title,
                    decimal_digits,
                    binary_title,
                    binary_digits,
                    counting_title,
                    table_headers,
                    table_rows,
                    place_value_title,
                    place_group,
                    final_calc,
                )
            )
        )

    def data_encoding(self):
        """2.7: How different types of data are encoded in binary"""
        # Section title
        section_title = Text("Encoding Data in Binary", font_size=48, color=ORANGE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Introduction
        intro_text = Text(
            "How do we represent text, colors, sounds, and images using only 1s and 0s?",
            font_size=28,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(intro_text))
        self.wait(2)

        # ASCII Encoding
        ascii_title = Text("Text Encoding: ASCII", font_size=36, color=BLUE)
        ascii_title.next_to(intro_text, DOWN, buff=1)
        self.play(Write(ascii_title))

        # Show ASCII example
        ascii_example = VGroup(
            Text("Letter 'A'", font_size=24, color=WHITE),
            Text("→", font_size=24, color=YELLOW),
            Text("ASCII code: 65", font_size=24, color=GREEN),
            Text("→", font_size=24, color=YELLOW),
            Text("Binary: 01000001", font_size=24, color=ORANGE, font="monospace"),
        ).arrange(RIGHT, buff=0.5)

        ascii_example.next_to(ascii_title, DOWN, buff=0.5)

        for item in ascii_example:
            self.play(Write(item), run_time=1)
            self.wait(0.5)

        # Show more ASCII examples
        ascii_table = VGroup(
            Text("'H' → 72 → 01001000", font_size=20, color=WHITE, font="monospace"),
            Text("'e' → 101 → 01100101", font_size=20, color=WHITE, font="monospace"),
            Text("'l' → 108 → 01101100", font_size=20, color=WHITE, font="monospace"),
            Text("'o' → 111 → 01101111", font_size=20, color=WHITE, font="monospace"),
            Text("' ' → 32 → 00100000", font_size=20, color=WHITE, font="monospace"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        ascii_table.next_to(ascii_example, DOWN, buff=0.5)

        hello_demo = Text("Encoding 'Hello':", font_size=20, color=YELLOW)
        hello_demo.next_to(ascii_table, LEFT, buff=1)

        self.play(Write(hello_demo))

        for row in ascii_table:
            self.play(Write(row), run_time=0.8)

        # Color Encoding (RGB)
        rgb_title = Text("Color Encoding: RGB", font_size=36, color=RED)
        rgb_title.to_edge(LEFT, buff=1).shift(DOWN * 1)
        self.play(Write(rgb_title))

        # RGB explanation
        rgb_explanation = VGroup(
            Text("Red: 255 → 11111111", font_size=18, color=RED, font="monospace"),
            Text("Green: 0 → 00000000", font_size=18, color=GREEN, font="monospace"),
            Text("Blue: 0 → 00000000", font_size=18, color=BLUE, font="monospace"),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        rgb_explanation.next_to(rgb_title, DOWN, buff=0.3)

        # Show color square
        color_square = Rectangle(width=1, height=1, fill_color=RED, fill_opacity=1)
        color_square.next_to(rgb_explanation, RIGHT, buff=1)

        self.play(Write(rgb_explanation), FadeIn(color_square))

        # Sound Encoding
        sound_title = Text("Sound: Digital Sampling", font_size=36, color=PURPLE)
        sound_title.to_edge(RIGHT, buff=1).shift(DOWN * 1)
        self.play(Write(sound_title))

        # Sound wave visualization
        sound_wave = VGroup()
        for i in range(20):
            x = -2 + i * 0.2
            y = 0.5 * np.sin(2 * np.pi * x)
            point = Dot([x, y, 0], radius=0.03, color=PURPLE)
            sound_wave.add(point)

        sound_wave.next_to(sound_title, DOWN, buff=0.3)
        self.play(LaggedStartMap(FadeIn, sound_wave, lag_ratio=0.1))

        sound_text = Text("Each sample → number → binary", font_size=16, color=WHITE)
        sound_text.next_to(sound_wave, DOWN, buff=0.2)
        self.play(Write(sound_text))

        # Key insight
        key_insight = Text(
            "Everything in a computer is ultimately just numbers in binary!",
            font_size=28,
            color=YELLOW,
            weight=BOLD,
        ).to_edge(DOWN, buff=1)

        self.play(Write(key_insight))
        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    intro_text,
                    ascii_title,
                    ascii_example,
                    hello_demo,
                    ascii_table,
                    rgb_title,
                    rgb_explanation,
                    color_square,
                    sound_title,
                    sound_wave,
                    sound_text,
                    key_insight,
                )
            )
        )

    def why_programming_languages(self):
        """2.8: Why we need programming languages"""
        # Section title
        section_title = Text("Why Programming Languages?", font_size=48, color=BLUE)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # The problem
        problem_title = Text("The Problem:", font_size=36, color=RED)
        problem_title.next_to(section_title, DOWN, buff=1)
        self.play(Write(problem_title))

        problem_text = Text(
            "Computers only understand machine code (1s and 0s)",
            font_size=28,
            color=WHITE,
        ).next_to(problem_title, DOWN, buff=0.5)

        self.play(Write(problem_text))

        # Show overwhelming binary code
        binary_code = VGroup(
            Text(
                "10110000 01100001 11010011 00101100",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text(
                "01010101 11110000 00110011 10101010",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text(
                "11100011 00001111 01010101 11000011",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text(
                "00110101 10101000 11011100 01000001",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text(
                "11010111 00110100 10101011 01001101",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text("... hundreds more lines ...", font_size=16, color=RED),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)

        binary_code.next_to(problem_text, DOWN, buff=0.5)

        for line in binary_code:
            self.play(Write(line), run_time=1)
            self.wait(0.3)

        # Human perspective
        human_perspective = Text(
            "Humans think: 'I want to add 5 + 3'", font_size=28, color=BLUE
        ).next_to(binary_code, DOWN, buff=1)

        self.play(Write(human_perspective))

        # The solution
        solution_title = Text(
            "The Solution: Programming Languages!", font_size=36, color=GREEN
        )
        solution_title.next_to(human_perspective, DOWN, buff=1)
        self.play(Write(solution_title))

        # Show Python example
        python_example = Text(
            "result = 5 + 3\nprint(result)",
            font_size=32,
            color=YELLOW,
            font="monospace",
        ).next_to(solution_title, DOWN, buff=0.5)

        self.play(Write(python_example))

        # Translation explanation
        translation_text = Text(
            "Programming languages translate human-readable code\ninto machine code",
            font_size=24,
            color=WHITE,
        ).next_to(python_example, DOWN, buff=1)

        self.play(Write(translation_text))

        # Show bridge visualization
        bridge = Arrow(
            python_example.get_bottom() + DOWN * 0.5,
            binary_code.get_top() + UP * 0.5,
            color=GREEN,
            stroke_width=6,
        )

        self.play(GrowArrow(bridge))

        bridge_label = Text("Translation", font_size=20, color=GREEN)
        bridge_label.next_to(bridge, RIGHT, buff=0.3)
        self.play(Write(bridge_label))

        self.wait(3)

        # Clear for conclusion
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    problem_title,
                    problem_text,
                    binary_code,
                    human_perspective,
                    solution_title,
                    python_example,
                    translation_text,
                    bridge,
                    bridge_label,
                )
            )
        )

    def module_conclusion(self):
        """Module 2 conclusion and transition"""
        # Title
        conclusion_title = Text("Module 2 Complete!", font_size=56, color=YELLOW)
        self.play(Write(conclusion_title))
        self.wait(1)
        self.play(conclusion_title.animate.to_edge(UP))

        # Summary of what we learned
        summary_title = Text("What We Learned:", font_size=36, color=WHITE)
        summary_title.next_to(conclusion_title, DOWN, buff=1)
        self.play(Write(summary_title))

        # Key concepts
        concepts = [
            "✓ Computers are electrical devices with ON/OFF states",
            "✓ ON/OFF becomes 1s and 0s (binary)",
            "✓ 8 bits = 1 byte, bytes form computer memory",
            "✓ All data (text, images, sound) is encoded in binary",
            "✓ Programming languages bridge human thinking and machine code",
        ]

        concept_group = VGroup()
        for concept in concepts:
            concept_text = Text(concept, font_size=24, color=WHITE)
            concept_group.add(concept_text)

        concept_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        concept_group.next_to(summary_title, DOWN, buff=1)
        concept_group.shift(LEFT * 1)

        # Animate concepts appearing
        for concept in concept_group:
            self.play(Write(concept), run_time=1)
            self.wait(0.5)

        # Next module preview
        next_preview = Text(
            "Next: Module 3 - Introduction to Python",
            font_size=32,
            color=GREEN,
        ).next_to(concept_group, DOWN, buff=1.5)

        self.play(Write(next_preview))

        # Celebration animation
        celebration = VGroup()
        for _ in range(20):
            star = Text("⭐", font_size=30, color=random_bright_color())
            star.move_to([np.random.uniform(-6, 6), np.random.uniform(-2, 2), 0])
            celebration.add(star)

        self.play(LaggedStartMap(FadeIn, celebration, lag_ratio=0.1))

        # Animate stars
        self.play(
            LaggedStartMap(
                lambda s: s.animate.shift(
                    [np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0]
                ).scale(np.random.uniform(0.5, 1.5)),
                celebration,
                lag_ratio=0.05,
            ),
            run_time=3,
        )

        self.wait(2)


class Module3IntroductionToPython(Scene):
    def construct(self):
        """Module 3: Introduction to Python (30 min)"""
        self.camera.background_color = "#0f0f23"

        # Module introduction
        self.module_intro()

        # Why Python?
        self.why_python()

        # Setting up the environment
        self.setup_environment()

        # First Python program
        self.first_python_program()

        # REPL vs Scripts
        self.repl_vs_scripts()

        # Basic syntax and variables
        self.basic_syntax_and_variables()

        # Module conclusion
        self.module_conclusion()

    def module_intro(self):
        """Introduction to Module 3"""
        # Create animated title
        title = Text("Module 3", font_size=64, color=BLUE)
        subtitle = Text("Introduction to Python", font_size=48, color=GREEN)

        title.to_edge(UP, buff=1)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Create Python snake animation
        snake_body = []
        colors = [BLUE, GREEN, YELLOW, RED]

        for i in range(8):
            segment = Circle(radius=0.3, color=colors[i % len(colors)])
            segment.move_to(RIGHT * i * 0.6)
            snake_body.append(segment)

        snake = VGroup(*snake_body)
        snake.next_to(subtitle, DOWN, buff=1)

        # Animate intro
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)

        # Animate snake
        self.play(LaggedStartMap(FadeIn, snake, lag_ratio=0.2), run_time=2)

        # Make snake wiggle
        for _ in range(3):
            self.play(
                *[
                    segment.animate.shift(UP * 0.2 * np.sin(i * PI / 4))
                    for i, segment in enumerate(snake_body)
                ],
                run_time=0.5,
            )
            self.play(
                *[
                    segment.animate.shift(DOWN * 0.2 * np.sin(i * PI / 4))
                    for i, segment in enumerate(snake_body)
                ],
                run_time=0.5,
            )

        self.wait(1)
        self.play(FadeOut(VGroup(title, subtitle, snake)))

    def why_python(self):
        """Why choose Python for programming?"""
        # Title
        title = Text("Why Python?", font_size=56, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Python advantages
        advantages = [
            ("🐍 Readable & Simple", "English-like syntax that's easy to learn"),
            ("🚀 Versatile", "Web, AI, Data Science, Automation, Games"),
            ("📚 Rich Ecosystem", "Millions of libraries and packages"),
            ("👥 Strong Community", "Helpful community and extensive documentation"),
            ("💼 Industry Demand", "High-paying jobs in tech companies"),
            ("🔧 Beginner-Friendly", "Perfect first programming language"),
        ]

        # Create advantage cards
        cards = VGroup()
        for i, (emoji_title, description) in enumerate(advantages):
            # Create card background
            card = RoundedRectangle(
                width=5.5,
                height=1.2,
                corner_radius=0.1,
                color=YELLOW,
                fill_opacity=0.1,
                stroke_width=2,
            )

            # Add emoji and title
            emoji_text = Text(emoji_title, font_size=28, color=YELLOW)
            emoji_text.move_to(card.get_top() + DOWN * 0.3)

            # Add description
            desc_text = Text(description, font_size=20, color=WHITE)
            desc_text.move_to(card.get_bottom() + UP * 0.3)

            card_group = VGroup(card, emoji_text, desc_text)
            cards.add(card_group)

        # Arrange cards in 2x3 grid
        cards.arrange_in_grid(rows=3, cols=2, buff=0.3)
        cards.next_to(title, DOWN, buff=0.8)

        # Animate cards appearing
        self.play(LaggedStartMap(FadeIn, cards, lag_ratio=0.3), run_time=4)
        self.wait(2)

        # Highlight some key advantages
        self.play(cards[0].animate.set_color(GREEN), run_time=1)  # Readable
        self.wait(0.5)
        self.play(cards[1].animate.set_color(GREEN), run_time=1)  # Versatile
        self.wait(0.5)
        self.play(cards[4].animate.set_color(GREEN), run_time=1)  # Industry demand

        self.wait(2)
        self.play(FadeOut(VGroup(title, cards)))

    def setup_environment(self):
        """Setting up Python development environment"""
        title = Text("Setting Up Your Environment", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Installation steps
        steps = [
            "1. Download Python from python.org",
            "2. Install Python (check 'Add to PATH')",
            "3. Verify installation: python --version",
            "4. Choose an IDE (VS Code, PyCharm, IDLE)",
            "5. Install packages with pip",
        ]

        step_objects = VGroup()
        for i, step in enumerate(steps):
            step_text = Text(step, font_size=32, color=WHITE)

            # Add checkmark animation
            checkmark = Text("✓", font_size=40, color=GREEN)
            checkmark.next_to(step_text, LEFT, buff=0.5)
            checkmark.set_opacity(0)

            step_group = VGroup(checkmark, step_text)
            step_objects.add(step_group)

        step_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        step_objects.next_to(title, DOWN, buff=1)

        # Animate steps with checkmarks
        for step_group in step_objects:
            checkmark, step_text = step_group
            self.play(Write(step_text), run_time=1)
            self.play(checkmark.animate.set_opacity(1), run_time=0.5)
            self.wait(0.5)

        # Show IDE comparison
        self.wait(1)

        # Create IDE comparison
        ide_title = Text("Popular Python IDEs", font_size=36, color=YELLOW)
        ide_title.move_to(UP * 1)

        ides = [
            ("VS Code", "Free, lightweight, great extensions"),
            ("PyCharm", "Professional, feature-rich, debugger"),
            ("IDLE", "Built-in, simple, good for beginners"),
            ("Jupyter", "Interactive, great for data science"),
        ]

        ide_cards = VGroup()
        for name, desc in ides:
            card = RoundedRectangle(
                width=2.8, height=1.5, corner_radius=0.1, color=BLUE, fill_opacity=0.1
            )
            name_text = Text(name, font_size=24, color=BLUE)
            desc_text = Text(desc, font_size=16, color=WHITE)

            name_text.move_to(card.get_top() + DOWN * 0.4)
            desc_text.move_to(card.get_center() + DOWN * 0.2)
            desc_text.scale(0.8)

            ide_card = VGroup(card, name_text, desc_text)
            ide_cards.add(ide_card)

        ide_cards.arrange(RIGHT, buff=0.3)
        ide_cards.next_to(ide_title, DOWN, buff=0.5)

        self.play(FadeOut(VGroup(title, step_objects)))
        self.play(Write(ide_title))
        self.play(LaggedStartMap(FadeIn, ide_cards, lag_ratio=0.2), run_time=2)

        self.wait(2)
        self.play(FadeOut(VGroup(ide_title, ide_cards)))

    def first_python_program(self):
        """Your first Python program - Hello World"""
        title = Text("Your First Python Program", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create code editor mockup
        editor_bg = Rectangle(width=10, height=6, color=BLACK, fill_opacity=0.9)
        editor_bg.set_stroke(color=GRAY, width=2)

        # Editor title bar
        title_bar = Rectangle(width=10, height=0.8, color=DARK_GRAY, fill_opacity=1)
        title_bar.move_to(editor_bg.get_top() + DOWN * 0.4)

        editor_title = Text("hello.py", font_size=20, color=WHITE)
        editor_title.move_to(title_bar)

        # Code content
        code_lines = [
            "# My first Python program",
            'print("Hello, World!")',
            "",
            "# Let's add more",
            'print("Welcome to Python programming!")',
            'print("Python is awesome!")',
        ]

        code_objects = VGroup()
        for i, line in enumerate(code_lines):
            if line.startswith("#"):
                # Comment line
                line_text = Text(line, font_size=24, color=GREEN)
            elif "print" in line:
                # Print statement
                line_text = Text(line, font_size=24, color=YELLOW)
            else:
                # Regular line
                line_text = Text(line, font_size=24, color=WHITE)

            line_text.move_to(editor_bg.get_top() + DOWN * (1.5 + i * 0.6))
            line_text.align_to(editor_bg.get_left() + RIGHT * 0.5, LEFT)
            code_objects.add(line_text)

        # Show editor
        self.play(Create(editor_bg))
        self.play(Create(title_bar), Write(editor_title))

        # Type code line by line
        for line_obj in code_objects:
            self.play(Write(line_obj), run_time=1)
            self.wait(0.3)

        # Show output
        output_title = Text("Output:", font_size=32, color=GREEN)
        output_title.next_to(editor_bg, DOWN, buff=0.5)
        output_title.align_to(editor_bg.get_left(), LEFT)

        output_lines = [
            "Hello, World!",
            "Welcome to Python programming!",
            "Python is awesome!",
        ]

        output_objects = VGroup()
        for i, output in enumerate(output_lines):
            output_text = Text(output, font_size=28, color=WHITE)
            output_text.next_to(output_title, DOWN, buff=0.3 + i * 0.4)
            output_text.align_to(output_title, LEFT)
            output_objects.add(output_text)

        self.play(Write(output_title))

        # Simulate running the program
        run_button = Circle(radius=0.3, color=GREEN, fill_opacity=1)
        play_symbol = Triangle(color=WHITE, fill_opacity=1).scale(0.3)
        play_symbol.move_to(run_button)
        run_group = VGroup(run_button, play_symbol)
        run_group.move_to(title_bar.get_right() + LEFT * 0.5)

        self.play(FadeIn(run_group))
        self.play(run_group.animate.scale(1.2), run_time=0.2)
        self.play(run_group.animate.scale(1), run_time=0.2)

        # Show output appearing
        for output_obj in output_objects:
            self.play(Write(output_obj), run_time=0.8)
            self.wait(0.3)

        # Celebration
        celebration = Text(
            "🎉 Congratulations! You've written your first Python program!",
            font_size=28,
            color=YELLOW,
        )
        celebration.next_to(output_objects, DOWN, buff=0.8)

        self.play(Write(celebration), run_time=2)
        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    title,
                    editor_bg,
                    title_bar,
                    editor_title,
                    code_objects,
                    output_title,
                    output_objects,
                    run_group,
                    celebration,
                )
            )
        )

    def repl_vs_scripts(self):
        """REPL vs Script files - Interactive vs File-based programming"""
        title = Text("REPL vs Script Files", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create split screen
        divider = Line(UP * 3, DOWN * 3, color=WHITE, stroke_width=2)

        # REPL side
        repl_title = Text("REPL (Interactive)", font_size=36, color=GREEN)
        repl_title.move_to(LEFT * 3 + UP * 2.5)

        repl_desc = VGroup(
            Text("• Read-Eval-Print Loop", font_size=20, color=WHITE),
            Text("• Interactive shell", font_size=20, color=WHITE),
            Text("• Test code quickly", font_size=20, color=WHITE),
            Text("• Immediate feedback", font_size=20, color=WHITE),
        )
        repl_desc.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        repl_desc.next_to(repl_title, DOWN, buff=0.5)

        # REPL demo
        repl_demo = VGroup(
            Text(">>> print('Hello')", font_size=20, color=YELLOW),
            Text("Hello", font_size=20, color=WHITE),
            Text(">>> 2 + 3", font_size=20, color=YELLOW),
            Text("5", font_size=20, color=WHITE),
            Text(">>> len('Python')", font_size=20, color=YELLOW),
            Text("6", font_size=20, color=WHITE),
        )
        repl_demo.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        repl_demo.next_to(repl_desc, DOWN, buff=0.5)

        # Script side
        script_title = Text("Script Files", font_size=36, color=BLUE)
        script_title.move_to(RIGHT * 3 + UP * 2.5)

        script_desc = VGroup(
            Text("• Save code in .py files", font_size=20, color=WHITE),
            Text("• Reusable programs", font_size=20, color=WHITE),
            Text("• Complex projects", font_size=20, color=WHITE),
            Text("• Share with others", font_size=20, color=WHITE),
        )
        script_desc.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        script_desc.next_to(script_title, DOWN, buff=0.5)

        # Script demo
        script_demo = VGroup(
            Text("# calculator.py", font_size=20, color=GREEN),
            Text("def add(a, b):", font_size=20, color=YELLOW),
            Text("    return a + b", font_size=20, color=WHITE),
            Text("", font_size=20, color=WHITE),
            Text("result = add(5, 3)", font_size=20, color=WHITE),
            Text("print(result)", font_size=20, color=YELLOW),
        )
        script_demo.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        script_demo.next_to(script_desc, DOWN, buff=0.5)

        # Animate everything
        self.play(Create(divider))
        self.play(Write(repl_title), Write(script_title))
        self.play(LaggedStartMap(FadeIn, repl_desc, lag_ratio=0.2))
        self.play(LaggedStartMap(FadeIn, script_desc, lag_ratio=0.2))
        self.play(LaggedStartMap(Write, repl_demo, lag_ratio=0.3))
        self.play(LaggedStartMap(Write, script_demo, lag_ratio=0.3))

        # When to use each
        when_title = Text("When to use each?", font_size=32, color=YELLOW)
        when_title.move_to(DOWN * 2.5)

        when_text = VGroup(
            Text("REPL: Quick tests, learning, debugging", font_size=24, color=GREEN),
            Text(
                "Scripts: Real programs, sharing, automation", font_size=24, color=BLUE
            ),
        )
        when_text.arrange(DOWN, buff=0.3)
        when_text.next_to(when_title, DOWN, buff=0.3)

        self.play(Write(when_title))
        self.play(LaggedStartMap(Write, when_text, lag_ratio=0.5))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    title,
                    divider,
                    repl_title,
                    script_title,
                    repl_desc,
                    script_desc,
                    repl_demo,
                    script_demo,
                    when_title,
                    when_text,
                )
            )
        )

    def basic_syntax_and_variables(self):
        """Basic Python syntax and variables"""
        title = Text("Basic Syntax & Variables", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Python syntax rules
        syntax_title = Text("Python Syntax Rules", font_size=36, color=GREEN)
        syntax_title.move_to(UP * 2)

        syntax_rules = [
            "• Indentation matters (use 4 spaces)",
            "• Case sensitive (Name ≠ name)",
            "• No semicolons needed",
            "• Comments start with #",
            "• Clean and readable code",
        ]

        rules_objects = VGroup()
        for rule in syntax_rules:
            rule_text = Text(rule, font_size=24, color=WHITE)
            rules_objects.add(rule_text)

        rules_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        rules_objects.next_to(syntax_title, DOWN, buff=0.5)

        self.play(Write(syntax_title))
        self.play(LaggedStartMap(Write, rules_objects, lag_ratio=0.3))

        self.wait(2)
        self.play(FadeOut(VGroup(syntax_title, rules_objects)))

        # Variables section
        var_title = Text("Variables & Assignment", font_size=36, color=YELLOW)
        var_title.move_to(UP * 2)

        # Variable examples
        var_examples = [
            ("name = 'Alice'", "String variable"),
            ("age = 25", "Integer variable"),
            ("height = 5.6", "Float variable"),
            ("is_student = True", "Boolean variable"),
            ("favorite_colors = ['blue', 'green']", "List variable"),
        ]

        example_objects = VGroup()
        for code, description in var_examples:
            # Code
            code_text = Text(code, font_size=24, color=YELLOW)

            # Description
            desc_text = Text(f"# {description}", font_size=20, color=GREEN)
            desc_text.next_to(code_text, RIGHT, buff=1)

            example_group = VGroup(code_text, desc_text)
            example_objects.add(example_group)

        example_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        example_objects.next_to(var_title, DOWN, buff=0.8)

        self.play(Write(var_title))

        # Animate each variable assignment
        for example in example_objects:
            self.play(Write(example), run_time=1.5)
            self.wait(0.5)

        # Variable naming rules
        naming_title = Text("Variable Naming Rules", font_size=28, color=RED)
        naming_title.next_to(example_objects, DOWN, buff=0.8)

        naming_rules = VGroup(
            Text("✓ snake_case (recommended)", font_size=20, color=GREEN),
            Text("✓ Start with letter or underscore", font_size=20, color=GREEN),
            Text("✗ No spaces or special characters", font_size=20, color=RED),
            Text("✗ Don't start with numbers", font_size=20, color=RED),
        )
        naming_rules.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        naming_rules.next_to(naming_title, DOWN, buff=0.3)

        self.play(Write(naming_title))
        self.play(LaggedStartMap(Write, naming_rules, lag_ratio=0.3))

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(title, var_title, example_objects, naming_title, naming_rules)
            )
        )

    def module_conclusion(self):
        """Conclusion for Module 3"""
        # Create celebration scene
        title = Text("Module 3 Complete!", font_size=56, color=GREEN)
        title.move_to(UP * 1.5)

        # Summary of what was learned
        summary = VGroup(
            Text("✓ Why Python is perfect for beginners", font_size=28, color=WHITE),
            Text("✓ Set up your development environment", font_size=28, color=WHITE),
            Text("✓ Write your first Python program", font_size=28, color=WHITE),
            Text("✓ Understand REPL vs Script files", font_size=28, color=WHITE),
            Text("✓ Learn basic syntax and variables", font_size=28, color=WHITE),
        )
        summary.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=0.8)

        # Next module preview
        next_module = Text(
            "Next: Core Python Concepts & Data Types", font_size=32, color=YELLOW
        )
        next_module.next_to(summary, DOWN, buff=1)

        # Animate conclusion
        self.play(Write(title), run_time=2)
        self.play(LaggedStartMap(FadeIn, summary, lag_ratio=0.2), run_time=3)
        self.play(Write(next_module), run_time=2)

        # Add some celebration particles
        particles = VGroup()
        for _ in range(20):
            particle = Dot(radius=0.05, color=random.choice([BLUE, GREEN, YELLOW, RED]))
            particle.move_to(
                np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-3, 3) * UP
            )
            particles.add(particle)

        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.1), run_time=2)

        # Make particles float
        self.play(
            *[
                particle.animate.shift(UP * np.random.uniform(0.5, 2))
                for particle in particles
            ],
            run_time=2,
        )

        self.wait(2)


# Main execution
if __name__ == "__main__":
    # This allows the file to be run directly
    pass
