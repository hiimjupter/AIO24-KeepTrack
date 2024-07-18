import random
import math

def calculate_loss(num_samples, loss_name):
  # Check if num_samples is integer
  if not num_samples.isnumeric():
      print('number of samples must be an integer')
      return
  else:
    # Convert num_samples to integer
    num_samples = int(num_samples)

    # Initialize total_loss
    total_loss = 0

    # Iterate num_samples times
    for i in range(num_samples):
        # Set up predict and target
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)

        # Calc loss based on loss_name
        if loss_name == 'MAE':
            loss = abs(predict - target)
        elif loss_name == 'MSE':
            loss = (predict - target) ** 2
        elif loss_name == 'RMSE':
            loss = math.sqrt((predict - target) ** 2)
        else:
            print(f'{loss_name} is not supported')

        # Calc new total_loss
        total_loss += loss

        # Output each iteration
        print(f'loss_name: {loss_name}; sample: {i}; pred: {predict}; targ: {target}; loss: {loss}')

    # Calc final_loss based on loss_name
    if loss_name == 'MAE' or loss_name == 'MSE':
      final_loss = total_loss / num_samples
    else:
      final_loss = math.sqrt(total_loss / num_samples)

    print(f'final {loss_name}: {final_loss}')

# Test function
num_samples = input("Input number of samples (int) which are generated: ")
loss_name = input("Input loss name (MAE, MSE, RMSE): ")
calculate_loss(num_samples, loss_name)
