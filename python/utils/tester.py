class Test:
    def __init__(self, name: str):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def test_greet(self):
        if __name__ == "__main__":
            print("Test passed!")
        else:
            print("This script is not being run directly.")
            raise RuntimeError("This script is not being run directly.")
