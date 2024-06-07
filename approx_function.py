import math
import random

def factorial(n):
  if n == 0:
    return 1
  # E.g: 4! = 4 * 3!
  else:
    return n * factorial(n-1)

def calculate_function(x, n):
  # Check if n is a positive integer
  if n <= 0:
    print('n must be a positive integer greater than 0')
  else:
    # Calculate each function
    for function_name in ['sin', 'cos', 'sinh', 'cosh']:
      # Initialize approx for each function
      approx = 0
      for i in range(n):
        if function_name == 'sin':
          result = ((-1)**i)*(x**(2*i+1))/factorial(2*i+1)
        elif function_name == 'cos':
          result = ((-1)**i)*(x**(2*i))/factorial(2*i)
        elif function_name == 'sinh':
          result = (x**(2*i+1))/factorial(2*i+1)
        elif function_name == 'cosh':
          result = (x**(2*i))/factorial(2*i)
        # Add the result to approx
        approx += result
      # Print the result for each function
      print(f"approx_{function_name}(x={x}, n={n}) is {round(approx, 8)}")

# Test function
x = float(input("Enter a number for x (in radians): "))
n = int(input("Enter the number of iterations for approximation: "))
calculate_function(x, n)
