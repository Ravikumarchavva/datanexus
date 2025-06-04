"""
Module 0: Welcome to MagicBehindAI Channel
=========================================

This is the introductory module for the MagicBehindAI YouTube channel's
comprehensive Python programming course. This module welcomes viewers,
introduces the channel, and provides an overview of what they'll learn
throughout the complete course series.

Author: MagicBehindAI
Course: Complete Python Programming Tutorial
Duration: ~15 minutes
"""

from manimlib import *
import numpy as np


class Module0ChannelWelcome(Scene):
    """
    Module 0: Welcome to MagicBehindAI Channel

    This opening module introduces viewers to the MagicBehindAI channel
    and provides a comprehensive overview of the Python programming course
    they're about to embark on.

    Demonstrations:
    1. Channel introduction and branding
    2. Course overview and structure
    3. Learning objectives and outcomes
    4. What makes this course special
    5. Prerequisites and requirements
    6. How to get the most from the course
    7. Community and support resources
    8. Course roadmap preview
    """

    def construct(self):
        """Main construction method for Module 0"""
        # Set background color for consistent branding
        self.camera.background_color = "#0f0f23"

        # Module structure
        self.channel_introduction()
        self.course_overview()
        self.what_makes_special()
        self.learning_path()
        self.prerequisites_requirements()
        self.how_to_succeed()
        self.community_support()
        self.course_roadmap()
        self.call_to_action()

    def channel_introduction(self):
        """Introduce the MagicBehindAI channel with animated branding"""
        # Main channel logo animation
        magic_text = Text("Magic", font_size=72, color=PURPLE)
        behind_text = Text("Behind", font_size=72, color=BLUE)
        ai_text = Text("AI", font_size=72, color=GREEN)

        # Arrange channel name
        channel_name = VGroup(magic_text, behind_text, ai_text)
        channel_name.arrange(RIGHT, buff=0.2)
        channel_name.move_to(UP * 1.5)

        # Channel tagline
        tagline = Text(
            "Making AI and Programming Accessible to Everyone",
            font_size=32,
            color=YELLOW,
        )
        tagline.next_to(channel_name, DOWN, buff=0.5)

        # Animated magic wand
        wand = Line(LEFT * 2, RIGHT * 2, color=GOLD, stroke_width=8)
        wand.next_to(tagline, DOWN, buff=0.8)

        # Magic sparkles
        sparkles = VGroup()
        for _ in range(12):
            # Create sparkle using crossed lines
            sparkle = VGroup(
                Line(UP * 0.1, DOWN * 0.1, color=random.choice([YELLOW, WHITE, GOLD])),
                Line(
                    LEFT * 0.1, RIGHT * 0.1, color=random.choice([YELLOW, WHITE, GOLD])
                ),
            )
            sparkle.move_to(
                np.random.uniform(-6, 6) * RIGHT + np.random.uniform(-3, 3) * UP
            )
            sparkles.add(sparkle)

        # Welcome message
        welcome_msg = Text(
            "Welcome to our Complete Python Programming Course!",
            font_size=28,
            color=WHITE,
        )
        welcome_msg.next_to(wand, DOWN, buff=1)

        # Animate channel introduction
        self.play(
            LaggedStart(
                Write(magic_text), Write(behind_text), Write(ai_text), lag_ratio=0.3
            ),
            run_time=3,
        )

        self.play(Write(tagline), run_time=2)
        self.play(Create(wand), run_time=1.5)

        # Animate sparkles
        self.play(LaggedStartMap(FadeIn, sparkles, lag_ratio=0.1), run_time=2)
        self.play(
            *[sparkle.animate.rotate(PI).scale(1.5) for sparkle in sparkles],
            run_time=1.5,
        )

        self.play(Write(welcome_msg), run_time=2)

        # Pause for impact
        self.wait(2)

        # Clear screen
        self.play(FadeOut(VGroup(channel_name, tagline, wand, sparkles, welcome_msg)))

    def course_overview(self):
        """Provide comprehensive course overview"""
        title = Text("What You'll Learn in This Course", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Course overview sections
        overview_sections = [
            (
                "🖥️ Computer Fundamentals",
                "How computers work, binary, and programming basics",
            ),
            ("🧠 Programming Logic", "Problem-solving and algorithmic thinking"),
            ("🐍 Python Basics", "Syntax, variables, and first programs"),
            ("💾 Core Concepts", "Data types, control structures, and operations"),
            ("🔧 Functions & Modules", "Code organization and reusability"),
            (
                "🏗️ Object-Oriented Programming",
                "Classes, inheritance, and design patterns",
            ),
            ("📁 File Handling", "Working with files and error management"),
            ("⚡ Advanced Features", "Decorators, generators, and Python magic"),
            ("📚 Libraries & Frameworks", "Popular Python ecosystem and tools"),
            ("🚀 Project Development", "Complete project lifecycle and career prep"),
        ]

        # Create animated course modules
        module_cards = VGroup()
        for i, (emoji_title, description) in enumerate(overview_sections):
            # Create module card
            card = RoundedRectangle(
                width=6,
                height=1,
                corner_radius=0.1,
                color=BLUE,
                fill_opacity=0.1,
                stroke_width=2,
            )

            # Module title with emoji
            title_text = Text(emoji_title, font_size=22, color=YELLOW)
            title_text.move_to(card.get_top() + DOWN * 0.3)

            # Module description
            desc_text = Text(description, font_size=16, color=WHITE)
            desc_text.move_to(card.get_bottom() + UP * 0.25)
            desc_text.scale(0.9)

            # Module number
            module_num = Circle(radius=0.2, color=GREEN, fill_opacity=1)
            num_text = Text(str(i + 1), font_size=16, color=BLACK)
            num_text.move_to(module_num)

            module_number = VGroup(module_num, num_text)
            module_number.move_to(card.get_left() + RIGHT * 0.3)

            module_card = VGroup(card, title_text, desc_text, module_number)
            module_cards.add(module_card)

        # Arrange in two columns
        left_column = VGroup(*module_cards[:5])
        right_column = VGroup(*module_cards[5:])

        left_column.arrange(DOWN, buff=0.2)
        right_column.arrange(DOWN, buff=0.2)

        columns = VGroup(left_column, right_column)
        columns.arrange(RIGHT, buff=0.5)
        columns.next_to(title, DOWN, buff=0.6)

        # Animate modules appearing
        self.play(LaggedStartMap(FadeIn, module_cards, lag_ratio=0.15), run_time=5)

        # Highlight progression
        for card in module_cards[:3]:
            self.play(card.animate.set_color(GREEN), run_time=0.3)
            self.wait(0.2)
            self.play(card.animate.set_color(BLUE), run_time=0.3)

        self.wait(2)
        self.play(FadeOut(VGroup(title, module_cards)))

    def what_makes_special(self):
        """Explain what makes this course unique"""
        title = Text("What Makes This Course Special?", font_size=48, color=PURPLE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Special features
        features = [
            ("🎨 Visual Learning", "Animated explanations make complex concepts clear"),
            ("🎯 Beginner-Friendly", "No prior programming experience required"),
            ("💡 Practical Focus", "Real-world projects and applications"),
            ("📈 Progressive Learning", "Each module builds on the previous one"),
            ("🔬 Interactive Demos", "See code execution in action"),
            ("💼 Career-Oriented", "Industry best practices and job preparation"),
            ("🌟 Quality Content", "Professional-grade tutorials and explanations"),
            ("🤝 Community Support", "Join our learning community"),
        ]

        feature_objects = VGroup()
        for emoji_title, description in features:
            # Feature icon
            icon = Text(emoji_title.split()[0], font_size=40)

            # Feature title
            feature_title = Text(
                emoji_title.split(" ", 1)[1], font_size=24, color=YELLOW
            )

            # Feature description
            feature_desc = Text(description, font_size=18, color=WHITE)

            # Arrange feature elements
            feature_content = VGroup(feature_title, feature_desc)
            feature_content.arrange(DOWN, buff=0.1)

            feature_group = VGroup(icon, feature_content)
            feature_group.arrange(RIGHT, buff=0.3)

            feature_objects.add(feature_group)

        # Arrange in grid
        feature_objects.arrange_in_grid(rows=4, cols=2, buff=(1, 0.4))
        feature_objects.next_to(title, DOWN, buff=0.8)

        # Animate features
        self.play(LaggedStartMap(FadeIn, feature_objects, lag_ratio=0.2), run_time=4)

        # Add emphasis animation
        emphasis_box = SurroundingRectangle(feature_objects[1], color=GREEN, buff=0.1)
        self.play(Create(emphasis_box), run_time=1)
        self.wait(1)
        self.play(FadeOut(emphasis_box))

        self.wait(2)
        self.play(FadeOut(VGroup(title, feature_objects)))

    def learning_path(self):
        """Show the learning journey and progression"""
        title = Text("Your Learning Journey", font_size=48, color=GREEN)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Create learning path visualization
        path_points = [
            ("Complete Beginner", "👶", RED),
            ("Programming Fundamentals", "🔤", ORANGE),
            ("Python Basics", "🐍", YELLOW),
            ("Intermediate Skills", "⚙️", BLUE),
            ("Advanced Concepts", "🔥", PURPLE),
            ("Professional Developer", "💼", GREEN),
        ]

        # Create path nodes
        path_nodes = VGroup()
        path_lines = VGroup()

        for i, (stage, emoji, color) in enumerate(path_points):
            # Create node
            node_circle = Circle(radius=0.4, color=color, fill_opacity=0.3)
            node_emoji = Text(emoji, font_size=32)
            node_text = Text(stage, font_size=20, color=color)
            node_text.next_to(node_circle, DOWN, buff=0.3)

            node = VGroup(node_circle, node_emoji, node_text)

            # Position nodes along curved path
            angle = -PI / 2 + (i * PI / (len(path_points) - 1))
            radius = 3
            x = radius * np.cos(angle)
            y = radius * np.sin(angle) - 0.5
            node.move_to([x, y, 0])

            path_nodes.add(node)

            # Create connecting lines
            if i > 0:
                prev_pos = path_nodes[i - 1][0].get_center()
                curr_pos = node_circle.get_center()
                line = Line(prev_pos, curr_pos, color=WHITE, stroke_width=3)
                path_lines.add(line)

        # Animate path creation
        self.play(Create(path_lines), run_time=2)
        self.play(LaggedStartMap(FadeIn, path_nodes, lag_ratio=0.3), run_time=3)

        # Animate progression
        progress_dot = Dot(color=GOLD, radius=0.15)
        progress_dot.move_to(path_nodes[0][0].get_center())

        self.play(FadeIn(progress_dot))

        for i in range(1, len(path_nodes)):
            self.play(
                progress_dot.animate.move_to(path_nodes[i][0].get_center()),
                path_nodes[i - 1].animate.set_opacity(0.5),
                path_nodes[i][0].animate.set_color(GOLD),
                run_time=1,
            )
            self.wait(0.5)

        # Success celebration
        success_text = Text("🎉 You'll be here soon! 🎉", font_size=32, color=GOLD)
        success_text.next_to(path_nodes[-1], DOWN, buff=0.8)

        self.play(Write(success_text), run_time=2)
        self.wait(2)

        self.play(
            FadeOut(VGroup(title, path_nodes, path_lines, progress_dot, success_text))
        )

    def prerequisites_requirements(self):
        """Outline prerequisites and requirements"""
        title = Text("Prerequisites & Requirements", font_size=48, color=ORANGE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Prerequisites section
        prereq_title = Text(
            "Prerequisites (What you need to know)", font_size=32, color=GREEN
        )
        prereq_title.move_to(UP * 2)

        prerequisites = VGroup(
            Text("✅ Basic computer literacy", font_size=24, color=WHITE),
            Text(
                "✅ Ability to download and install software", font_size=24, color=WHITE
            ),
            Text("✅ Willingness to learn and practice", font_size=24, color=WHITE),
            Text(
                "❌ NO prior programming experience needed!", font_size=24, color=GREEN
            ),
        )
        prerequisites.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        prerequisites.next_to(prereq_title, DOWN, buff=0.5)

        # Requirements section
        req_title = Text("Technical Requirements", font_size=32, color=BLUE)
        req_title.next_to(prerequisites, DOWN, buff=1)

        requirements = VGroup(
            Text("🖥️ Computer (Windows, Mac, or Linux)", font_size=24, color=WHITE),
            Text("🌐 Internet connection for downloads", font_size=24, color=WHITE),
            Text("💾 At least 2GB free disk space", font_size=24, color=WHITE),
            Text(
                "🐍 Python 3.7+ (we'll show you how to install)",
                font_size=24,
                color=WHITE,
            ),
        )
        requirements.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        requirements.next_to(req_title, DOWN, buff=0.5)

        # Animate sections
        self.play(Write(prereq_title))
        self.play(LaggedStartMap(FadeIn, prerequisites, lag_ratio=0.3), run_time=2)

        self.play(Write(req_title))
        self.play(LaggedStartMap(FadeIn, requirements, lag_ratio=0.3), run_time=2)

        # Highlight the "no experience needed"
        highlight = SurroundingRectangle(prerequisites[3], color=GREEN, buff=0.1)
        self.play(Create(highlight), run_time=1)
        self.wait(1)
        self.play(FadeOut(highlight))

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, prereq_title, prerequisites, req_title, requirements))
        )

    def how_to_succeed(self):
        """Tips for success in the course"""
        title = Text("How to Succeed in This Course", font_size=48, color=YELLOW)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Success tips
        tips = [
            (
                "📝 Practice Actively",
                "Don't just watch - code along with every example",
            ),
            ("🔄 Repeat & Review", "Rewatch modules if concepts aren't clear"),
            ("💪 Build Projects", "Apply what you learn in personal projects"),
            ("❓ Ask Questions", "Use comments section and community forums"),
            ("⏰ Be Consistent", "Set aside regular time for learning"),
            ("🤝 Join Community", "Learn with others and share your progress"),
            ("🎯 Set Goals", "Define what you want to build with Python"),
            ("🚀 Stay Motivated", "Remember why you started learning"),
        ]

        tip_objects = VGroup()
        for emoji_title, description in tips:
            # Tip card
            card = RoundedRectangle(
                width=7,
                height=0.8,
                corner_radius=0.1,
                color=YELLOW,
                fill_opacity=0.1,
                stroke_width=2,
            )

            # Tip title
            tip_title = Text(emoji_title, font_size=22, color=YELLOW)
            tip_title.move_to(card.get_left() + RIGHT * 1.5)

            # Tip description
            tip_desc = Text(description, font_size=18, color=WHITE)
            tip_desc.move_to(card.get_right() + LEFT * 2.5)

            tip_card = VGroup(card, tip_title, tip_desc)
            tip_objects.add(tip_card)

        # Arrange tips
        tip_objects.arrange(DOWN, buff=0.15)
        tip_objects.next_to(title, DOWN, buff=0.6)

        # Animate tips appearing
        self.play(LaggedStartMap(FadeIn, tip_objects, lag_ratio=0.2), run_time=4)

        # Emphasize key tips
        key_tips = [0, 2, 4]  # Practice, Projects, Consistency
        for tip_index in key_tips:
            self.play(tip_objects[tip_index].animate.set_color(GREEN), run_time=0.5)
            self.wait(0.3)
            self.play(tip_objects[tip_index].animate.set_color(YELLOW), run_time=0.5)

        self.wait(2)
        self.play(FadeOut(VGroup(title, tip_objects)))

    def community_support(self):
        """Information about community and support"""
        title = Text("Join Our Learning Community", font_size=48, color=BLUE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Community features
        community_items = [
            ("💬 Comments Section", "Ask questions directly on videos"),
            ("🎥 Live Q&A Sessions", "Regular community calls and help"),
            ("📱 Discord Server", "Chat with fellow learners 24/7"),
            ("🏆 Coding Challenges", "Practice with fun programming puzzles"),
            ("👥 Study Groups", "Form groups with other students"),
            ("📚 Resource Library", "Additional materials and references"),
            ("🎉 Success Stories", "Celebrate achievements together"),
            ("🔄 Code Reviews", "Get feedback on your projects"),
        ]

        # Create community visualization
        center_circle = Circle(radius=1.5, color=BLUE, fill_opacity=0.2)
        center_text = Text("MagicBehindAI\nCommunity", font_size=24, color=WHITE)
        center_text.move_to(center_circle.get_center())

        community_center = VGroup(center_circle, center_text)

        # Surrounding community features
        feature_circles = VGroup()
        for i, (feature_title, description) in enumerate(community_items):
            # Feature circle
            feature_circle = Circle(radius=0.4, color=GREEN, fill_opacity=0.1)

            # Feature icon (first emoji)
            icon = Text(feature_title.split()[0], font_size=24)
            icon.move_to(feature_circle.get_center())

            # Position around center
            angle = i * 2 * PI / len(community_items)
            x = 3 * np.cos(angle)
            y = 2 * np.sin(angle)

            feature_group = VGroup(feature_circle, icon)
            feature_group.move_to([x, y, 0])

            # Connecting line
            line = Line(
                center_circle.get_boundary_point([x, y, 0]),
                feature_circle.get_center(),
                color=WHITE,
                stroke_width=2,
            )

            feature_circles.add(VGroup(feature_group, line))

        # Animate community network
        self.play(FadeIn(community_center), run_time=1.5)
        self.play(LaggedStartMap(FadeIn, feature_circles, lag_ratio=0.2), run_time=3)

        # Community benefits text
        benefits_text = Text(
            "Learning is better together! Join thousands of students on their Python journey.",
            font_size=24,
            color=YELLOW,
        )
        benefits_text.next_to(community_center, DOWN, buff=2)

        self.play(Write(benefits_text), run_time=2)

        # Pulse animation for community
        self.play(community_center.animate.scale(1.1), run_time=0.5)
        self.play(community_center.animate.scale(1), run_time=0.5)

        self.wait(2)
        self.play(
            FadeOut(VGroup(title, community_center, feature_circles, benefits_text))
        )

    def course_roadmap(self):
        """Preview of the complete course roadmap"""
        title = Text("Complete Course Roadmap", font_size=48, color=PURPLE)
        title.to_edge(UP, buff=0.5)

        self.play(Write(title))

        # Course phases
        phases = [
            (
                "Foundation Phase",
                [
                    "Module 1: Computer Fundamentals",
                    "Module 2: Programming Logic",
                    "Module 3: Python Introduction",
                ],
                RED,
            ),
            (
                "Core Skills Phase",
                [
                    "Module 4: Core Python Concepts",
                    "Module 5: Functions & Modules",
                    "Module 6: Object-Oriented Programming",
                ],
                ORANGE,
            ),
            (
                "Advanced Phase",
                [
                    "Module 7: File Handling & Errors",
                    "Module 8: Advanced Python Features",
                    "Module 9: Libraries & Frameworks",
                ],
                BLUE,
            ),
            (
                "Professional Phase",
                [
                    "Module 10: Project Development",
                    "Career Guidance",
                    "Portfolio Building",
                ],
                GREEN,
            ),
        ]

        phase_objects = VGroup()
        for i, (phase_name, modules, color) in enumerate(phases):
            # Phase container
            phase_box = RoundedRectangle(
                width=7,
                height=2.5,
                corner_radius=0.2,
                color=color,
                fill_opacity=0.1,
                stroke_width=3,
            )

            # Phase title
            phase_title = Text(phase_name, font_size=24, color=color)
            phase_title.move_to(phase_box.get_top() + DOWN * 0.4)

            # Module list
            module_list = VGroup()
            for module in modules:
                module_text = Text(f"• {module}", font_size=16, color=WHITE)
                module_list.add(module_text)

            module_list.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            module_list.next_to(phase_title, DOWN, buff=0.3)

            # Duration estimate
            duration = Text(f"~{len(modules) * 3} hours", font_size=14, color=GRAY)
            duration.move_to(phase_box.get_bottom() + UP * 0.2)

            phase_group = VGroup(phase_box, phase_title, module_list, duration)
            phase_objects.add(phase_group)

        # Arrange phases in 2x2 grid
        phase_objects.arrange_in_grid(rows=2, cols=2, buff=0.4)
        phase_objects.next_to(title, DOWN, buff=0.6)

        # Animate roadmap
        self.play(LaggedStartMap(FadeIn, phase_objects, lag_ratio=0.4), run_time=4)

        # Show progression arrows
        arrows = VGroup()
        # Right arrow (Foundation -> Core)
        arrow1 = Arrow(
            phase_objects[0].get_right(), phase_objects[1].get_left(), color=YELLOW
        )
        # Down arrow (Core -> Advanced)
        arrow2 = Arrow(
            phase_objects[1].get_bottom(), phase_objects[3].get_top(), color=YELLOW
        )
        # Left arrow (Advanced -> Professional)
        arrow3 = Arrow(
            phase_objects[3].get_left(), phase_objects[2].get_right(), color=YELLOW
        )

        arrows.add(arrow1, arrow2, arrow3)

        self.play(LaggedStartMap(GrowArrow, arrows, lag_ratio=0.3), run_time=2)

        # Total course info
        total_info = Text(
            "Total Course: 10 Modules • ~12 Hours • Complete Python Mastery",
            font_size=24,
            color=GOLD,
        )
        total_info.next_to(phase_objects, DOWN, buff=0.8)

        self.play(Write(total_info), run_time=2)
        self.wait(2)

        self.play(FadeOut(VGroup(title, phase_objects, arrows, total_info)))

    def call_to_action(self):
        """Final call to action and course start"""
        # Epic finale title
        main_title = Text(
            "Ready to Begin Your Python Journey?", font_size=48, color=GOLD
        )
        main_title.move_to(UP * 2)

        self.play(Write(main_title), run_time=2)

        # Action items
        actions = VGroup(
            Text("👆 Subscribe & Ring the Bell for Updates", font_size=28, color=WHITE),
            Text("💬 Leave a Comment - Tell Us Your Goals!", font_size=28, color=WHITE),
            Text("👍 Like This Video if You're Excited!", font_size=28, color=WHITE),
            Text(
                "📚 Get Ready for Module 1: Computer Fundamentals",
                font_size=28,
                color=GREEN,
            ),
        )
        actions.arrange(DOWN, buff=0.4)
        actions.next_to(main_title, DOWN, buff=1)

        self.play(LaggedStartMap(FadeIn, actions, lag_ratio=0.5), run_time=3)

        # Countdown to start
        countdown_text = Text("Course starts in...", font_size=32, color=YELLOW)
        countdown_text.next_to(actions, DOWN, buff=1)

        self.play(Write(countdown_text))

        # Countdown animation
        for i in range(3, 0, -1):
            count_num = Text(str(i), font_size=72, color=RED)
            count_num.next_to(countdown_text, DOWN, buff=0.5)
            self.play(Write(count_num), run_time=0.5)
            self.wait(0.5)
            self.play(FadeOut(count_num), run_time=0.3)

        # Final message
        start_text = Text("Let's Code! 🚀", font_size=64, color=GREEN)
        start_text.next_to(countdown_text, DOWN, buff=0.5)

        self.play(Write(start_text), run_time=1.5)

        # Celebration explosion
        celebration = VGroup()
        for _ in range(30):
            particle = Star(
                n=5, color=random.choice([YELLOW, GREEN, BLUE, RED, PURPLE])
            )
            particle.scale(0.3)
            particle.move_to(start_text.get_center())
            celebration.add(particle)

        self.play(
            LaggedStartMap(
                lambda p: p.animate.move_to(
                    start_text.get_center()
                    + np.random.uniform(-4, 4) * RIGHT
                    + np.random.uniform(-3, 3) * UP
                ).rotate(PI),
                celebration,
                lag_ratio=0.05,
            ),
            run_time=2,
        )

        # Final channel branding
        final_branding = VGroup(
            Text("MagicBehindAI", font_size=36, color=PURPLE),
            Text("Making AI Accessible", font_size=20, color=BLUE),
            Text("Subscribe for More! 🔔", font_size=24, color=YELLOW),
        )
        final_branding.arrange(DOWN, buff=0.2)
        final_branding.move_to(DOWN * 2.5)

        self.play(FadeIn(final_branding), run_time=2)

        # Hold final frame
        self.wait(3)

        # Fade to black
        self.play(
            FadeOut(
                VGroup(
                    main_title,
                    actions,
                    countdown_text,
                    start_text,
                    celebration,
                    final_branding,
                )
            ),
            run_time=2,
        )


# Additional utility function for course navigation
def create_module_navigation():
    """
    Creates a navigation system for the complete course.
    This can be used in video descriptions or course materials.
    """
    navigation = {
        "Module 0": "Channel Welcome & Course Overview",
        "Module 1": "Computer Fundamentals",
        "Module 2": "Programming Logic & Problem Solving",
        "Module 3": "Introduction to Python",
        "Module 4": "Core Python Concepts",
        "Module 5": "Functions and Modules",
        "Module 6": "Object-Oriented Programming",
        "Module 7": "File Handling & Error Management",
        "Module 8": "Advanced Python Features",
        "Module 9": "Libraries & Frameworks",
        "Module 10": "Project Development & Career Prep",
    }
    return navigation


# Main execution
if __name__ == "__main__":
    # This allows the file to be run directly for testing
    print("Module 0: MagicBehindAI Channel Welcome")
    print("=" * 50)
    print("This module introduces the MagicBehindAI channel and")
    print("provides a comprehensive overview of the Python programming course.")
    print("\nTo render this module:")
    print("manim -pql module0_channel_welcome.py Module0ChannelWelcome")
