def calc_f1_score(tp, fp, fn):
  inputs = {'tp': tp, 'fp': fp, 'fn': fn}
  error_messages = []
  # Iterate through dictionary
  for name, value in inputs.items():
    # isinstance to check datatype
    if not isinstance(value, int):
      error_messages.append(f'{name} must be int')
    elif value <= 0:
      error_messages.append(f'{name} must be larger than 0')
  # Check if there is error --> dont calc metrics
  if error_messages:
    print("Errors:")
    print("\n".join(error_messages))
  else:
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision*recall)/(precision+recall))
    print(f'Precision: {round(precision, 2)}, Recall: {round(recall, 2)}, F1 Score: {round(f1_score, 2)}')

# Test the function
calc_f1_score(1, 2, 3)
