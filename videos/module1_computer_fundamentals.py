from manimlib import *
import numpy as np


class Module1ComputerFundamentals(Scene):
    def construct(self):
        """Module 1: Computer Fundamentals & Data Representation (30 min)"""
        # Set up the scene
        self.camera.background_color = "#0f0f23"

        # Module introduction
        self.module_intro()

        # 1.1: What is a computer?
        self.what_is_computer()

        # 1.2: Hardware vs Software
        self.hardware_vs_software()

        # 1.3: Electricity and transistors
        self.electricity_and_transistors()

        # 1.4: ON/OFF states to bits
        self.on_off_to_bits()

        # 1.5: Bits to bytes and memory
        self.bits_to_bytes()

        # 1.6: Binary number system
        self.binary_numbers()

        # 1.7: Data encoding (ASCII, RGB, etc.)
        self.data_encoding()

        # 1.8: Why programming languages are needed
        self.why_programming_languages()

        # Module conclusion
        self.module_conclusion()

    def module_intro(self):
        """Introduction to Module 1"""
        # Title with animated particles
        main_title = Text("Module 1", font_size=72, color=BLUE)
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

        # Clear for main content
        self.play(
            FadeOut(main_title),
            FadeOut(subtitle),
            FadeOut(description),
            FadeOut(particles),
            run_time=2,
        )

    def what_is_computer(self):
        """1.1: What is a computer?"""
        # Section title
        section_title = Text("What is a Computer?", font_size=48, color=YELLOW)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # Definition with visual
        definition = Text(
            "A computer is an electronic device that:\n"
            "• Processes information\n"
            "• Stores data\n"
            "• Executes instructions",
            font_size=32,
            color=WHITE,
        ).next_to(section_title, DOWN, buff=1)

        self.play(Write(definition))
        self.wait(2)

        # Show different types of computers
        computer_types = VGroup(
            Text("💻 Laptop", font_size=28, color=BLUE),
            Text("📱 Smartphone", font_size=28, color=GREEN),
            Text("🖥️ Desktop", font_size=28, color=ORANGE),
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
        """1.2: Hardware vs Software distinction"""
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
        """1.3: Electricity, transistors, and the foundation of computing"""
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
        """1.4: From ON/OFF states to bits"""
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
        """1.5: How bits form bytes and words"""
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
        """1.6: Understanding the binary number system"""
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
        """1.7: How different types of data are encoded in binary"""
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
        """1.8: Why we need programming languages"""
        # Section title
        section_title = Text("Why Programming Languages?", font_size=48, color=GREEN)
        self.play(Write(section_title))
        self.wait(1)
        self.play(section_title.animate.to_edge(UP))

        # The problem
        problem_title = Text("The Problem", font_size=36, color=RED)
        problem_title.next_to(section_title, DOWN, buff=1)
        self.play(Write(problem_title))

        # Show binary complexity
        binary_code = VGroup(
            Text("To add 5 + 3 in pure binary:", font_size=24, color=WHITE),
            Text(
                "10110101 11001010 01110011 00101101",
                font_size=16,
                color="#808080",
                font="monospace",
            ),
            Text(
                "01101110 10010110 11000101 01010010",
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

        binary_code.next_to(problem_title, DOWN, buff=0.5)

        for line in binary_code:
            self.play(Write(line), run_time=1)
            self.wait(0.3)

        # Human perspective
        human_perspective = Text(
            "Humans think: 'I want to add 5 + 3'", font_size=28, color=BLUE
        ).next_to(binary_code, DOWN, buff=1)

        self.play(Write(human_perspective))

        # Computer perspective
        computer_perspective = Text(
            "Computer understands: '10110101 11001010...'", font_size=28, color=ORANGE
        ).next_to(human_perspective, DOWN, buff=0.3)

        self.play(Write(computer_perspective))

        # The solution
        solution_title = Text(
            "The Solution: Programming Languages!", font_size=36, color=GREEN
        )
        solution_title.next_to(computer_perspective, DOWN, buff=1)
        self.play(Write(solution_title))

        # Show translation layers
        translation_demo = VGroup()

        # Human level
        human_level = VGroup(
            Text("Human writes:", font_size=20, color=BLUE),
            Text("result = 5 + 3", font_size=24, color=YELLOW, font="monospace"),
        ).arrange(DOWN, buff=0.2)

        # Arrow down
        arrow1 = Arrow(ORIGIN, DOWN * 0.8, color=WHITE)

        # Compiler level
        compiler_level = VGroup(
            Text("Compiler translates to:", font_size=20, color=GREEN),
            Text("Assembly instructions", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2)

        # Arrow down
        arrow2 = Arrow(ORIGIN, DOWN * 0.8, color=WHITE)

        # Machine level
        machine_level = VGroup(
            Text("Machine executes:", font_size=20, color=ORANGE),
            Text(
                "10110101 11001010...", font_size=16, color="#808080", font="monospace"
            ),
        ).arrange(DOWN, buff=0.2)

        # Arrange vertically
        translation_demo.add(human_level, arrow1, compiler_level, arrow2, machine_level)
        translation_demo.arrange(DOWN, buff=0.3)
        translation_demo.next_to(solution_title, DOWN, buff=0.5)

        # Animate translation process
        self.play(FadeIn(human_level))
        self.wait(1)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(compiler_level))
        self.wait(1)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(machine_level))
        self.wait(2)

        # Benefits of programming languages
        benefits_title = Text("Benefits:", font_size=28, color=PURPLE)
        benefits_title.to_edge(DOWN, buff=2)
        self.play(Write(benefits_title))

        benefits = VGroup(
            Text("✓ Human-readable", font_size=20, color=GREEN),
            Text("✓ Less error-prone", font_size=20, color=GREEN),
            Text("✓ Faster development", font_size=20, color=GREEN),
            Text("✓ Reusable code", font_size=20, color=GREEN),
        ).arrange(RIGHT, buff=1)

        benefits.next_to(benefits_title, UP, buff=0.3)

        for benefit in benefits:
            self.play(Write(benefit), run_time=0.8)
            self.wait(0.2)

        self.wait(3)

        # Clear for next section
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    problem_title,
                    binary_code,
                    human_perspective,
                    computer_perspective,
                    solution_title,
                    translation_demo,
                    benefits_title,
                    benefits,
                )
            )
        )

    def module_conclusion(self):
        """Module 1 conclusion and transition"""
        # Title
        conclusion_title = Text("Module 1 Complete!", font_size=56, color=YELLOW)
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
            concept_text = Text(concept, font_size=22, color=GREEN)
            concept_group.add(concept_text)

        concept_group.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        concept_group.next_to(summary_title, DOWN, buff=0.8)

        for concept in concept_group:
            self.play(Write(concept), run_time=1.2)
            self.wait(0.3)

        # Next module preview
        next_title = Text("Coming Up - Module 2:", font_size=32, color=BLUE)
        next_title.next_to(concept_group, DOWN, buff=1)
        self.play(Write(next_title))

        next_preview = Text(
            "Introduction to Python Programming", font_size=28, color=YELLOW
        ).next_to(next_title, DOWN, buff=0.3)

        self.play(Write(next_preview))

        # Celebration animation
        particles = VGroup()
        for _ in range(40):
            particle = Text(
                np.random.choice(["1", "0"]),
                font_size=np.random.randint(16, 32),
                color=random_bright_color(),
            )
            particle.move_to([np.random.uniform(-7, 7), np.random.uniform(-3, 3), 0])
            particles.add(particle)

        self.play(LaggedStartMap(FadeIn, particles, lag_ratio=0.02), run_time=2)

        # Final floating animation
        self.play(
            LaggedStartMap(
                lambda p: p.animate.shift(
                    [np.random.uniform(-1, 1), np.random.uniform(-1, 1), 0]
                ).set_color(random_bright_color()),
                particles,
                lag_ratio=0.01,
            ),
            run_time=3,
        )

        self.wait(2)

        # Fade out everything
        all_objects = VGroup(
            conclusion_title,
            summary_title,
            concept_group,
            next_title,
            next_preview,
            particles,
        )
        self.play(FadeOut(all_objects, run_time=3))

        self.wait(1)


# Main execution
if __name__ == "__main__":
    # This allows the file to be run directly
    pass
