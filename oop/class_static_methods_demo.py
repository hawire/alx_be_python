
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: works independently of class or instance."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: accesses class-level data."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
