import math

# Check if x can be converted into a number
def is_number(x):
  try:
    float(x)
  except ValueError:
    return False
  return True

def activation_function(x, function_name):
  if not is_number(x):
    print(f'{x} must be a number')
  else:
    # Convert x to float
    x = float(x)
    # Initialize value
    alpha = 0.01

    # Check function_name and call the relevant equation
    if function_name == 'sigmoid':
      result = 1 / (1 + math.exp(-x))
    elif function_name == 'relu':
      result = x if x > 0 else 0
    elif function_name == 'elu':
      result = x if x > 0 else alpha * (math.exp(x) - 1)
    # Only support three function names
    else:
      print(f'{function_name} is not supported')
    # Print out result
    print(f'{function_name}: f({x})={result}')

# Test function
x = input("Enter a number for x: ")
function_name = input("Enter the activation function name (sigmoid, relu, elu): ")
activation_function(x, function_name)


