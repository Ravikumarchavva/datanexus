from manimlib import *
import numpy as np

# Import all modules
from module1_computer_fundamentals import Module1ComputerFundamentals
from module2_programming_logic import Module2ProgrammingLogic
from module3_introduction_to_python import Module3IntroductionToPython
from module4_core_python_concepts import Module4CorePythonConcepts
from module5_functions_and_modules import Module5FunctionsAndModules
from module6_object_oriented_programming import Module6ObjectOrientedProgramming
from module7_file_handling_error_management import Module7FileHandlingErrorManagement
from module8_advanced_python_features import Module8AdvancedPythonFeatures
from module9_libraries_frameworks import Module9LibrariesFrameworks
from module10_project_development import Module10ProjectDevelopment


class CompletePythonCourse(Scene):
    """
    Complete Python Programming Course

    A comprehensive visual programming tutorial using Manim animations
    covering everything from computer fundamentals to advanced Python development.

    Course Structure:
    - Module 1: Computer Fundamentals
    - Module 2: Programming Logic & Problem Solving
    - Module 3: Introduction to Python
    - Module 4: Core Python Concepts
    - Module 5: Functions and Modules
    - Module 6: Object-Oriented Programming
    - Module 7: File Handling & Error Management
    - Module 8: Advanced Python Features
    - Module 9: Libraries & Frameworks
    - Module 10: Project Development
    """

    def construct(self):
        self.show_course_introduction()
        self.show_course_overview()
        self.show_learning_objectives()
        self.show_course_structure()
        self.show_getting_started()

    def show_course_introduction(self):
        """Show the main course introduction"""
        # Main title with animation
        main_title = Text(
            "Complete Python Programming Course", font_size=42, color=GOLD
        )
        subtitle = Text(
            "From Fundamentals to Professional Development", font_size=24, color=BLUE
        )

        # Python logo-inspired design
        python_symbol = Text("🐍", font_size=60)

        title_group = VGroup(python_symbol, main_title, subtitle).arrange(
            DOWN, buff=0.5
        )

        # Animated entrance
        self.play(Write(python_symbol))
        self.wait(0.5)
        self.play(Write(main_title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait(2)

        # Transform to smaller version
        compact_title = (
            VGroup(
                Text("🐍 Python Course", font_size=28, color=GOLD),
                Text("Professional Programming Tutorial", font_size=16, color=BLUE),
            )
            .arrange(DOWN)
            .to_edge(UP)
        )

        self.play(Transform(title_group, compact_title))
        self.wait(1)

    def show_course_overview(self):
        """Show course overview and benefits"""
        overview_title = Text("Course Overview", font_size=32, color=GREEN)
        overview_title.to_edge(UP).shift(DOWN * 1.5)

        benefits = (
            VGroup(
                Text("✨ What You'll Learn:", font_size=24, color=PURPLE),
                Text("", font_size=12),
                Text(
                    "🔹 Master Python from absolute beginner to advanced", font_size=16
                ),
                Text("🔹 Understand computer science fundamentals", font_size=16),
                Text("🔹 Learn problem-solving and algorithmic thinking", font_size=16),
                Text("🔹 Build real-world projects and applications", font_size=16),
                Text("🔹 Explore popular libraries and frameworks", font_size=16),
                Text("🔹 Develop professional coding practices", font_size=16),
                Text("🔹 Prepare for Python career opportunities", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
        )

        features = (
            VGroup(
                Text("🎯 Course Features:", font_size=24, color=ORANGE),
                Text("", font_size=12),
                Text("📺 Visual animations for complex concepts", font_size=16),
                Text("💻 Hands-on coding examples", font_size=16),
                Text("🧪 Interactive demonstrations", font_size=16),
                Text("📋 Comprehensive project development", font_size=16),
                Text("🔄 Progressive skill building", font_size=16),
                Text("📚 Industry best practices", font_size=16),
                Text("🚀 Career guidance and paths", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.85)
        )

        # Position side by side
        content_group = VGroup(benefits, features).arrange(RIGHT, buff=1.5)

        self.play(Write(overview_title))
        self.wait(0.5)
        self.play(Write(benefits))
        self.wait(1)
        self.play(Write(features))
        self.wait(3)
        self.clear()

    def show_learning_objectives(self):
        """Show detailed learning objectives"""
        objectives_title = Text("Learning Objectives", font_size=36, color=BLUE)
        self.play(Write(objectives_title))
        self.wait(1)

        # Create skill progression
        skill_levels = [
            (
                "Beginner",
                ["Basic syntax", "Variables & data types", "Control structures"],
                GREEN,
            ),
            (
                "Intermediate",
                ["Functions & modules", "OOP concepts", "File handling"],
                YELLOW,
            ),
            (
                "Advanced",
                [
                    "Decorators & generators",
                    "Libraries & frameworks",
                    "Project development",
                ],
                ORANGE,
            ),
            (
                "Professional",
                ["Best practices", "Testing & deployment", "Career readiness"],
                RED,
            ),
        ]

        skill_visualization = VGroup()

        for i, (level, skills, color) in enumerate(skill_levels):
            # Level header
            level_rect = Rectangle(width=6, height=0.8, color=color, fill_opacity=0.7)
            level_text = Text(level, font_size=20, color=WHITE).move_to(level_rect)
            level_header = VGroup(level_rect, level_text)

            # Skills list
            skills_list = VGroup()
            for skill in skills:
                skill_item = Text(f"• {skill}", font_size=14, color=color)
                skills_list.add(skill_item)
            skills_list.arrange(DOWN, aligned_edge=LEFT)

            # Combine level and skills
            level_group = VGroup(level_header, skills_list).arrange(DOWN, buff=0.3)
            level_group.move_to(UP * (2 - i * 1.5))

            skill_visualization.add(level_group)

        # Animate skill levels
        for level_group in skill_visualization:
            self.play(Create(level_group[0]), run_time=0.5)  # Header
            self.play(Write(level_group[1]), run_time=0.8)  # Skills

        # Show progression arrow
        arrow = Arrow(
            skill_visualization[0].get_bottom(),
            skill_visualization[-1].get_top(),
            color=PURPLE,
            stroke_width=6,
        )
        arrow_label = Text("Your Journey", font_size=16, color=PURPLE).next_to(
            arrow, RIGHT
        )

        self.play(Create(arrow), Write(arrow_label))
        self.wait(3)
        self.clear()

    def show_course_structure(self):
        """Show the complete course structure"""
        structure_title = Text(
            "Course Structure (10 Modules)", font_size=36, color=PURPLE
        )
        self.play(Write(structure_title))
        self.wait(1)

        # Module information
        modules = [
            ("Module 1", "Computer Fundamentals", "Binary, hardware, algorithms", BLUE),
            ("Module 2", "Programming Logic", "Problem solving, flowcharts", GREEN),
            (
                "Module 3",
                "Python Introduction",
                "Syntax, environment, philosophy",
                YELLOW,
            ),
            ("Module 4", "Core Concepts", "Variables, loops, data structures", ORANGE),
            ("Module 5", "Functions & Modules", "Code organization, scope", RED),
            (
                "Module 6",
                "Object-Oriented Programming",
                "Classes, inheritance, polymorphism",
                PURPLE,
            ),
            (
                "Module 7",
                "File Handling & Errors",
                "I/O operations, exception handling",
                TEAL,
            ),
            (
                "Module 8",
                "Advanced Features",
                "Decorators, generators, comprehensions",
                PINK,
            ),
            (
                "Module 9",
                "Libraries & Frameworks",
                "NumPy, Pandas, Flask, Django",
                MAROON,
            ),
            (
                "Module 10",
                "Project Development",
                "Complete applications, deployment",
                GOLD,
            ),
        ]

        # Create module boxes
        module_boxes = VGroup()

        for i, (module_num, title, description, color) in enumerate(modules):
            # Module box
            box = Rectangle(width=5.5, height=1, color=color, fill_opacity=0.3)

            # Module number and title
            module_text = Text(f"{module_num}: {title}", font_size=14, color=color)
            module_text.move_to(box.get_top() + DOWN * 0.3)

            # Description
            desc_text = Text(description, font_size=11, color=GRAY)
            desc_text.move_to(box.get_bottom() + UP * 0.25)

            module_group = VGroup(box, module_text, desc_text)
            module_boxes.add(module_group)

        # Arrange in two columns
        left_modules = VGroup(*module_boxes[:5]).arrange(DOWN, buff=0.2)
        right_modules = VGroup(*module_boxes[5:]).arrange(DOWN, buff=0.2)

        both_columns = VGroup(left_modules, right_modules).arrange(RIGHT, buff=1)
        both_columns.scale(0.8)

        # Animate modules appearing
        for module in module_boxes:
            self.play(Create(module), run_time=0.3)

        # Show estimated time
        time_info = (
            VGroup(
                Text("⏱️ Estimated Duration:", font_size=18, color=BLUE),
                Text("• Each module: 45-60 minutes", font_size=14),
                Text("• Total course: 8-10 hours", font_size=14),
                Text("• Self-paced learning", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(DOWN)
        )

        self.play(Write(time_info))
        self.wait(3)
        self.clear()

    def show_getting_started(self):
        """Show how to get started with the course"""
        getting_started_title = Text("Getting Started", font_size=36, color=GREEN)
        self.play(Write(getting_started_title))
        self.wait(1)

        # Prerequisites
        prerequisites = (
            VGroup(
                Text("📋 Prerequisites", font_size=24, color=BLUE),
                Text("", font_size=12),
                Text(
                    "✓ No prior programming experience required",
                    font_size=16,
                    color=GREEN,
                ),
                Text("✓ Basic computer literacy", font_size=16),
                Text("✓ Willingness to learn and practice", font_size=16),
                Text("✓ Access to a computer", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(LEFT)
        )

        # Setup instructions
        setup = (
            VGroup(
                Text("🛠️ Setup Required", font_size=24, color=ORANGE),
                Text("", font_size=12),
                Text("1. Install Python 3.8+", font_size=16),
                Text("   Download from python.org", font_size=14, color=GRAY),
                Text("", font_size=8),
                Text("2. Install Manim (for animations)", font_size=16),
                Text("   pip install manim", font_size=14, color=GRAY),
                Text("", font_size=8),
                Text("3. Choose a code editor", font_size=16),
                Text("   VS Code, PyCharm, or similar", font_size=14, color=GRAY),
                Text("", font_size=8),
                Text("4. Set up virtual environment", font_size=16),
                Text("   python -m venv course_env", font_size=14, color=GRAY),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .to_edge(RIGHT)
        )

        # How to run
        how_to_run = (
            VGroup(
                Text("🚀 How to Run Course Modules", font_size=20, color=PURPLE),
                Text("", font_size=12),
                Text("# Run individual modules:", font_size=16, color=GRAY),
                Text(
                    "manim -pql module1_computer_fundamentals.py Module1ComputerFundamentals",
                    font_size=12,
                ),
                Text("", font_size=8),
                Text("# Run specific demonstrations:", font_size=16, color=GRAY),
                Text("# Each module has multiple demo methods", font_size=12),
                Text("", font_size=8),
                Text("# View in browser after rendering", font_size=16, color=GRAY),
                Text("# Videos saved in media/videos/", font_size=12),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .scale(0.8)
            .to_edge(DOWN)
        )

        # Animate
        self.play(Write(prerequisites))
        self.wait(1)
        self.play(Write(setup))
        self.wait(1)
        self.play(Write(how_to_run))
        self.wait(3)

        # Final encouragement
        final_message = VGroup(
            Text("🎓 Ready to Begin Your Python Journey?", font_size=28, color=GOLD),
            Text("", font_size=16),
            Text(
                "Start with Module 1: Computer Fundamentals", font_size=18, color=BLUE
            ),
            Text("and work your way through each module.", font_size=18, color=BLUE),
            Text("", font_size=16),
            Text("Remember: Practice makes perfect! 🐍", font_size=20, color=GREEN),
        ).arrange(DOWN)

        self.play(Transform(VGroup(prerequisites, setup, how_to_run), final_message))
        self.wait(4)


class CourseNavigator(Scene):
    """
    Course Navigator - Quick access to all modules
    """

    def construct(self):
        title = Text("Python Course Navigator", font_size=36, color=GOLD)
        self.play(Write(title))
        self.wait(1)

        # Module menu
        modules = [
            "Module 1: Computer Fundamentals",
            "Module 2: Programming Logic & Problem Solving",
            "Module 3: Introduction to Python",
            "Module 4: Core Python Concepts",
            "Module 5: Functions and Modules",
            "Module 6: Object-Oriented Programming",
            "Module 7: File Handling & Error Management",
            "Module 8: Advanced Python Features",
            "Module 9: Libraries & Frameworks",
            "Module 10: Project Development",
        ]

        menu = VGroup()
        for i, module in enumerate(modules):
            module_item = Text(f"{i + 1:2d}. {module}", font_size=16)
            if i % 2 == 0:
                module_item.set_color(BLUE)
            else:
                module_item.set_color(GREEN)
            menu.add(module_item)

        menu.arrange(DOWN, aligned_edge=LEFT).scale(0.9)

        instructions = (
            VGroup(
                Text("Select any module to begin:", font_size=18, color=PURPLE),
                Text(
                    "Each module builds upon previous concepts",
                    font_size=14,
                    color=GRAY,
                ),
            )
            .arrange(DOWN)
            .to_edge(DOWN)
        )

        self.play(Transform(title, title.copy().scale(0.7).to_edge(UP)))
        self.play(Write(menu))
        self.play(Write(instructions))
        self.wait(3)


if __name__ == "__main__":
    """
    Course Execution Guide:
    
    To run the complete course introduction:
    manim -pql complete_python_course.py CompletePythonCourse
    
    To run the course navigator:
    manim -pql complete_python_course.py CourseNavigator
    
    To run individual modules:
    manim -pql module1_computer_fundamentals.py Module1ComputerFundamentals
    manim -pql module2_programming_logic.py Module2ProgrammingLogic
    ... and so on for all 10 modules
    
    Course Structure:
    - Start with CompletePythonCourse for overview
    - Use CourseNavigator to see all modules
    - Work through modules 1-10 in order
    - Each module contains multiple demonstration methods
    - Practice coding alongside the animations
    """
    pass
