from manimlib import *

class HelloManimGL(Scene):
    def construct(self):
        # Create text with 3B1B style
        title = Text("Hello ManimGL!", font_size=60)
        title.set_color(BLUE)
        
        # Animate text appearance
        self.play(Write(title))
        self.wait(2)
        
        # Transform to new text
        subtitle = Text("3Blue1Brown Style!", font_size=48)
        subtitle.set_color(YELLOW)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(subtitle))
        self.wait(2)

class InteractiveDemo(Scene):
    def construct(self):
        # Create interactive elements
        circle = Circle(radius=1, color=BLUE)
        square = Square(side_length=2, color=RED).shift(RIGHT * 3)
        
        # Add to scene
        self.add(circle, square)
        
        # This is where ManimGL shines - you can interact with this!
        self.wait(10)  # Keep scene alive for interaction

class MathVisualization(Scene):
    def construct(self):
        # Create coordinate system
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={
                "stroke_color": GREY_A,
                "stroke_width": 1,
            }
        )
        
        # Mathematical function
        func = plane.get_graph(
            lambda x: np.sin(x),
            color=YELLOW,
            x_range=[-5, 5]
        )
        
        # Function label
        label = Tex(r"f(x) = \sin(x)")
        label.to_corner(UL)
        label.set_color(YELLOW)
        
        # Animate everything
        self.play(ShowCreation(plane))
        self.play(ShowCreation(func), Write(label))
        self.wait(3)

class DataScienceConcept(Scene):
    def construct(self):
        # Title
        title = Text("Linear Regression", font_size=48)
        title.to_edge(UP)
        title.set_color(BLUE)
        
        # Create scatter plot points
        points = VGroup()
        data_points = [(1, 2), (2, 3.5), (3, 4.8), (4, 6.2), (5, 7.5)]
        
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 8, 1],
            x_length=6,
            y_length=4,
        ).shift(DOWN * 0.5)
        
        for x, y in data_points:
            point = Dot(axes.c2p(x, y), color=RED, radius=0.08)
            points.add(point)
        
        # Regression line
        line = axes.get_graph(lambda x: 1.5 * x + 0.3, color=YELLOW, x_range=[0.5, 5.5])
        
        # Animate
        self.play(Write(title))
        self.play(ShowCreation(axes))
        self.play(ShowIncreasingSubsets(points), run_time=2)
        self.play(ShowCreation(line))
        
        # Add equation
        equation = Tex(r"y = 1.5x + 0.3", font_size=36)
        equation.next_to(axes, RIGHT)
        equation.set_color(YELLOW)
        self.play(Write(equation))
        
        self.wait(3)