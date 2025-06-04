from manimlib import *
import numpy as np
import random


class Module9LibrariesFrameworks(Scene):
    """
    Module 9: Libraries & Frameworks

    This module covers:
    1. Python Package Index (PyPI)
    2. Virtual Environments
    3. Essential Libraries (NumPy, Pandas, Requests)
    4. Web Frameworks (Flask, Django)
    5. Data Science Libraries
    6. GUI Frameworks
    7. Testing Frameworks
    8. Package Management with pip
    """

    def construct(self):
        # Module title
        title = Text("Module 9: Libraries & Frameworks", font_size=48)
        subtitle = Text("Exploring Python's Rich Ecosystem", font_size=32)
        VGroup(title, subtitle).arrange(DOWN).move_to(ORIGIN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.clear()

        # Show all demonstrations
        self.demonstrate_pypi_ecosystem()
        self.demonstrate_virtual_environments()
        self.demonstrate_numpy_basics()
        self.demonstrate_pandas_data_analysis()
        self.demonstrate_web_requests()
        self.demonstrate_flask_framework()
        self.demonstrate_data_science_stack()
        self.demonstrate_gui_frameworks()
        self.demonstrate_testing_frameworks()
        self.demonstrate_package_management()
        self.show_module_summary()

    def demonstrate_pypi_ecosystem(self):
        """Demonstrate the Python Package Index ecosystem"""
        title = Text("Python Package Index (PyPI)", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Create PyPI ecosystem visualization
        center = Circle(radius=1, color=BLUE).move_to(ORIGIN)
        center_text = Text("PyPI", font_size=24, color=WHITE)

        # Popular packages around the center
        packages = [
            ("NumPy", RED, UP + LEFT),
            ("Pandas", GREEN, UP + RIGHT),
            ("Requests", YELLOW, LEFT),
            ("Flask", PURPLE, RIGHT),
            ("Django", ORANGE, DOWN + LEFT),
            ("Matplotlib", PINK, DOWN + RIGHT),
            ("TensorFlow", TEAL, UP),
            ("SQLAlchemy", MAROON, DOWN),
        ]

        package_circles = []
        package_texts = []
        arrows = []

        for name, color, direction in packages:
            pos = direction * 2.5
            circle = Circle(radius=0.5, color=color).move_to(pos)
            text = Text(name, font_size=16, color=WHITE).move_to(pos)
            arrow = Arrow(center.get_center(), pos, color=GRAY, stroke_width=2)

            package_circles.append(circle)
            package_texts.append(text)
            arrows.append(arrow)

        # Animate the ecosystem
        self.play(Create(center), Write(center_text))
        self.wait(0.5)

        for arrow, circle, text in zip(arrows, package_circles, package_texts):
            self.play(Create(arrow), Create(circle), Write(text), run_time=0.3)

        # Show statistics
        stats = (
            VGroup(
                Text("400,000+ packages", font_size=20),
                Text("5+ billion downloads/month", font_size=20),
                Text("Free and open source", font_size=20),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        self.play(Write(stats))
        self.wait(2)
        self.clear()

    def demonstrate_virtual_environments(self):
        """Demonstrate virtual environments concept"""
        title = Text("Virtual Environments", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show system Python vs virtual environments
        system_python = Rectangle(width=3, height=2, color=BLUE).to_edge(LEFT)
        system_text = Text("System Python", font_size=20).next_to(system_python, UP)
        system_packages = (
            VGroup(
                Text("requests==2.25.1", font_size=14),
                Text("numpy==1.20.0", font_size=14),
                Text("pandas==1.2.0", font_size=14),
            )
            .arrange(DOWN)
            .move_to(system_python)
        )

        # Virtual environments
        venv1 = Rectangle(width=2.5, height=1.8, color=GREEN).move_to(
            RIGHT * 2.5 + UP * 1.5
        )
        venv1_text = Text("Project A\nVenv", font_size=16).next_to(venv1, UP)
        venv1_packages = (
            VGroup(
                Text("django==3.2", font_size=12), Text("psycopg2==2.8", font_size=12)
            )
            .arrange(DOWN)
            .move_to(venv1)
        )

        venv2 = Rectangle(width=2.5, height=1.8, color=PURPLE).move_to(
            RIGHT * 2.5 + DOWN * 1.5
        )
        venv2_text = Text("Project B\nVenv", font_size=16).next_to(venv2, DOWN)
        venv2_packages = (
            VGroup(Text("flask==2.0", font_size=12), Text("sqlite3", font_size=12))
            .arrange(DOWN)
            .move_to(venv2)
        )

        # Animation
        self.play(Create(system_python), Write(system_text))
        self.play(Write(system_packages))
        self.wait(1)

        self.play(Create(venv1), Write(venv1_text))
        self.play(Write(venv1_packages))
        self.wait(0.5)

        self.play(Create(venv2), Write(venv2_text))
        self.play(Write(venv2_packages))

        # Show command examples
        commands = (
            VGroup(
                Text("# Create virtual environment", font_size=16, color=GRAY),
                Text("python -m venv myproject", font_size=16),
                Text("", font_size=16),
                Text("# Activate (Windows)", font_size=16, color=GRAY),
                Text("myproject\\Scripts\\activate", font_size=16),
                Text("", font_size=16),
                Text("# Activate (Mac/Linux)", font_size=16, color=GRAY),
                Text("source myproject/bin/activate", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
            .scale(0.8)
        )

        self.play(Write(commands))
        self.wait(3)
        self.clear()

    def demonstrate_numpy_basics(self):
        """Demonstrate NumPy for numerical computing"""
        title = Text("NumPy: Numerical Computing", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show array creation and operations
        code_examples = (
            VGroup(
                Text("import numpy as np", font_size=20),
                Text("", font_size=16),
                Text("# Create arrays", font_size=16, color=GRAY),
                Text("arr = np.array([1, 2, 3, 4, 5])", font_size=18),
                Text("matrix = np.array([[1, 2], [3, 4]])", font_size=18),
                Text("", font_size=16),
                Text("# Mathematical operations", font_size=16, color=GRAY),
                Text("result = arr * 2", font_size=18),
                Text("mean = np.mean(arr)", font_size=18),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(LEFT)
        )

        # Visual representation of arrays
        array_visual = VGroup()

        # 1D array visualization
        array_1d = VGroup(
            *[Square(0.6, color=BLUE, fill_opacity=0.5) for _ in range(5)]
        )
        array_1d.arrange(RIGHT, buff=0.1)
        numbers_1d = VGroup(*[Text(str(i + 1), font_size=24) for i in range(5)])
        for i, num in enumerate(numbers_1d):
            num.move_to(array_1d[i])

        array_1d_group = VGroup(array_1d, numbers_1d).scale(0.8)

        # 2D array visualization
        array_2d = VGroup()
        for i in range(2):
            row = VGroup(
                *[Square(0.6, color=GREEN, fill_opacity=0.5) for _ in range(2)]
            )
            row.arrange(RIGHT, buff=0.1)
            array_2d.add(row)
        array_2d.arrange(DOWN, buff=0.1)

        numbers_2d = VGroup()
        values = [[1, 2], [3, 4]]
        for i in range(2):
            for j in range(2):
                num = Text(str(values[i][j]), font_size=24)
                num.move_to(array_2d[i][j])
                numbers_2d.add(num)

        array_2d_group = VGroup(array_2d, numbers_2d).scale(0.8)

        # Arrange visuals
        visual_group = (
            VGroup(
                VGroup(Text("1D Array", font_size=20), array_1d_group).arrange(DOWN),
                VGroup(Text("2D Array", font_size=20), array_2d_group).arrange(DOWN),
            )
            .arrange(DOWN, buff=1)
            .to_edge(RIGHT)
        )

        # Animate
        self.play(Write(code_examples))
        self.wait(1)
        self.play(Create(visual_group))

        # Show operation animation
        self.wait(1)
        doubled_numbers = VGroup(
            *[Text(str((i + 1) * 2), font_size=24, color=RED) for i in range(5)]
        )
        for i, num in enumerate(doubled_numbers):
            num.move_to(array_1d[i])

        self.play(Transform(numbers_1d, doubled_numbers))

        self.wait(2)
        self.clear()

    def demonstrate_pandas_data_analysis(self):
        """Demonstrate Pandas for data analysis"""
        title = Text("Pandas: Data Analysis", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Create a sample DataFrame visualization
        df_title = Text("Sample DataFrame", font_size=24)

        # Table headers
        headers = ["Name", "Age", "City", "Salary"]
        header_row = VGroup(
            *[
                Rectangle(width=1.5, height=0.6, color=BLUE, fill_opacity=0.7)
                for _ in headers
            ]
        )
        header_row.arrange(RIGHT, buff=0)
        header_texts = VGroup(*[Text(h, font_size=16, color=WHITE) for h in headers])
        for i, text in enumerate(header_texts):
            text.move_to(header_row[i])

        # Table data
        data = [
            ["Alice", "25", "NYC", "70000"],
            ["Bob", "30", "LA", "80000"],
            ["Charlie", "35", "Chicago", "75000"],
            ["Diana", "28", "Seattle", "85000"],
        ]

        data_rows = []
        data_texts = []

        for i, row in enumerate(data):
            row_squares = VGroup(
                *[
                    Rectangle(width=1.5, height=0.6, color=WHITE, stroke_color=GRAY)
                    for _ in row
                ]
            )
            row_squares.arrange(RIGHT, buff=0)
            row_squares.next_to(header_row, DOWN, buff=0).shift(DOWN * i * 0.6)

            row_texts = VGroup(*[Text(cell, font_size=14, color=BLACK) for cell in row])
            for j, text in enumerate(row_texts):
                text.move_to(row_squares[j])

            data_rows.append(row_squares)
            data_texts.append(row_texts)

        # Combine table
        table = VGroup(header_row, header_texts, *data_rows, *data_texts)
        table.scale(0.8).to_edge(LEFT)

        # Code examples
        code = (
            VGroup(
                Text("import pandas as pd", font_size=18),
                Text("", font_size=12),
                Text("# Read data", font_size=14, color=GRAY),
                Text("df = pd.read_csv('data.csv')", font_size=16),
                Text("", font_size=12),
                Text("# Basic operations", font_size=14, color=GRAY),
                Text("df.head()", font_size=16, color=GREEN),
                Text("df.describe()", font_size=16, color=GREEN),
                Text("df.groupby('City').mean()", font_size=16, color=GREEN),
                Text("", font_size=12),
                Text("# Filtering", font_size=14, color=GRAY),
                Text("high_earners = df[df['Salary'] > 75000]", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(RIGHT)
        )

        # Animate
        self.play(Write(df_title))
        self.play(Create(header_row), Write(header_texts))

        for row, text in zip(data_rows, data_texts):
            self.play(Create(row), Write(text), run_time=0.5)

        self.play(Write(code))

        # Highlight filtering
        self.wait(1)
        high_earner_rows = [1, 3]  # Bob and Diana
        for i in high_earner_rows:
            self.play(data_rows[i].animate.set_color(YELLOW), run_time=0.5)

        self.wait(2)
        self.clear()

    def demonstrate_web_requests(self):
        """Demonstrate the Requests library for HTTP"""
        title = Text("Requests: HTTP Made Simple", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show client-server communication
        client = Rectangle(width=2, height=1.5, color=BLUE, fill_opacity=0.5)
        client_text = Text("Client\n(Python)", font_size=16, color=WHITE)
        client_text.move_to(client)
        client_group = VGroup(client, client_text).to_edge(LEFT)

        server = Rectangle(width=2, height=1.5, color=GREEN, fill_opacity=0.5)
        server_text = Text("Server\n(API)", font_size=16, color=WHITE)
        server_text.move_to(server)
        server_group = VGroup(server, server_text).to_edge(RIGHT)

        # HTTP request arrow
        request_arrow = Arrow(client.get_right(), server.get_left(), color=RED)
        request_text = Text("GET /api/users", font_size=14, color=RED)
        request_text.next_to(request_arrow, UP)

        # HTTP response arrow
        response_arrow = Arrow(server.get_left(), client.get_right(), color=BLUE)
        response_text = Text("200 OK + JSON", font_size=14, color=BLUE)
        response_text.next_to(response_arrow, DOWN)

        # Code example
        code = (
            VGroup(
                Text("import requests", font_size=20),
                Text("", font_size=12),
                Text("# GET request", font_size=16, color=GRAY),
                Text(
                    "response = requests.get('https://api.github.com/users/octocat')",
                    font_size=14,
                ),
                Text("", font_size=12),
                Text("# Check status", font_size=16, color=GRAY),
                Text("if response.status_code == 200:", font_size=16),
                Text("    data = response.json()", font_size=16),
                Text("    print(data['name'])", font_size=16),
                Text("", font_size=12),
                Text("# POST request", font_size=16, color=GRAY),
                Text(
                    "data = {'name': 'John', 'email': 'john@example.com'}", font_size=14
                ),
                Text(
                    "response = requests.post('https://api.example.com/users', json=data)",
                    font_size=14,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Create(client_group))
        self.play(Create(server_group))
        self.wait(0.5)

        self.play(Create(request_arrow), Write(request_text))
        self.wait(0.5)
        self.play(Create(response_arrow), Write(response_text))

        self.play(Write(code))
        self.wait(3)
        self.clear()

    def demonstrate_flask_framework(self):
        """Demonstrate Flask web framework"""
        title = Text("Flask: Micro Web Framework", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Flask application structure
        structure = (
            VGroup(
                Text("Flask Application Structure", font_size=24, color=BLUE),
                Text("", font_size=12),
                Text("app.py", font_size=18, color=GREEN),
                Text("├── Routes", font_size=16),
                Text("├── Templates (HTML)", font_size=16),
                Text("├── Static files (CSS, JS)", font_size=16),
                Text("└── Database models", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(LEFT)
        )

        # Simple Flask code
        flask_code = (
            VGroup(
                Text("from flask import Flask, render_template", font_size=16),
                Text("", font_size=10),
                Text("app = Flask(__name__)", font_size=16),
                Text("", font_size=10),
                Text("@app.route('/')", font_size=16, color=YELLOW),
                Text("def home():", font_size=16),
                Text("    return '<h1>Hello, World!</h1>'", font_size=16),
                Text("", font_size=10),
                Text("@app.route('/user/<name>')", font_size=16, color=YELLOW),
                Text("def user(name):", font_size=16),
                Text("    return f'<h1>Hello, {name}!</h1>'", font_size=16),
                Text("", font_size=10),
                Text("if __name__ == '__main__':", font_size=16),
                Text("    app.run(debug=True)", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(RIGHT)
        )

        # Request-Response cycle
        cycle = (
            VGroup(
                Text("Request-Response Cycle", font_size=20, color=PURPLE),
                Text("", font_size=10),
                Text("1. Browser → GET /", font_size=14),
                Text("2. Flask routes request", font_size=14),
                Text("3. View function executes", font_size=14),
                Text("4. HTML response ← Flask", font_size=14),
                Text("5. Browser renders page", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(structure))
        self.wait(1)
        self.play(Write(flask_code))
        self.wait(1)
        self.play(Write(cycle))

        # Highlight decorators
        decorators = VGroup(flask_code[4], flask_code[8])
        self.play(decorators.animate.set_color(ORANGE))

        self.wait(3)
        self.clear()

    def demonstrate_data_science_stack(self):
        """Demonstrate the Python data science ecosystem"""
        title = Text("Data Science Stack", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Create a pyramid of data science tools
        levels = [
            (["Jupyter", "IDEs"], PURPLE, "Development Environment"),
            (["Matplotlib", "Seaborn", "Plotly"], BLUE, "Visualization"),
            (["Scikit-learn", "TensorFlow", "PyTorch"], RED, "Machine Learning"),
            (["Pandas", "NumPy"], GREEN, "Data Processing"),
            (["Python"], ORANGE, "Foundation"),
        ]

        pyramid = VGroup()
        level_y = 2

        for tools, color, category in levels:
            # Category label
            category_text = Text(category, font_size=16, color=color).move_to(
                UP * level_y + LEFT * 4
            )

            # Tool boxes
            tool_boxes = VGroup()
            for i, tool in enumerate(tools):
                box = Rectangle(width=1.5, height=0.6, color=color, fill_opacity=0.6)
                text = Text(tool, font_size=14, color=WHITE).move_to(box)
                tool_box = VGroup(box, text)
                tool_boxes.add(tool_box)

            tool_boxes.arrange(RIGHT, buff=0.2).move_to(UP * level_y)

            level_group = VGroup(category_text, tool_boxes)
            pyramid.add(level_group)
            level_y -= 1.2

        # Workflow arrows
        arrows = VGroup()
        for i in range(len(levels) - 1):
            arrow = Arrow(
                pyramid[i + 1][1].get_top(),
                pyramid[i][1].get_bottom(),
                color=GRAY,
                stroke_width=2,
            )
            arrows.add(arrow)

        # Animate pyramid build-up
        for level in reversed(pyramid):
            self.play(Write(level[0]), Create(level[1]), run_time=0.8)

        self.play(Create(arrows))

        # Show typical workflow
        workflow = (
            VGroup(
                Text("Typical Data Science Workflow:", font_size=18, color=YELLOW),
                Text("1. Load data (Pandas)", font_size=14),
                Text("2. Clean & explore (NumPy, Pandas)", font_size=14),
                Text("3. Visualize (Matplotlib, Seaborn)", font_size=14),
                Text("4. Model (Scikit-learn, TensorFlow)", font_size=14),
                Text("5. Deploy (Flask, Django)", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
            .scale(0.9)
        )

        self.play(Write(workflow))
        self.wait(3)
        self.clear()

    def demonstrate_gui_frameworks(self):
        """Demonstrate GUI frameworks"""
        title = Text("GUI Frameworks", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show different GUI options
        frameworks = [
            ("Tkinter", "Built-in", BLUE),
            ("PyQt/PySide", "Professional", GREEN),
            ("Kivy", "Mobile/Touch", PURPLE),
            ("Streamlit", "Web Apps", ORANGE),
            ("Dash", "Analytics", RED),
        ]

        framework_boxes = VGroup()
        for name, desc, color in frameworks:
            box = Rectangle(width=2.5, height=1.5, color=color, fill_opacity=0.3)
            name_text = Text(name, font_size=18, color=color).move_to(
                box.get_top() + DOWN * 0.3
            )
            desc_text = Text(desc, font_size=14, color=GRAY).move_to(
                box.get_bottom() + UP * 0.3
            )
            framework_box = VGroup(box, name_text, desc_text)
            framework_boxes.add(framework_box)

        framework_boxes.arrange_in_grid(rows=2, cols=3, buff=0.5)

        # Tkinter example
        tkinter_code = (
            VGroup(
                Text("import tkinter as tk", font_size=16),
                Text("", font_size=10),
                Text("root = tk.Tk()", font_size=16),
                Text("root.title('My App')", font_size=16),
                Text("", font_size=10),
                Text("label = tk.Label(root, text='Hello!')", font_size=16),
                Text("label.pack()", font_size=16),
                Text("", font_size=10),
                Text("button = tk.Button(root, text='Click Me')", font_size=16),
                Text("button.pack()", font_size=16),
                Text("", font_size=10),
                Text("root.mainloop()", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(DOWN)
        )

        # Animate
        for box in framework_boxes:
            self.play(Create(box), run_time=0.5)

        self.wait(1)

        # Highlight Tkinter
        self.play(framework_boxes[0].animate.set_stroke(YELLOW, width=4))
        self.play(Write(tkinter_code))

        self.wait(3)
        self.clear()

    def demonstrate_testing_frameworks(self):
        """Demonstrate testing frameworks"""
        title = Text("Testing Frameworks", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Testing pyramid
        pyramid_levels = [
            ("E2E Tests", RED, 1),
            ("Integration Tests", ORANGE, 2),
            ("Unit Tests", GREEN, 3),
        ]

        pyramid = VGroup()
        for i, (level_name, color, width) in enumerate(pyramid_levels):
            rect = Rectangle(width=width * 2, height=0.8, color=color, fill_opacity=0.6)
            text = Text(level_name, font_size=16, color=WHITE).move_to(rect)
            level = VGroup(rect, text).move_to(UP * (2 - i) * 1.2)
            pyramid.add(level)

        # Testing frameworks
        frameworks_text = (
            VGroup(
                Text("Python Testing Frameworks:", font_size=20, color=BLUE),
                Text("", font_size=12),
                Text("• unittest (built-in)", font_size=16),
                Text("• pytest (popular)", font_size=16),
                Text("• nose2", font_size=16),
                Text("• doctest (for documentation)", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(LEFT)
        )

        # pytest example
        pytest_code = (
            VGroup(
                Text("# test_calculator.py", font_size=16, color=GRAY),
                Text("import pytest", font_size=16),
                Text("", font_size=10),
                Text("def add(a, b):", font_size=16),
                Text("    return a + b", font_size=16),
                Text("", font_size=10),
                Text("def test_add():", font_size=16, color=GREEN),
                Text("    assert add(2, 3) == 5", font_size=16),
                Text("    assert add(-1, 1) == 0", font_size=16),
                Text("    assert add(0, 0) == 0", font_size=16),
                Text("", font_size=10),
                Text("# Run: pytest test_calculator.py", font_size=14, color=GRAY),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(RIGHT)
        )

        # Animate
        self.play(Create(pyramid))
        self.wait(1)
        self.play(Write(frameworks_text))
        self.wait(1)
        self.play(Write(pytest_code))

        # Show test results animation
        results = (
            VGroup(
                Text("Test Results:", font_size=18, color=GREEN),
                Text("✓ test_add PASSED", font_size=16, color=GREEN),
                Text("========================", font_size=16),
                Text("1 passed in 0.01s", font_size=16, color=GREEN),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        self.play(Write(results))
        self.wait(3)
        self.clear()

    def demonstrate_package_management(self):
        """Demonstrate package management with pip"""
        title = Text("Package Management with pip", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # pip commands
        commands = (
            VGroup(
                Text("Essential pip Commands", font_size=24, color=BLUE),
                Text("", font_size=12),
                Text("# Install a package", font_size=16, color=GRAY),
                Text("pip install requests", font_size=18, color=GREEN),
                Text("", font_size=10),
                Text("# Install specific version", font_size=16, color=GRAY),
                Text("pip install django==3.2.0", font_size=18, color=GREEN),
                Text("", font_size=10),
                Text("# Install from requirements", font_size=16, color=GRAY),
                Text("pip install -r requirements.txt", font_size=18, color=GREEN),
                Text("", font_size=10),
                Text("# List installed packages", font_size=16, color=GRAY),
                Text("pip list", font_size=18, color=GREEN),
                Text("", font_size=10),
                Text("# Show package info", font_size=16, color=GRAY),
                Text("pip show numpy", font_size=18, color=GREEN),
                Text("", font_size=10),
                Text("# Uninstall package", font_size=16, color=GRAY),
                Text("pip uninstall requests", font_size=18, color=GREEN),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(LEFT)
        )

        # requirements.txt example
        requirements = (
            VGroup(
                Text("requirements.txt", font_size=20, color=PURPLE),
                Text("", font_size=12),
                Rectangle(
                    width=4,
                    height=3,
                    color=WHITE,
                    fill_opacity=0.1,
                    stroke_color=PURPLE,
                ),
            )
            .arrange(DOWN)
            .to_edge(RIGHT)
        )

        req_content = (
            VGroup(
                Text("numpy==1.21.0", font_size=14),
                Text("pandas>=1.3.0", font_size=14),
                Text("requests==2.25.1", font_size=14),
                Text("flask==2.0.1", font_size=14),
                Text("matplotlib>=3.4.0", font_size=14),
                Text("pytest>=6.0.0", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(requirements[2])
        )

        # Best practices
        best_practices = (
            VGroup(
                Text("Best Practices:", font_size=18, color=ORANGE),
                Text("• Use virtual environments", font_size=14),
                Text("• Pin versions in production", font_size=14),
                Text("• Keep requirements.txt updated", font_size=14),
                Text("• Use pip freeze > requirements.txt", font_size=14),
                Text("• Consider using pipenv or poetry", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(commands))
        self.wait(1)
        self.play(Write(requirements))
        self.play(Write(req_content))
        self.wait(1)
        self.play(Write(best_practices))

        self.wait(3)
        self.clear()

    def show_module_summary(self):
        """Show module summary and key takeaways"""
        title = Text("Module 9 Summary", font_size=36, color=GOLD)
        self.play(Write(title))
        self.wait(1)

        summary_points = (
            VGroup(
                Text(
                    "🔧 Key Libraries & Frameworks Covered:", font_size=20, color=BLUE
                ),
                Text("", font_size=12),
                Text("• PyPI ecosystem with 400k+ packages", font_size=16),
                Text("• Virtual environments for project isolation", font_size=16),
                Text("• NumPy for numerical computing", font_size=16),
                Text("• Pandas for data analysis", font_size=16),
                Text("• Requests for HTTP communications", font_size=16),
                Text("• Flask for web development", font_size=16),
                Text("• Data science stack integration", font_size=16),
                Text("• GUI frameworks for desktop apps", font_size=16),
                Text("• Testing frameworks for quality assurance", font_size=16),
                Text("• Package management with pip", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.9)
        )

        next_steps = (
            VGroup(
                Text(
                    "🚀 Next: Module 10 - Project Development",
                    font_size=18,
                    color=GREEN,
                ),
                Text("Building complete applications", font_size=14, color=GRAY),
            )
            .arrange(DOWN)
            .to_edge(DOWN)
        )

        # Animate summary
        for i in range(0, len(summary_points), 2):
            self.play(Write(summary_points[i : i + 2]), run_time=0.8)

        self.wait(1)
        self.play(Write(next_steps))
        self.wait(3)
        self.clear()

        # Final message
        final_message = VGroup(
            Text("🎯 Practice Exercise", font_size=24, color=YELLOW),
            Text("", font_size=12),
            Text("Create a virtual environment and build a small", font_size=18),
            Text("web application using Flask with data from", font_size=18),
            Text("an API using the Requests library", font_size=18),
            Text("", font_size=12),
            Text("Great job completing Module 9!", font_size=20, color=GREEN),
        ).arrange(DOWN)

        self.play(Write(final_message))
        self.wait(4)


if __name__ == "__main__":
    # To render this scene, run:
    # manim -pql module9_libraries_frameworks.py Module9LibrariesFrameworks
    pass
