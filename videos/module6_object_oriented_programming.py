from manimlib import *
import numpy as np


class Module6ObjectOrientedProgramming(Scene):
    """
    Module 6: Object-Oriented Programming in Python

    This module covers:
    1. Introduction to OOP concepts
    2. Classes and Objects
    3. Attributes and Methods
    4. Constructor (__init__)
    5. Instance vs Class attributes
    6. Inheritance
    7. Polymorphism
    8. Encapsulation
    9. Method overriding
    10. Super() function
    """

    def construct(self):
        # Module title
        title = Text(
            "Module 6: Object-Oriented Programming", font_size=48, color=BLUE
        ).to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Clear title
        self.play(FadeOut(title))

        # Section 1: Introduction to OOP
        self.introduction_to_oop()

        # Section 2: Classes and Objects
        self.classes_and_objects()

        # Section 3: Attributes and Methods
        self.attributes_and_methods()

        # Section 4: Constructor (__init__)
        self.constructor_method()

        # Section 5: Instance vs Class attributes
        self.instance_vs_class_attributes()

        # Section 6: Inheritance
        self.inheritance_concepts()

        # Section 7: Polymorphism
        self.polymorphism_concepts()

        # Section 8: Encapsulation
        self.encapsulation_concepts()

        # Section 9: Method Overriding
        self.method_overriding()

        # Section 10: Super() function
        self.super_function()

        # Course conclusion
        self.course_conclusion()

    def introduction_to_oop(self):
        """Introduction to Object-Oriented Programming concepts"""
        section_title = Text("Introduction to OOP", font_size=36, color=YELLOW).to_edge(
            UP
        )
        self.play(Write(section_title))

        # OOP vs Procedural comparison
        procedural_box = Rectangle(width=5, height=4, color=RED).shift(LEFT * 3)
        oop_box = Rectangle(width=5, height=4, color=GREEN).shift(RIGHT * 3)

        procedural_title = Text(
            "Procedural Programming", font_size=24, color=RED
        ).next_to(procedural_box, UP)
        oop_title = Text(
            "Object-Oriented Programming", font_size=24, color=GREEN
        ).next_to(oop_box, UP)

        # Procedural characteristics
        proc_items = (
            VGroup(
                Text("• Functions operate on data", font_size=16),
                Text("• Data and functions separate", font_size=16),
                Text("• Code can become complex", font_size=16),
                Text("• Harder to maintain", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(procedural_box)
        )

        # OOP characteristics
        oop_items = (
            VGroup(
                Text("• Objects contain data & methods", font_size=16),
                Text("• Data and behavior together", font_size=16),
                Text("• Code is organized & modular", font_size=16),
                Text("• Easier to maintain & extend", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(oop_box)
        )

        self.play(Create(procedural_box), Create(oop_box))
        self.play(Write(procedural_title), Write(oop_title))
        self.play(Write(proc_items), Write(oop_items))
        self.wait(3)

        # Clear screen
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    procedural_box,
                    oop_box,
                    procedural_title,
                    oop_title,
                    proc_items,
                    oop_items,
                )
            )
        )

        # Four pillars of OOP
        pillars_title = Text("Four Pillars of OOP", font_size=32, color=BLUE).to_edge(
            UP
        )
        self.play(Write(pillars_title))

        # Create pillars as columns
        pillar_positions = [LEFT * 4.5, LEFT * 1.5, RIGHT * 1.5, RIGHT * 4.5]
        pillar_colors = [RED, ORANGE, GREEN, PURPLE]
        pillar_names = ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"]

        pillars = VGroup()
        for i, (pos, color, name) in enumerate(
            zip(pillar_positions, pillar_colors, pillar_names)
        ):
            # Create pillar
            pillar = Rectangle(
                width=1.5, height=3, color=color, fill_opacity=0.3
            ).move_to(pos)
            pillar_label = Text(name, font_size=16, color=color).next_to(
                pillar, DOWN, buff=0.2
            )

            # Add description
            descriptions = [
                "Hide internal\ndetails",
                "Reuse code from\nparent classes",
                "Same interface,\ndifferent behavior",
                "Simplify complex\nsystems",
            ]
            desc = Text(descriptions[i], font_size=12).move_to(pillar)

            pillar_group = VGroup(pillar, pillar_label, desc)
            pillars.add(pillar_group)

        # Animate pillars appearing
        for pillar in pillars:
            self.play(FadeIn(pillar), run_time=0.8)

        self.wait(3)
        self.play(FadeOut(VGroup(pillars_title, pillars)))

    def classes_and_objects(self):
        """Demonstrate classes and objects"""
        section_title = Text("Classes and Objects", font_size=36, color=YELLOW).to_edge(
            UP
        )
        self.play(Write(section_title))

        # Class as blueprint analogy
        blueprint_title = Text("Class = Blueprint", font_size=24, color=BLUE).shift(
            UP * 2
        )
        self.play(Write(blueprint_title))

        # Create a class blueprint
        class_box = Rectangle(width=6, height=3, color=BLUE, fill_opacity=0.1).shift(
            UP * 0.5
        )
        class_label = Text("class Car:", font_size=20, color=BLUE).next_to(
            class_box, UP, aligned_edge=LEFT
        )

        class_content = (
            VGroup(
                Text("• brand", font_size=16),
                Text("• model", font_size=16),
                Text("• year", font_size=16),
                Text("• start()", font_size=16),
                Text("• stop()", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(class_box)
            .shift(LEFT * 1.5)
        )

        self.play(Create(class_box), Write(class_label))
        self.play(Write(class_content))
        self.wait(2)

        # Objects from class
        objects_title = Text("Objects = Instances", font_size=24, color=GREEN).shift(
            DOWN * 1.5
        )
        self.play(Write(objects_title))

        # Create multiple car objects
        car_positions = [LEFT * 3, ORIGIN, RIGHT * 3]
        car_names = ["car1", "car2", "car3"]
        car_details = [
            "Toyota\nCamry\n2020",
            "Honda\nAccord\n2021",
            "Ford\nMustang\n2022",
        ]

        cars = VGroup()
        for pos, name, details in zip(car_positions, car_names, car_details):
            car_box = (
                Rectangle(width=1.8, height=1.5, color=GREEN, fill_opacity=0.2)
                .move_to(pos)
                .shift(DOWN * 2.5)
            )
            car_label = Text(name, font_size=14, color=GREEN).next_to(
                car_box, UP, buff=0.1
            )
            car_info = Text(details, font_size=10).move_to(car_box)

            car_group = VGroup(car_box, car_label, car_info)
            cars.add(car_group)

        # Animate cars creation
        for car in cars:
            arrow = Arrow(class_box.get_bottom(), car[0].get_top(), color=YELLOW)
            self.play(Create(arrow))
            self.play(FadeIn(car), FadeOut(arrow), run_time=0.8)

        self.wait(3)
        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    blueprint_title,
                    class_box,
                    class_label,
                    class_content,
                    objects_title,
                    cars,
                )
            )
        )

        # Code example
        code_title = Text("Python Class Example", font_size=28, color=BLUE).to_edge(UP)
        self.play(Write(code_title))

        code_text = """class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        return f"The {self.brand} {self.model} is starting!"
    
    def stop(self):
        return f"The {self.brand} {self.model} has stopped!"

# Creating objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2021)

print(car1.start())  # The Toyota Camry is starting!"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=16,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(code_title, code_display)))

    def attributes_and_methods(self):
        """Demonstrate attributes and methods"""
        section_title = Text(
            "Attributes and Methods", font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(Write(section_title))

        # Visual representation of object structure
        object_box = Rectangle(width=8, height=5, color=BLUE).shift(DOWN * 0.5)
        object_title = Text("Object: my_car", font_size=24, color=BLUE).next_to(
            object_box, UP
        )

        # Divide into attributes and methods
        divider = Line(
            object_box.get_left() + RIGHT * 4,
            object_box.get_right() + LEFT * 4,
            color=WHITE,
        )

        attr_title = Text("Attributes (Data)", font_size=20, color=GREEN).move_to(
            object_box.get_left() + RIGHT * 2 + UP * 1.8
        )
        method_title = Text("Methods (Behavior)", font_size=20, color=RED).move_to(
            object_box.get_right() + LEFT * 2 + UP * 1.8
        )

        # Attributes list
        attributes = (
            VGroup(
                Text("• brand = 'Tesla'", font_size=16, color=GREEN),
                Text("• model = 'Model 3'", font_size=16, color=GREEN),
                Text("• year = 2023", font_size=16, color=GREEN),
                Text("• color = 'Red'", font_size=16, color=GREEN),
                Text("• is_running = False", font_size=16, color=GREEN),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(object_box.get_left() + RIGHT * 2 + DOWN * 0.5)
        )

        # Methods list
        methods = (
            VGroup(
                Text("• start()", font_size=16, color=RED),
                Text("• stop()", font_size=16, color=RED),
                Text("• accelerate()", font_size=16, color=RED),
                Text("• brake()", font_size=16, color=RED),
                Text("• get_info()", font_size=16, color=RED),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(object_box.get_right() + LEFT * 2 + DOWN * 0.5)
        )

        self.play(Create(object_box), Write(object_title))
        self.play(Create(divider))
        self.play(Write(attr_title), Write(method_title))
        self.play(Write(attributes), Write(methods))
        self.wait(3)

        # Demonstrate method call
        method_call = Text("my_car.start()", font_size=24, color=ORANGE).shift(
            DOWN * 3.5
        )
        arrow = Arrow(methods[0].get_bottom(), method_call.get_top(), color=ORANGE)

        self.play(Write(method_call), Create(arrow))
        self.wait(2)

        # Show result
        result = Text(
            "Result: 'The Tesla Model 3 is starting!'", font_size=18, color=ORANGE
        ).next_to(method_call, DOWN)
        self.play(Write(result))
        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    section_title,
                    object_box,
                    object_title,
                    divider,
                    attr_title,
                    method_title,
                    attributes,
                    methods,
                    method_call,
                    arrow,
                    result,
                )
            )
        )

    def constructor_method(self):
        """Demonstrate the __init__ constructor method"""
        section_title = Text(
            "Constructor Method (__init__)", font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(Write(section_title))

        # Show constructor purpose
        purpose_text = Text(
            "The __init__ method initializes new objects", font_size=24, color=BLUE
        ).shift(UP * 2)
        self.play(Write(purpose_text))

        # Step-by-step object creation
        steps_title = Text("Object Creation Process:", font_size=20, color=GREEN).shift(
            UP * 1
        )
        self.play(Write(steps_title))

        # Steps
        steps = (
            VGroup(
                Text("1. Python creates empty object", font_size=16),
                Text("2. Calls __init__ method", font_size=16),
                Text("3. Sets initial attributes", font_size=16),
                Text("4. Returns initialized object", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .shift(RIGHT * 0.5)
        )

        for step in steps:
            self.play(Write(step), run_time=0.8)

        self.wait(2)

        # Visual demonstration
        self.play(FadeOut(VGroup(purpose_text, steps_title, steps)))

        # Show code example
        code_text = """class Student:
    def __init__(self, name, age, grade):
        self.name = name      # Set name attribute
        self.age = age        # Set age attribute
        self.grade = grade    # Set grade attribute
        print(f"Created student: {name}")
    
    def study(self):
        return f"{self.name} is studying!"

