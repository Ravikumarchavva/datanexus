from manimlib import *
import numpy as np
import random


class Module10ProjectDevelopment(Scene):
    """
    Module 10: Project Development

    This module covers:
    1. Project Planning & Design
    2. Code Organization & Structure
    3. Version Control with Git
    4. Development Workflow
    5. Complete Project Walkthrough
    6. Deployment Strategies
    7. Documentation & Maintenance
    8. Career Path & Next Steps
    """

    def construct(self):
        # Module title
        title = Text("Module 10: Project Development", font_size=48)
        subtitle = Text("Building Complete Python Applications", font_size=32)
        VGroup(title, subtitle).arrange(DOWN).move_to(ORIGIN)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.clear()

        # Show all demonstrations
        self.demonstrate_project_planning()
        self.demonstrate_code_organization()
        self.demonstrate_version_control()
        self.demonstrate_development_workflow()
        self.demonstrate_complete_project()
        self.demonstrate_deployment_strategies()
        self.demonstrate_documentation()
        self.show_career_paths()
        self.show_course_completion()

    def demonstrate_project_planning(self):
        """Demonstrate project planning and design process"""
        title = Text("Project Planning & Design", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show planning phases
        phases = [
            ("1. Requirements", "What needs to be built?", BLUE),
            ("2. Design", "How will it work?", GREEN),
            ("3. Architecture", "What components needed?", PURPLE),
            ("4. Implementation", "Write the code", ORANGE),
            ("5. Testing", "Does it work correctly?", RED),
            ("6. Deployment", "Make it available", YELLOW),
        ]

        phase_circles = VGroup()
        connections = VGroup()

        for i, (phase, desc, color) in enumerate(phases):
            # Create circle for phase
            circle = Circle(radius=0.8, color=color, fill_opacity=0.3)
            phase_text = Text(phase, font_size=14, color=color).move_to(
                circle.get_top() + DOWN * 0.3
            )
            desc_text = Text(desc, font_size=10, color=GRAY).move_to(
                circle.get_bottom() + UP * 0.3
            )

            phase_group = VGroup(circle, phase_text, desc_text)

            # Position in a flow
            if i < 3:
                phase_group.move_to(LEFT * 4 + UP * (1 - i) * 2)
            else:
                phase_group.move_to(RIGHT * 4 + UP * (4 - i) * 2)

            phase_circles.add(phase_group)

            # Add connection arrow to next phase
            if i < len(phases) - 1:
                if i == 2:  # Turn from left to right
                    arrow = CurvedArrow(
                        phase_group.get_bottom() + DOWN * 0.2,
                        phases[i + 1][2]
                        and LEFT * 4 + DOWN * 0.2
                        or RIGHT * 4 + UP * 0.2,
                        color=GRAY,
                    )
                else:
                    next_pos = (
                        LEFT * 4 + UP * (-i) * 2
                        if i < 2
                        else RIGHT * 4 + UP * (3 - i) * 2
                    )
                    # Simplified arrow for demonstration
                    arrow = Arrow(
                        phase_group.get_bottom(),
                        next_pos + UP * 0.8,
                        color=GRAY,
                        stroke_width=2,
                    )
                connections.add(arrow)

        # Example project: Task Manager
        example = (
            VGroup(
                Text("Example Project: Task Manager App", font_size=20, color=GOLD),
                Text("", font_size=12),
                Text("Requirements:", font_size=16, color=GRAY),
                Text("• Create, edit, delete tasks", font_size=14),
                Text("• Mark tasks as complete", font_size=14),
                Text("• Categorize tasks", font_size=14),
                Text("• Web-based interface", font_size=14),
                Text("", font_size=10),
                Text("Tech Stack:", font_size=16, color=GRAY),
                Text("• Flask (web framework)", font_size=14),
                Text("• SQLite (database)", font_size=14),
                Text("• HTML/CSS (frontend)", font_size=14),
                Text("• Bootstrap (styling)", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(DOWN)
        )

        # Animate
        for phase in phase_circles:
            self.play(Create(phase), run_time=0.6)

        # Don't show arrows for simplicity, focus on content
        self.play(Write(example))
        self.wait(3)
        self.clear()

    def demonstrate_code_organization(self):
        """Demonstrate proper code organization and project structure"""
        title = Text("Code Organization & Structure", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show project structure
        structure_title = Text("Project Structure", font_size=24, color=BLUE)

        file_structure = (
            VGroup(
                Text("task_manager/", font_size=16, color=YELLOW),
                Text("├── app.py                 # Main application", font_size=14),
                Text("├── config.py              # Configuration", font_size=14),
                Text("├── requirements.txt       # Dependencies", font_size=14),
                Text("├── README.md             # Documentation", font_size=14),
                Text("├── models/", font_size=16, color=YELLOW),
                Text("│   ├── __init__.py", font_size=14),
                Text("│   └── task.py           # Task model", font_size=14),
                Text("├── views/", font_size=16, color=YELLOW),
                Text("│   ├── __init__.py", font_size=14),
                Text("│   └── routes.py         # Route handlers", font_size=14),
                Text("├── templates/", font_size=16, color=YELLOW),
                Text("│   ├── base.html         # Base template", font_size=14),
                Text("│   └── tasks.html        # Task templates", font_size=14),
                Text("├── static/", font_size=16, color=YELLOW),
                Text("│   ├── css/style.css     # Styles", font_size=14),
                Text("│   └── js/app.js         # JavaScript", font_size=14),
                Text("└── tests/", font_size=16, color=YELLOW),
                Text("    ├── __init__.py", font_size=14),
                Text("    └── test_tasks.py     # Unit tests", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(LEFT)
        )

        # Design principles
        principles = (
            VGroup(
                Text("Design Principles", font_size=24, color=GREEN),
                Text("", font_size=12),
                Text("🔹 Separation of Concerns", font_size=16),
                Text("  Keep different aspects separate", font_size=12, color=GRAY),
                Text("", font_size=8),
                Text("🔹 DRY (Don't Repeat Yourself)", font_size=16),
                Text("  Avoid code duplication", font_size=12, color=GRAY),
                Text("", font_size=8),
                Text("🔹 KISS (Keep It Simple, Stupid)", font_size=16),
                Text("  Simple solutions are better", font_size=12, color=GRAY),
                Text("", font_size=8),
                Text("🔹 Modular Design", font_size=16),
                Text("  Break into small modules", font_size=12, color=GRAY),
                Text("", font_size=8),
                Text("🔹 Clear Naming", font_size=16),
                Text("  Use descriptive names", font_size=12, color=GRAY),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(RIGHT)
        )

        # Animate
        self.play(Write(structure_title))
        self.play(Write(file_structure))
        self.wait(1)
        self.play(Write(principles))
        self.wait(3)
        self.clear()

    def demonstrate_version_control(self):
        """Demonstrate version control with Git"""
        title = Text("Version Control with Git", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Git workflow visualization
        workflow_title = Text("Git Workflow", font_size=24, color=BLUE)

        # Create commits as circles
        commits = []
        commit_messages = [
            "Initial commit",
            "Add task model",
            "Add web routes",
            "Add CSS styling",
            "Fix bug #1",
        ]

        for i, message in enumerate(commit_messages):
            commit = Circle(radius=0.3, color=GREEN, fill_opacity=0.7)
            commit.move_to(LEFT * 4 + RIGHT * i * 1.5)

            # Add commit hash
            hash_text = Text(f"a{i + 1}b{i + 2}", font_size=10, color=WHITE).move_to(
                commit
            )

            # Add commit message
            msg_text = Text(message, font_size=10).next_to(commit, DOWN, buff=0.2)

            commit_group = VGroup(commit, hash_text, msg_text)
            commits.append(commit_group)

        # Connect commits with arrows
        arrows = []
        for i in range(len(commits) - 1):
            arrow = Arrow(
                commits[i][0].get_right(),
                commits[i + 1][0].get_left(),
                color=GRAY,
                stroke_width=2,
                max_tip_length_to_length_ratio=0.1,
            )
            arrows.append(arrow)

        # Git commands
        commands = (
            VGroup(
                Text("Essential Git Commands", font_size=20, color=PURPLE),
                Text("", font_size=12),
                Text("# Initialize repository", font_size=14, color=GRAY),
                Text("git init", font_size=16, color=GREEN),
                Text("", font_size=10),
                Text("# Add files to staging", font_size=14, color=GRAY),
                Text("git add .", font_size=16, color=GREEN),
                Text("", font_size=10),
                Text("# Commit changes", font_size=14, color=GRAY),
                Text("git commit -m 'Add new feature'", font_size=16, color=GREEN),
                Text("", font_size=10),
                Text("# Push to remote", font_size=14, color=GRAY),
                Text("git push origin main", font_size=16, color=GREEN),
                Text("", font_size=10),
                Text("# Check status", font_size=14, color=GRAY),
                Text("git status", font_size=16, color=GREEN),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(workflow_title))

        # Show commits appearing one by one
        for i, commit in enumerate(commits):
            self.play(Create(commit), run_time=0.5)
            if i < len(arrows):
                self.play(Create(arrows[i]), run_time=0.3)

        self.wait(1)
        self.play(Write(commands))

        # Show branching concept
        branch_arrow = CurvedArrow(
            commits[2][0].get_center(),
            commits[2][0].get_center() + UP * 1.5 + RIGHT * 1,
            color=ORANGE,
        )
        feature_commit = Circle(radius=0.3, color=ORANGE, fill_opacity=0.7)
        feature_commit.move_to(commits[2][0].get_center() + UP * 1.5 + RIGHT * 1)
        feature_text = Text("feature\nbranch", font_size=10).next_to(feature_commit, UP)

        self.play(Create(branch_arrow), Create(feature_commit), Write(feature_text))

        self.wait(3)
        self.clear()

    def demonstrate_development_workflow(self):
        """Demonstrate development workflow and best practices"""
        title = Text("Development Workflow", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Development cycle
        cycle_steps = [
            ("Plan", BLUE, "Define requirements\nBreak into tasks"),
            ("Code", GREEN, "Write implementation\nFollow best practices"),
            ("Test", ORANGE, "Unit tests\nIntegration tests"),
            ("Review", PURPLE, "Code review\nPeer feedback"),
            ("Deploy", RED, "Release to production\nMonitor performance"),
            ("Monitor", YELLOW, "Track usage\nFix issues"),
        ]

        # Create circular workflow
        center = ORIGIN
        radius = 2.5

        step_objects = []
        for i, (step, color, description) in enumerate(cycle_steps):
            angle = i * 2 * PI / len(cycle_steps) - PI / 2  # Start from top
            pos = center + radius * np.array([np.cos(angle), np.sin(angle), 0])

            # Step circle
            circle = Circle(radius=0.5, color=color, fill_opacity=0.6).move_to(pos)
            step_text = Text(step, font_size=14, color=WHITE).move_to(pos)

            # Description
            desc_text = Text(description, font_size=10).next_to(
                circle, direction=pos / np.linalg.norm(pos[:2]), buff=0.5
            )

            step_group = VGroup(circle, step_text, desc_text)
            step_objects.append(step_group)

        # Add arrows between steps
        arrows = []
        for i in range(len(step_objects)):
            next_i = (i + 1) % len(step_objects)
            start_pos = step_objects[i][0].get_center()
            end_pos = step_objects[next_i][0].get_center()

            # Create curved arrow
            arrow = CurvedArrow(start_pos, end_pos, color=GRAY, angle=PI / 6)
            arrows.append(arrow)

        # Best practices
        practices = (
            VGroup(
                Text("Development Best Practices", font_size=18, color=GOLD),
                Text("", font_size=10),
                Text("✓ Write clean, readable code", font_size=14),
                Text("✓ Use meaningful variable names", font_size=14),
                Text("✓ Add comments and docstrings", font_size=14),
                Text("✓ Follow PEP 8 style guide", font_size=14),
                Text("✓ Write tests for your code", font_size=14),
                Text("✓ Use version control regularly", font_size=14),
                Text("✓ Keep dependencies updated", font_size=14),
                Text("✓ Document your project", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(DOWN)
        )

        # Animate
        for step in step_objects:
            self.play(Create(step), run_time=0.5)

        for arrow in arrows:
            self.play(Create(arrow), run_time=0.2)

        self.wait(1)
        self.play(Write(practices))
        self.wait(3)
        self.clear()

    def demonstrate_complete_project(self):
        """Demonstrate a complete project walkthrough"""
        title = Text("Complete Project: Task Manager", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Show main application code
        app_code = (
            VGroup(
                Text("# app.py - Main Application", font_size=16, color=BLUE),
                Text(
                    "from flask import Flask, render_template, request, redirect",
                    font_size=12,
                ),
                Text("from models.task import Task", font_size=12),
                Text("", font_size=8),
                Text("app = Flask(__name__)", font_size=12),
                Text("tasks = []  # In-memory storage for demo", font_size=12),
                Text("", font_size=8),
                Text("@app.route('/')", font_size=12, color=YELLOW),
                Text("def index():", font_size=12),
                Text(
                    "    return render_template('tasks.html', tasks=tasks)",
                    font_size=12,
                ),
                Text("", font_size=8),
                Text(
                    "@app.route('/add', methods=['POST'])", font_size=12, color=YELLOW
                ),
                Text("def add_task():", font_size=12),
                Text("    title = request.form.get('title')", font_size=12),
                Text("    task = Task(title)", font_size=12),
                Text("    tasks.append(task)", font_size=12),
                Text("    return redirect('/')", font_size=12),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(LEFT)
        )

        # Show Task model
        model_code = (
            VGroup(
                Text("# models/task.py", font_size=16, color=GREEN),
                Text("from datetime import datetime", font_size=12),
                Text("", font_size=8),
                Text("class Task:", font_size=12),
                Text("    def __init__(self, title):", font_size=12),
                Text("        self.title = title", font_size=12),
                Text("        self.completed = False", font_size=12),
                Text("        self.created_at = datetime.now()", font_size=12),
                Text("", font_size=8),
                Text("    def mark_complete(self):", font_size=12),
                Text("        self.completed = True", font_size=12),
                Text("", font_size=8),
                Text("    def __str__(self):", font_size=12),
                Text("        status = '✓' if self.completed else '○'", font_size=12),
                Text("        return f'{status} {self.title}'", font_size=12),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.7)
            .to_edge(RIGHT)
        )

        # Features overview
        features = (
            VGroup(
                Text("📋 Features Implemented:", font_size=18, color=PURPLE),
                Text("• Add new tasks", font_size=14),
                Text("• View all tasks", font_size=14),
                Text("• Mark tasks complete", font_size=14),
                Text("• Delete tasks", font_size=14),
                Text("• Responsive web interface", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(app_code))
        self.wait(1)
        self.play(Write(model_code))
        self.wait(1)
        self.play(Write(features))
        self.wait(3)
        self.clear()

    def demonstrate_deployment_strategies(self):
        """Demonstrate different deployment strategies"""
        title = Text("Deployment Strategies", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Deployment options
        deployment_options = [
            ("Local Development", "Your computer", BLUE),
            ("Heroku", "Cloud platform", GREEN),
            ("AWS/Azure/GCP", "Cloud providers", PURPLE),
            ("VPS/Docker", "Virtual servers", ORANGE),
            ("GitHub Pages", "Static sites", RED),
        ]

        option_boxes = VGroup()
        for name, desc, color in deployment_options:
            box = Rectangle(width=2.5, height=1.2, color=color, fill_opacity=0.3)
            name_text = Text(name, font_size=14, color=color).move_to(
                box.get_top() + DOWN * 0.3
            )
            desc_text = Text(desc, font_size=12, color=GRAY).move_to(
                box.get_bottom() + UP * 0.3
            )
            option_box = VGroup(box, name_text, desc_text)
            option_boxes.add(option_box)

        option_boxes.arrange_in_grid(rows=2, cols=3, buff=0.5).move_to(UP * 1)

        # Deployment process
        process = (
            VGroup(
                Text("Deployment Process", font_size=20, color=GOLD),
                Text("", font_size=12),
                Text("1. 🧪 Test locally", font_size=16),
                Text("2. 📝 Prepare requirements.txt", font_size=16),
                Text("3. 🔧 Configure environment variables", font_size=16),
                Text("4. 📤 Push to repository", font_size=16),
                Text("5. 🚀 Deploy to platform", font_size=16),
                Text("6. 🔍 Monitor and maintain", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Example deployment command
        heroku_example = (
            VGroup(
                Text("Heroku Deployment Example:", font_size=16, color=GREEN),
                Text("git add .", font_size=14, color=GRAY),
                Text("git commit -m 'Ready for deployment'", font_size=14, color=GRAY),
                Text("heroku create my-task-manager", font_size=14, color=GRAY),
                Text("git push heroku main", font_size=14, color=GRAY),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(RIGHT)
        )

        # Animate
        for box in option_boxes:
            self.play(Create(box), run_time=0.4)

        self.wait(1)
        self.play(Write(process))
        self.play(Write(heroku_example))
        self.wait(3)
        self.clear()

    def demonstrate_documentation(self):
        """Demonstrate documentation and maintenance"""
        title = Text("Documentation & Maintenance", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # README.md example
        readme_title = Text("README.md Example", font_size=20, color=BLUE)
        readme_content = (
            VGroup(
                Text("# Task Manager App", font_size=16, color=GREEN),
                Text("", font_size=10),
                Text("A simple web-based task management application", font_size=12),
                Text("built with Flask and Python.", font_size=12),
                Text("", font_size=10),
                Text("## Features", font_size=14, color=GREEN),
                Text("- Create and manage tasks", font_size=12),
                Text("- Mark tasks as complete", font_size=12),
                Text("- Clean web interface", font_size=12),
                Text("", font_size=10),
                Text("## Installation", font_size=14, color=GREEN),
                Text("```", font_size=12),
                Text("pip install -r requirements.txt", font_size=12),
                Text("python app.py", font_size=12),
                Text("```", font_size=12),
                Text("", font_size=10),
                Text("## Usage", font_size=14, color=GREEN),
                Text("Open http://localhost:5000 in your browser", font_size=12),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.6)
            .to_edge(LEFT)
        )

        # Documentation types
        doc_types = (
            VGroup(
                Text("📚 Documentation Types", font_size=18, color=PURPLE),
                Text("", font_size=12),
                Text("• README.md - Project overview", font_size=14),
                Text("• Docstrings - Function documentation", font_size=14),
                Text("• Comments - Code explanations", font_size=14),
                Text("• API docs - Usage instructions", font_size=14),
                Text("• User manual - How to use", font_size=14),
                Text("• Developer guide - How to contribute", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(RIGHT)
        )

        # Maintenance tasks
        maintenance = (
            VGroup(
                Text("🔧 Maintenance Tasks", font_size=18, color=ORANGE),
                Text("", font_size=12),
                Text("• Fix bugs and issues", font_size=14),
                Text("• Update dependencies", font_size=14),
                Text("• Add new features", font_size=14),
                Text("• Improve performance", font_size=14),
                Text("• Security updates", font_size=14),
                Text("• User feedback integration", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(readme_title))
        self.play(Write(readme_content))
        self.wait(1)
        self.play(Write(doc_types))
        self.wait(1)
        self.play(Write(maintenance))
        self.wait(3)
        self.clear()

    def show_career_paths(self):
        """Show different Python career paths"""
        title = Text("Python Career Paths", font_size=36)
        self.play(Write(title))
        self.wait(1)

        # Career paths with descriptions
        paths = [
            ("Web Developer", ["Flask/Django", "HTML/CSS/JS", "Databases"], BLUE),
            (
                "Data Scientist",
                ["Pandas/NumPy", "Machine Learning", "Visualization"],
                GREEN,
            ),
            ("DevOps Engineer", ["Automation", "Cloud Platforms", "CI/CD"], PURPLE),
            ("Software Engineer", ["Algorithms", "System Design", "Testing"], ORANGE),
            ("AI/ML Engineer", ["TensorFlow/PyTorch", "Deep Learning", "NLP"], RED),
            (
                "Automation Engineer",
                ["Scripting", "Testing", "Process Automation"],
                YELLOW,
            ),
        ]

        career_grid = VGroup()
        for i, (title_text, skills, color) in enumerate(paths):
            # Career box
            box = Rectangle(width=3, height=2, color=color, fill_opacity=0.2)
            title_label = Text(title_text, font_size=16, color=color).move_to(
                box.get_top() + DOWN * 0.3
            )

            skills_text = VGroup()
            for skill in skills:
                skill_item = Text(f"• {skill}", font_size=12)
                skills_text.add(skill_item)
            skills_text.arrange(DOWN, aligned_edge=LEFT).move_to(
                box.get_center() + DOWN * 0.2
            )

            career_box = VGroup(box, title_label, skills_text)
            career_grid.add(career_box)

        career_grid.arrange_in_grid(rows=2, cols=3, buff=0.5)

        # Learning path
        learning_path = (
            VGroup(
                Text("🎯 Continued Learning Path", font_size=20, color=GOLD),
                Text("", font_size=12),
                Text("1. Master the fundamentals (you're here!)", font_size=14),
                Text("2. Build projects and portfolio", font_size=14),
                Text("3. Learn specialized libraries", font_size=14),
                Text("4. Contribute to open source", font_size=14),
                Text("5. Network with other developers", font_size=14),
                Text("6. Keep learning new technologies", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        # Animate
        for career in career_grid:
            self.play(Create(career), run_time=0.5)

        self.wait(1)
        self.play(Write(learning_path))
        self.wait(3)
        self.clear()

    def show_course_completion(self):
        """Show course completion and final message"""
        # Congratulations
        congrats = Text("🎉 Congratulations! 🎉", font_size=48, color=GOLD)
        self.play(Write(congrats))
        self.wait(1)

        # Course summary
        summary = (
            VGroup(
                Text(
                    "You've Completed the Python Programming Course!",
                    font_size=24,
                    color=GREEN,
                ),
                Text("", font_size=16),
                Text("✓ Computer Fundamentals", font_size=18),
                Text("✓ Programming Logic & Problem Solving", font_size=18),
                Text("✓ Python Introduction & Syntax", font_size=18),
                Text("✓ Core Python Concepts", font_size=18),
                Text("✓ Functions & Modules", font_size=18),
                Text("✓ Object-Oriented Programming", font_size=18),
                Text("✓ File Handling & Error Management", font_size=18),
                Text("✓ Advanced Python Features", font_size=18),
                Text("✓ Libraries & Frameworks", font_size=18),
                Text("✓ Project Development", font_size=18),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
        )

        self.play(Transform(congrats, summary))
        self.wait(2)

        # Final motivation
        final_message = VGroup(
            Text("🚀 Your Python Journey Starts Now!", font_size=28, color=BLUE),
            Text("", font_size=16),
            Text("Remember:", font_size=20, color=PURPLE),
            Text("• Practice regularly", font_size=16),
            Text("• Build real projects", font_size=16),
            Text("• Join the Python community", font_size=16),
            Text("• Never stop learning", font_size=16),
            Text("", font_size=16),
            Text("Happy Coding! 🐍", font_size=24, color=GREEN),
        ).arrange(DOWN)

        self.play(Transform(summary, final_message))
        self.wait(3)

        # Final animation - Python logo-inspired
        python_colors = [BLUE, YELLOW]
        circles = VGroup()
        for i in range(20):
            circle = Circle(
                radius=random.uniform(0.1, 0.3),
                color=random.choice(python_colors),
                fill_opacity=0.7,
            )
            circle.move_to(random.uniform(-6, 6) * RIGHT + random.uniform(-3, 3) * UP)
            circles.add(circle)

        self.play(Create(circles), run_time=2)
        self.play(circles.animate.scale(0), run_time=1)
        self.wait(2)


if __name__ == "__main__":
    # To render this scene, run:
    # manim -pql module10_project_development.py Module10ProjectDevelopment
    pass
