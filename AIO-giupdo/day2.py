def compute_interest(money, period):
    result = money
    daily_interest_rate = 1 / period
    for i in range(period):
        result *= (1 + daily_interest_rate)

    return result


print(compute_interest(1, 365))