# Creating objects calls __init__ automatically
student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 19, "B")"""

        code_display = (
            Code(
                code=code_text,
                language="python",
                font_size=16,
                background="window",
                style="monokai",
            )
            .scale(0.8)
            .shift(DOWN * 0.5)
        )

        self.play(Write(code_display))
        self.wait(3)

        # Show execution flow
        execution_box = Rectangle(
            width=6, height=2, color=ORANGE, fill_opacity=0.1
        ).shift(DOWN * 2.8)
        execution_text = (
            VGroup(
                Text("Output:", font_size=16, color=ORANGE),
                Text("Created student: Alice", font_size=14),
                Text("Created student: Bob", font_size=14),
            )
            .arrange(DOWN)
            .move_to(execution_box)
        )

        self.play(Create(execution_box), Write(execution_text))
        self.wait(2)

        self.play(
            FadeOut(VGroup(section_title, code_display, execution_box, execution_text))
        )

    def instance_vs_class_attributes(self):
        """Demonstrate instance vs class attributes"""
        section_title = Text(
            "Instance vs Class Attributes", font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(Write(section_title))

        # Create visual comparison
        instance_box = Rectangle(width=5, height=4, color=GREEN).shift(LEFT * 3)
        class_box = Rectangle(width=5, height=4, color=BLUE).shift(RIGHT * 3)

        instance_title = Text("Instance Attributes", font_size=20, color=GREEN).next_to(
            instance_box, UP
        )
        class_title = Text("Class Attributes", font_size=20, color=BLUE).next_to(
            class_box, UP
        )

        # Instance attributes characteristics
        instance_items = (
            VGroup(
                Text("• Unique to each object", font_size=14),
                Text("• Defined in __init__", font_size=14),
                Text("• Use self.attribute", font_size=14),
                Text("• Different values per instance", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(instance_box)
        )

        # Class attributes characteristics
        class_items = (
            VGroup(
                Text("• Shared by all objects", font_size=14),
                Text("• Defined in class body", font_size=14),
                Text("• Same for all instances", font_size=14),
                Text("• Memory efficient", font_size=14),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .move_to(class_box)
        )

        self.play(Create(instance_box), Create(class_box))
        self.play(Write(instance_title), Write(class_title))
        self.play(Write(instance_items), Write(class_items))
        self.wait(3)

        self.play(
            FadeOut(
                VGroup(
                    instance_box,
                    class_box,
                    instance_title,
                    class_title,
                    instance_items,
                    class_items,
                )
            )
        )

        # Code example
        code_text = """class Dog:
    # Class attribute (shared by all dogs)
    species = "Canis familiaris"
    
    def __init__(self, name, breed):
        # Instance attributes (unique to each dog)
        self.name = name
        self.breed = breed

