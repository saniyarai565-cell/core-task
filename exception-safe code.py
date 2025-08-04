class SafeCalculator:
    def divide(self, a, b):
        try:
            result = a / b
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except TypeError:
            print("Error: Invalid input type. Please use numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            calc = SafeCalculator()
            calc.divide(10, 2)
            calc.divide(10, 0)
            calc.divide(10,'a')