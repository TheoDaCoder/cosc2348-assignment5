#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Test for Division
result = run("6 / 2")
assert result.output == "3", f"Expected '3', but got {result.output}"

# Test for Subtraction
result = run("10 - 3")
assert result.output == "7", f"Expected '7', but got {result.output}"

###

print("All tests passed!")
