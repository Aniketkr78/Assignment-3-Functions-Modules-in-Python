import math

# Ask user for input
num = float(input("Enter a number: "))

# Using math module for calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)  # natural logarithm (base e)
sine_val = math.sin(num)  # sine function expects radians

print(f"Square root: {sqrt_val}")
print(f"logarithm: {log_val}")
print(f"Sine : {sine_val}")
