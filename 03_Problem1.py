a = 1
b = 3

if a == b // 2:
    b = a   # Make sure you take note of the variables and the outputs

if b == (2 * a + 1) % 2:
    a = 2 * b  # Keep note of the difference in number of equal signs

a = a + b
b = a % 3