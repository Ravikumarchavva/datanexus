#!/usr/bin/env python3
"""
Python Programming Course Launcher

This script provides an easy way to run individual modules or the complete course.
It handles module selection, execution, and provides helpful information about the course.

Usage:
    python course_launcher.py                    # Interactive menu
    python course_launcher.py --module 0        # Run specific module (0-10)
    python course_launcher.py --list            # List all modules
    python course_launcher.py --complete        # Run complete course intro
"""

import os
import sys
import argparse
from typing import List, Dict


class CourseLauncher:
    """Handles course module execution and management"""

    def __init__(self):
        self.modules = {
            0: {
                "name": "Welcome to MagicBehindAI",
                "file": "module0_channel_welcome.py",
                "class": "Module0ChannelWelcome",
                "duration": "15 min",
                "description": "Channel introduction and course overview",
            },
            1: {
                "name": "Computer Fundamentals",
                "file": "module1_computer_fundamentals.py",
                "class": "Module1ComputerFundamentals",
                "duration": "60 min",
                "description": "Learn computer basics, binary systems, and programming concepts",
            },
            2: {
                "name": "Programming Logic",
                "file": "module2_programming_logic.py",
                "class": "Module2ProgrammingLogic",
                "duration": "50 min",
                "description": "Develop logical thinking and problem-solving skills",
            },
            3: {
                "name": "Introduction to Python",
                "file": "module3_introduction_to_python.py",
                "class": "Module3IntroductionToPython",
                "duration": "70 min",
                "description": "Get started with Python syntax and basic programming",
            },
            4: {
                "name": "Core Python Concepts",
                "file": "module4_core_python_concepts.py",
                "class": "Module4CorePythonConcepts",
                "duration": "90 min",
                "description": "Master data types, control structures, and core concepts",
            },
            5: {
                "name": "Functions and Modules",
                "file": "module5_functions_and_modules.py",
                "class": "Module5FunctionsAndModules",
                "duration": "80 min",
                "description": "Learn to organize code with functions and modules",
            },
            6: {
                "name": "Object-Oriented Programming",
                "file": "module6_object_oriented_programming.py",
                "class": "Module6ObjectOrientedProgramming",
                "duration": "90 min",
                "description": "Master OOP principles and design patterns",
            },
            7: {
                "name": "File Handling & Error Management",
                "file": "module7_file_handling_error_management.py",
                "class": "Module7FileHandlingErrorManagement",
                "duration": "70 min",
                "description": "Handle files and manage errors professionally",
            },
            8: {
                "name": "Advanced Python Features",
                "file": "module8_advanced_python_features.py",
                "class": "Module8AdvancedPythonFeatures",
                "duration": "80 min",
                "description": "Explore decorators, generators, and advanced concepts",
            },
            9: {
                "name": "Libraries & Frameworks",
                "file": "module9_libraries_frameworks.py",
                "class": "Module9LibrariesFrameworks",
                "duration": "70 min",
                "description": "Work with Python ecosystem and popular libraries",
            },
            10: {
                "name": "Project Development",
                "file": "module10_project_development.py",
                "class": "Module10ProjectDevelopment",
                "duration": "80 min",
                "description": "Complete project lifecycle and career preparation",
            },
        }

    def check_dependencies(self) -> bool:
        """Check if required dependencies are installed"""
        try:
            import importlib.util

            spec = importlib.util.find_spec("manimlib")
            return spec is not None
        except ImportError:
            print("❌ ManimGL is required but not installed.")
            print("Install with: pip install manimgl")
            print("Or: pip install manimlib")
            return False

    def list_modules(self):
        """Display all available modules"""
        print("🐍 Python Programming Course Modules\n")
        print("=" * 60)

        total_duration = 0
        for num, info in self.modules.items():
            duration_num = int(info["duration"].split()[0])
            total_duration += duration_num

            print(f"Module {num:2d}: {info['name']}")
            print(f"           Duration: {info['duration']}")
            print(f"           {info['description']}")
            print(f"           File: {info['file']}")
            print()

        print("=" * 60)
        print(
            f"Total Course Duration: ~{total_duration} minutes ({total_duration // 60}h {total_duration % 60}m)"
        )
        print(f"Total Modules: {len(self.modules)}")

    def verify_module_exists(self, module_num: int) -> bool:
        """Check if module file exists"""
        if module_num not in self.modules:
            return False

        module_file = self.modules[module_num]["file"]
        return os.path.exists(module_file)

    def run_module(self, module_num: int):
        """Execute a specific module"""
        if not self.verify_module_exists(module_num):
            print(f"❌ Module {module_num} not found or file missing")
            return False

        module_info = self.modules[module_num]
        print(f"🚀 Starting Module {module_num}: {module_info['name']}")
        print(f"📁 File: {module_info['file']}")
        print(f"⏱️  Duration: {module_info['duration']}")
        print(f"📝 Description: {module_info['description']}")
        print("\nTo render animations, use:")
        print(f"manimgl {module_info['file']} {module_info['class']}")
        print("\nFor high quality:")
        print(f"manimgl {module_info['file']} {module_info['class']} -w")
        return True

    def run_complete_course(self):
        """Run the complete course introduction"""
        print("🎓 Starting Complete Python Programming Course")
        print("📁 File: complete_python_course.py")
        print("\nTo render course introduction:")
        print("manimgl complete_python_course.py CompletePythonCourse")
        print("\nTo render course navigator:")
        print("manimgl complete_python_course.py CourseNavigator")

    def interactive_menu(self):
        """Show interactive menu for module selection"""
        while True:
            print("\n" + "=" * 60)
            print("🐍 Python Programming Course Launcher")
            print("=" * 60)
            print("1. List all modules")
            print("2. Run specific module")
            print("3. Run complete course introduction")
            print("4. Check dependencies")
            print("5. Course information")
            print("0. Exit")
            print("-" * 60)

            try:
                choice = input("Select an option (0-5): ").strip()

                if choice == "0":
                    print("👋 Thanks for using the Python Course!")
                    break
                elif choice == "1":
                    self.list_modules()
                elif choice == "2":
                    self.list_modules()
                    try:
                        module_num = int(input("\nEnter module number (0-10): "))
                        self.run_module(module_num)
                    except ValueError:
                        print("❌ Please enter a valid number")
                elif choice == "3":
                    self.run_complete_course()
                elif choice == "4":
                    if self.check_dependencies():
                        print("✅ All dependencies are installed")
                    else:
                        print("❌ Missing dependencies")
                elif choice == "5":
                    self.show_course_info()
                else:
                    print("❌ Invalid option. Please try again.")

            except KeyboardInterrupt:
                print("\n👋 Course launcher interrupted. Goodbye!")
                break

    def show_course_info(self):
        """Display comprehensive course information"""
        print("\n🎓 Complete Python Programming Course")
        print("=" * 60)
        print("📖 Description:")
        print("   A comprehensive visual programming tutorial using Manim animations")
        print("   covering everything from computer fundamentals to advanced Python.")
        print()
        print("🎯 Target Audience:")
        print("   • Complete programming beginners")
        print("   • Students learning Python")
        print("   • Self-taught developers")
        print("   • Career changers into tech")
        print()
        print("✨ Key Features:")
        print("   • Visual animations for complex concepts")
        print("   • Progressive skill building")
        print("   • Real-world project development")
        print("   • Industry best practices")
        print("   • Career guidance")
        print()
        print("📋 Prerequisites:")
        print("   • Basic computer literacy")
        print("   • Python 3.7+ installed")
        print("   • ManimGL library for animations")
        print()
        print("🏆 Learning Outcomes:")
        print("   • Master Python programming from basics to advanced")
        print("   • Understand computer science fundamentals")
        print("   • Build real-world applications")
        print("   • Prepare for Python career opportunities")


def main():
    """Main entry point for the course launcher"""
    parser = argparse.ArgumentParser(description="Python Programming Course Launcher")
    parser.add_argument("--module", "-m", type=int, help="Run specific module (0-10)")
    parser.add_argument("--list", "-l", action="store_true", help="List all modules")
    parser.add_argument(
        "--complete", "-c", action="store_true", help="Run complete course"
    )
    parser.add_argument(
        "--info", "-i", action="store_true", help="Show course information"
    )

    args = parser.parse_args()
    launcher = CourseLauncher()

    # Check dependencies first
    if not launcher.check_dependencies():
        sys.exit(1)

    if args.list:
        launcher.list_modules()
    elif args.module:
        launcher.run_module(args.module)
    elif args.complete:
        launcher.run_complete_course()
    elif args.info:
        launcher.show_course_info()
    else:
        # Run interactive menu
        launcher.interactive_menu()


if __name__ == "__main__":
    main()