# Create instances
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Instance attributes are different
print(dog1.name)    # Buddy
print(dog2.name)    # Max

# Class attribute is the same for all
print(dog1.species) # Canis familiaris
print(dog2.species) # Canis familiaris"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=14,
            background="window",
            style="monokai",
        ).scale(0.9)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def inheritance_concepts(self):
        """Demonstrate inheritance concepts"""
        section_title = Text("Inheritance", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(section_title))

        # Visual inheritance hierarchy
        # Parent class
        parent_box = Rectangle(width=4, height=2, color=BLUE, fill_opacity=0.2).shift(
            UP * 2
        )
        parent_title = Text("Animal (Parent)", font_size=18, color=BLUE).next_to(
            parent_box, UP, buff=0.1
        )
        parent_content = (
            VGroup(
                Text("• name", font_size=12),
                Text("• eat()", font_size=12),
                Text("• sleep()", font_size=12),
            )
            .arrange(DOWN)
            .move_to(parent_box)
        )

        # Child classes
        child1_box = Rectangle(
            width=3, height=1.5, color=GREEN, fill_opacity=0.2
        ).shift(DOWN * 1 + LEFT * 3)
        child1_title = Text("Dog", font_size=16, color=GREEN).next_to(
            child1_box, UP, buff=0.1
        )
        child1_content = Text("• bark()", font_size=12).move_to(child1_box)

        child2_box = Rectangle(width=3, height=1.5, color=RED, fill_opacity=0.2).shift(
            DOWN * 1 + RIGHT * 3
        )
        child2_title = Text("Cat", font_size=16, color=RED).next_to(
            child2_box, UP, buff=0.1
        )
        child2_content = Text("• meow()", font_size=12).move_to(child2_box)

        # Inheritance arrows
        arrow1 = Arrow(
            parent_box.get_bottom() + LEFT * 1, child1_box.get_top(), color=YELLOW
        )
        arrow2 = Arrow(
            parent_box.get_bottom() + RIGHT * 1, child2_box.get_top(), color=YELLOW
        )

        # Draw the hierarchy
        self.play(Create(parent_box), Write(parent_title), Write(parent_content))
        self.wait(1)
        self.play(Create(arrow1), Create(arrow2))
        self.play(Create(child1_box), Write(child1_title), Write(child1_content))
        self.play(Create(child2_box), Write(child2_title), Write(child2_content))
        self.wait(2)

        # Show inheritance benefit
        benefit_text = Text(
            "Dog and Cat inherit eat() and sleep() from Animal!",
            font_size=16,
            color=ORANGE,
        ).shift(DOWN * 3)
        self.play(Write(benefit_text))
        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    parent_box,
                    parent_title,
                    parent_content,
                    child1_box,
                    child1_title,
                    child1_content,
                    child2_box,
                    child2_title,
                    child2_content,
                    arrow1,
                    arrow2,
                    benefit_text,
                )
            )
        )

        # Code example
        code_text = """class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        return f"{self.name} says Woof!"

class Cat(Animal):  # Cat inherits from Animal
    def meow(self):
        return f"{self.name} says Meow!"

# Using inheritance
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.eat())    # Inherited method
print(dog.bark())   # Own method
print(cat.sleep())  # Inherited method
print(cat.meow())   # Own method"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=13,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def polymorphism_concepts(self):
        """Demonstrate polymorphism"""
        section_title = Text("Polymorphism", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(section_title))

        # Definition
        definition = Text(
            "Polymorphism: Same interface, different behavior", font_size=24, color=BLUE
        ).shift(UP * 2.5)
        self.play(Write(definition))

        # Visual example with shapes
        shape_title = Text(
            "Example: Different shapes, same method", font_size=20, color=GREEN
        ).shift(UP * 1.5)
        self.play(Write(shape_title))

        # Create different shapes
        circle = Circle(radius=0.8, color=RED, fill_opacity=0.3).shift(LEFT * 3)
        circle_label = Text("Circle", font_size=16).next_to(circle, DOWN)
        circle_method = Text("area()", font_size=14, color=RED).next_to(
            circle_label, DOWN
        )

        rectangle = Rectangle(width=1.5, height=1, color=GREEN, fill_opacity=0.3)
        rect_label = Text("Rectangle", font_size=16).next_to(rectangle, DOWN)
        rect_method = Text("area()", font_size=14, color=GREEN).next_to(
            rect_label, DOWN
        )

        triangle = Polygon(
            [-0.8, -0.5, 0], [0.8, -0.5, 0], [0, 0.5, 0], color=BLUE, fill_opacity=0.3
        ).shift(RIGHT * 3)
        tri_label = Text("Triangle", font_size=16).next_to(triangle, DOWN)
        tri_method = Text("area()", font_size=14, color=BLUE).next_to(tri_label, DOWN)

        shapes = VGroup(
            VGroup(circle, circle_label, circle_method),
            VGroup(rectangle, rect_label, rect_method),
            VGroup(triangle, tri_label, tri_method),
        )

        for shape_group in shapes:
            self.play(FadeIn(shape_group), run_time=0.8)

        # Show same method name, different calculations
        same_name = Text("Same method name: area()", font_size=18, color=ORANGE).shift(
            DOWN * 2
        )
        diff_calc = Text(
            "Different calculations inside!", font_size=16, color=ORANGE
        ).shift(DOWN * 2.5)

        self.play(Write(same_name))
        self.play(Write(diff_calc))
        self.wait(3)

        self.play(
            FadeOut(VGroup(definition, shape_title, shapes, same_name, diff_calc))
        )

        # Code example
        code_text = """class Shape:
    def area(self):
        pass  # To be overridden by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area()}")  # Same method call, different behavior"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=14,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def encapsulation_concepts(self):
        """Demonstrate encapsulation"""
        section_title = Text("Encapsulation", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(section_title))

        # Definition and concept
        definition = Text(
            "Encapsulation: Hide internal details, control access",
            font_size=22,
            color=BLUE,
        ).shift(UP * 2.5)
        self.play(Write(definition))

        # Visual representation of access levels
        access_title = Text("Python Access Levels", font_size=20, color=GREEN).shift(
            UP * 1.5
        )
        self.play(Write(access_title))

        # Create boxes for different access levels
        public_box = Rectangle(
            width=2.5, height=1.5, color=GREEN, fill_opacity=0.2
        ).shift(LEFT * 3 + UP * 0.2)
        protected_box = Rectangle(
            width=2.5, height=1.5, color=ORANGE, fill_opacity=0.2
        ).shift(UP * 0.2)
        private_box = Rectangle(
            width=2.5, height=1.5, color=RED, fill_opacity=0.2
        ).shift(RIGHT * 3 + UP * 0.2)

        public_title = Text("Public", font_size=16, color=GREEN).next_to(
            public_box, UP, buff=0.1
        )
        protected_title = Text("Protected", font_size=16, color=ORANGE).next_to(
            protected_box, UP, buff=0.1
        )
        private_title = Text("Private", font_size=16, color=RED).next_to(
            private_box, UP, buff=0.1
        )

        public_content = (
            VGroup(
                Text("name", font_size=12),
                Text("Accessible", font_size=10),
                Text("everywhere", font_size=10),
            )
            .arrange(DOWN)
            .move_to(public_box)
        )

        protected_content = (
            VGroup(
                Text("_age", font_size=12),
                Text("Convention:", font_size=10),
                Text("internal use", font_size=10),
            )
            .arrange(DOWN)
            .move_to(protected_box)
        )

        private_content = (
            VGroup(
                Text("__salary", font_size=12),
                Text("Name mangled,", font_size=10),
                Text("truly private", font_size=10),
            )
            .arrange(DOWN)
            .move_to(private_box)
        )

        access_levels = VGroup(
            VGroup(public_box, public_title, public_content),
            VGroup(protected_box, protected_title, protected_content),
            VGroup(private_box, private_title, private_content),
        )

        for level in access_levels:
            self.play(FadeIn(level), run_time=0.8)

        self.wait(2)
        self.play(FadeOut(VGroup(definition, access_title, access_levels)))

        # Code example
        code_text = """class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        # Public
        self._account_id = 12345  # Protected (convention)
        self.__balance = balance  # Private (name mangled)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance     # Controlled access
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

account = BankAccount("Alice", 1000)
print(account.owner)        # Accessible
print(account.get_balance()) # Controlled access
# print(account.__balance)  # Error! Can't access directly"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=13,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def method_overriding(self):
        """Demonstrate method overriding"""
        section_title = Text("Method Overriding", font_size=36, color=YELLOW).to_edge(
            UP
        )
        self.play(Write(section_title))

        # Definition
        definition = Text(
            "Method Overriding: Child class redefines parent's method",
            font_size=22,
            color=BLUE,
        ).shift(UP * 2.5)
        self.play(Write(definition))

        # Visual example
        # Parent method
        parent_box = Rectangle(width=4, height=1.5, color=BLUE, fill_opacity=0.2).shift(
            UP * 1
        )
        parent_title = Text("Parent: Vehicle", font_size=16, color=BLUE).next_to(
            parent_box, UP, buff=0.1
        )
        parent_method = Text("start() → 'Vehicle starting'", font_size=14).move_to(
            parent_box
        )

        # Child methods (overriding)
        child1_box = Rectangle(
            width=4, height=1.5, color=GREEN, fill_opacity=0.2
        ).shift(DOWN * 1 + LEFT * 2.5)
        child1_title = Text("Child: Car", font_size=16, color=GREEN).next_to(
            child1_box, UP, buff=0.1
        )
        child1_method = Text("start() → 'Engine roaring'", font_size=14).move_to(
            child1_box
        )

        child2_box = Rectangle(width=4, height=1.5, color=RED, fill_opacity=0.2).shift(
            DOWN * 1 + RIGHT * 2.5
        )
        child2_title = Text("Child: Bike", font_size=16, color=RED).next_to(
            child2_box, UP, buff=0.1
        )
        child2_method = Text("start() → 'Pedaling...'", font_size=14).move_to(
            child2_box
        )

        # Arrows showing override
        arrow1 = Arrow(
            parent_box.get_bottom() + LEFT * 1, child1_box.get_top(), color=YELLOW
        )
        arrow2 = Arrow(
            parent_box.get_bottom() + RIGHT * 1, child2_box.get_top(), color=YELLOW
        )

        override_label1 = Text("OVERRIDE", font_size=12, color=YELLOW).next_to(
            arrow1, RIGHT, buff=0.1
        )
        override_label2 = Text("OVERRIDE", font_size=12, color=YELLOW).next_to(
            arrow2, LEFT, buff=0.1
        )

        self.play(Create(parent_box), Write(parent_title), Write(parent_method))
        self.wait(1)
        self.play(Create(arrow1), Create(arrow2))
        self.play(Write(override_label1), Write(override_label2))
        self.play(Create(child1_box), Write(child1_title), Write(child1_method))
        self.play(Create(child2_box), Write(child2_title), Write(child2_method))
        self.wait(2)

        self.play(
            FadeOut(
                VGroup(
                    definition,
                    parent_box,
                    parent_title,
                    parent_method,
                    child1_box,
                    child1_title,
                    child1_method,
                    child2_box,
                    child2_title,
                    child2_method,
                    arrow1,
                    arrow2,
                    override_label1,
                    override_label2,
                )
            )
        )

        # Code example
        code_text = """class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle is starting"

