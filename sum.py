def divide(a, b):
    # Handle division by zero with a clear error message expected by tests.
    # Also handle non-numeric inputs by returning an error message.
    try:
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    except TypeError:
        return "Error: Invalid operands for division"
