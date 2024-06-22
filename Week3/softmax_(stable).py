import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        sum_exp_x = exp_x.sum(0, keepdim=True)

        return exp_x / sum_exp_x


class MySoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x-x_max.values)
        sum_x_exp = x_exp.sum(0, keepdim=True)
        return x_exp / sum_x_exp


# Test case for MySoftmax
data_a = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output_a = softmax_function(data_a)
print(output_a)

# Test case for MySoftmaxStable
data_b = torch.Tensor([1, 2, 3])
softmax = MySoftmaxStable()
output_b = softmax(data_b)
print(output_b)