class Car(Vehicle):
    def start(self):  # Override parent method
        return f"{self.brand} car engine is roaring!"

class Bicycle(Vehicle):
    def start(self):  # Override parent method
        return f"Starting to pedal the {self.brand} bike"

# Method overriding in action
vehicles = [
    Vehicle("Generic"),
    Car("Toyota"),
    Bicycle("Trek")
]

for vehicle in vehicles:
    print(vehicle.start())  # Different output for each!"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=14,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def super_function(self):
        """Demonstrate the super() function"""
        section_title = Text(
            "The super() Function", font_size=36, color=YELLOW
        ).to_edge(UP)
        self.play(Write(section_title))

        # Purpose explanation
        purpose = Text(
            "super() allows access to parent class methods", font_size=24, color=BLUE
        ).shift(UP * 2.5)
        self.play(Write(purpose))

        # When to use super()
        when_title = Text("Common uses:", font_size=20, color=GREEN).shift(UP * 1.8)
        when_list = (
            VGroup(
                Text("• Extend parent's __init__ method", font_size=16),
                Text("• Add to parent's method behavior", font_size=16),
                Text("• Avoid code duplication", font_size=16),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .shift(UP * 0.8)
        )

        self.play(Write(when_title))
        for item in when_list:
            self.play(Write(item), run_time=0.6)

        self.wait(2)
        self.play(FadeOut(VGroup(purpose, when_title, when_list)))

        # Code example
        code_text = """class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")    # Call parent's __init__
        self.breed = breed                  # Add dog-specific attribute
    
    def make_sound(self):
        parent_sound = super().make_sound()  # Get parent's behavior
        return f"{parent_sound} - Woof!"     # Extend it

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Feline")    # Call parent's __init__
        self.color = color
    
    def make_sound(self):
        return f"{super().make_sound()} - Meow!"  # Extend parent's method

# Using super()
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(dog.make_sound())  # Buddy makes a sound - Woof!
print(cat.make_sound())  # Whiskers makes a sound - Meow!"""

        code_display = Code(
            code=code_text,
            language="python",
            font_size=13,
            background="window",
            style="monokai",
        ).scale(0.8)

        self.play(Write(code_display))
        self.wait(4)
        self.play(FadeOut(VGroup(section_title, code_display)))

    def course_conclusion(self):
        """Conclusion of the OOP module"""
        title = Text("Module 6 Complete!", font_size=40, color=GREEN).shift(UP * 2)
        self.play(Write(title))

        # Summary of what was covered
        summary_title = Text("What you learned:", font_size=24, color=BLUE).shift(
            UP * 0.5
        )

        topics = (
            VGroup(
                Text("✓ Classes and Objects", font_size=18, color=WHITE),
                Text("✓ Attributes and Methods", font_size=18, color=WHITE),
                Text("✓ Constructor (__init__)", font_size=18, color=WHITE),
                Text("✓ Inheritance", font_size=18, color=WHITE),
                Text("✓ Polymorphism", font_size=18, color=WHITE),
                Text("✓ Encapsulation", font_size=18, color=WHITE),
                Text("✓ Method Overriding", font_size=18, color=WHITE),
                Text("✓ super() Function", font_size=18, color=WHITE),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .shift(DOWN * 1.5)
        )

        self.play(Write(summary_title))
        for topic in topics:
            self.play(Write(topic), run_time=0.4)

        # Next steps
        next_steps = Text(
            "Next: Module 7 - File Handling & Error Management",
            font_size=20,
            color=ORANGE,
        ).shift(DOWN * 3.5)
        self.play(Write(next_steps))

        self.wait(3)
        self.play(FadeOut(VGroup(title, summary_title, topics, next_steps)))

        # Final message
        final_message = VGroup(
            Text(
                "Great job learning Object-Oriented Programming!",
                font_size=24,
                color=YELLOW,
            ),
            Text(
                "You now understand how to create classes, use inheritance,",
                font_size=18,
            ),
            Text("and apply OOP principles in Python!", font_size=18),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(final_message))
        self.wait(3)
        self.play(FadeOut(final_message))
